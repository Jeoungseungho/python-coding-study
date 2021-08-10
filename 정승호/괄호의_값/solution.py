formula = list(input())

stack = []
answer = 0

for i in formula:
    if i == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2*temp)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                temp += int(top)
    elif i == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if temp == 0 else temp*3)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                temp += int(top)
    else :
        stack.append(i)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        answer += i
print(answer)



