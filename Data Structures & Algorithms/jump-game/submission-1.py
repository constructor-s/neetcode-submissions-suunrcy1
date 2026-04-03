class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(2, len(nums)+1):
            if nums[-i] >= i-1:
                return self.canJump(nums[:-i+1])
        return False
