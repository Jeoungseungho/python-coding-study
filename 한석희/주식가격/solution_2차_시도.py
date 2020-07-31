def solution(prices):
    #
    entryNum = len(prices)
    #
    answer = [0] * entryNum
    #
    for i in range( entryNum ) :
        for j in range(i+1, entryNum) :
            if prices[i] <= prices[j] :
                answer[i] += 1
            else :
                answer[i] += 1
                break
    #
    return answer
