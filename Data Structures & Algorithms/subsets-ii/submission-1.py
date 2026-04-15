class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = [[]]
        prev_end = 0
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                iter_range = range(prev_end, len(res))
            else:
                iter_range = range(len(res))
            end = len(res)
            for j in iter_range:
                res.append(res[j] + [nums[i]])
            prev_end = end

        return res
