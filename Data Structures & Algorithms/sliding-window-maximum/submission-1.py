from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # stores indices
        l = 0
        r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            while q[0] < l:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
                r += 1
            else: # not enough for first window
                r += 1

        return res
