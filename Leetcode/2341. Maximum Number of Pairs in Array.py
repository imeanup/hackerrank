class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        answer = [0,len(nums)]
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[i] = -1
                answer[0] += 1
                answer[1] -= 2
        return answer
