class Solution:
    def sumZero(self, n: int) -> List[int]:
        num, rem = n//2, n%2
        answer = []
        if rem != 0: answer.append(0)
        for i in range(1, num+1):
            answer.append(-i)
            answer.append(i)
        return answer

