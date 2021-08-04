from collections import deque
import sys

input = sys.stdin.readline
N = int(input())


for i in range(N):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        big = max(queue)
        front = queue.popleft()
        m-=1
        if big == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue)-1

