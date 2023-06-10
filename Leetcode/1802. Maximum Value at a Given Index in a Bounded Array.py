class Solution:
    def getSum(self, index, value, n):
        count = 0
        # left index
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
        # right index
        if value >= n - index:
            count += (value + value - (n - 1) + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value

        return count - value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left

    def constructArray(self, n: int, index: int, maxSum: int) -> [int]:
        max_value = self.maxValue(n, index, maxSum)
        result = [0] * n
        result[index] = max_value

        # left of the index
        current_value = max_value
        for i in range(index - 1, -1, -1):
            current_value = max(current_value - 1, 1)
            result[i] = current_value

        # right of the index
        current_value = max_value
        for i in range(index + 1, n):
            current_value = max(current_value - 1, 1)
            result[i] = current_value

        return result

solution = Solution()
print(solution.constructArray(4, 2, 6))
print(solution.constructArray(6, 1, 10))
print(solution.constructArray(8, 5, 13))

'''
 >> There will be an arithmetic sequence to its left, and (possibly) a consecutive sequence of 1s if nums[index] is less than the number of elements to the left.

If nums[index] is greater than or equal to the number of elements to its left, then there will be an arithmetic sequence to its left. This means that the values to the left of nums[index] will decrease by 1 for each position until it reaches 1.

If nums[index] is less than the number of elements to its left, then there will be an arithmetic sequence to its left followed by a consecutive sequence of 1s. This means that the values to the left of nums[index] will decrease by 1 for each position until it reaches 1, and then all remaining positions to the left will be filled with 1s.

For example, let’s say we have an array of length 6 with nums[index] = 4 at index 2. Since nums[index] is greater than the number of elements to its left (2), there will be an arithmetic sequence to its left. The resulting array would be [2, 3, 4, 3, 2, 1].

Now let’s say we have an array of length 6 with nums[index] = 2 at index 2. Since nums[index] is less than the number of elements to its left (2), there will be an arithmetic sequence to its left followed by a consecutive sequence of 1s. The resulting array would be [1, 1, 2, 1, 1, 1].

>> We need to determine the length of the arithmetic sequence based on the relative sizes of index and value.

If value is less than or equal to index, it means that there will be an arithmetic sequence from value to 1 and a continuous sequence of 1s with length index - value + 1. The length of the arithmetic sequence in this case would be value.

If value is greater than index, it means that there is only one arithmetic sequence on the left side of index, with the first item being value and the last item being value - index. The length of the arithmetic sequence in this case would be index + 1.

>> AP
An arithmetic progression (AP) is a sequence of numbers such that the difference between any two consecutive terms is constant. This constant difference is called the common difference of the arithmetic progression
Let a be the first term of the progression, d be the common difference, and n be the number of terms in the progression. Then, the formulas for an arithmetic progression are given by:

The nth term of an AP: an = a + (n - 1)d
The common difference of an AP: d = a2 - a1 = a3 - a2 = a4 - a3 = ... = an - an-1
The sum of the first n terms of an AP: Sn = n/2 (2a + (n - 1)d), where l is the last term of the arithmetic progression.
'''
