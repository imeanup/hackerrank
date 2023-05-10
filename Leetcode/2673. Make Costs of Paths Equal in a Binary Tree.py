class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def dfs(node):
            if node > n:
                return 0
            left = dfs(node * 2)
            right = dfs(node * 2 + 1)
            max_cost = max(left, right)
            res[0] += 2 * max_cost - (left + right)
            return max_cost + cost[node - 1]
        res = [0]
        dfs(1)
        return res[0]
