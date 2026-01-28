#### Problem: 

Find the maximum matching in a Bipartite Graph. A matching is a set of edges without common vertices.

**Complexity**: $O(E \sqrt{V})$, where $E$ -> no of edge, $V$ -> no of vertices
**Memory**: $O(V+E)$, depends mainly by edges and \sqrt{n+m}. `n/m` near $10^9$ is infeasible. 

Alternate: DFS/BFS based Max Flow (Ford-Fulkerson). Complexity: $O(V\cdot E)$ for bipartite matching.

#### How it works

The algorithm relies on the concept of  **Augmenting Paths** : paths that start at an unmatched vertex on the left, alternate between unmatched and matched edges, and end at an unmatched vertex on the right. Flipping the edges along this path increases the size of the matching by 1.

Hopcroft-Karp improves upon standard algorithms by finding **multiple augmenting paths** simultaneously in phases:

1. **BFS Phase (Build Level Graph):**
   * It runs a Breadth-First Search starting from **all** unmatched vertices on the left side simultaneously.
   * It calculates the distance (layer) to every reachable vertex.
   * It determines the length of the **shortest** augmenting path. If no augmenting path is found, the algorithm terminates.
2. **DFS Phase (Find Paths):**
   * It runs a Depth-First Search to actually find the augmenting paths.
   * Crucially, the DFS is restricted to follow the "layers" defined by the BFS (only moving from distance **$k$** to **$k+1$**). This ensures we only find **shortest** augmenting paths.
   * It finds a **maximal set** of disjoint shortest augmenting paths.

By finding the maximal set of shortest paths in one go, it can be proven that the length of the shortest augmenting path strictly increases with each phase, leading to the **$O(\sqrt{V})$** iteration bound.

### Why is it faster than Kuhn's (Standard DFS)?

Standard DFS (Kuhn's algorithm) may traverse the same long paths over and over again to find a single augmentation. Hopcroft-Karp ensures that we always augment along the **shortest** possible paths first. Since we find a maximal set of these shortest paths in one pass (**$O(E)$**), the "length" of the augmenting paths strictly increases. Since the max path length is **$V$**, it can be mathematically proven that the loop runs only **$\sqrt{V}$** times.

```cpp
template<typename T = int>
struct HopcroftKarp {
    T n, m;
    vector<vector<T>> adj;
    vector<T> dist, pairU, pairV;

    HopcroftKarp(T n, T m) : n(n), m(m) {
        adj.assign(n, {});
        dist.assign(n, 0);
        pairU.assign(n, -1);
        pairV.assign(m, -1);
    }

    void add_edge(T u, T v) {
        adj[u].push_back(v);
    }

    bool bfs() {
        queue<T> q;
        for (T u = 0; u < n; u++) {
            if (pairU[u] == -1) {
                dist[u] = 0;
                q.push(u);
            }
            else 
                dist[u] = -1;
        }
        bool found = false;
        while (!q.empty()) {
            T u = q.front(); q.pop();
            for (T v : adj[u]) {
                T nu = pairV[v];
                if (nu == -1) {
                    found = true;
                }
                else if (dist[nu] == -1) {
                    dist[nu] = dist[u] + 1;
                    q.push(nu);
                }
            }
        }
        return found;
    }

    bool dfs(T u) {
        for (T v : adj[u]) {
            T nu = pairV[v];
            if (nu == -1 || (dist[nu] == dist[u] + 1 && dfs(nu))) {
                pairU[u] = v;
                pairV[v] = u;
                return true;
            } 
        }
        dist[u] = -1; 
        return false;
    }

    T operator()() { // run max matching
        T match = 0;
        while (bfs()) {
            for(T u = 0; u < n; u++) {
                if (pairU[u] == -1 && dfs(u)) 
                    match++;
            }
        }
        return match;
    }
};

signed main() {
    /*
    left partition size = 4 (0, 1, 2, 3)
    right partition size = 4 (0, 1, 2, 3)
    */
    HopcroftKarp<int> hk(4, 4);
    // add edges (u -> left, v -> right)
    hk.add_edge(0, 0);
    hk.add_edge(0, 1);
    hk.add_edge(1, 0);
    hk.add_edge(1, 2);
    hk.add_edge(2, 2);
    hk.add_edge(2, 3);
    hk.add_edge(3, 3);

    cout << hk() << endl;
    cout << "Matches: " << "\n";
    for (int u = 0; u < 4; u++) {
        if(hk.pairU[u] != -1) {
            cout << "Left: " << u << " -> with right: " << hk.pairU[u] << endl;
        }
    }
    return 0;
}
// n, m ~1e5 with E ~1e5..1e6   
// Use sparse or arbitary strigns when 10^9
```
