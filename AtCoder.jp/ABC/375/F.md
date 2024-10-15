## [F - Road Blocked](https://atcoder.jp/contests/abc375/tasks/abc375_f)

<details><summary> Japanese </summary><br>
  
都市を頂点、道路を辺としたグラフの問題として考えます。

クエリを逆から処理することで、辺削除クエリのかわりに辺追加クエリがあるとみなせます。

辺追加クエリがなければワーシャルフロイド法による $O(N^3)$ の前計算の下、クエリに $O(1)$ で答えることができます。

辺追加クエリの処理を考えます。頂点 $u$ から頂点 $v$ への辺が追加されたとき、頂点 $x$ から頂点 $y$ への最短経路は、新たに追加された辺を通るか通らないかによって

* 元と変わらない
* $x$ から $u$ への最短経路、$u$ から $v$、$v$ から $y$ への最短経路、をこの順に繋げたもの
* $x$ から $v$ への最短経路、$v$ から $u$、$u$ から $y$ への最短経路、をこの順に繋げたもの

のいずれかになります。よって、元々の全頂点間最短距離がわかっていればこれは $O(1)$ で求めることができ、全頂点間最短距離を $O(N^2)$ で更新できます。

以上より、辺削除クエリの回数を $T$ として、$O(N^3+TN^2+Q)$ でこの問題を解くことができました。

</summary><br>

---

Let's think of the problem as a graph where cities are vertices and roads are edges.

By processing queries in reverse order, we can treat edge removal queries as if they were edge addition queries.

If there are no edge addition queries, we can precompute using the Floyd-Warshall algorithm in $O(N^3)$ time, allowing us to answer each query in $O(1)$.

Now, consider handling edge addition queries. When an edge between vertex $u$ and vertex $v$ is added, the shortest path between vertex $x$ and vertex $y$ will either:

* Remain unchanged
* Be the shortest path from $x$ to $u$, followed by $u$ to $v$, and then $v$ to $y$
* Be the shortest path from $x$ to $v$, followed by $v$ to $u$, and then $u$ to $y$

Thus, if we know the original shortest distances between all pairs of vertices, we can determine this in $O(1)$ time, and update the shortest paths between all pairs of vertices in $O(N^2)$.

Therefore, given $T$ edge removal queries, the problem can be solved in $O(N^3 + TN^2 + Q)$.

<details><summary> C++ Floyd Warshall </summary><br>

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
const ll INF = 1e18;

struct Query {
     int type, x, y;
};

int main() {
    int n, m, q;
    cin >> n >> m >> q;

    vector<tuple<int, int, int>> to;

    rep(i, m){
        int a, b, c; 
        cin >> a >> b >> c;
        a--, b--;
        to.emplace_back(a, b, c);
    }

    vector<bool> blocked(m);

    vector<Query> qs;
    rep(qi, q){
        int type;
        cin >> type;

        if (type == 1){
            int i; 
            cin >> i;
            i--;
            blocked[i] = true;
            qs.emplace_back(type, i, -1);
        }
        else {
            int x, y;
            cin >> x >> y;
            x--, y--;
            qs.emplace_back(type, x, y);
        }
    }

    vector dist(n, vector<ll>(n, INF));

    rep(i, n) dist[i][i] = 0;

    rep(i, m) {
        if (!blocked[i]) {
            auto [a, b, c] = to[i];
            dist[a][b] = dist[b][a] = c;
        }
    }

    rep(k, n) rep(i, n) rep(j, n){
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
    }


    vector<ll> ans;

    for (int qi = q-1; qi >= 0; qi--){
        auto [type, x, y] = qs[qi];

        if (type == 1){
            auto [a, b, c] = to[x];

            rep(i, n) rep(j, n){
                dist[i][j] = min(dist[i][j], dist[i][a] + c + dist[b][j]);
                dist[i][j] = min(dist[i][j], dist[i][b] + c + dist[a][j]);
            }
        }
        else{
            ans.push_back(dist[x][y]);
        }
    }

    reverse(ans.begin(), ans.end());

    for (ll val : ans){
        if (val == INF) val = -1;
        cout << val << endl;
    }
    return 0;
}
```

</details><br>

<details><summary> C++ Dijkstra </summary><br>

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
const ll INF = 1e18;
template<class T, class U> inline bool chmin(T &a, const U& b){if (a > b) {a = b; return true;} return false; }

struct Query {
    int type, x, y;
    Query(int type, int x, int y) : type(type), x(x), y(y) {}
};

struct Edge {
    int u, v;
    ll c;
    Edge(int u, int v, ll c) : u(u), v(v), c(c) {}
};

int main() {
    int n, m, q;
    cin >> n >> m >> q;

    vector<Edge> edges;  
    rep(i, m) {
        int a, b;
        ll c;
        cin >> a >> b >> c;
        a--, b--;
        edges.emplace_back(a, b, c);
    }

    vector<bool> blocked(m, false); 

    vector<Query> qs;

    rep(qi, q) {
        int type;
        cin >> type;
        if (type == 1) {
            int i;
            cin >> i;
            i--;
            blocked[i] = true;
            qs.emplace_back(type, i, -1);
        } else {
            int x, y;
            cin >> x >> y;
            x--, y--;
            qs.emplace_back(type, x, y);
        }
    }

    vector<vector<Edge>> to(n);
    rep(i, m) {
        if (!blocked[i]) { 
            auto &[a, b, c] = edges[i];
            to[a].emplace_back(a, b, c);
            to[b].emplace_back(b, a, c);
        }
    }
    
    vector dist(n, vector<ll>(n, INF));
    rep(i, n) dist[i][i] = 0;
    vector<bool> visited(n, false);

    function<void(int, vector<ll>&)> dijkstra = [&](int s, vector<ll>& dist) -> void {
        rep(i, n) dist[i] = INF;
        dist[s] = 0;
        vector<bool>seen(n, false);

        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
        pq.emplace(0, s);
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (seen[u]) continue;
            seen[u] = true;
            for (auto [a, b, c] : to[u]){
                if (seen[b]) continue;
                if (dist[b] > dist[u] + c){
                    dist[b] = dist[u] + c;
                    pq.emplace(dist[b], b);
                }
            }
        }
    };

    rep(i, n) dijkstra(i, dist[i]);

    vector<ll> ans;

    for (int qi = q-1; qi >= 0; qi--){
        auto [type, x, y] = qs[qi];

        if (type == 1){
            auto [a, b, c] = edges[x];
            to[a].emplace_back(a, b, c);
            to[b].emplace_back(b, a, c);
            chmin(dist[a][b], c);
            chmin(dist[b][a], c);

            rep(i, n) rep(j, n){
                chmin(dist[i][j], dist[i][a] + c + dist[b][j]);
                chmin(dist[i][j], dist[i][b] + c + dist[a][j]);
            }
        }
        else{
            ans.emplace_back(dist[x][y]);
        }
    }
    reverse(ans.begin(), ans.end());

    for (ll val : ans){
        if (val == INF) val = -1;
        cout << val << endl;
    }

    return 0;
}
```

</details><br>
