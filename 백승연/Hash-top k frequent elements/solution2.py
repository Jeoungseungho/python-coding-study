# 카운터 모듈 사용

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = Counter(nums).most_common(k)
        return list(zip(*freqs))[0]
