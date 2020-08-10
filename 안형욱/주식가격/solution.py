# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        target = prices[i]
        count = 0
        flag = False
        for j in range(i+1, n):
            if prices[j]<target:
                answer.append(count+1)
                flag = True
                break
            count+=1
        if not flag:
            answer.append(count)
    return answer

print(solution([1, 2, 3, 2, 3]))