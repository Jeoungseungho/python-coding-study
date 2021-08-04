from collections import deque
N = int(input())
arr = deque([i for i in range(1, N+1)])

while True:
    tmp = arr.popleft()
    if not arr:
        print(tmp)
        break
    arr.append(arr.popleft())

