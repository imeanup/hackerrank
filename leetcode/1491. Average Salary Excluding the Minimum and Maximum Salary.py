class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = float('inf')
        maxSalary = -float('inf')
        sum_ = 0
        for s in salary:
            sum_ += s
            minSalary = min(minSalary, s)
            maxSalary = max(maxSalary, s)

        return (sum_ - minSalary - maxSalary) / (len(salary) - 2)
