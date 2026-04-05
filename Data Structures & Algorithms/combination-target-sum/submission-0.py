class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = [set() for _ in range(target + 1)] # sums[i] are the combinations to reach a sum of i

        for targ in range(target+1):
            for n in nums:
                if targ - n == 0:
                    sums[targ].add((n, ))
                elif targ - n > 0:
                    for comb in sums[targ - n]:
                        sums[targ].add(tuple(sorted(
                            list(comb) + [n]
                        )))
        
        return [list(i) for i in sums[targ]]
