class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        # opt[i] = max(opt[i-2] + nums[i], opt[i-1])
        opt_rob0 = [0] * len(nums)
        opt_not0 = [0] * len(nums)

        opt_rob0[0] = nums[0]
        opt_rob0[1] = nums[0]
        opt_not0[1] = nums[1]
        for i in range(2, len(nums) - 1):
            opt_rob0[i] = max(opt_rob0[i-2]+nums[i], opt_rob0[i-1])
            opt_not0[i] = max(opt_not0[i-2]+nums[i], opt_not0[i-1])
        
        opt_rob0[-1] = max(opt_rob0[-3], opt_rob0[-2]) # cannot rob last one
        opt_not0[-1] = max(opt_not0[-3]+nums[-1], opt_not0[-2])

        print(opt_rob0)
        print(opt_not0)
        return max(opt_rob0[-1], opt_not0[-1])
