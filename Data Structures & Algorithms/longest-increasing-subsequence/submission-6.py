class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        f(i, j) = lengthOfLIS starting at index i, and every element > nums[j]
        j = -1 indicates nothing taken yet
        f(i, j) is the max of:
        - does not include i: f(i+1, j)
        - include i: 1 + f(i+1, i)

        
        from functools import cache

        @cache
        def llis(i=0, j=-1):
            if i == len(nums):
                return 0                
            len0 = llis(i + 1, j)
            if j == -1 or nums[i] > nums[j]:
                len1 = 1 + llis(i + 1, i)
                return max(len0, len1)
            else:
                return len0

        return llis()
        """

        dp = [[0 for j in range(len(nums)+1)] for i in range(len(nums)+1)]

        for i in range(len(nums)-1, -1, -1):
            for j in range(-1, len(nums)):
                dp[i][j] = dp[i+1][j]
                if j == -1 or nums[i] > nums[j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i+1][i])
        return dp[0][-1]
