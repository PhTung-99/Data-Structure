def check(s):
    map = {
        '{': '}',
        '[': ']',
        '(': ')'\
            
    }
    stack = []

    openning, closing = map.keys(), map.values()
    for char in s:
        if char in openning:
            stack.append(char)
        elif char in closing:
            if stack and char == map[stack[-1]]:
                stack.pop()
            else:
                return False
    return not stack

# print(check("[](){}"))
print(check("(([]){})"))