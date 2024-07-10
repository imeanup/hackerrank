## [E - Tree and Hamilton Path 2](https://atcoder.jp/contests/abc361/tasks/abc361_e)


<details><summary><b>Japanese Editorial</b></summary>

街を頂点、道路を辺としたグラフを考えます。問題文中で与えられた条件からこのグラフは木です。

木の直径を $D$ とします。求める答えは $2 \sum C_i - D$ となります。 木の直径は以下の手順により $O(N)$ で求めることができるため、$O(N)$ でこの問題を解くことができます。

* 適当な頂点 $v$ から最も遠い頂点 $u$ を求める
* 頂点 $u$ から最も遠い頂点 $s$ を求める
* $u, s$ が直径の両端となる頂点である

木の直径が上述の手順で求められることの証明は省略します。以下では、元の問題の答えが $2 \sum C_i - D$ となることを証明します。

まず、「すべての頂点を $1$ 度以上訪れ、最初の頂点に戻るときの移動距離の最小値」を考えます。

各辺について、その辺を取り除くことでできる $2$ つの連結成分の間の行き来を考えることで、どの辺も $2$ 度以上通る必要があることがわかります。(解の下界)

適当な頂点から始めてDFSで全ての頂点を巡ると、全ての辺をちょうど $2$ 回通って最初の頂点に戻ることができます。(下界が達成可能)
よって求める答えは $2 \sum C_i$ となります。

元の問題に戻ります。

すべての頂点を $1$ 度以上訪れる移動経路は、終点から始点への移動を追加することで「すべての頂点を $1$ 度以上訪れ、最初の頂点に戻る」移動経路となります。この最小値は先ほど求めた通り $2 \sum C_i$ であり、終点から始点への移動距離の最大値は木の直径に等しいことから、全ての頂点を $1$ 度以上訪れるための移動距離は $2 \sum C_i - D$ 以上になることがわかります。(解の下界)

木の直径を任意に取りその両端の頂点を $x, y$ とします。$x$ を始点としたDFSを、「DFS の遷移先として複数の頂点が選べるときは、$y$ に近づかない頂点を優先する」として行うことで、$x$ と $y$ を最短で結ぶパス上の辺を $1$ 度だけ通るようにすることができ、移動距離 $2 \sum C_i - D$ で全ての頂点を $1$ 度以上訪れることができます。(下界が達成可能)

以上により求める最小値が $2 \sum C_i - D$ であることが証明できました。

</details><br>

Consider a graph where cities are vertices and roads are edges. Based on the conditions given in the problem statement, this graph is a tree.

Let $D$ be the diameter of the tree. The desired answer is $2 \sum C_i - D$. Since the diameter of a tree can be determined in $O(N)$, this problem can be solved in $O(N)$.

* Find the farthest vertex $u$ from an arbitrary vertex $v$.
* Find the farthest vertex $s$ from vertex $u$.
* $u$ and $s$ are the endpoints of the diameter.

The proof of finding the diameter using the above steps is omitted. Below, we prove that the answer to the original problem is $2 \sum C_i - D$.

First, consider the "minimum travel distance required to visit all vertices at least once and return to the starting vertex."

By considering the travel between the two connected components created by removing each edge, it can be understood that each edge needs to be traversed at least twice (lower bound of the solution).

Starting from an arbitrary vertex and performing DFS to visit all vertices, all edges can be traversed exactly twice to return to the starting vertex (achieving the lower bound). Hence, the desired answer is $2 \sum C_i$.

Returning to the original problem.

The travel path to visit all vertices at least once becomes a travel path that "visits all vertices at least once and returns to the starting vertex" by adding the travel from the endpoint back to the start. This minimum value is $2 \sum C_i$, and since the maximum travel distance from the endpoint to the start is equal to the diameter of the tree, the travel distance required to visit all vertices at least once is at least $2 \sum C_i - D$ (lower bound).

Taking any arbitrary diameter endpoints $x$ and $y$, perform a DFS starting from $x$ with the condition that "when multiple vertices can be chosen as DFS transition destinations, prioritize vertices that do not approach $y$." This way, the edges on the shortest path between $x$ and $y$ are traversed only once, and the travel distance to visit all vertices at least once is $2 \sum C_i - D$ (achieving the lower bound).

Thus, we have proven that the minimum value is $2 \sum C_i - D$.
