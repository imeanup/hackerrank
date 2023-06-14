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
