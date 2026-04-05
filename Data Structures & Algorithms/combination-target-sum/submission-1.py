class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = [[] for _ in range(target + 1)] # sums[i] are the combinations to reach a sum of i

        for n in nums:
            sums[n].append([n])
            for targ in range(n + 1, target + 1):
                for comb in sums[targ - n]:
                    sums[targ].append(comb + [n])
        
        return sums[targ]
