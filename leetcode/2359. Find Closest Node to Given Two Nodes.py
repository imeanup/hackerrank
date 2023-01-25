# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf') for _ in range(n)]
        dist2 = [float('inf') for _ in range(n)]
        self.bfs(node1, edges, dist1)
        self.bfs(node2, edges, dist2)
        minDistNode = -1
        minDistTillNow = float('inf')
        for currNode in range(n):
            if minDistTillNow > max(dist1[currNode], dist2[currNode]):
                minDistNode = currNode
                minDistTillNow = max(dist1[currNode], dist2[currNode])
        return minDistNode

    def bfs(self, startNode, edges, dist):
        n = len(edges)
        q = []
        q.append(startNode)
        visited = [False]*n
        dist[startNode] = 0
        while q:
            node = q.pop(0)
            if visited[node]:
                continue
            visited[node] = True
            nbr = edges[node]
            if nbr != -1 and visited[nbr] == False:
                dist[nbr] = 1 + dist[node]
                q.append(nbr)
