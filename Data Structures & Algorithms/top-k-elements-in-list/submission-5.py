class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        top = list(counts.items()) # [(int - value, int - count)]
        if len(top) > k:
            for i in range(k, len(top)):
                for j in range(0, k):
                    if top[j][1] < top[i][1]:
                        top[j], top[i] = top[i], top[j]
                        # No break, continue swapping the rest
                        

        return [i[0] for i in top[:k]]
