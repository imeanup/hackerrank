# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i = 0
        j = 0
        q = deque()
        ans = list()
        while j < n:
            while q:
                if nums[j] > q[-1]:
                    q.pop()
                else:
                    break
            q.append(nums[j])

            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                ans.append(q[0])
                if nums[i] == q[0]:
                    q.popleft()
                i += 1
                j += 1
        return ans
