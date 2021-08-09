import sys

input = sys.stdin.readline

N = int(input())
ballons = list(map(int, input().split()))
result = []
index = [i for i in range(1, N+1)]
ballon_num = ballons.pop(0)
result.append(index.pop(0))
idx = 0

while ballons:
    if ballon_num < 0:
        idx = (idx + ballon_num) % len(ballons)
    else:
        idx = (idx + (ballon_num-1)) % len(ballons)
    ballon_num = ballons.pop(idx)
    result.append(index.pop(idx))

for r in result:
    print(r, end=' ')
