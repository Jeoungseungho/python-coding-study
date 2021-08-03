from sys import stdin
T = input()
queue, commands = [], stdin.readlines()
index = 0

for command in commands:
    cmd = command.split()

    # push
    if cmd[0] == "push":
        queue.append(cmd[1])

    # pop
    elif cmd[0] == "pop":
        if len(queue) > index:
            print(queue[index])
            index += 1
        else: print(-1)

    # size
    elif cmd[0] == "size":
        print(len(queue)-index)

    # empty
    elif cmd[0] == "empty":
        if len(queue) == index:
            print(1)
            index = 0
            queue = []
        else: print(0)

    # front
    elif cmd[0] == "front":
        if len(queue) > index : print(queue[index])
        else: print(-1)

    # back
    elif cmd[0] == "back":
        if len(queue) > index: print(queue[-1])
        else: print(-1)

