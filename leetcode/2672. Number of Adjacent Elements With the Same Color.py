class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0] * n
        answer = []
        same_color_count = 0
        for index, color in queries:
            if nums[index] == color:
                answer.append(same_color_count)
                continue
            if index > 0 and nums[index - 1] == nums[index] and nums[index] != 0:
                same_color_count -= 1
            if index < n - 1 and nums[index + 1] == nums[index] and nums[index] != 0:
                same_color_count -= 1
            nums[index] = color
            if index > 0 and nums[index - 1] == nums[index]:
                same_color_count += 1
            if index < n - 1 and nums[index + 1] == nums[index]:
                same_color_count += 1
            answer.append(same_color_count)
        return answer
