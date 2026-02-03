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
