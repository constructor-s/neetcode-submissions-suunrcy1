class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        for i in range(len(hand) // groupSize):
            start = hand[0]
            for i in range(groupSize):
                if start + i in hand:
                    hand.remove(start + i)
                else:
                    return False

        return True
        