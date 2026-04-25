class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # iff can find subset with sum = sum / 2
        # Since everything is an integer, the sum must be even
        s = sum(nums)
        if s % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(len(dp)-1, -1, -1):
                if dp[i] and i + n <= target:
                    dp[i + n] = True
            if dp[target]:
                return True
        
        return dp[target]