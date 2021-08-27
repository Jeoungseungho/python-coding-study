from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
rule = deque(map(int, input().split()))
after = deque(range(1, N+1))
before = deque()
while rule:
    t = rule.pop()
    a = after.popleft()
    if t == 1:
        before.appendleft(a)
    elif t == 2:
        before.insert(1,a)
    elif t == 3:
        before.append(a)

print(*before)


