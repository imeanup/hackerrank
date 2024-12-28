## [G - Many MST](https://atcoder.jp/contests/abc386/tasks/abc386_g) 

辺の重みを $0$ 以上 $M$ 未満として考え，最後に $(N−1)\times M^{N(N−1)/2}$ を加えることにします．

辺の重みが $0$ 以上 $M$ 未満の整数であるような連結グラフ $G$ に対して，その最小全域木の重みの和は $G_k$ を $G$ の辺のうち重みが $k$ 未満であるものからなる（重みなし）グラフ，$c(G_k)$ を $G_k$ の連結成分数として， $\displaystyle\sum_{k=1}^M c(G_k) − M$ と表されます．

$S_N$ を辺の重みが $0$ 以上 $M$ 未満であるような $N$ 頂点完全グラフすべての集合，$C(G_k)$ を $G_k$ の連結成分の集合として，求める答えは

$$
\sum_{G\in S}^N \sum_{k=1}^M c(G_k) − M = − M\times M^{N(N−1)/2} + \sum_{k=1}^M \sum_{G\in S}^N c(G_k) = − M\times M^{N(N−1)/2} + \sum_{k=1}^M \sum_{G\in S_N} \sum_{H \in C(G_k)} 1
$$

です．$（c(G_k) = |C(G_k)|$ を用いています．）以下では各 $k$ に対して $\sum_{G\in S}^N \sum_{H\in C(G_k)} 1$ を求める方法を導出します．

（ここまでのお気持ち：答えへの寄与を辺の重みに注目して分解することで **重みなし** の **連結グラフ** の数え上げ問題に帰着でき，数えやすくしています．）

$H$ を固定して考えると（$H$ は $N$ 頂点完全グラフの部分グラフのうち連結であるものです），$H\in C(G_k)$ となるような $G\in S_N$ の個数は，$V(H)$ を $H$ の頂点集合，$m(H)$ を $H$ の辺の本数として

$$
(M−k)^{|V(H)|(|V(H)| − 1)/2−m(H)} \times k^{m(H)} \times (M−k)^{|V(H)|(N−|V(H)|)} \times M^{(N−|V(H)|)(N−|V(H)|−1)/2}
$$

個です．これは，条件を満たす $G$ の各辺の重みを考えたとき，両端が $V(H)$ に含まれる辺ならば， $H$ に含まれるものについては $k$ 未満，含まれないものについては $k$ 以上であり，また $V(H)$ と $\{1,2, \dots, N\}∖V(H)$ の間にある辺であれば $k$ 以上，両端が $\{1,2,\dots, N\}∖V(H)$ に含まれる辺であれば任意であることから従います．

よって主客転倒により（$H$ に注目して式を変形することで）

$$
\sum_{G\in S_N} \sum_{H\in C(G_k)} 1 = \sum_H (M−k)^{|V(H)|(|V(H)|−1)/2−m(H)} \times k^{m(H)} \times (M−k)^{|V(H)|(N−|V(H)|)} \times M(N−|V(H)|)(N−|V(H)|−1)/2
$$

です．$H$ のうち頂点数が $s$ であるものは $H$ のうち頂点集合が $\{1,2, \dots, s\}$ であるものの $\binom{N}{s}$ 倍あるので，$H$ のうち頂点集合が $\{1,2, \dots ,s\}$ であるもののすべてに対する $(M−k)^{|V(H)|(|V(H)|−1)/2−m(H)} \times k^{m(H)}$ の総和を $f(s)$ とすれば

$$
\sum_H (M−k)^{|V(H)|(|V(H)|−1)/2−m(H)} \times k^{m(H)} \times (M−k)^{|V(H)|(N−|V(H)|)} \times M^{(N−|V(H)|)(N−|V(H)|−1)/2} = \sum_{s=1}^N \binom{N}{s} f(s) \times (M−k)^{s(N−s)} \times M^{(N−s)(N−s−1)/2}
$$

となります．

