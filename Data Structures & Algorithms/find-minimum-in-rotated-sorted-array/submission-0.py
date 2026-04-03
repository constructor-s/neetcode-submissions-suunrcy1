class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        else:
            mid = (l + r) // 2
            if nums[l] < nums[mid]:
                return self.findMin(nums[mid:r+1])
            else:
                return self.findMin(nums[l:mid+1])
