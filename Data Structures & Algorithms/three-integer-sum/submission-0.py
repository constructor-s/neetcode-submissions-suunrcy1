class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if i == j or j == k or i == k:
                        continue
                    elif nums[i] + nums[j] + nums[k] == 0:
                        item = sorted([nums[i], nums[j], nums[k]])
                        if item not in res:
                            res.append(item)

        return res
