# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ansLevel = -1
        if not root:
            return
        q = []
        level = 1
        q.append(root)
        maxSum = -float('inf')
        while q:
            localSum = 0
            n = len(q)
            for _ in range(n):
                tmp = q.pop(0)
                localSum += tmp.val
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            if maxSum < localSum:
                maxSum = max(maxSum, localSum)
                ansLevel = level
            level += 1

        return ansLevel
