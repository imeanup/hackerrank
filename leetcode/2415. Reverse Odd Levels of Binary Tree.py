# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level += 1
            if level%2 != 0:
                self.swap(q)
        return root
        
    def swap(self, q):
        for i in range(len(q)//2):
            a = q[i]
            b = q[len(q)-1-i]
            a.val, b.val = b.val, a.val
