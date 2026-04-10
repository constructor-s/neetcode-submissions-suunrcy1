class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost0 = 0
        cost1 = 0
        
        for i in range(2, len(cost) + 1):
            cost2 = min(cost0 + cost[i-2], cost1 + cost[i-1])
            cost0 = cost1
            cost1 = cost2
        return cost2
