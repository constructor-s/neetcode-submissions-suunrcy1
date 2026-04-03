class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, n_i in enumerate(nums[:-1]):
            for j, n_j in enumerate(nums[i+1:]):
                if n_i == n_j:
                    return True

        return False
