class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = []
        for h in height:
            if not l_max:
                l_max.append(h)
            else:
                l_max.append(max(l_max[-1], h))

        r_max = []
        for h in reversed(height):
            if not r_max:
                r_max.append(h)
            else:
                r_max.append(max(r_max[-1], h))
        r_max.reverse()

        vol = 0
        for i in range(len(height)):
            if i == 0:
                continue
            elif i == len(height) - 1:
                continue
            else:
                vol += max(0, min(l_max[i-1], r_max[i+1]) - height[i])
        
        return vol
