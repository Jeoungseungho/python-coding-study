import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
queue = [i for i in range(1, N+1)]
answer = 0

for target in arr:
    index = queue.index(target)
    if len(queue)//2 >= index: answer += index
    else: answer += len(queue) - index
    queue = queue[index + 1:] + queue[:index]

print(answer)

