class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = 1 + freq.get(ch,0)
            
        result = 0
        appears = set()
        for k in freq.values():
            while k in appears:
                k-=1
                result+=1
            if k:
                appears.add(k)
        return result
