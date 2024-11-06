## [F - Add One Edge 2](https://atcoder.jp/contests/abc378/tasks/abc378_f)

問題文の条件を分かりやすく言い換えましょう。

頂点 $u,v$ を結ぶ辺を追加すると、$u−v$ パス上の頂点が閉路に含まれます。このことから、問題は、「頂点を $3$ 個以上含む単純パスであって、端点の次数が $2$ 、それ以外の頂点の次数が $3$ であるものの個数を求めよ。」と言い換えられます。

言い換え後の問題を木 DP により解きます。適当な頂点を選び、木を根付き木にします。

ここで、数えるパスの端点の LCA を考えます。すると、LCA は端点に一致するか、パス（端点除く）上の点に一致します。

まず、端点の LCA が端点に一致する場合を考えます。LCA の頂点を $u$ とすると、この場合数えたいパスの個数は $u$ の部分木に含まれる次数 $2$ の頂点であって、$u$ から次数 $3$ の頂点を $1$ 個以上取って到達できるものの個数に等しいです。これは木 DP でボトムアップに計算できます。

次に、端点のLCA が端点に一致しない場合を考えます。LCA の頂点を $u$ を考えます。 $u$ の部分木に含まれる次数 $2$ の頂点であって、$u$ から次数 $3$ の頂点を $1$ 個以上取って到達できるものの集合を $S$ とすると、求めるパスの個数は、$S$ から二つの頂点を選ぶ方法のうち、選んだ二つの頂点の LCA が $u$ に一致するものの個数と等しいです。

これは、$u$ 以下の部分木から $u$ を取り除くことで何個かの部分木に分かれますが、分かれた部分木の中から二つを選び、そこから頂点を選ぶ方法と等しく、こちらも同様の DP によって計算できます。

計算量は $O(N)$ です。

---

Let’s rephrase the problem conditions for clarity.

When an edge connecting vertices $u$ and $v$ is added, the vertices on the path from $u$ to $v$ form a cycle. This allows us to restate the problem as follows: **find the number of simple paths containing three or more vertices, where the endpoints have degree 2 and all other vertices have degree 3.**

We will solve this reformulated problem using tree dynamic programming (tree DP). First, select an appropriate vertex and convert the tree into a rooted tree.

Now, consider the **Lowest Common Ancestor (LCA)** of the path endpoints we are counting. The LCA can either match one of the endpoints or lie on a vertex within the path (excluding the endpoints).

* **Case 1:** The LCA matches one of the endpoints.

    Let $u$ be the LCA vertex. In this case, the number of paths we need to count is equal to the number of degree-2 vertices within $u$'s subtree that can be reached by taking at least one degree-3 vertex from $u$. This can be calculated using a bottom-up approach with tree DP.

* **Case 2:** The LCA does not match the endpoints.

    Again, let $u$ be the LCA. Define the set $S$ as the collection of degree-2 vertices in $u$'s subtree that can be reached by taking at least one degree-3 vertex from $u$. The number of paths we seek is then equivalent to the number of ways to select two vertices from $S$ such that their LCA is $u$.

To compute this, consider removing $u$ from its subtree, which separates it into several smaller subtrees. The required paths correspond to selecting two subtrees and then picking one vertex from each. This can also be computed using a similar DP approach.

The time complexity for this solution is $O(N)$.

<details><summary><b>c++</b></summary>

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()

int main() {
    int n;
    cin >> n;
    vector<vector<int>> to(n);
    rep(i, n-1){
        int u, v;
        cin >> u >> v;
        u--, v--;
        to[u].push_back(v);
        to[v].push_back(u);
    }

    // built the rooted tree, which helps in modifying the tree
    // to do this do dfs in the tree to add the child in the tree.
    function<vector<vector<int>>(int)> root_to_leaf = [&](int root) -> vector<vector<int>> {
        vector<vector<int>> res(n);   
        vector<bool> seen(n, false);
        seen[0] = true;
        auto dfs = [&](auto self, int u) -> void {
            for (auto v : to[u]){
                if (seen[v]) continue;
                seen[v] = true;
                res[u].emplace_back(v);
                self(self, v);
            }
        };
        dfs(dfs, 0);
        return res;
    };
    // dp using LCA
    auto h = root_to_leaf(0);
    ll res = 0;
    function<int(int)> dfs = [&](int u) -> int {
        if (to[u].size() == 2){
            for (auto v : h[u]){
                ll tmp = dfs(v);
                if(to[v].size() != 2) 
                    res += tmp;
            }
            return 1;
        }
        else if (to[u].size() == 3){
            vector<ll> dp(2, 0ll);
            for (auto v : h[u]){
                ll tmp = dfs(v);
                dp[1] += dp[0] * tmp;
                dp[0] += tmp;
            }
            res += dp[1];
            return dp[0];
        }
        else {
            for (auto v : h[u]){
                dfs(v);
            }
            return 0;
        }
    };
    dfs(0);
    cout << res << "\n";
    return 0;
}
```

</details><br>

---

**別解**

---

数えたいものは、頂点のペア $(u,v)$（ただし $u < v$）であって次の条件を満たすものの個数です。

* 頂点 $u,v$ の次数はともに $2$
* 頂点 $u,v$ を結ぶ単純パス上の頂点（$u,v$ を除く）の次数はすべて $3$

これは、次数 $3$ の頂点すべてからなる頂点集合が誘導する部分グラフの連結成分を列挙すれば求められます。各連結成分について、それと隣接する次数 $2$ の頂点の個数を $c$ とすると、その連結成分から $\dfrac{c(c−1)}{2}$ 個のペアが得られます。

---

**Alternative Solution**

---

What we want to count is the number of pairs of vertices $(u, v)$ (where $u < v$) that satisfy the following conditions:

* Both vertices $u$ and $v$ have degree 2.
* All vertices on the simple path connecting $u$ and $v$ (excluding $u$ and $v$) have degree 3.

To achieve this, we can enumerate the connected components of the subgraph induced by the set of all degree-3 vertices. For each connected component, let $c$ be the number of degree-2 vertices adjacent to that component. Then, from that component, we can obtain $\frac{c(c-1)}{2}$ pairs.

---

<details><summary>C++</summary><br>

```cpp
#include<bits/stdc++.h>
using namespace std;
#include <atcoder/dsu>
using namespace atcoder;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()

int main() {
    int n;
    cin >> n;
    vector<int> u(n-1), v(n-1);
    vector<int> deg(n, 0);
    rep(i, n-1){
        cin >> u[i] >> v[i];
        u[i]--, v[i]--;
        deg[u[i]]++;
        deg[v[i]]++;
    }

    dsu d(n);
    vector<int> c(n, 0);
    rep(i, n-1){
        if (deg[u[i]] == 3 && deg[v[i]] == 3){
            d.merge(u[i], v[i]);
        }
        else if (deg[u[i]] == 3 && deg[v[i]] == 2){
            c[u[i]]++;
        }
        else if (deg[u[i]] == 2 && deg[v[i]] == 3){
            c[v[i]]++;
        }
    }
    ll ans = 0;
    for (auto g : d.groups()){
        ll now = 0;
        for (auto v : g){
            now += c[v];
        }
        ans += now * (now-1)/2;
    }

    cout << ans << endl;
    return 0;
}
```

</details><br>
