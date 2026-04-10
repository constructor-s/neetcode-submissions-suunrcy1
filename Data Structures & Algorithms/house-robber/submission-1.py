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

        # opt = [0] * len(nums)
        opt0 = nums[0]
        opt1 = nums[1]
        opt2 = nums[0] + nums[2]
        for i in range(3, len(nums)):
            opt3 = max(opt1, opt0) + nums[i]
            opt0 = opt1
            opt1 = opt2
            opt2 = opt3

        return max(opt2, opt1)
