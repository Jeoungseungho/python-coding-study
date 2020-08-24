class Solution:
    def isPalindrome(self, s: str) -> bool:
        # deque 자료형을 이용해서 문제를 풀면 
        # brute force보다 실행시간이 더 빠르다.
        strs = collections.deque()
        
        for char in  s:
            if char.isalnum():
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True
