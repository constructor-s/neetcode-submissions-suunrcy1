class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res_curr = [[]]
        for i in range(len(nums)):
            res_next = []
            for j in range(len(res_curr)):
                perm = res_curr[j]
                for k in range(len(perm) + 1):
                    res_next.append(
                        perm[:k] + [nums[i]] + perm[k:]
                    )
            res_curr = res_next
        return res_curr
