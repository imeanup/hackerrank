class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []
        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                mp[num] = stack[-1]
            else:
                mp[num] = -1
            stack.append(num)
            # print(stack)

        # print(mp)
        return [mp[num] for num in nums1]
