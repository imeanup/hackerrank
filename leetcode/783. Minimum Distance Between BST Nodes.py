# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.inorderTraversal(root)
        
        return self.minDistance
    
    def __init__(self):
        self.minDistance = sys.maxsize
        self.prevValue = None

    def inorderTraversal(self, root):
        if root is None:
            return
        
        self.inorderTraversal(root.left)

        if self.prevValue is not None:
            self.minDistance = min(self.minDistance, root.val - self.prevValue.val)
        
        self.prevValue = root
        
        self.inorderTraversal(root.right)
