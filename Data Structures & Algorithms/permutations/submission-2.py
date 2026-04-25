from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def f(nums, remaining_idx, part):
            if len(part) == len(nums):
                res.append(part.copy())
            else:
                for _ in range(len(remaining_idx)):
                    # add number
                    i = remaining_idx.popleft()
                    part.append(nums[i])
                    # recurse
                    f(nums, remaining_idx, part)
                    # recover
                    assert part.pop() == nums[i]
                    remaining_idx.append(i)
                    
        f(nums, deque(range(len(nums))), [])
        return res
