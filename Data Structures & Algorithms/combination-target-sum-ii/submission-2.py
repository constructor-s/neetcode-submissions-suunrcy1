class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # return [cand] + combinationSum2({candidates}-cand, target-cand)
        candidates.sort()

        def search(candidates, target):
            res = []

            for i in range(len(candidates)):
                if i == 0 or candidates[i] != candidates[i-1]:
                    if target - candidates[i] == 0:
                        res.append([candidates[i]])
                    elif target - candidates[i] > 0:
                        res.extend(
                            [candidates[i]] + item for item in search(candidates[i+1:], target-candidates[i])
                        )
            return res

        return search(candidates, target)        
