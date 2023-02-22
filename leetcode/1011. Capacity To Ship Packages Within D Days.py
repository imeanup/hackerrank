class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_load, max_load = 0, 0
        for weight in weights:
            total_load += weight
            max_load = max(max_load, weight)
        l, r = max_load, total_load
        while l < r:
            mid = (l + r) // 2
            if self.feasible(weights, mid, days):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, weights, c, days):
        days_needed, current_load = 1, 0
        for weight in weights:
            current_load += weight
            if current_load > c:
                days_needed += 1
                current_load = weight
        return days_needed <= days
