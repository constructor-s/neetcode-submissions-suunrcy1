class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # print(bin(n))
            res = res + ((n & 1) << (31 - i))
            # print(bin(res))
            n = n >> 1
            if n == 0:
                break
        return res
