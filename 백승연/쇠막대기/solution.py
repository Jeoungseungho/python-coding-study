inp = input()
stack = []
cnt = 0

for i in range(len(inp)):
    if inp[i] == '(':
        stack.append(inp[i])
    else:
        if inp[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)