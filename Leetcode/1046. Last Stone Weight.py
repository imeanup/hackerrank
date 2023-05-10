# https://leetcode.com/problems/last-stone-weight/description/

from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            if x != y:
                heappush(stones, y - x)
            else: 
                continue
        return -heappop(stones) if stones else 0

    
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort(reverse=True)
            y = stones.pop(0)
            x = stones.pop(0)
            if x != y:
                stones.append(y - x)
            else: 
                continue
        return stones[0] if stones else 0
