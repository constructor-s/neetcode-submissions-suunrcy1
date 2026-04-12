class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 1

        jumps = 0
        while r < len(nums):
            r_new = r
            for i in range(l, r):
                r_new = max(r_new, i + nums[i] + 1)
            l = r
            r = r_new
            jumps += 1
        
        return jumps
