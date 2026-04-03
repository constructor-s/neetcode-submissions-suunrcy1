class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            while numbers[i] + numbers[j] > target:
                # decrement right
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            i += 1
