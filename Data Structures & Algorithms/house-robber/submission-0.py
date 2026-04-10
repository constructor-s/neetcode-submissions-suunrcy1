class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        opt = [0] * len(nums)
        opt[0] = nums[0]
        opt[1] = nums[1]
        opt[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            opt[i] = max(opt[i-2], opt[i-3]) + nums[i]

        return max(opt[-1], opt[-2])
