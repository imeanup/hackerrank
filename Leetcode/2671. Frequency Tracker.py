class FrequencyTracker:

    def __init__(self):
        self.numbers = {}
        self.frequencies = {}

    def add(self, number: int) -> None:
        if number in self.numbers:
            self.frequencies[self.numbers[number]] -= 1
            if self.frequencies[self.numbers[number]] == 0:
                del self.frequencies[self.numbers[number]]
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1
        if self.numbers[number] in self.frequencies:
            self.frequencies[self.numbers[number]] += 1
        else:
            self.frequencies[self.numbers[number]] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.numbers:
            self.frequencies[self.numbers[number]] -= 1
            if self.frequencies[self.numbers[number]] == 0:
                del self.frequencies[self.numbers[number]]
            self.numbers[number] -= 1
            if self.numbers[number] == 0:
                del self.numbers[number]
            elif self.numbers[number] in self.frequencies:
                self.frequencies[self.numbers[number]] += 1
            else:
                self.frequencies[self.numbers[number]] = 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.frequencies

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
