def solution(x):
    answer = True
    temp = 0
    y = x
    
    while y != 0:
        temp += y%10
        y = y//10
    
    if x%temp != 0:
        return False
        
    return answer
