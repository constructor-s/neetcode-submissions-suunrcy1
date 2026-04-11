class Solution:
    def jump(self, nums: List[int]) -> int:
        opt = [float("inf")] * len(nums)
        opt[0] = 0

        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums):
                    break
                opt[j] = min(opt[j], opt[i] + 1)
        
        return opt[-1]
