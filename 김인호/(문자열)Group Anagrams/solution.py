class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        for s in strs:
            temp = str(sorted(list(s)))
            if temp in dic:
                dic[temp].append(s)
            else:
                dic[temp] = [s]
        
        for _,v in dic.items():
            ans.append(v)
        
        return ans