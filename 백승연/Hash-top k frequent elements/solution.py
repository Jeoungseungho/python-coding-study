class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        ht = dict()

        for i in nums:
            ht[i] = ht.get(i, 0) + 1

        max = 0

        for i in range(k):
            for j in ht.keys():
                if max < ht.get(j):
                    max = ht.get(j)
                    maxkey = j
            res.append(maxkey)
            del ht[maxkey]
            max = 0

        return res
