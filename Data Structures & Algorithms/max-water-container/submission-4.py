class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = min(heights[0], heights[-1]) * (len(heights) - 1)

        if len(heights) == 2:
            return area

        if heights[0] < heights[-1]:
            return max(area, self.maxArea(heights[1:]))
        else:
            return max(area, self.maxArea(heights[:-1]))
