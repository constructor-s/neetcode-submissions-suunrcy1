class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for (p, s) in zip(position, speed)]
        cars.sort(reverse=True)

        duration = [(target - p) * 1.0/s for (p, s) in cars]

        print(duration)
        n = 0
        for i in range(len(duration)):
            if i == 0 or duration[i] > duration[i-1]:
                n += 1
            else:
                duration[i] = duration[i-1]
        return n
