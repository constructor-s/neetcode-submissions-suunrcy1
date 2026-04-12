class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = len(cost) - 1
        amt = 0
        looped = 0
        while True:
            amt = amt + cost[i] - gas[i]
            if amt <= 0:
                amt = 0
                if looped:
                    return i
            i -= 1
            if i < 0:
                looped += 1
                i %= len(gas)
                if looped == 2:
                    return -1
