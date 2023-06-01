class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.travel_times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        travel_time = t - start_time
        self.travel_times[(start_station, stationName)].append(travel_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_times = self.travel_times[(startStation, endStation)]
        return sum(travel_times) / len(travel_times)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
