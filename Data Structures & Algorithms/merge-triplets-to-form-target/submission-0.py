class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False] * len(target)
        for i in range(len(triplets)):
            for j in range(len(target)):
                if triplets[i][j] > target[j]:
                    break
            else:
                for j in range(len(target)):
                    assert triplets[i][j] <= target[j]
                    if triplets[i][j] == target[j]:
                        found[j] = True

        return all(found)
