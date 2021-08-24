import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    pass_word = input().rstrip()
    left_stack = []
    right_stack = []

    for word in pass_word:
        if word == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif word == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif word == '-':
            if left_stack:
                left_stack.pop()
        else: left_stack.append(word)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
