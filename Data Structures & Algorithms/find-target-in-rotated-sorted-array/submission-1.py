class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r - 1:
            m = (l + r) // 2
            
            # Find the interval that is non-decreasing
            # if the target is within the interval, 
            # narrow down to this interval
            if nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m # move to l, m
                else:
                    l = m
            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m # move to m, r
                else:
                    r = m

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
