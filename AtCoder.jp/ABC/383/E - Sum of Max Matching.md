## [E - Sum of Max Matching](https://atcoder.jp/contests/abc383/tasks/abc383_e)

まず、$f(x, y)$ の性質について考えます。

$f(x, y)$ は 重みが $w$ 以下である辺だけの部分グラフにおいて頂点 $x$ と頂点 $y$ が連結になるような $w$ としてありえる最小値と等しいです。このことから、相異なる $3$ 頂点 $x,y,z$ において $f(x,y) \le f(x,z)$ ならば $f(x,z)=f(y,z)$ が言えます。

これがどういう意味かというと、重み $w$ 以下の辺で連結である頂点 $x,y$ について、そのグラフにおいて連結でない頂点 $z$ とは $f(x,z)=f(y,z)$ であるということです。

また、この問題は $B$ を並べ替える問題から $A$ の要素と $B$ の要素をマッチングさせるというような言い換えができます。

よって、以下のような貪欲法が考えられます。以降、辺が重みの昇順でソートされていて、$w_1 \le w_2 \dots \le w_M$ であるとします。

* はじめに $N$ 頂点の辺がないグラフがある。また、各頂点についてその頂点が $A$ に含まれるかと、$B$ に含まれるかをそれぞれ管理します。
* $i = 1,2, \dots, M$ の順に以下を行う。

  * 頂点 $u_i, v_i$ が連結でない場合、グラフに辺 $\{u_i, v_i\}$ を追加する。 連結である場合は次の辺に行く。
  * 辺の追加によって異なる $2$ つの連結成分が連結になったとき、片方の連結成分に含まれる $A$ の頂点ともう片方に含まれる $B$ の頂点をペアがあるだけマッチさせる。
  * マッチした数だけ $w_i$ を答えに加算する
  * その連結成分に残っている $A$ もしくは $B$ に含まれる頂点を更新する。

この貪欲法によってできた $A$ の要素と $B$ の要素のマッチングが実は最適解です。

この問題では実際の $A$ の要素と $B$ の要素のマッチングを求める必要はないため、頂点自体を管理せずに $A$ の要素である頂点の個数、$B$ の要素である頂点の個数(被りを含む) を管理するだけでよいです。

連結成分の管理は Union Find などで適切に行えるため、計算量は $O((N+M) \alpha(N))$ となります $(\alpha(N)$ は逆アッカーマン関数)。詳細は実装例をご参照ください。

実装例(C++):

```cpp
#include <bits/stdc++.h>
#include <atcoder/dsu>
using namespace std;
using ll = long long;
static constexpr ll inf = 2e18;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<tuple<int, int, int>> edges(m);
    vector<int> a(k), b(k);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        edges[i] = {w, u, v};
    }
    for (int i = 0; i < k; ++i) cin >> a[i];
    for (int i = 0; i < k; ++i) cin >> b[i];

    vector<int> cnt_a(n), cnt_b(n); // 各連結成分の A の個数, Bの個数
    for (int i = 0; i < k; ++i) {
        cnt_a[a[i] - 1]++;
        cnt_b[b[i] - 1]++;
    }
    sort(edges.begin(), edges.end());
    long long ans = 0;
    atcoder::dsu d(n);
    for (int i = 0; i < m; ++i) {
        auto [c, u, v] = edges[i];
        if (d.same(u, v)) continue; //すでに連結ならば無視する
        int ru = d.leader(u), rv = d.leader(v);
        d.merge(u, v);
        int new_root = d.leader(u);
        cnt_a[new_root] = cnt_a[ru] + cnt_a[rv];
        cnt_b[new_root] = cnt_b[ru] + cnt_b[rv];
        ans += 1LL * c * min(cnt_a[new_root], cnt_b[new_root]); //あるだけペアを作る
        const int e = min(cnt_a[new_root], cnt_b[new_root]);
        cnt_a[new_root] -= e;
        cnt_b[new_root] -= e;
    }

    cout << ans << endl;
}
```

---

First, let's consider the properties of $f(x, y)$.

The function $f(x, y)$ represents the minimum value of $w$ such that vertices $x$ and $y$ are connected in a subgraph that includes only edges with weights at most $w$. From this, for any three distinct vertices $x, y, z$, if $f(x, y) \leq f(x, z)$, then $f(x, z) = f(y, z)$.

This means that for vertices $x, y$ connected by edges with weight at most $w$, any vertex $z$ that is not connected to them in this graph satisfies $f(x, z) = f(y, z)$.

Additionally, this problem can be rephrased as pairing elements from $A$ and $B$ by reordering $B$ and finding their matching.

### Greedy Approach

We can devise the following greedy algorithm. Assume that the edges are sorted in ascending order of weights $w_1 \leq w_2 \dots \leq w_M$:

