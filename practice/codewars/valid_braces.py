def valid_braces(string):
    leftbrackets = '({['
    rigthbrackets = ')}]'
    stack = []
    for char in string:
        if char in leftbrackets:
            stack.append(char)
        elif char in rigthbrackets:
            if not len(stack):
                return False

            stack_top = stack.pop()
            balancing_bracket = leftbrackets[rigthbrackets.index(char)]
            if stack_top != balancing_bracket:
                return False

        else:
            return False
    return not len(stack)
