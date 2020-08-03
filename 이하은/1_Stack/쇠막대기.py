'''
백준 10799
https://www.acmicpc.net/problem/10799
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다.
괄호 문자의 개수는 최대 100,000이다.
'''

input_list = list(map(str,input()))
prev = ""
result = 0
stack_list = []

for ch in input_list:
    if ch == '(':
        stack_list.append(ch)
    else:
        stack_list.pop()
        if prev == '(': # 절단
            result += len(stack_list)
        else: # 쇠막대기 끝
           result += 1
    prev = ch
print(result)