1. Start with a graph of $N$ vertices and no edges. Track for each vertex whether it belongs to $A$ or $B$.
2. Iterate over the edges $i = 1, 2, \dots, M$:
   - If vertices $u_i$ and $v_i$ are not connected, add the edge $\{u_i, v_i\}$ to the graph. If they are already connected, move to the next edge.
   - If adding the edge connects two previously disjoint connected components, match as many vertices from $A$ in one component with vertices from $B$ in the other as possible.
   - Add $w_i \times$ the number of matches to the answer.
   - Update the remaining unmatched vertices in each component.

This greedy approach produces the optimal matching of elements from $A$ and $B$.

### Simplification

Since the problem does not require explicitly determining the matches, we only need to manage the count of vertices belonging to $A$ and $B$ in each connected component. This eliminates the need to directly track the vertices themselves.

Managing connected components can be efficiently done using a **Union-Find** (Disjoint Set Union) data structure. The time complexity is $O((N + M) \alpha(N))$, where $\alpha(N)$ is the inverse Ackermann function.

---

### Implementation Example (C++)

```cpp
#include <bits/stdc++.h>
#include <atcoder/dsu>
using namespace std;
using ll = long long;
static constexpr ll inf = 2e18;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<tuple<int, int, int>> edges(m);
    vector<int> a(k), b(k);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        edges[i] = {w, u, v};
    }
    for (int i = 0; i < k; ++i) cin >> a[i];
    for (int i = 0; i < k; ++i) cin >> b[i];

    vector<int> cnt_a(n), cnt_b(n); // Number of A and B vertices in each component
    for (int i = 0; i < k; ++i) {
        cnt_a[a[i] - 1]++;
        cnt_b[b[i] - 1]++;
    }
    sort(edges.begin(), edges.end());
    long long ans = 0;
    atcoder::dsu d(n);
    for (int i = 0; i < m; ++i) {
        auto [c, u, v] = edges[i];
        if (d.same(u, v)) continue; // Skip if already connected
        int ru = d.leader(u), rv = d.leader(v);
        d.merge(u, v);
        int new_root = d.leader(u);
        cnt_a[new_root] = cnt_a[ru] + cnt_a[rv];
        cnt_b[new_root] = cnt_b[ru] + cnt_b[rv];
        ans += 1LL * c * min(cnt_a[new_root], cnt_b[new_root]); // Match as many as possible
        int e = min(cnt_a[new_root], cnt_b[new_root]);
        cnt_a[new_root] -= e;
        cnt_b[new_root] -= e;
    }

    cout << ans << endl;
}
```



**貪欲の証明**

---

注: 解説放送や解説の（証明の）方針とは異なるかも知れません

### 補題

$w$ の昇順に辺をグラフに追加していくことを考える。ここで、初めて $A$, $B$ 同士で連結となった頂点のペアが  $(A_i, B_j)$ ならば、$A_i$ と $B_j$ でマッチングするような最適解が存在する。

### 補題の証明

最適解を1つ取る。もし、$A_i$ と $B_j$ がマッチングされていたら問題ない。

ここで、$A_i$ と $B_k$ が、及び $A_l$ と $B_j$ がマッチングされていたとする。マッチング相手をswapしても答えが悪化しない事、つまり、

$$
\begin{align}
f(A_i,B_k) + f(A_l, B_j)\ge f(A_i,B_j) + f(A_l, B_k)
\end{align}
$$

を示せば良い。ここで、仮定より

$$
f(A_i, B_j) \le f(A_l, B_j), f(A_i, B_k), f(A_l, B_k)
$$

が従う。

以後、$A_i−B_j, A_l − B_j, A_i − B_k, A_l−B_k$ の4つの連結性だけを考えれば良い。特に、 $A_i−B_j$ は最初に成立する。

まず、 $f(A_l, B_j) \ge f(A_l, B_k)$ が成立する場合、仮定より直ちに (1)**(**1**)** が成立する。以後、 $f(Al,Bj)≤f(Al,Bk)$ とする。よって、調べるべきは 3**3** 通りである。

#### $f(A_l, B_j) \le f(A_i, B_k) \le f(A_l,B_k)$ の時

$A_i − B_k$ の連結性が成立した時点で、 $A_l − B_k$ の連結性も成立している（図を書くとわかりやすい）。つまり、 $f(A_i, B_k) = f(A_l, B_k)$ である。 よって

$$
(1) \Leftrightarrow f(A_i, B_k) + f(A_l, B_k) \ge f(A_i, B_j) + f(A_l, B_k) \\

\Leftrightarrow f(A_i, B_k) \ge f(A_i, B_j)
$$

であり、これは仮定より成立。

#### $f(A_l, B_j) \le f(A_l, B_k) \le f(A_i, B_k)$ の時

同様の整理の元、 $f(A_l, B_k) = f(A_i, B_k)$ から $(1)$ 成立。

#### $f(A_i, B_k) \le f(A_l, B_j) \le f(A_l, B_k)$ の時

