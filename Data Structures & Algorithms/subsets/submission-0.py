class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        res = self.subsets(nums[:-1])
        res2 = [i + [nums[-1]] for i in res]
        return res + res2
