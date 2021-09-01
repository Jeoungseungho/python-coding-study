import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
answer = 0
for _ in range(N):
    S.add(input())

for _ in range(M):
    string = input()
    if string in S:
        answer += 1

print(answer)

