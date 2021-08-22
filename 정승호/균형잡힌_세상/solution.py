import sys


input = sys.stdin.readline

while 1:
    string = input().rstrip()
    stack = []
    balance = True
    for ch in string:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balance = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balance = False
                break
    if string == '.':
        break

    print("yes" if balance and len(stack) == 0 else "no")


