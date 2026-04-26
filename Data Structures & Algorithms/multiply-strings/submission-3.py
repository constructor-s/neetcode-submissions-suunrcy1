class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        c2i = lambda c: ord(c) - ord('0')
        i2c = lambda i: chr(ord('0') + i)
        def f(num1, num2):
            if len(num2) == 1:
                product = 0
                for i in range(len(num1)):
                    product += c2i(num1[-i-1]) * c2i(num2) * (10 ** i)
                return product
            else:
                product = 0
                for i in range(len(num2)):
                    product += f(num1, num2[-i-1]) * (10 ** i)
                return product

        i = f(num1, num2)
        res = []
        while i:
            res.append(i2c(i % 10))
            i = i // 10
        res.reverse()
        if not res:
            return "0"
        else:
            return "".join(res)
