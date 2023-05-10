# https://en.wikipedia.org/wiki/Modular_exponentiation

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(''.join(map(str, b)))
        return self.modPow(a, b, 1337)

    def modPow(self, b, e, m):
        if m == 1:
            return 0
        r = 1
        b = b % m
        while e > 0:
            if e % 2 == 1:
                r = (r * b) % m
            b = (b * b) % m
            e = e >> 1
        return r
