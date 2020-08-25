class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        # 짝수 번째 숫자일때
        if K % 2 == 0:
            if self.kthGrammar(N - 1, K // 2) == 0:
                return 1
            else:
                return 0
        else:
        #  홀수 번째 숫자일때
            if self.kthGrammar(N - 1, (K + 1) // 2) == 0:
                return 0
            else:
                return 1


# 써가면서 패턴 파악. N row의 K번째 숫자가 N-1 row의 몇번째 숫자에서 나왔는지 파악한다.

#  row1 : 0
#  row2 : 01
#  row3 : 0110
#  row4 : 0110 1001
#  row5 : 0110 1001 1001 0110
#  row6 : 0110 1001 1001 0110 1001 0110 0110 1001
#  row7 : 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110