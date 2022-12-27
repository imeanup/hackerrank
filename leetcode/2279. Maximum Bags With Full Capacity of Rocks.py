class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        rcap = [c - r for c, r in zip(capacity, rocks)]
        rcap.sort()

        bag = 0

        for i in rcap:
            if additionalRocks >= i:
                additionalRocks -= i
                bag += 1
            else:
                break

        return bag
  
  def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]

        capacity.sort()

        for i, c in enumerate(capacity):
            if c > additionalRocks:
                return i
            additionalRocks -= c
        return len(capacity)
        
