## [F - Distance Component Size Query](https://atcoder.jp/contests/abc356/tasks/abc356_f)

<details><summary>Japanese</summary>


$3$ つの数 $a < b$ と任意の $K$ について、$c - a \le K$ ならば $b-a\le K$ かつ $c-b\le K$ です。つまり、$a$ と $c$ の間に辺が張られるならば、$a$ と $b$、$b$ と $c$ の間にもそれぞれ辺が張られます。よって、辺は$S$ の元をソートしたときに隣り合う数の間だけで張るとしても連結性は変わりません。

まず、簡単のため、頂点の追加/削除を行う問題ではなく辺の追加/削除を行う次の問題を考えます。

問題：$N$ 頂点 $0$ 辺のグラフがある。以下の $2$ 種類のクエリを処理せよ。

* $x$ が与えられる。頂点 $x$ と $x + 1$ を結ぶ辺がなければ追加し、あれば削除する
* 頂点 $x$ の属する連結成分のサイズを求める

$A_i$ を、$i$ と $i+1$ を結ぶ辺があれば $1$、なければ $0$ と定めます。このとき、2つのクエリは以下のように処理できます。

* 辺の追加/削除クエリは $A_i$ の値の更新になります。
* 連結成分数を求めるクエリは、まず、頂点 $x$ がどこまで右側の頂点と連結かを考えます。$y > x$ が $x$ と連結であるための必要十分条件は、$A[x] + \dots + A[y-1] = y-x$ となることです。このような最大の $y$ は $A$ の区間和が高速に求まるならば二分探索により高速に求めることができます。左側についても同様にできます。

以上から、配列 $A$ を segment tree で管理することでこの問題は解けます。

もとの問題に戻ります。もとの問題は頂点の追加/削除を行いますが、辺の有無だけではなく頂点の有無も管理するような、以下の $2$ つの配列 $A, B$ を segment tree を用いて管理することでほとんど同様に解くことができます。

* $x$ が $S$ に含まれれば $A_i = 1$、含まれなければ $A_i = 0$
* $x$ と”右隣”の要素の間に辺があれば $B_i = 1$、辺がなければ $B_i = 0$

クエリ先読み＋座標圧縮や、動的 segment tree を用いることで、segment tree のノード数は十分小さく抑えられ、 計算量は $O(Q \log Q)$ や $O(Q \log \max x_i)$ となります。

</details><br>

For any three numbers $a < b < c$ and any $K$, if $c - a \le K$, then $b-a \le K$ and $c-b \le K$ must also hold. This means that if an edge is drawn between $a$ and $c$, edges must also be drawn between $a$ and $b$ as well as between $b$ and $c$. Therefore, the connectivity does not change even if we only consider drawing edges between adjacent numbers when $S$ is sorted.

First, for simplicity, consider a problem involving the addition/deletion of edges instead of vertices:

**Problem:** Given a graph with $N$ vertices and 0 edges, handle the following two types of queries:

* Given $x$, if there is no edge connecting vertex $x$ and $x + 1$, add it; if there is, remove it.
* Determine the size of the connected component to which vertex $x$ belongs.

Define $A_i$ such that $A_i = 1$ if there is an edge between $i$ and $i+1$, and $A_i = 0$ otherwise. The two queries can then be handled as follows:

* The add/delete edge query corresponds to updating the value of $A_i$.
* To determine the size of the connected component, first consider how far to the right vertex $x$ is connected. The necessary and sufficient condition for $y > x$ to be connected to $x$ is that the sum $A[x] + \dots + A[y-1] = y - x$. The maximum such $y$ can be efficiently found using binary search if the interval sum of $A$ can be computed quickly. The same method applies for the left side.

Thus, by managing array $A$ with a segment tree, this problem can be solved.

Returning to the original problem, which involves adding/deleting vertices, the solution can be adapted by managing the presence of both vertices and edges with two arrays $A$ and $B$ using a segment tree as follows:

* $A_i = 1$ if $x$ is included in $S$, and $A_i = 0$ otherwise.
* $B_i = 1$ if there is an edge between $x$ and the "right adjacent" element, and $B_i = 0$ otherwise.

By using query preprocessing and coordinate compression, or dynamic segment trees, the number of nodes in the segment tree can be kept sufficiently small, and the computational complexity can be $O(Q \log Q)$ or $O(Q \log \max x_i)$.
