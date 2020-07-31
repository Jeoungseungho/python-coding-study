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


# Q : 주가가 계속해서 상승하고, 데이터 갯수가 10^5개인 경우, 각 i에 대하여, 각각 n-1번, n-2번, n-3번, .... 1번 이터레이션이 필요합니다. 이 경우, 데이터 갯수가 n이라고 할 때, n(n+1)/2 - n -> 결과적으
# O(n^2)가 되는데, 여전히 효율성 테스트를 통과하긴 하네요. 왜 그런 걸까요?
