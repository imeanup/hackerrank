class Solution:
    def countBlackBlocks(self, m: int, n: int, coo: List[List[int]]) -> List[int]:
        count = [0] * 5
        blocks = {}
        for x, y in coo:
            for i in range(max(0, x - 1), min(m - 1, x + 1)):
                for j in range(max(0, y - 1), min(n - 1, y + 1)):
                    if (i, j) not in blocks:
                        blocks[(i, j)] = 0
                    count[blocks[(i, j)]] -= 1
                    blocks[(i, j)] += 1
                    count[blocks[(i, j)]] += 1

        count[0] = (m - 1) * (n - 1) - sum(count[1:])
        return count
