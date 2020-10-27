class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n, start, agg = len(gas), 0, 0
        for i in range(n):
            agg += (gas[i]- cost[i])
            if agg < 0:
                start, agg = i+1, 0
        return start
      
