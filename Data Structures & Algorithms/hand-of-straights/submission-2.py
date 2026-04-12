from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        groups = 0
        while groups < len(hand) // groupSize:
            x = next(iter(counts.keys()))
            while x - 1 in counts:
                x -= 1
            
            for i in range(groupSize):
                if x + i not in counts:
                    return False
                counts[x+i] -= 1
                if counts[x+i] == 0:
                    del counts[x+i]
                
            groups += 1
        
        return True
        