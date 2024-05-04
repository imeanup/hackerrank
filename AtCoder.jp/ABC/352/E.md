## [E - Clique Connect](https://atcoder.jp/contests/abc352/tasks/abc352_e)

<!-- 
**解説**

---

最小全域木を求めるアルゴリズムの  $1$ つにクラスカル法があります。クラスカル法は簡単には以下のようなアルゴリズムです。

* どの辺もグラフに追加されていない状態から初めて、重みが小さい順に各辺を見ていく。今見ている辺の端点を  $u, v$ としたとき、頂点  $u, v$ がまだ連結でないならば、その辺をグラフに追加する。

グラフの連結性を union-find などのデータ構造でうまく管理すれば、このアルゴリズムはソート部分がボトルネックとなって  $(O(E\log E))$ の計算量で動作します（ $E$ は辺の数）。

しかし、本問題においては辺の数が最大で  $O((\sum K)^2)$ 本程度あるためこのままでは間に合いません。そこで、最小全域木に関する以下の性質を用います。

* 以下を満たす辺 $e=(u, v)$ が存在する場合、辺 $e$ を候補から消してしまっても最小全域木に含まれる辺の重みの総和は変化しない。
  * 頂点 $u$ と頂点 $v$ を結ぶパスであって、辺 $e$ の重み以下の辺のみで構成され、かつ辺 $e$ を含まないようなものが存在する。

正当性はクラスカル法の動作を考えると分かります（辺 $e$ の順番になったときには  $u, v$ は既に連結になっているので、辺 $e$ が使われることはない）。本問題において $i$ 回目の操作で追加される辺は

> $\{A_{i, 1}, A_{i, 2}, \cdots, A_{i, K} \}$ に含まれる異なる $2$ 頂点の組  $u, v$ 全てについて、頂点 $u$ と頂点 $v$ の間を結ぶ重み $C_i$ の辺

でしたが、上記の性質を用いれば、実際には以下の辺だけを追加することにしてもよいと分かります。

> 各 $j = 2, 3, \cdots, K_i$ について、$A_{i, 1}$ と $A_{i, j}$ を結ぶ重み $C_i$ の辺

これによって辺の数の合計が $O(\sum K)$ 本となるので、あとはクラスカル法を適用することによって本問題を解くことができます。

実装例 (C++): -->

**Explanation**

---

One of the algorithms for finding the minimum spanning tree is Kruskal's algorithm. Kruskal's algorithm can be described as follows:

* Start with no edges added to the graph and consider each edge in ascending order of weight. If the endpoints $u, v$ of the current edge are not yet connected, add that edge to the graph.

By effectively managing the connectivity of the graph using data structures like union-find, this algorithm operates with a time complexity of $O(E\log E)$, where $E$ is the number of edges.

However, in this problem, the number of edges can be as large as $O((\sum K)^2)$, which makes the straightforward application of Kruskal's algorithm inefficient. Therefore, we utilize the following property related to the minimum spanning tree:

* If there exists an edge $e=(u, v)$ satisfying the following conditions, removing edge $e$ from consideration does not change the total weight of edges included in the minimum spanning tree:
  * There exists a path connecting vertices $u$ and $v$ composed only of edges with weights less than or equal to that of edge $e$, and this path does not include edge $e$.

The validity of this property can be understood by considering how Kruskal's algorithm operates (when edge $e$ is reached, vertices $u, v$ are already connected, so edge $e$ is not used). In this problem, the edges added in the $i$-th operation are:

> The edge with weight $C_i$ connecting every pair of distinct vertices $u, v$ in $\{A_{i, 1}, A_{i, 2}, \cdots, A_{i, K} \}$.

However, by utilizing the above property, it becomes apparent that we can add only the following edges:

> For each $j = 2, 3, \cdots, K_i$, the edge with weight $C_i$ connecting vertices $A_{i, 1}$ and $A_{i, j}$.

This reduces the total number of edges to $O(\sum K)$, allowing us to apply Kruskal's algorithm to solve the problem.

Implementation Example (C++):

```cpp
#include <bits/stdc++.h>
#include <atcoder/dsu>

using namespace std;
using namespace atcoder;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> k(m), c(m);
    vector<vector<int>> a(m);
    for (int i = 0; i < m; i++) {
        cin >> k[i] >> c[i];
        a[i].resize(k[i]);
        for (int &j: a[i]) {
            cin >> j;
            --j;
        }
    }
    vector<int> ord(m);
    iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int i, int j) { return c[i] < c[j]; });
    dsu uf(n);
    long long ans = 0;
    for (int i: ord) {
        for (int j = 1; j < k[i]; j++) {
            if (uf.same(a[i][0], a[i][j])) continue;
            uf.merge(a[i][0], a[i][j]);
            ans += c[i];
        }
    }
    cout << (uf.groups().size() == 1 ? ans : -1) << endl;
}
```