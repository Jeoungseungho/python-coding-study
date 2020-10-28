class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        rightMost = {c:index for index, c in enumerate(S)}
        result = []
        left , right = 0,0 
        for i, letter in enumerate(S):
            right = max(right, rightMost[letter])
            if i == right:
                result += [right - left + 1]
                left = i +1
                
        return result 
