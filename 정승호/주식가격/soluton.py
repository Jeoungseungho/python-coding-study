def solution(prices):
    l = len(prices)
    a = [0]*l
    for i in range(l-1):
        for j in range(i+1, l):
            if prices[i] > prices[j]:
                break;
        a[i] = j-i
    return a

