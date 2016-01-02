def valid_braces(string):

    if len(string) % 2 != 0:
        return False
    center = int(len(string) / 2)
    if string[center - 1] == '{' and string[center] == '}':
        return True
    elif string[center - 1] == '[' and string[center] == ']':
        return True
    elif string[center - 1] == '(' and string[center] == ')':
        return True
    elif string[center - 1] == ')' and string[center] == '(':
        if string[center - 2] == '(' and string[center+1] == ')':
            return True
    elif string[center - 1] == ')' and string[center] == '{':
        if string[center - 2] == '(' and string[center+1] == '}':
            return True
    elif string[center - 1] == ')' and string[center] == '[':
        if string[center - 2] == '(' and string[center+1] == ']':
            return True



    else:
        return False
