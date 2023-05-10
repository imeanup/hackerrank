# https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=study-plan&id=level-2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_ = 0

        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            self.max_ = max(self.max_, left + right)

            return max(left, right) + 1

        height(root)
        return self.max_
