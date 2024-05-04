## [F - Estimate Order](https://atcoder.jp/contests/abc352/tasks/abc352_f)


<!-- $N$ 頂点 $M$ 辺のグラフであって、$i$ 番目の辺が頂点 $A_i$ と頂点 $B_i$ を結ぶ辺であるようなものを考えます。

制約から、整数列 $D = (D_1, D_2, \cdots, D_N)$ であって、各 $i$ について $D_{A_i} - D_{B_i} = C_i$ であるようなものを取ることができます。 この整数列は上で与えたグラフ上で適切に DFS や BFS などを行うことで得ることができます。

人 $i$ の順位を $X_i$ とすると、$X = (X_1, X_2, \cdots, X_N)$ としてあり得る数列は $(1, 2, \cdots, N)$ の並べ替えであって以下の条件を満たすもの、またそのようなものに限られます。

* 各連結成分ごとに適当な整数 $v$ を選び、連結成分上の各頂点 $i$ に対して $X_i = D_i + v$ とする。

ここで、クエリを連結成分ごとに解くことを考えます。

$i$ 番目のクエリの答えを求める際には、頂点 $i$ を含まない連結成分を配置していく bit dp を行います。具体的には、$dp_{x, y} を（頂点 $i$ が含まれる連結成分を除き）$x 番目までの連結成分の頂点に対応する順位の集合が $y$ になる可能性があるかを表す bool 値として持てばよいです。

各連結成分ごとに順位の組としてあり得るものは $O(N)$ 個しかないため、上の dp は素朴に時間計算量 $O(N^2 2^N)$ の値から考えるべき $y$ の popcount が $1$ つに決まることを利用すると時間計算量 $O(N 2^N)$ で行えます。

よって全体として時間計算量 $O(N^2 2^N)$ でこの問題を解くことができました。 -->

Consider a graph with $N$ vertices and $M$ edges, where the $i$-th edge connects vertices $A_i$ and $B_i$.

Due to the constraints, we can consider an integer sequence $D = (D_1, D_2, \cdots, D_N)$ such that for each $i$, $D_{A_i} - D_{B_i} = C_i$. This integer sequence can be obtained by performing appropriate DFS or BFS on the graph given above.

Let $X = (X_1, X_2, \cdots, X_N)$ denote the ranking of people $i$. The possible sequences for $X$ are permutations of $(1, 2, \cdots, N)$ that satisfy the following conditions, and they are limited to such sequences:

* For each connected component, choose a suitable integer $v$, and set $X_i = D_i + v$ for each vertex $i$ in the connected component.

Now, let's consider solving queries for each connected component.

When finding the answer to the $i$-th query, we perform bit DP to place connected components excluding vertex $i$. Specifically, we can maintain a boolean value $dp_{x, y}$ for each possibility of the set of rankings corresponding to vertices of the first $x$ connected components being $y$, excluding the connected component containing vertex $i$.

Since there are only $O(N)$ possible combinations of rankings for each connected component, we can perform the DP mentioned above in $O(N 2^N)$ time by exploiting the fact that the popcount of $y$ determining the value from the naive time complexity of $O(N^2 2^N)$.

Therefore, we can solve this problem with a overall time complexity of $O(N^2 2^N)$.