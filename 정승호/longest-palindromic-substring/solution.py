class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        def check(l,r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -=1 
                r +=1
            return s[l+1:r]
                
        for i in range(len(s)):
            temp = check(i,i)
            if len(temp) > len(answer):
                answer = temp
                
            temp = check(i,i+1)
            if len(temp) > len(answer):
                answer = temp
        return answer
        
        
