"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        q = deque([root])
        
        while q:
            rightNode = None
            
            for _ in range(len(q)):
                rem = q.popleft()
                rem.next, rightNode = rightNode, rem
                
                if rem.right:
                    q.extend([rem.right, rem.left])
        return root
        
        
        
