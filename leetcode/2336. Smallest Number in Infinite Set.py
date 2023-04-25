class SmallestInfiniteSet:

    def __init__(self):
        self.isPresent = set()
        self.container = []
        self.counter = 1

    def popSmallest(self) -> int:
        if len(self.container):
            minimum = heapq.heappop(self.container)
            self.isPresent.remove(minimum)
        else:
            minimum = self.counter
            self.counter += 1
        return minimum

    def addBack(self, num: int) -> None:
        if self.counter <= num or num in self.isPresent:
            return
        heapq.heappush(self.container, num)
        self.isPresent.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
