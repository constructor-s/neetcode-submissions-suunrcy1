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
            if l + r == target:
                res.append([l, r])
            if l + r >= target:
                while right >= 0 and nums[right] == r:
                    right -= 1
            else:
                left += 1
            
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []
        
        i = 0
        while i < len(nums):
            for two in self.twoSumSorted(nums[i+1:], -nums[i]):
                res.append([nums[i]] + two)
            val = nums[i]
            while i < len(nums) and nums[i] == val:
                i += 1

        return res
