## [F - MST Query](https://atcoder.jp/contests/abc355/tasks/abc355_f)

<details><summary><b>Japanese</b></summary>

辺の重みの最大値を $W = 10$ とします．グラフ $G$ の部分グラフであって，$G$ の辺のうち重みが $k$ 以下であるものからなる（重みなし）グラフを $G_k (0 \le k \le W)$ とします．グラフ $H$ の連結部分数を $c(H)$ とするとき，グラフ $G$ の MST （最小全域木）に含まれる辺の重みの和は $\Big( \sum_{k=0}^{W-1} c(G_k) - 1 \Big)$ と等しくなります．

（証明）
（方針 1） $G$ の MST に含まれる辺のうち，重みが $k$ **以下** であるものは $N - c(G_k)$ 個です（クラスカル法のアルゴリズムより，重みが小さい辺を MST に追加できるだけ追加するべきであるため）．したがって，重みが **ちょうど** $k$ であるものは $(N - c(G_k)) - (N - c(G_{k-1})) = c(G_{k-1}-c(G_k))$ 個あり，グラフ $G$ の MST に含まれる辺の重みの和は $\sum_{k=1}^W k(c(G_{k-1}) -c(G_k)) = \Big( \sum_{k-0}^{W-1} c(G_k) \Big) - W\cdot c(G_W) = \Big(\sum_{k=0}^{W-1} c(G_k)-1\Big)$ です．

（方針 2）$G$ の MST に含まれる辺のうち，重みが $k$ 以上のものは $c(G_{k-1}) - 1$ 個です（$G_{k-1}$ を連結にするためには $c(G_{k-1}) - 1$ 個の辺を追加する必要があるため）．したがって，主客転倒によりグラフ $G$ の MST に含まれる辺の重みの和は $\Big( \sum_{k=1}^W c(G_{k-1}) - 1\Big) = \Big(\sum_{k=0}^{W-1}c(G_k)-1 \Big)$ です（証明終）

各 $k(0\le k < W)$ に対して， $G_k$ の連結成分数を Union-Find で管理することによってこの問題を計算量 $O(W(N+Q)\propto (N))$ で解くことができます．（計算量は $O((WN + Q)\propto (N))$ に落とすことが可能です．）

以下の実装例では次のような工夫をしています．

</details><br>

* $G$ には最初から $N-1$ 個の重み $10$ の辺 $\{1, 2\}, \{1, 3\}, \dots, \{1, N\}$ が貼られており，$N-1+Q$ 個の辺追加クエリがあるとみなす．
* 答えを直接管理する．最初の時点では $c(G_k) = N(0 \le k < 10)$ であるため $ans = 10N-10$ である．各クエリに対して，連結成分数が減るごとに答えを更新する．

Let's assume the maximum weight of an edge is $W = 10$. We define $G_k (0 \leq k \leq W)$ as the subgraph of graph $G$ that consists of the edges in $G$ with weights not exceeding $k$. Let $c(H)$ denote the number of connected components in a graph $H$. The sum of the weights of the edges in the MST (Minimum Spanning Tree) of graph $G$ is equal to $\left( \sum_{k=0}^{W-1} c(G_k) - 1 \right)$.

(Proof)
(Approach 1) Among the edges included in the MST of $G$, the number of edges with weights **not exceeding** $k$ is $N - c(G_k)$ (according to Kruskal's algorithm, where edges with smaller weights are added to the MST as much as possible). Thus, the number of edges with weights **exactly** $k$ is $(N - c(G_k)) - (N - c(G_{k-1})) = c(G_{k-1}) - c(G_k)$. Therefore, the sum of the weights of the edges in the MST of graph $G$ is $\sum_{k=1}^W k (c(G_{k-1}) - c(G_k)) = \left( \sum_{k=0}^{W-1} c(G_k) \right) - W \cdot c(G_W) = \left( \sum_{k=0}^{W-1} c(G_k) - 1 \right)$.

(Approach 2) Among the edges included in the MST of $G$, the number of edges with weights at least $k$ is $c(G_{k-1}) - 1$ (since $c(G_{k-1}) - 1$ edges are needed to make $G_{k-1}$ connected). Therefore, by reversing the perspective, the sum of the weights of the edges in the MST of graph $G$ is $\left( \sum_{k=1}^W c(G_{k-1}) - 1 \right) = \left( \sum_{k=0}^{W-1} c(G_k) - 1 \right)$. (End of proof)

This problem can be solved in $O(W(N + Q))$ time complexity by managing the number of connected components of $G_k$ for each $k(0 \leq k < W)$ using Union-Find. (The time complexity can be reduced to $O((WN + Q) \log(N))$).

In the following implementation example, the following optimizations are made:

* Initially, graph $G$ has $N-1$ edges with weight $10$ connecting nodes $\{1, 2\}, \{1, 3\}, ..., \{1, N\}$, and there are $N-1 + Q$ edge addition queries.
* The answer is managed directly. Initially, $c(G_k) = N$ for $0 \leq k < 10$, so $ans = 10N - 10$. For each query, the answer is updated whenever the number of connected components decreases.

<details><summary>Python <b>Code</b></summary><br>

```py
from atcoder.dsu import DSU

N, Q = map(int, input().split())
uf = [DSU(N + 1) for i in range(10)]
ans = 10 * N - 10
for i in range(N - 1 + Q):
    a, b, c = map(int, input().split())
    for j in range(c, 10):
        if not uf[j].same(a, b):
            ans -= 1
            uf[j].merge(a, b)
    if i >= N - 1:
        print(ans)
```

</details>