class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sgn = -1
            x = -x
            max_int = 2 ** 31 - 1
        else:
            sgn = 1
            max_int = 2 ** 31
        res = 0

        while x:
            res *= 10
            res += x % 10
            x = x // 10
            if res > max_int:
                return 0
        return res * sgn
