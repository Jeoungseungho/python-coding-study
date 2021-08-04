
n = int(input())
stack = []
count = 0
result = []
flag = True

for _ in range(n):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if not flag:
    print("NO")
else:
    for i in result :
        print(i)

