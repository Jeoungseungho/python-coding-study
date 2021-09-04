import sys
import heapq

input = sys.stdin.readline

N = int(input())
exp = []
for _ in range(N):
    exp.append(int(input()))

heap = []
heapq.heapify(heap)
for i in exp:
    if i == 0 and len(heap)==0:
        print(0)
    elif i == 0:
        print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -i)

