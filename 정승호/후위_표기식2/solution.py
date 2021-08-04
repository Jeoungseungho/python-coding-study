import sys

input = sys.stdin.readline

N = int(input())

formula = input().split()

alpha = [0]*N
stack = []
for i in range(N):
    alpha[i] = int(input())

for s in formula[0]:
    if s.isupper():
        stack.append(alpha[ord(s) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if s == '+':
            stack.append(n1+n2)
        elif s == '-':
            stack.append(n1-n2)
        elif s == '*':
            stack.append(n1*n2)
        elif s == '/':
            stack.append(n1/n2)
print(format(stack[0], ".2f"))

