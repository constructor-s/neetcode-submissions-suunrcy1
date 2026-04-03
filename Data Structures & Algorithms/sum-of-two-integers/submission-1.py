"""
x   y
0 + 0 -> bit 0, carry 0
0 + 1 -> bit 1, carry 0
1 + 0 -> bit 1, carry 0
1 + 1 -> bit 0, carry 1
        x XOR y  x AND y

2-bit int
0b00 -> 0 0
0b01 -> 1 1
0b10 -> 2 -1
0b11 -> 3 -2
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        for i in range(32):
            bit = (a & 0b1) ^ (b & 0b1) ^ carry
            carry = (
                ((a & 0b1) & (b & 0b1)) |
                ((a & 0b1) & carry) |
                (carry & (b & 0b1))
            )
            a = a >> 1
            b = b >> 1
            result = result | (bit << i)

        if result > 0x7FFFFFFF:
            result = ~(result ^ 0xFFFFFFFF)

        return result
