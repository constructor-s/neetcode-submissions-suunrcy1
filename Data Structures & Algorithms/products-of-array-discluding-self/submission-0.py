class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if i != j:
                    result[i] *= v2
        return result
