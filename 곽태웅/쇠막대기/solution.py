def solution(inp):
    cnt_st, answer = 0, 0
    top = ''
    for i in inp:
        if i == '(':
            cnt_st += 1
            answer += 1
        elif i == ')':
            if top == '(':
                cnt_st -= 1
                answer -= 1
                answer += cnt_st
            else:
                cnt_st -= 1
        top = i
        
    return answer

print(solution(input()))

## 수정 0802, 23:23
## 수정 0802, 23:48
