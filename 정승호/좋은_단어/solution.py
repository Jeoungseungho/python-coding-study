import sys

input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    word_list = input().rstrip()
    stack = []

    for ch in word_list:

        if stack and stack[-1] == ch:
            stack.pop()

        else: stack.append(ch)

    if not stack:
        answer += 1


print(answer)
