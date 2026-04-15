class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[-1]
        p = 0
        for i in range(len(nums)):
            if nums[i] > pivot: # sort descending
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        nums[p], nums[-1] = nums[-1], nums[p]
        assert all(i >= pivot for i in nums[:p])
        assert nums[p] == pivot
        assert all(i <= pivot for i in nums[p+1:]), (pivot, nums)
        
        # now the original nums[-1] is at index p
        if p + 1 == k:
            return pivot
        elif p + 1 > k:
            return self.findKthLargest(nums[:p], k)
        else:
            return self.findKthLargest(nums[p+1:], k-p-1)

        
