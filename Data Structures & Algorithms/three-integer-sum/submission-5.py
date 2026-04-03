class Solution:
    def twoSumSorted(self, nums, target):
        if len(nums) < 2:
            return []

        res = []
        left = 0
        right = len(nums) - 1
        while left < right:
            l = nums[left]
            r = nums[right]
            if l + r > target:
                right -= 1
            elif l + r < target:
                left += 1
            else:
                res.append([l, r])
                while left < len(nums) and nums[left] == l:
                    left += 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []
        
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            for two in self.twoSumSorted(nums[i+1:], -nums[i]):
                res.append([nums[i]] + two)
            val = nums[i]
            while i < len(nums) and nums[i] == val:
                i += 1

        return res