同様の整理の元、 $f(A_l,B_j) = f(A_l, B_k)$ から

$$
(1) \Leftrightarrow f(A_i, B_k) + f(A_l, B_k) \ge f(A_i, B_j) + f(A_l, B_k) \\
\Leftrightarrow f(A_i, B_k) \ge f(A_i, B_j)
$$

であり、これは仮定より成立。

よって、 $(1)$ が示され、補題は示された。

### 貪欲の証明

与えられた問題は次であった。

> $(A_1, \dots , A_k)$ と $(B_1, \dots, B_k)$ が与えられた時、 $\sum f(A_i,B_i)$　が最小になるように $B$ を並び替えよ。

ここで補題の手続きによって得られる $a \in A$ と $b \in B$ をマッチングさせる。すると、補題から示されたことより、残りの $(A_1, \dots, A_{k−1})$ と $(B_1,\dots, B_{k−1})$ に対し、$\sum f(A_i, B_i)$　が最小になるように $B$ を並びかえれば最適解の $1$ つを得る。

ここで、帰着後の問題が帰着前の問題とほとんど同じ形をしていることより、この手続きを繰り返すことにより最適解の $1$ つを得る。

そして、解説の貪欲はこの手続きを行なっていると解釈できるので、貪欲の正当性が示された。


---


**Proof of Greediness**

---

*Note: This explanation may differ from the commentary or suggested proof strategy.*

### Lemma

Consider adding edges to a graph in ascending order of their weight $w$. Suppose the first pair of vertices $(A_i, B_j)$ that connects sets $A$ and $B$ becomes connected at this step. Then, there exists an optimal solution where $A_i$ is matched with $B_j$.

### Proof of the Lemma

Take one optimal solution. If $A_i$ is already matched with $B_j$, there is no problem.

Now, assume $A_i$ is matched with $B_k$, and $A_l$ is matched with $B_j$. Swapping their matches does not worsen the solution if we can show:

$$
f(A_i, B_k) + f(A_l, B_j) \geq f(A_i, B_j) + f(A_l, B_k).
$$

From the assumption, we know:

$$
f(A_i, B_j) \leq f(A_l, B_j), \quad f(A_i, B_j) \leq f(A_i, B_k), \quad f(A_i, B_j) \leq f(A_l, B_k).
$$

Thus, we only need to consider the connectivity among $A_i-B_j$, $A_l-B_j$, $A_i-B_k$, and $A_l-B_k$. In particular, $A_i-B_j$ is the first to become connected.

### Case Analysis

#### Case 1: $f(A_l, B_j) \geq f(A_l, B_k)$

In this case, inequality $(1)$ immediately holds from the assumption.

#### Case 2: $f(A_l, B_j) \leq f(A_l, B_k)$

This breaks into three subcases:

##### Subcase 2.1: $f(A_l, B_j) \leq f(A_i, B_k) \leq f(A_l, B_k)$

By the time $A_i-B_k$ becomes connected, $A_l-B_k$ is also connected (this can be visualized clearly in a diagram). Thus, $f(A_i, B_k) = f(A_l, B_k)$, and we get:

$$
(1) \Leftrightarrow f(A_i, B_k) + f(A_l, B_k) \geq f(A_i, B_j) + f(A_l, B_k),
$$
$$
\Leftrightarrow f(A_i, B_k) \geq f(A_i, B_j),
$$

which holds by assumption.

##### Subcase 2.2: $f(A_l, B_j) \leq f(A_l, B_k) \leq f(A_i, B_k)$

Similarly, from $f(A_l, B_k) = f(A_i, B_k)$, $(1)$ holds.

##### Subcase 2.3: $f(A_i, B_k) \leq f(A_l, B_j) \leq f(A_l, B_k)$

From $f(A_l, B_j) = f(A_l, B_k)$, we deduce:

$$
(1) \Leftrightarrow f(A_i, B_k) + f(A_l, B_k) \geq f(A_i, B_j) + f(A_l, B_k),
$$
$$
\Leftrightarrow f(A_i, B_k) \geq f(A_i, B_j),
$$

which also holds by assumption.

Thus, $(1)$ is proven in all cases, and the lemma is established.

### Proof of Greediness

The problem is as follows:

> Given $(A_1, \dots, A_k)$ and $(B_1, \dots, B_k)$, rearrange $B$ to minimize $\sum f(A_i, B_i)$.

Using the procedure established in the lemma, match the pair $a \in A$ and $b \in B$. By the lemma, the remaining subproblem $(A_1, \dots, A_{k-1})$ and $(B_1, \dots, B_{k-1})$ also satisfies the condition for minimizing $\sum f(A_i, B_i)$.

Since the reduced problem retains the same structure as the original, repeating this procedure yields an optimal solution.

Finally, as the described greedy method follows this procedure, its correctness is established.
