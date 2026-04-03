class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        left = [nums[0]] # left[i] is the product from 0 to i inclusive
        right = [nums[-1]] # right[i] is the product from len-1 to len-i-1 inclusive
        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i])
        for i in range(len(nums)-2, -1, -1):
            right.append(right[-1] * nums[i])
        # print(left)
        # print(right)
        result = [right[len(nums)-2]]
        for i in range(1, len(nums)-1):
            result.append(left[i-1] * right[len(nums)-2-i])
            # print(result)
        result.append(left[len(nums)-2])
        return result
