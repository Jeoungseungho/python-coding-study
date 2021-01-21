def solution(n):
    answer = 0
    temp = []
    
    while n  :
        temp.append(str(n%3))
        n = int(n/3)
    
    digit = 1
    for i in reversed(temp):
        answer += int(i)*digit
        digit *= 3
        
    return answer
