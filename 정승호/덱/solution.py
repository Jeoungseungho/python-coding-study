import sys

input = sys.stdin.readline
deque = []
N = int(input())

for i in range(N):
    command = input().split()
    cmd = command[0]
    if len(command) == 2:
        num = command[1]

    # push_front
    if cmd == "push_front": deque.insert(0, num)

    # push_back
    if cmd == "push_back": deque.append(num)

    # pop_front
    elif cmd == "pop_front":
        if len(deque) == 0: print(-1)
        else : print(deque.pop(0))

    # pop_back
    elif cmd == "pop_back":
        if len(deque) == 0: print(-1)
        else: print(deque.pop(-1))

    # size
    elif cmd == "size": print(len(deque))

    # empty
    elif cmd == "empty":
        if len(deque) == 0: print(1)
        else: print(0)

    # front
    elif cmd == "front":
        if len(deque) == 0: print(-1)
        else: print(deque[0])

    # back
    elif cmd == "back":
        if len(deque) == 0: print(-1)
        else: print(deque[-1])



