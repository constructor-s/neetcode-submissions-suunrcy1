from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        res = []
        corp = list(corpus)
        for _ in range(num_merges):
            counts = {}
            for i in range(len(corp) - 1):
                pair = (corp[i], corp[i+1])
                counts[pair] = counts.get(pair, 0) + 1
            
            # max_pair = max(counts, key=counts.get)
            max_count = max(counts.values())
            max_pair = None
            for pair, count in counts.items():
                if count == max_count:
                    if max_pair is None:
                        max_pair = pair
                    elif pair < max_pair:
                        max_pair = pair
            res.append(max_pair)

            corp_new = []
            i = 0
            while i < len(corp) - 1:
                pair = (corp[i], corp[i+1])
                if pair == max_pair:
                    corp_new.append(corp[i]+corp[i+1])
                    i += 2
                else:
                    corp_new.append(corp[i])
                    i += 1
            if i == len(corp) - 2:
                corp_new.append(corp[i+1])
            corp = corp_new
                
        return res
