def generate_bc(url, separator):
    splitted_url = url_cleaner(url).split('/')

    if len(splitted_url) < 2:
        return '<span class="active">HOME</span>'

    links = []
    for page in splitted_url:
        if len(page) > 30:
            links.append(shortener(page))
        else:
            new_page = ''
            for char in page:
                if '-' == char:
                    new_page += ' '
                else:
                    new_page += char
            links.append(new_page.upper())

    output = []
    output = ['<a href="/">HOME</a>', separator]

    i = 1
    while i < len(links) - 1:
        new_url = ''
        j = 1
        while j <= i:
            new_url += '/' + splitted_url[j]
            j += 1
        output.append('<a href="' + new_url +'/">' + links[i] + '</a>' + separator )
        i += 1

    last = []
    for char in links[-1]:
        if char == '.':
            break
        elif char == '-':
            last.append(' ')
        else:
            last.append(char)

    links.pop()
    links.append(''.join(last))

    if links[-1] == 'INDEX':
        links.pop(-1)
        output.pop(-1)

    if len(output) < 2:
        return '<span class="active">HOME</span>'

    output.append('<span class="active">' + links[-1] + '</span>')

    return ''.join(output)

def url_cleaner(url):
    cleaned_url = ''
    if url[:7] == 'http://':
        url = url[7:]
    elif url[:8] == 'https://':
        url = url[8:]

    for char in url:
        if char == '#' or char == '?' or char == '&':
            break
        else:
            cleaned_url += char

    if cleaned_url[-1] == '/':
        cleaned_url = cleaned_url[:-1]

    return cleaned_url


def shortener(string):
    ignored_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]
    new_word = ''
    splitted_page = string.split('-')
    for word in splitted_page:
        if word not in ignored_words:
            new_word += word[0].upper()
    return new_word
