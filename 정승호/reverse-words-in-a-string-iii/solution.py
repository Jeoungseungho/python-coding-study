class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split(" ")
        result = ""
        
        for word in temp:
            word = word[::-1]
            result += word + " "
        return result[:-1]
    
    
    
