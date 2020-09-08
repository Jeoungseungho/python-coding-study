import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap, ans = [], []
        key, dic = [], {}
        for i in nums:
            if i in dic:
                # 나온 횟수를 저장.
                dic[i] += 1
            else:
                dic[i] = 1
                # dict의 key 리스트 저장.
                key.append(i)
        for i in key:
            # 큐에서 횟수가 큰 순서대로 먼저 나오게 하기 위해서 -를 붙임.
            heapq.heappush(heap, (-dic[i], i))

        for i in range(k):
            # 횟수가 큰 수의 숫자를 ans에 담는다. 
            _, v = heapq.heappop(heap)
            ans.append(v)

        return ans

