def solution(d, budget):
    answer = 0
    temp = 0
    d.sort()
    for i in d:
        temp += i
        if temp <= budget:
            answer+=1
        else :
            break
            
    return answer
