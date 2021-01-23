def solution(arr, divisor):
    answer = []
    for i in arr :
        if (i >= divisor) and (i % divisor == 0):
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
        
    answer.sort()
    return answer
