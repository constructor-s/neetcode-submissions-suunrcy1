class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 0:
            return 0

        opt = [0] * (amount + 1) # opt for the current c
        # Initialize with the first coin
        c = coins[0]
        for i in range(0, amount + 1, c):
            opt[i] = 1
        opt_new = [0] * (amount + 1) # opt for the current c
        
        for i in range(1, len(coins)): # add one possibility at a time
            c = coins[i]
            for i in range(amount + 1):
                if i < c:
                    opt_new[i] = opt[i]
                else:
                    opt_new[i] = opt[i] + opt_new[i - c]

            # print(opt)
            # print(opt_new)
            # print()
            opt, opt_new = opt_new, opt

        return opt[amount]
