def solution(s):
    answer = 0
    
    for index, num in enumerate(s[::-1]):
        if num == '-':
            answer *= -1
        elif num == '+':
            continue
        else :
            answer += int(num)* (10 ** index)
            
    return answer
