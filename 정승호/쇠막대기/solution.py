def solution(arrangement):
    answer = 0
    stick = 0
    steel = list(arrangement)
    before = '('
    for i in steel:
        if i == '(':
            stick +=1
            before = i
        else:
            if before == '(':
                stick -=1
                answer += stick
                before = i
            else :
                stick -=1
                answer +=1
                
    return answer
