class Encoder:
    def __init__(self, word):
        self.word = word

    def duplicate_encode(word):
        counter = {}
        word = word.lower()
        for char in word:
            if not char in counter:
                counter[char] = 0
            counter[char] += 1

        output = ''
        for char in word:
            if counter[char] > 1:
                output += ')'
            else:
                output += '('

        return output
