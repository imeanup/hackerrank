# Hint 1: If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same.
# Hint 2: If the range (high - low + 1) is odd, the solution will depend on the parity of high and low.
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - low//2
        
