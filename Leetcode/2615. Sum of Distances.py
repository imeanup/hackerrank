class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index = defaultdict(list)
        for i, num in enumerate(nums):
            index[num].append(i)
        # print(index)

        res = [0] * n
        for indices in index.values():
            m = len(indices)
            prefix_sum = [0] * (m + 1)
            for i in range(m):
                prefix_sum[i + 1] = prefix_sum[i] + indices[i]
            # print(prefix_sum)

            for i in range(m):
                res[indices[i]] = prefix_sum[m] - 2 * prefix_sum[i + 1] + indices[i] * (2 * i - m + 2)
            # print(res)

        return res