結局 $f(s)$ が $s=1,2, \dots, N$ に対して求められれば良いことになります．これは [ABC213G](https://atcoder.jp/contests/abc213/tasks/abc213_g) の解説にあるような連結グラフの数え上げと同様に考えることができ，$f(s)=M^{s(s−1)/2} − \sum_{i=1}^{s−1} f(i) \binom{s−1}{i−1} (M−k)^{i(s−i)} M^{(s−i)(s−i−1)/2}$ が成り立ちます．この式に基づいて計算することで $f(1),f(2), \dots,f(N)$ を $O(N^2)$ で求めることができます．

以上を $k=1, 2, \dots,M$ それぞれについて行うことで，答えを $O(N^2M)$ で求めることができます．

---

Consider the edge weights to be integers in the range from $0$ to $M-1$, and then add $(N-1) \times M^{N(N-1)/2}$ at the end.

For a connected graph $G$ with edge weights between $0$ and $M-1$, the sum of the weights of its minimum spanning tree is represented as:

$$
\sum_{k=1}^M c(G_k) - M
$$
where $G_k$ is a subgraph of $G$ consisting of edges with weights less than $k$ (a graph with no weights), and $c(G_k)$ is the number of connected components of $G_k$.

Let $S_N$ be the set of all complete graphs with $N$ vertices and edge weights between $0$ and $M-1$, and let $C(G_k)$ be the set of connected components of $G_k$. The desired answer can be expressed as:

$$
\sum_{G \in S_N} \sum_{k=1}^M c(G_k) - M = -M \times M^{N(N-1)/2} + \sum_{k=1}^M \sum_{G \in S_N} c(G_k) = -M \times M^{N(N-1)/2} + \sum_{k=1}^M \sum_{G \in S_N} \sum_{H \in C(G_k)} 1
$$

(where $c(G_k) = |C(G_k)|$).

The task now is to derive a method to compute $\sum_{G \in S_N} \sum_{H \in C(G_k)} 1$ for each $k$.

(Up to this point, the approach has been to decompose the problem by focusing on the contribution of edge weights, reducing the problem to counting **connected graphs** without weights, which makes counting easier.)

If we fix $H$ (where $H$ is a connected subgraph of the complete graph on $N$ vertices), the number of graphs $G \in S_N$ such that $H \in C(G_k)$ is given by:

$$
(M-k)^{|V(H)|(|V(H)| - 1)/2 - m(H)} \times k^{m(H)} \times (M-k)^{|V(H)|(N-|V(H)|)} \times M^{(N-|V(H)|)(N-|V(H)|-1)/2}
$$

where $V(H)$ is the set of vertices of $H$, and $m(H)$ is the number of edges in $H$. This expression follows because:

- For edges within $V(H)$, the weights must be less than $k$ for edges in $H$ and greater than or equal to $k$ for edges not in $H$.
- For edges between $V(H)$ and the complement of $V(H)$ in the vertex set $\{1, 2, \dots, N\}$, the weights must be at least $k$.
- For edges within the complement of $V(H)$, the weights can be arbitrary.

Thus, by changing the focus to $H$, we get:

$$
\sum_{G \in S_N} \sum_{H \in C(G_k)} 1 = \sum_H (M-k)^{|V(H)|(|V(H)|-1)/2 - m(H)} \times k^{m(H)} \times (M-k)^{|V(H)|(N-|V(H)|)} \times M^{(N-|V(H)|)(N-|V(H)|-1)/2}
$$

For subgraphs $H$ with $s$ vertices, the number of such subgraphs is $\binom{N}{s}$ times the above expression, so we can define:

$$
f(s) = \sum_{H \in \{1, 2, \dots, s\}} (M-k)^{|V(H)|(|V(H)|-1)/2 - m(H)} \times k^{m(H)}
$$

Thus, the final expression becomes:

$$
\sum_H (M-k)^{|V(H)|(|V(H)|-1)/2 - m(H)} \times k^{m(H)} \times (M-k)^{|V(H)|(N-|V(H)|)} \times M^{(N-|V(H)|)(N-|V(H)|-1)/2} = \sum_{s=1}^N \binom{N}{s} f(s) \times (M-k)^{s(N-s)} \times M^{(N-s)(N-s-1)/2}
$$

In the end, we only need to compute $f(s)$ for $s=1, 2, \dots, N$. This can be done by applying a recurrence relation similar to the one for counting connected graphs, where:

$$
f(s) = M^{s(s-1)/2} - \sum_{i=1}^{s-1} f(i) \binom{s-1}{i-1} (M-k)^{i(s-i)} M^{(s-i)(s-i-1)/2}
$$

This recurrence allows us to compute $f(1), f(2), \dots, f(N)$ in $O(N^2)$ time.

Finally, by performing this for each $k=1, 2, \dots, M$, the answer can be computed in $O(N^2M)$ time.
