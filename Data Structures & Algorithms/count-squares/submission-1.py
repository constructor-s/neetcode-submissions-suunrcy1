from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.d = defaultdict(lambda : 0)

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        count = 0
        x0, y0 = point
        for (x1, y1), counts in list(self.d.items()):
            if abs(x1 - x0) == abs(y1 - y0) > 0: # a valid diagonal
                count += self.d[(x1, y1)] * self.d[(x1, y0)] * self.d[(x0, y1)]
        return count
