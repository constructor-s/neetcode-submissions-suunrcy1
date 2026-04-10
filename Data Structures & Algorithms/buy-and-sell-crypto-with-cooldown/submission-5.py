class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        if len(prices) == 2:
            return max(0, prices[1] - prices[0])

        opt_0 = [None] * len(prices) # has zero coins by continuing from index i-1, or from opt_1[i-2]
        opt_1 = [None] * len(prices) # has one coin after index i

        # After index 0
        opt_0[0] = 0
        opt_1[0] = -prices[0]

        # After index 1
        opt_0[1] = 0
        opt_1[1] = max(opt_1[0], opt_0[0] - prices[1])

        # After index 2
        # opt_0[2] = max(opt_0[1], opt_1[0] + prices[1])
        # opt_1[2] = max(opt_1[1], opt_0[1] - prices[2])

        for i in range(2, len(prices) - 1):
            opt_0[i] = max(opt_0[i-1], opt_1[i-2] + prices[i-1])
            opt_1[i] = max(opt_1[i-1], opt_0[i-1] - prices[i])

        return max(opt_0[-2], opt_1[-3] + prices[-2], opt_1[-2] + prices[-1])



