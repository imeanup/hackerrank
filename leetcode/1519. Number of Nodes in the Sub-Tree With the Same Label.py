from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Create adjacency list
        v = defaultdict(list)
        for x, y in edges:
            v[x].append(y)
            v[y].append(x)
        
        # Create count array
        s = [[0] * 26 for _ in range(n)]
        res = [0] * n
        
        def dfs(x, pre):
            # Count the number of occurrences of the label of the current node
            s[x][ord(labels[x]) - ord('a')] += 1
            
            # Visit the children of the current node
            for y in v[x]:
                if y == pre:
                    continue
                dfs(y, x)
                
                # Add the count of each label in the children to the current node's count
                for i in range(26):
                    s[x][i] += s[y][i]
            
            # Store the count of the current node's label in the result array
            res[x] = s[x][ord(labels[x]) - ord('a')]
        
        # Start the DFS from the root node
        dfs(0, -1)
        return res
