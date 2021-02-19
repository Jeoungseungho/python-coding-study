def solution(N, number):
    answer = 0
    if N == number:
        return 1
    
    DP = [set() for _ in range(8)]
    for index, num in enumerate(DP):
        num.add(int(str(N)*(index+1)))
    
    for i in range(1,8):
        for j in range(i):
            for val1 in DP[j]:
                for val2 in DP[i-j-1]:
                    DP[i].add(val1+val2)
                    DP[i].add(val1-val2)
                    DP[i].add(val1*val2)
                    if val2 != 0:
                        DP[i].add(val1//val2)
        if number in DP[i]:
            answer = i+1
            break
    else :
        answer = -1
        
    return answer
