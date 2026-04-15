class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum2ways = {0: 1}
        for n in nums:
            s2w = {}
            for s, w in sum2ways.items():
                s2w[s+n] = s2w.get(s+n, 0) + w
                s2w[s-n] = s2w.get(s-n, 0) + w
            sum2ways = s2w
        return sum2ways.get(target, 0)
