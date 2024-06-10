## [F - Second Largest Query](https://atcoder.jp/contests/abc343/tasks/abc343_f)

<details><summary>Japanese Editorial</summary>

以下では説明の簡略化のため $A_x, A_{x+1}, \dots, A_{y-1}$ のことを区間 $[x, y)$ と呼びます。

$l < m < r$$ のとき区間 $[l, r)$ における $2$ 番目に大きな値は区間 $[l, m)$ における最大値、区間 $[l, m)$ における $2$ 番目に大きい値、区間 $[m, r)$ における最大値、区間 $[m, r)$ における $2$ 番目に大きい値のいずれかになります。

また同様に、区間 $[l, r)$ における最大値は区間 $[l, m)$ における最大値あるいは区間 $[m, r)$ における最大値のいずれかとなります。

したがって (最大値, 最大値の個数, $2$ 番目に大きい値, $2$ 番目に大きい値の個数) の組は区間 $[l, m)$ および区間 $[m, r)$ についてわかっていれば区間 $[l, r)$ についても定数時間で計算可能であるため segtree を用いて全体として時間計算量 $O(N+Q\log N)$ でこの問題が解けます。


---

### ACL を用いた詳細な実装方法の説明

---

この問題は，セグメント木に複数の値の組を載せることによって解きます． [ACL/segtree](https://atcoder.github.io/ac-library/document_ja/segtree.html) をベースに実装方法の説明を行いますので，以降を読む前にあらかじめ確認しておくことを推奨します．

ACL のセグメント木は，載せる値の組の構造体 $S$，区間結合時の二項演算 $op$，および単位元の値 $e$ を指定して利用します．ここでの目標は，**1 点の変更および区間の値の取得に対応できるように，$S, op, e$ を設定すること**です．

今回の問題では，「区間の二番目の最大値の個数」を取得することが要求されます．この要件を満たせるように， $S, op, e$ を設定していきましょう．

唐突ですが，$S$ に（区間の最大値，区間の最大値の個数，区間の二番目の最大値，区間の二番目の最大値の個数）を指定することにします．これは，区間結合時の二項演算を実現するのに必要な情報となるから，というのが理由になります（詳細な演算の方法は後述）．以降，これら $4$ 個の値をそれぞれ $(f, cf, s, cs)$ とおきます．

$op$ を具体的に考えましょう．ここですべきことは，左側の区間についての情報 $S_l$ および右側の区間についての情報 $S_r$ が与えられた際に，それを結合した区間についての情報 $S_c = (f_c, cf_c, s_c, cs_c)$ を求める，ということになります．以降，$S_l = (f_l, cf_l, s_l, cs_l)$ および $S_r = (f_r, cf_r, s_r, cs_r)$ とします．

[![2024-03-03-004032](https://i.ibb.co/Jp0RgLj/2024-03-03-004032.png)](https://ibb.co/pKGv5Dj)

具体的な $S_r = (f_r, cf_r, s_r, cs_r)$ の求め方についてですが

* $f_c$ について．$f_c = \max(f_l, f_r)$ となります．
* $cf_c$ について．$f_l$ と $f_r$ の中で，$f_c$ と等しい値に対応する個数の和となります．
* $s_c$ について．$f_l, f_r, s_l, s_r$ の中で，二番目に大きい値となります．具体的な形は実装例を参照してください．
* $cs_c$ について．$f_l, f_r, s_l, s_r$ の中で，$s_c$ と等しい値に対応する個数の和となります．

よって，$op$ には $S_l$ および $S_r$ が与えられたときに，上の演算によって求めた $S_c = (f_c, cf_c, s_c, cs_c)$ を返す関数を指定すればよいことになります．

$e$ についてですが，結合時に影響のない値，すなわち

* $S_e = (f_e, cf_e, s_e, cs_e)$ に対し，$S$ と $S_e$ を結合させたときに $S$ を返すような $S_e$

を適切に設定すればよいです．今回の制約では，$S_e = (-1, 0, -2, 0)$ などに設定すればよいでしょう．

実際に使用する際には，$S$ の初期化（セグ木の各点に乗せる情報）も考える必要があります．このときは $1$ 点だけの場合に，$S$ の各値がどうなるか考えればよいです．まず，明らかに $f = A_i,c_f = 1$ なので，それを指定すればよいです．$s, cs$ については，今回の場合は存在しないですが，仮想的に結合時に影響のない適当な値（$s = -1, cs = 0$ など）に設定すればよいでしょう．結局，各要素の初期化の際には，`seg.set(i, S{A[i], 1, -1, 0})` などのように記述すればよいです．（一点更新の際も，ほぼ同様のことをすればよいです）

これらを用いることで，実装することができます．

[実装例（C++，ACL/segtree使用）](https://atcoder.jp/contests/abc343/submissions/50850917)

</details><br>

Below, for simplicity, we will refer to $A_x, A_{x+1}, \dots, A_{y-1}$ as the interval $[x, y)$.

When $l < m < r$, the second largest value in the interval $[l, r)$ will be one of the following:
- The maximum value in the interval $[l, m)$,
- The second largest value in the interval $[l, m)$,
- The maximum value in the interval $[m, r)$,
- The second largest value in the interval $[m, r)$.

Similarly, the maximum value in the interval $[l, r)$ will be either the maximum value in the interval $[l, m)$ or the maximum value in the interval $[m, r)$.

Therefore, if we know the tuples (maximum value, count of the maximum value, second largest value, count of the second largest value) for the intervals $[l, m)$ and $[m, r)$, we can compute these values for the interval $[l, r)$ in constant time. Using a segment tree, we can solve this problem with a total time complexity of $O(N + Q \log N)$.

---

### Detailed Implementation Using ACL

---

This problem can be solved by using a segment tree with multiple value tuples. We will base the implementation on [ACL/segtree](https://atcoder.github.io/ac-library/document_ja/segtree.html). It is recommended to review this documentation before reading further.

The ACL segment tree requires specifying a struct $S$ for the value tuple, a binary operation $op$ for combining intervals, and an identity element $e$. Our goal is to set $S, op,$ and $e$ to support both single point updates and interval queries.

For this problem, we need to obtain the count of the second largest value in an interval. To meet this requirement, we will set $S$ to include (maximum value, count of the maximum value, second largest value, count of the second largest value). This is necessary to implement the binary operation for combining intervals (details will be provided later). Let these four values be denoted as $(f, cf, s, cs)$.

Let's consider the binary operation $op$. Given the information for the left interval $S_l$ and the right interval $S_r$, we need to calculate the information for the combined interval $S_c = (f_c, cf_c, s_c, cs_c)$. Let $S_l = (f_l, cf_l, s_l, cs_l)$ and $S_r = (f_r, cf_r, s_r, cs_r)$.

Here is how to determine $S_c = (f_c, cf_c, s_c, cs_c)$:

* For $f_c$: $f_c = \max(f_l, f_r)$.
* For $cf_c$: The sum of the counts corresponding to values equal to $f_c$ from $f_l$ and $f_r$.
* For $s_c$: The second largest value among $f_l, f_r, s_l, s_r$. Refer to the implementation example for specific details.
* For $cs_c$: The sum of the counts corresponding to values equal to $s_c$ from $f_l, f_r, s_l, s_r$.

Thus, $op$ is a function that takes $S_l$ and $S_r$ and returns $S_c = (f_c, cf_c, s_c, cs_c)$ calculated as above.

For $e$, we need a value $S_e = (f_e, cf_e, s_e, cs_e)$ such that when combined with any $S$, it returns $S$. Given the constraints, $S_e = (-1, 0, -2, 0)$ is a suitable choice.

When using this in practice, we also need to initialize $S$ (the information loaded into each point of the segment tree). For a single point, $f = A_i$ and $cf = 1$, so we set these values accordingly. For $s$ and $cs$, we can use arbitrary values that do not affect the combination (e.g., $s = -1, cs = 0$). Therefore, we can initialize each element with `seg.set(i, S{A[i], 1, -1, 0})`. The same applies to single point updates.

Using these settings, we can implement the solution.

[Implementation Example (C++, using ACL/segtree)](https://atcoder.jp/contests/abc343/submissions/50850917)