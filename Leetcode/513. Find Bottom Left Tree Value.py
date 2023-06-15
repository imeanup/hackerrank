# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        leftMost = None
        
        def dfs(node, depth):
            nonlocal max_depth, leftMost
            if not node:
                return
            if depth > max_depth:
                max_depth = depth
                leftMost = node.val 
            dfs(node.left, depth+1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        
        return leftMost

            
        
# BFS
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def bfs(node):
            if not node:
                return 
            q = [node]
            while q:
                for _ in range(len(q)):
                    curr = q.pop(0)
                    if curr.right:
                        q.append(curr.right)
                    if curr.left:
                        q.append(curr.left)
                    
            return curr.val

        return bfs(root)
