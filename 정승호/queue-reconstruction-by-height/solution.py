class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for i in sorted(people, key = lambda x : (-x[0], x[1])):
            result.insert(i[1], i)
        return result 
        
