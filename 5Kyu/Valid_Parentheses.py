def valid_parentheses(s):
    if s.strip() == "": return True
    if len(s) == 0 or len(s) == 1 or s[0] == ')': return False #edge cases
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        elif p == ')':
            try:
                stack.pop()
            except:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
