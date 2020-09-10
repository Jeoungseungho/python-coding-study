class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for ana in strs:
            answer[''.join(sorted(ana))].append(ana)
        return answer.values()
