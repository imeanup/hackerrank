## [F - Dangerous Sugoroku ](https://atcoder.jp/contests/abc388/tasks/abc388_f)

### $A=B$ のとき

明らかに $1 \equiv N(\mod A)$ が必要です。

$1\equiv N(\mod A)$ のとき、通るマスはマス $1, A+1, 2A+1, \dots , N−A, N$ となるため、$1 \equiv x(\mod A)$ なる $x$ であってマス $x$ が悪いマスであるようなものが存在するか判定すればよいです。これは各 $i$ について $L_i \le j \le R_i$ かつ $1 \approx j(\mod A)$ なる $j$ が存在するか判定すればよく、$O(M)$ 時間でできます。

### $A < B$ のとき

マスは全部で $N$ 個あるため、各マスについて辿り着けるか判定することはできません。そこで、一部のマスのみについて辿り着けるか判定することで高速化を行います。

長さ $M+1$ の数列 $S,T$ を以下のように定めます。

* $S_1 = 1$
* $S_i = R_{i−1}+1 (i > 1)$
* $T_i = L_{i−1} (i \le M)$
* $T_{M+1} = N$

また、数列 $I_i$ を $(S_i, S_{i+1}, \dots, T_i) として定めます。

$I_i$ の先頭 $B$ 項を $X_i$、末尾 $B$ 項を $Y_i$ とします。ただし、$I_i$ の長さが $B$ より短いときは $X_i = Y_i = I_i$ とします。また、単に数列の要素が表すマスのことを数列のマスというように表記します。

$X_i$ および $Y_i$ の長さの合計は $O(MB)$ であり、これらの数列のマスについてのみ辿りつけるか判定を行うことを目指します。

$X_1, X_2, \dots, X_i$ および $Y_1, Y_2, \dots, Y_i のマスに対して辿り着けるか計算できているとき、$X_{i+1}$ のマスに辿り着けるか判定することは各マスについて前 $B$ マスを見ることで $O(B^2)$ 時間で簡単に行えます。

$X_1, X_2, \dots, X_i$ および $Y_1, Y_2, \dots,Y_{i−1}$ のマスに対して辿り着けるか計算できているとき、$Y_i$ のマスに辿り着けるか判定することを考えます。これは上と同様に前 $B$ マスに対して判定した上で、$X_i$ の各マスから複数回の移動により到達できるか判定すればよいです（悪いマスを $1$ つ以上飛び越えて到達する場合は前者、そうでない場合は後者により判定できています）。

したがって、間に悪いマスがないときに $w$ マス進めるか？という問題が $O(1)$ 時間で解ければこの場合も $O(B^2)$ 時間で計算が行えます。

$A<B$ より $B−1$ マス進むことと $B$ マス進むことはできるため、$w \ge B^2−3B+2$ のときは $w$ マス進むことはできます。$w < B^2−3B+2$ のときは愚直な $O(B^3)$ 時間の dp により前計算をしておくとよいです。

以上により全体として $O(MB^2 + B^3)$ 時間で計算が完了します。実際の実装上は、set や map などを用いた $O(MB^2+MB\log⁡(MB)+B^3)$ 時間解法を用いることも有力でしょう。$O(MB^2 \log⁡(MB)+B^3)$ 時間解法も定数倍が重くないものは AC することを確認しています。


---

### When $A = B$

Clearly, the condition $1 \equiv N(\mod A)$ is required.

When $1 \equiv N(\mod A)$, the squares we pass through will be $1, A+1, 2A+1, \dots, N-A, N$. Therefore, it suffices to check if there exists a square $x$ where $1 \equiv x(\mod A)$ and $x$ is a "bad" square. This can be done by checking if, for each $i$, there exists a $j$ in the range $L_i \leq j \leq R_i$ such that $1 \equiv j(\mod A)$. This can be done in $O(M)$ time.

### When $A < B$

Since there are $N$ squares in total, it is not feasible to check if each square is reachable. Therefore, we optimize by only checking certain squares to determine if they are reachable.

We define two sequences, $S$ and $T$, of length $M+1$ as follows:

* $S_1 = 1$
* $S_i = R_{i-1} + 1 \text{ (for } i > 1)$
* $T_i = L_{i-1} \text{ (for } i \leq M)$
* $T_{M+1} = N$

We also define the sequence $I_i$ as $(S_i, S_{i+1}, \dots, T_i).

Let the first $B$ elements of $I_i$ be $X_i$ and the last $B$ elements be $Y_i$. If the length of $I_i$ is shorter than $B$, then set $X_i = Y_i = I_i$. Furthermore, we will refer to the elements of the sequence as the squares represented by the sequence.

The total length of $X_i$ and $Y_i$ is $O(MB)$, and we aim to determine if these squares are reachable.

When we have already computed whether the squares in $X_1, X_2, \dots, X_i$ and $Y_1, Y_2, \dots, Y_i$ are reachable, checking if the squares in $X_{i+1}$ are reachable can be easily done in $O(B^2)$ time by looking at the previous $B$ squares.

Next, we consider how to check if the squares in $Y_i$ are reachable, given that we have already determined whether the squares in $X_1, X_2, \dots, X_i$ and $Y_1, Y_2, \dots, Y_{i-1}$ are reachable. This can be done by checking the previous $B$ squares, then checking if the squares in $X_i$ can be reached through multiple steps. If a "bad" square is skipped during the move, the first method applies; if no bad squares are skipped, the second method applies.

Thus, the problem of determining if we can move $w$ squares forward when there are no bad squares in between can be solved in $O(1)$ time. If this is the case, the calculation can be done in $O(B^2)$ time.

