class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        left = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]: # can expand beyond stack[-1]
                stack.pop()
            if stack:
                left[i] = stack[-1] + 1
            else:
                left[i] = 0
            stack.append(i)

        right = [-1] * len(heights)
        stack.clear()
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = len(heights)
            stack.append(i)
        
        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(
                maxArea,
                heights[i] * (right[i] - left[i])
            )
        print(left)
        print(right)
        return maxArea
            
