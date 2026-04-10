from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def get_max_profit(i: int, holding: int) -> int:
            if i == len(prices):
                assert holding == 0
                return 0

            if i == len(prices) - 1:
                if holding == 0:
                    return 0
                else:
                    return +prices[i]

            if holding == 0:
                # can only sell
                return max(
                    # buy
                    -prices[i] + get_max_profit(i+1, holding+1),
                    # not buy
                    get_max_profit(i+1, holding)
                )
            else: # holding == 1
                return max(
                    # sell
                    +prices[i] + get_max_profit(i+2, holding-1),
                    # not sell
                    get_max_profit(i+1, holding)
                )


        return get_max_profit(i=0, holding=0)
