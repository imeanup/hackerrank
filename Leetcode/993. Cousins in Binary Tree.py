class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xDepth = yDepth = -1
        xPar = yPar = None

        def levelOrder(node):
            nonlocal xDepth, yDepth, xPar, yPar
            if not node:
                return
            q = []
            level = 0
            q.append((node, None))
            while q:
                n = len(q)
                for i in range(n):
                    tmp, parent = q.pop(0)
                    if tmp.val == x:
                        xDepth = level
                        xPar = parent
                    if tmp.val == y:
                        yDepth = level
                        yPar = parent

                    if tmp.left: q.append((tmp.left, tmp))
                    if tmp.right: q.append((tmp.right, tmp))

                level += 1

        levelOrder(root)
        return xDepth == yDepth and xPar != yPar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        info = {}
        def levelOrder(node):
            if not node:
                return
            q = []
            level = 0
            q.append((node, None))
            while q:
                levelSize = len(q)
                for i in range(levelSize):
                    tmp, parent = q.pop(0)
                    info[tmp.val] = (level, parent)
                    if (tmp.left): q.append((tmp.left, tmp))
                    if (tmp.right): q.append((tmp.right, tmp))
                level += 1

        levelOrder(root)
        # print(info)
        
        return info[x][0] == info[y][0] and info[x][1] != info[y][1]
