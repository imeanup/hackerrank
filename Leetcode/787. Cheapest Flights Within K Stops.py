# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for e in flights:
            adj[e[0]].append([e[1], e[2]])

        # print(adj)
        dist = [float('inf') for _ in range(n)]
        q = [[src, 0]]
        stops = 0
        while stops <= k and q:
            sz = len(q)
            while sz:
                node, distance = q.pop(0)   
                for neighbour, price in adj[node]:
                    if (price + distance >= dist[neighbour]): 
                        continue
                    dist[neighbour] = price + distance
                    q.append([neighbour, dist[neighbour]])
                sz -= 1
            stops += 1
        return -1 if dist[dst] == float('inf') else dist[dst]
