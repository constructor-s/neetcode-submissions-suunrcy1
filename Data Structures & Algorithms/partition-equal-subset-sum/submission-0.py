class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # iff can find subset with sum = sum / 2
        target = sum(nums) / 2.0

        poss = set()
        for n in nums:
            for p in list(poss):
                if p + n == target:
                    return True
                poss.add(p + n)
            if n == target:
                return True
            poss.add(n)

        return False
