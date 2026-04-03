class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run = float("-inf")
        chain = float("-inf")
        for i in range(len(nums)):
            chain = max(chain, 0) + nums[i]
            run = max(run, chain)

        return run
        