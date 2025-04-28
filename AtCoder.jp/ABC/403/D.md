## [D - Forbidden Difference](https://atcoder.jp/contests/abc403/tasks/abc403_d)


### $D=0$ の場合

$D=0$ の場合，$|A_i − A_j| =0 \Leftrightarrow A_i = A_j$ なので，$A$ に同じ値が現れないようにすればよいです．

$A$ に現れる相異なる値の個数を $X$ としたとき，それぞれの値を持つ要素を $1$ つだけ残せるので，$B$ の長さは最大で $X$ です．よって，最小の操作回数は $N − X$ です．

### $D \ge 1$ の場合：問題の言い換え

$A$ に $x(0 \le x \le 10^6)$ が現れる個数を $C_x$ とします．$A$ の要素を $1$ つ削除することは，$C$ の非ゼロの要素を $1$ 減らすことに対応します．また， $|A_i−A_j| = D$ なる $i,j$ が存在することは，$C_x > 0$ かつ $C_{x + D} > 0$ なる $x$ が存在することと対応します．よって，問題は以下のように言い換えられます．

* $C_x$ の非ゼロ要素を $1$ つ選んで $1$ 減らすことを最小で何回繰り返せば，すべての $x$ について $C_x = 0$ または $C_{x+D} = 0$ が成り立つようにできるか？

「すべての $x$ について $C_x = 0$ または $C_{x+D} = 0$」という条件は，$x \mod ⁡D$ に注目することで，以下のように分解することができます．

* すべての $i=0,1,\dots ,D−1$ について以下が成り立つ
  * すべての $j=0,1,\dots ,\lfloor(10^6−i)/D\rfloor − 1$ について $C_{i+D_j} = 0$ または $C_{i+D_{(j+1)}} = 0$

### 動的計画法による解法

この問題は，$i=0,1,\dots ,D−1$ について独立に解くことができます．**動的計画法**を用います．$i$ を固定し，$dp[j]$ を，「$C_i, C_{i+D}, \dots , C_{i+D_j}$ の間で条件を満たすために必要な操作回数」とします．

$dp[0], \dots,dp[j]$ までわかっているときに，$dp[j+1]$ を計算する方法を考えます．$C_{i+D_{(j+1)}}$ を $0$ にするか否かで場合分けをします．

* $C_{i+D_{(j+1)}}$ を $0$ にする場合：$C_{i+D_{(j+1)}}$ 回操作をする必要があります．このとき，$C_{i+D_j}$ の値は何でも良く，単に $C_i, \dots ,C_{i+D_j}$ の間で条件を満たしていれば良いので，全体の操作回数は $dp[j]+C_{i+D_{(j+1)}}$ です．
* $C_{i+D_{(j+1)}}$ を $0$ にしない場合：$C_{i+D_{(j+1)}}$ には $1$ 回も操作する必要がありません．このとき，$C_{i+D_j}$ を $0$ にする必要があり，さらに $C_i, \dots ,C_{i+D_{(j−1)}}$ の間で条件を満たす必要があります．全体の操作回数は $dp[j−1] + C_{i+D_j}$ です．

以上 $2$ 通りのうち，小さい方を取ればよいので， $dp[j+1]= \min⁡ \{ dp[j] + C_{i+D_{(j−1)}}, dp[j−1] + C_{i+D_j} \}$ という漸化式が得られます．$dp[\lfloor(10^6−i)/D\rfloor]$ が答えです．

以上の動的計画法を各 $i$ について実行し，総和を求めることで，問題を解くことができます．時間計算量は， $M=10^6$ として $O(M)$ です．

[実装例 (Python)](https://atcoder.jp/contests/abc403/submissions/65083840)


---

### Case $D = 0$

When $D = 0$, the condition $\lvert A_i - A_j\rvert = 0$ is equivalent to $A_i = A_j$.  Thus, we must ensure no value appears more than once in $A$.

Let $X$ be the number of distinct values in $A$.  We can keep exactly one occurrence of each distinct value, so the maximum possible length of $B$ is $X$.  Hence the minimum number of deletions needed is
$$
N - X.
$$

---

### Case $D \ge 1$: Rephrasing the Problem

Define $C_x$ to be the count of occurrences of the value $x$ ($0 \le x \le 10^6$) in $A$.  Removing one element from $A$ corresponds to decrementing one nonzero $C_x$ by 1.  The existence of a pair $(i,j)$ with $\lvert A_i - A_j\rvert = D$ is equivalent to there being some $x$ for which
$$
C_x > 0
\quad\text{and}\quad
C_{x+D} > 0.
$$
Thus the task becomes:

> Repeatedly choose a nonzero $C_x$ and decrement it by 1.  What is the minimum number of such decrements needed so that for every $x$, either $C_x = 0$ or $C_{x+D} = 0$?

Notice that the condition “for all $x$, either $C_x = 0$ or $C_{x+D} = 0$” can be checked independently for each residue class modulo $D$.  More precisely, for each $i = 0,1,\dots,D-1$, consider the sequence
$$
C_i, \; C_{i+D}, \; C_{i+2D},\;\dots
$$
We require that in this sequence, no two consecutive entries are both positive.

---

### Dynamic Programming Solution

We solve separately for each residue $i = 0,1,\dots,D-1$.  Let
$$
dp[j] = \text{the minimum number of decrements needed so that, among }
\{\,C_i, C_{i+D}, \dots, C_{i+jD}\},\text{ no two consecutive are both positive.}
$$
We build up $dp$ in increasing $j$.  To compute $dp[j+1]$, we look at two possibilities for the next term $C_{i+(j+1)D}$:

1. **We reduce $C_{i+(j+1)D}$ to zero.**  
   That costs $C_{i+(j+1)D}$ decrements.  The earlier $C_{i+jD}$ can be anything—only the condition among the first $j+1$ terms matters—so this yields
   $$
   dp[j] + C_{i+(j+1)D}.
   $$

2. **We leave $C_{i+(j+1)D}$ positive (i.e.\ make no decrements there).**  
   Then we must force the previous count $C_{i+jD}$ to zero (to avoid a forbidden pair).  That costs $C_{i+jD}$ decrements, and we need the condition satisfied among the first $j$ terms.  Thus this option gives
   $$
   dp[j-1] + C_{i+jD}.
   $$

Taking the minimum of these two cases,
$$
dp[j+1]
= \min\bigl(dp[j] + C_{i+(j+1)D},\; dp[j-1] + C_{i+jD}\bigr).
$$
After filling out $dp$ up to $j = \bigl\lfloor(10^6 - i)/D\bigr\rfloor$, the value $dp[\lfloor(10^6 - i)/D\rfloor]$ is the answer for residue $i$.  Summing these answers over all $i=0,1,\dots,D-1$ gives the total minimum deletions.

Since the total range is $10^6$, this runs in $O(10^6)$ time.

---

[Sample implementation in Python](https://atcoder.jp/contests/abc403/submissions/65083840)
