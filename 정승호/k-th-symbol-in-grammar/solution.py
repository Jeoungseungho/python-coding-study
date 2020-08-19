class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        
        if(K%2 == 1):
            return self.kthGrammar(N-1, (K//2)+1)
        
        if self.kthGrammar(N-1, K//2) == 0:
            return 1
        
        if self.kthGrammar(N-1, K//2) == 1:
            return 0
