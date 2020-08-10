#  시간 복잡도 O(n2), 
def solution(prices):
    answer = []
    for i in range(len(prices)):
        s = 0
        for j in range(i + 1, len(prices)):
            s += 1
            if prices[i] > prices[j]:
                break
        answer.append(s)

    return answer
# Worst case 같은 경우 시간초과. 
# arr = [i for i in range(100000)]
solution(arr)
