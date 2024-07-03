## [F - InterSections](https://atcoder.jp/contests/abc360/tasks/abc360_f)

<details><summary>Japanese Editorial</summary><br>

区間 $[l, r]$ を二次元平面上に移して考えます。区間 $i$ と交差する $(l, r)$ は $L_i < l < R_i < r$ または $l < L_i < r < R_i$ を満たし、これはそれぞれ矩形領域になり、またこの二つの領域は重なりません。したがって、すべての区間に対して交差する $(l, r)$ の領域を求め、最も多くの領域が重なる場所を探せばよいです。

ここからは [ABC346-G Alone の公式解説](https://atcoder.jp/contests/abc346/editorial/9638) と同様の言い換えを行っています。

よって、以下の問題を解ければよいことがわかります。

> 整数の組 $(x_i, y_i, z_i, w_i)$ が $N$ 個与えられる。 $x_i \le L \le y_i, z_i \le R \le w_i$ を満たす $i$ の個数が最大となる $(L, R)$ を求めよ。

また、この問題を以下のように言い換えることができます。

> 最初に全ての要素が $0$ の $2$ 次元配列 $A$ があり、$N$ 個の整数の組 $(x_i, y_i, z_i, w_i)$ が与えられる。各 $i$ について、 $x_i \le l \le y_i, z_i \le r \le w_i$ を満たす $(l, r)$ に対して $A_l, r$ を $1$ 増やす。最終的に $A$ の最大値およびそれを達成する $(l, r)$ を求めよ。

この問題は以下のように平面走査をすることができます。

> 　最初にすべての要素が $0$ の配列 $C$ が与えられる。また、最大値を0で初期化する。 $N$ 個の整数の組 $(x_i, y_i, z_i, w_i)$ が与えられ、$l = 0, \dots, 10^9$ の順で以下の操作を行う
>
> * $x_j = l$ を満たす整数の組 $(x_j, y_j, w_j)$ について、$z_j \le r \le w_j$ を満たす $r$ に対して $C_r$ を $1$ 加算する。
> * $C$ の最大値を取得し、最大値が更新される場合はその時の $l$ と最大値を達成する最小の $r$ を記録する。
> * $y_j = l$ を満たす整数の組 $(x_j, y_j, w_j)$ について、$z_j \le r \le w_j$ を満たす $r$ に対して $C_r$ を $−1$ 加算する。

この問題のままだと $l$ や $r$ としてありえる値が多いですが、適切に座標圧縮することでそれぞれ $O(N)$ 個に限定することが可能です。具体的には $l$ は $L_i + 1$ や $R_i - 1$ などを取り得ます。また、$r$ は $L_i + 1$ や $R_i - 1$ や $R_i + 1$ などを取り得ます。

これを愚直に行なうと 計算量が $O(N^2)$ になってしまいますが、区間 Add 区間 Max のLazy Segment Tree を用いることによって $O(N\log N)$ で解くことができます。

また、実装の際には $f(l, r)$ の最大値が $0$ であるときの答えが必ず $l = 0, r = 1$ であることに注意してください。

詳細は実装例を参照してください。

[実装例(C++)](https://atcoder.jp/contests/abc360/submissions/55041402)

</details><br>

Consider the interval $[l, r]$ on a two-dimensional plane. An interval $i$ intersects with $(l, r)$ if $L_i < l < R_i < r$ or $l < L_i < r < R_i$, and each of these conditions forms a rectangular region that does not overlap with the other. Therefore, we need to determine the regions of $(l, r)$ that intersect with all intervals and find the location where the most regions overlap.

From here, we rephrase the problem similarly to the official explanation of [ABC346-G Alone](https://atcoder.jp/contests/abc346/editorial/9638).

Thus, the problem can be solved by addressing the following:

> Given $N$ tuples of integers $(x_i, y_i, z_i, w_i)$, find the $(L, R)$ that maximizes the number of $i$ such that $x_i \le L \le y_i$ and $z_i \le R \le w_i$.

This can further be rephrased as:

> Initially, you have a two-dimensional array $A$ with all elements set to 0. Given $N$ tuples of integers $(x_i, y_i, z_i, w_i)$, for each $i$, increase $A_{l, r}$ by 1 for all $(l, r)$ satisfying $x_i \le l \le y_i$ and $z_i \le r \le w_i$. Finally, determine the maximum value in $A$ and the corresponding $(l, r)$ that achieves it.

This problem can be solved using a plane sweep algorithm as follows:

> Initially, you are given an array $C$ with all elements set to 0 and a maximum value initialized to 0. Given $N$ tuples of integers $(x_i, y_i, z_i, w_i)$, perform the following operations for $l = 0, \dots, 10^9$:
>
> * For each tuple $(x_j, y_j, w_j)$ where $x_j = l$, increment $C_r$ by 1 for all $r$ satisfying $z_j \le r \le w_j$.
> * Retrieve the maximum value of $C$, and if the maximum value is updated, record the current $l$ and the smallest $r$ that achieves the maximum value.
> * For each tuple $(x_j, y_j, w_j)$ where $y_j = l$, decrement $C_r$ by 1 for all $r$ satisfying $z_j \le r \le w_j$.

Although the potential values for $l$ and $r$ are numerous, proper coordinate compression can limit them to $O(N)$ each. Specifically, $l$ can take values such as $L_i + 1$ and $R_i - 1$, while $r$ can take values such as $L_i + 1$, $R_i - 1$, and $R_i + 1$.

If performed naively, the time complexity would be $O(N^2)$, but using a lazy segment tree for range add and range max operations allows solving it in $O(N \log N)$.

Note that when implementing, if the maximum value of $f(l, r)$ is 0, the answer should default to $l = 0, r = 1$.

For details, refer to the implementation example.

[Example implementation (C++)](https://atcoder.jp/contests/abc360/submissions/55041402)
