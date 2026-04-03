class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums[:-1]):
            for j, n2 in enumerate(nums[i+1:]):
                if n1 + n2 == target:
                    return [i, i + j + 1]