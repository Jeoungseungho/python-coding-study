import sys

input = sys.stdin.readline

def dfs(index, depth):
    global answer, sub_value

    if index == depth:
        if ''.join(sub_value) != ''.join(formula):
            answer.add(''.join(sub_value))
        return

    is_bracket = formula[index]
    if is_bracket == '(':
        check[index] = True
        dfs(index+1, depth)
        check[index] = False

    if is_bracket == ')'and check[pair[index]]:
        dfs(index+1, depth)
    else:
        sub_value.append(is_bracket)
        dfs(index+1, depth)
        sub_value.pop()

formula = list(input().strip())
stack = []
check = [False for _ in range(len(formula))]
pair = [0 for _ in range(len(formula))]
answer = set()
sub_value = []

for index, bracket in enumerate(formula):
    if bracket == '(':
        stack.append(index)
    elif bracket == ')':
        pair[index] = stack[-1]
        pair[stack[-1]] = index
        stack.pop()

dfs(0, len(formula))

print('\n'.join(sorted(answer)))
