class Solution:
    def isWinner(self, one: List[int], two: List[int]) -> int:
        diff = self.score(one) - self.score(two)
        return 1 if diff > 0 else 2 if diff < 0 else 0

    def score(self, player):
        total = 0
        for i in range(len(player)):
            
            if (i and player[i-1] == 10) or (i >= 2 and player[i-2] == 10):
                total += 2 * player[i]
            else:
                total += player[i]
                
        return total