Since it is possible to move either $B-1$ squares or $B$ squares forward, if $w \ge B^2 - 3B + 2$, we can move $w$ squares forward. If $w < B^2 - 3B + 2$, it is best to precompute the solution using a straightforward $O(B^3)$ dynamic programming approach.

As a result, the overall time complexity will be $O(MB^2 + B^3)$. In practice, using a solution with a time complexity of $O(MB^2 + MB\log(MB) + B^3)$ with sets or maps is also a viable approach. We have confirmed that solutions with a time complexity of $O(MB^2\log(MB) + B^3)$ are accepted as long as the constant factors are not too heavy.

---


$R_i + 1 < L_{i+1}$ が成り立っていると仮定します。(実装上では適当な圧縮をしてください。)

$dp[i]$ を $0$ 以上 $2^B$ 未満の整数であって、$d = 0, 1, \dots,B−1$ に対して以下の条件を満たすものとします。

* $dp[i]$ の $2^d$ の桁が $1$ であることと、マス $i−d$ に到達可能であることが同値

$dp[N]$ の値が求まれば良いです。

まず、悪いマスがないときのことを考えます。

$dp[i+1]$ の値は $dp[i]$ の値のみに依存して求まります。よってダブリングすることで、 $dp[i]$ の値がわかっているとき、$dp[i+a]$ の値が時間計算量 $O(\log ⁡(a))$ で求まります。

上記のことを用いると、 $dp[R_i+1]$ がわかっているとき、 $dp[L_{i+1}−1]$ が高速に求められます。

$dp[L_i − 1]$ がわかっているとき、$dp[R_i]$ はシフトをすることで簡単に求まります。

マス $R_i + 1$ に到達可能であることは、$2^{A−1} \le dp[R_i]$ と同値であるため、 $dp[Ri+1]$ も簡単に求められます。

以上のことを用いると、 $dp[N]$ が時間計算量 $O((M+2^B)\log⁡(N))$ で求められます。

[c++ 実装例 173ms](https://atcoder.jp/contests/abc388/submissions/61607726)

---

Assume that the condition $R_i + 1 < L_{i+1}$ holds. (For implementation, perform appropriate compression.)

Let $dp[i]$ be an integer in the range $0 \le dp[i] < 2^B$, and for each $d = 0, 1, \dots, B - 1$, we assume the following condition holds:

* The $2^d$-th bit of $dp[i]$ being $1$ is equivalent to being able to reach square $i - d$.

The goal is to find the value of $dp[N]$.

First, consider the case where there are no "bad" squares.

The value of $dp[i+1]$ depends only on the value of $dp[i]$. Thus, by using doubling, when the value of $dp[i]$ is known, the value of $dp[i + a]$ can be computed in $O(\log(a))$ time.

Using the above, when $dp[R_i + 1]$ is known, $dp[L_{i+1} - 1]$ can be computed efficiently.

When $dp[L_i - 1]$ is known, $dp[R_i]$ can be easily computed by shifting.

Being able to reach square $R_i + 1$ is equivalent to $2^{A-1} \le dp[R_i]$, so $dp[R_i + 1]$ can also be computed easily.

Using all of the above, $dp[N]$ can be computed in $O((M + 2^B)\log(N))$ time complexity.

[C++ implementation example 173ms](https://atcoder.jp/contests/abc388/submissions/61607726)

---


[公式解説](https://atcoder.jp/contests/abc388/editorial/11910) では，「悪いマスが存在しないときにちょうど $w$ マス進めるか？」という部分問題を DP により解いていました．ここでは，別の方法を紹介します．

ちょうど $w$ マス進める必要十分条件は， $w\le \left\lfloor\dfrac{w}{A}\right\rfloor B$ と表されます．この条件は，以下のようにして導出されます．

ちょうど $k$ 回の操作で移動できるマスは， $k_A$ から $k_B$ の間のすべてのマスです．逆に，移動できるすべてのマス $w$ に対して，ある正整数 $k$ が存在して $k_A \le w \le k_B$ が成り立ちます．$k_A \le w$ を満たす最大の $k$ は $k^{\ast} = \left\lfloor \dfrac{w}{A} \right\rfloor$ であり，この $k^{\ast}$ に対して $w \le k^{\ast} B$ が成り立つかどうか判定すればよいです．この条件はすなわち $w\le \left\lfloor\dfrac{w}{A}\right\rfloor B$ です．

[実装例 (Python)](https://atcoder.jp/contests/abc388/submissions/61519459)

---

In the [official explanation](https://atcoder.jp/contests/abc388/editorial/11910), the subproblem "Can we move exactly $w$ squares when no bad squares exist?" is solved using dynamic programming. Here, we introduce an alternative method.

The necessary and sufficient condition for moving exactly $w$ squares is given by $w \le \left\lfloor \frac{w}{A} \right\rfloor B$. This condition can be derived as follows.

The squares that can be moved exactly $k$ times are all the squares between $k_A$ and $k_B$. Conversely, for any square $w$ that can be moved, there exists a positive integer $k$ such that $k_A \le w \le k_B$. The largest $k$ that satisfies $k_A \le w$ is $k^{\ast} = \left\lfloor \frac{w}{A} \right\rfloor$, and to check whether $w \le k^{\ast} B$ holds for this $k^{\ast}$ is sufficient. This condition is equivalent to $w \le \left\lfloor \frac{w}{A} \right\rfloor B$.

[Implementation Example (Python)](https://atcoder.jp/contests/abc388/submissions/61519459)
