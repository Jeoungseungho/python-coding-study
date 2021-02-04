class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for i in nums:
            if i in table:
                table[i] += 1
            else :
                table[i] = 1
                
        return sorted(table, key=table.get, reverse=True)[:k]
