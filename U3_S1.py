# testing123 with stack
def checkParenBalance(s):
    if len(s) == 0:
        return False

    stack = []
    
    for char in s:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0

string1 = "((()))"
print (f"{string1} -> {checkParenBalance(string1)}")

