# 시간 통과 x, 이진 탐색 x
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        N, M = len(matrix), len(matrix[0])
        ans = float("-inf")
        dp = [[0]*M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                total = matrix[i][j]
                if i>0:
                    total += dp[i-1][j]
                if j>0:
                    total += dp[i][j-1]
                if i>0 and j>0:
                    total -= dp[i-1][j-1]
                dp[i][j] = total
                
                for r in range(i+1):
                    for c in range(j+1):
                        temp = dp[i][j]
                        if r > 0:
                            temp -= dp[r-1][j]
                        if c > 0:
                            temp -= dp[i][c-1]
                        if r > 0 and c > 0:
                            temp += dp[r-1][c-1]
                        if temp<=k:
                            ans = max(temp,ans)   
        return ans


# 시간 통과 코드
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        
        M = max(m, n)
        N = min(m, n)
        ans = -1e9
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                slist, num = [], 0
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k:
                        ans = max(ans, num)
                    i = bisect.bisect_left(slist, num-k)
#                   i값이 slist의 맨끝이 아니면 즉, num이 젤 크지 않다면
                    if i != len(slist):
                        ans = max(ans, num - slist[i])
                    bisect.insort(slist, num)
        return ans