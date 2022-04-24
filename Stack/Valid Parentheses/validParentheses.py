
def isValid(s: str) -> bool:
    stack = ''
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack += char
        if char == ')' or char == '}' or char == ']':
            if len(stack) == 0:
                return False
            reverseString = stack[::-1]
            if char == ')':
                if reverseString[0] == '(':
                    stack =  stack[0:len(stack)-1]  
                else:
                    return False
            if char == '}':
                if reverseString[0] == '{':
                    stack =  stack[0:len(stack)-1]   
                else:
                    return False
            if char == ']':
                print(stack)
                print(reverseString)
                if reverseString[0] == '[':
                    stack =  stack[0:len(stack)-1]
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False

check = isValid("[[[]")
print(check)