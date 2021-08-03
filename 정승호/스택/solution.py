import sys


def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = []
for i in range(N):
    order = input().split()
    cmd = order[0]
    if len(order) == 2:
        num = order[1]

    # push
    if cmd == "push":
        stack.append(num)
    # pop
    elif cmd == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop(-1))

    # top
    elif cmd == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])

    # size
    elif cmd == "size":
        print(len(stack))

    # empty
    else:
        if len(stack) == 0:
            print("1")
        else :
            print("0")








