class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        for h in range(1, max(height) + 1):
            left = None
            for i in range(len(height)):
                if left is None:
                    if height[i] >= h:
                        left = i
                else:
                    if height[i] >= h:
                        right = i
                        volume += (right - left - 1)
                        left = i
        return volume
