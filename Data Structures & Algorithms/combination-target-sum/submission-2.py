class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def get_paths(nums, remaining):
            if remaining == 0:
                return [[]]
            results = []
            for i in range(len(nums)):
                if nums[i] > remaining:
                    break # pruning
                results.extend(
                    p + [nums[i]] for p in get_paths(nums[i:], remaining - nums[i])
                )
            return results
        
        return get_paths(nums, target)
