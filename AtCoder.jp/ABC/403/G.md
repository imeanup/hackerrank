## [G - Odd Position Sum Query](https://atcoder.jp/contests/abc403/tasks/abc403_g)


$M = \max x_i$ とします．

もし $M$ が $10^5$ 程度である場合や，あらかじめすべての $x_i$ が分かっている場合は座標圧縮することで，この問題をセグメント木で解くことができます．このとき，各ノードには以下の情報を持たせます：

* $l$ 以上 $r$ 未満の $A$ の要素の個数
* $l$ 以上 $r$ 未満の $A$ の要素を昇順に並べたときの，奇数番目の要素の総和
* $l$ 以上 $r$ 未満の $A$ の要素を昇順に並べたときの，偶数番目の要素の総和

しかし，本問題は $M$ が大きいためサイズが $M$ のセグメント木を作ることができません．このような場合は **動的セグメント木 (Dynamic Segment Tree)** を利用することで解くことができます．

通常のセグメント木は最初に $O(M)$ 個のノードを構築するため $M$ が大きいとメモリが不足します．一方で $Q \ll M$ の場合，多くのノードは単位元のままアクセスされないため，「必要になったときに新しくノードを作る」動的セグメント木を用いることが有効です．

動的セグメント木では各ノードに，モノイドの情報に加えてbinary trie のように親ノードや左右の子ノードへのポインタ（またはインデックス）を持たせます．

必要なノード数は $O(Q\log⁡ M)$ に抑えられ，計算量も $O(Q\log ⁡M)$ で解くことができます．

---

Let  
$$
M = \max x_i.
$$

If $M$ is on the order of $10^5$, or if you already know all of the $x_i$ in advance, you can apply coordinate compression and solve this problem with a segment tree. In that case, each node of the segment tree stores the following information:

- **Count** of elements of $A$ whose values lie in the half-open interval $[l, r)$.
- **Sum of the elements in odd positions** when those elements of $A$ in $[l, r)$ are sorted in ascending order.
- **Sum of the elements in even positions** when those elements of $A$ in $[l, r)$ are sorted in ascending order.

However, in this problem $M$ can be very large, so you cannot build a segment tree of size $M$. In such cases, you can use a **dynamic segment tree**.

A standard segment tree initially allocates $O(M)$ nodes, which is not feasible when $M$ is huge. On the other hand, if $Q \ll M$, most of those nodes would remain in their identity-element state and never be accessed. A dynamic segment tree overcomes this by **creating nodes on the fly only when they are needed**.

In a dynamic segment tree, each node stores, in addition to the usual monoid information, pointers (or indices) to its parent node and to its left and right children—much like a binary trie.

By doing so, the total number of nodes created is $O(Q\log M)$, and the overall time complexity of all operations remains $O(Q\log M)$.
