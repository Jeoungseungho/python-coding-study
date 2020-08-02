def solution(inp):
    cnt_list = []
    answer = 0
    top = ''
    for i in inp:
        if i == '(':
            cnt_list.append(1)
        elif i == ')':
            if top == '(':
                del cnt_list[-1]
                cnt_list = [cnt_list + 1 for cnt_list in cnt_list]
            else:
                answer += cnt_list[-1]
                del cnt_list[-1]
        top = i
        
    return answer

print(solution(input()))

## 0802, 23:23 수정
