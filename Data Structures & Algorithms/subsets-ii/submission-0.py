class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = [[]]
        prev_end = 0
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                end = len(res)
                for j in range(prev_end, len(res)):
                    res.append(res[j] + [nums[i]])
                prev_end = end
            else:
                end = len(res)
                for j in range(len(res)):
                    res.append(res[j] + [nums[i]])
                prev_end = end

        return res
