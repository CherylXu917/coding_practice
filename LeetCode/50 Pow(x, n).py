class Solution:
    # recursion
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1
        elif n < 0:
            return self.myPow(1 / x, -n)
        if n % 2:
            return self.myPow(x * x, n // 2) * x
        else:
            return self.myPow(x * x, n // 2)


    # iteration
    def myPow2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x, n = 1/x, -n
        res = 1
        while n > 1:
            if n % 2:
                res *= x
            x = x * x
            n = n // 2
        res *= x
        return res

