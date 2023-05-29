class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        n = len(nums)
        par = list(range(n))
        size = [1] * n

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if size[rx] < size[ry]:
                    rx, ry = ry, rx
                par[ry] = rx
                size[rx] += size[ry]

        def prime_factors(num):
            factors = set()
            while num % 2 == 0:
                factors.add(2)
                num //= 2
            for i in range(3, int(num**0.5)+1, 2):
                while num % i == 0:
                    factors.add(i)
                    num //= i
            if num > 2:
                factors.add(num)
            return factors

        pidx = defaultdict(list)
        for i, num in enumerate(nums):
            factors = prime_factors(num)
            for factor in factors:
                pidx[factor].append(i)

        for indices in pidx.values():
            for i in range(1, len(indices)):
                union(indices[i-1], indices[i])

        return len(set(find(i) for i in range(n))) == 1

