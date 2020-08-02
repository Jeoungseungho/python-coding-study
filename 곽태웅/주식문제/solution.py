def solution(prices):
    answer = []
    cnt = 1
    for i in prices:
        stop_temp = 0
        for j in range(cnt, len(prices)):
            if int(i) > int(prices[j]):
                answer.append(j - cnt + 1)  
                stop_temp = 1
                break
        if stop_temp == 0:
                answer.append(len(prices) - cnt)
        cnt += 1
        
    return answer
