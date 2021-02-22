import heapq
def solution(scoville, K):
    answer = 0
    data = []
    for s in scoville:
        heapq.heappush(data, s)
    
    while len(data) > 0:
        if data[0] >= K:
            return answer
        a = heapq.heappop(data)
        if data != []:
            b =heapq.heappop(data)
            heapq.heappush(data,a + (b *2))
        answer+=1
    
    return -1
