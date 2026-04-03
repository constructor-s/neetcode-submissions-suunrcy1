class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest = 1

        for i in nums:
            if i - 1 not in nums: # beginning
                count = 1
                while i + count in nums:
                    count += 1
                if count > longest:
                    longest = count

        return longest
