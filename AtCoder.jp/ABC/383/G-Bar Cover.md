## [G - Bar Cover](https://atcoder.jp/contests/abc383/tasks/abc383_g) 

$\displaystyle B_i = \sum_{j=i}^{j+K−1} A_i$ と置くと、問題を以下のように言い換えることが出来ます。

---

長さ $N−K+1$ の数列 $B = (B_1, \dots ,B_{N−K+1})$ が与えられる。この中から、選んだどの二つの要素の距離も $K$ 以上という条件を満たすように要素を $i$ 個選ぶとき、選んだ要素の総和を最大化せよ。

---

分割統治でこの問題を解きます。$dp[l][r][x][y][i]$ を、列 $(B_l, B_{l+1}, \dots, B_{r−1})$ について、左から $x$ 個の要素、右から $y$ 個の要素を選べないという条件が課されたときの、要素を $i$ 個選ぶときの選んだ要素の総和の最大値として定義します。

$dp[l][r][x][y]$ は、$m = l + r_2$ としたとき $dp[l][m][x][∗],dp[m][r][∗][y]$ から以下の方法で計算できます。

* $j = 0, \dots, K−1$ について、$dp[l][m][x][j]$ と $dp[m][r][K−1−j][y]$ をマージする。これらのマージ結果の最大値を取れば $dp[l][r][x][y]$ が得られる。

マージの計算は、愚直に行うと重いので工夫が必要です。ここで必要な観察は $dp[l][r][x][y]$ は $i$ について上に凸になっているということです。上に凸な二つの関数は、傾きを降順にソートすることで線形時間でマージが出来るので、傾きを管理することで高速にマージが行えます。

計算量は $O(NK^2\log⁡ N)$ です。

---

公式解説に対する重要な補足

この問題は、答えが $i$ に対して上に凸であることが重要です。ただし、この解説を書いている現在は[公式解説](https://atcoder.jp/contests/abc383/editorial/11500)には凸であることの証明が書かれておりません。

その証明を簡単にします。

示したいのは以下です。

> 補題
>
> $f(i)$ を最適解とします。このとき、整数 $1 \le i < \lfloor NK \rfloor$ に対して、$f(i)+f(i+2) \le 2f(i+1)$ が成り立つ。

$f(i)$ の最適解を満たすタイルの置き方の左端の index を昇順に並べた列を $g(i) = (a_{i,1}, a_{i,2}, \dots ,a_{i,i})$ とします。このとき、$a_{i,j+K} \le a_{i, j+1}$ が成り立ちます。

$g(i), g(i+2)$ をマージしてソートした列を $A = (A_1, A_2, \dots A_{2i+2})$ とします。

数列 $B,C$ を $B = (A_1, A_3, \dots, A_{2i+1})$ と $C = (A_2, A_4, \dots, A_{2i+2})$ としたとき、$B,C$ はいずれも昇順ソートされており、隣接要素が $K$ 以上離れています。よって、左端の index を昇順に並べた列として成り立ちます。

$B$ の index に沿ってタイルを置いたときの数の和を $b$ とし、$C$ の index に沿ってタイルを置いたときの数の和を $c$ とします。

以下の自明に成り立つ式より、補題が成り立ちます。

$$
f(i)+f(i+2) = b + c \le 2\max⁡(b,c) \le 2f(i+1)
$$

参考 : 以下のリンク先の補題 1

[Here](https://noshi91.github.io/algorithm-encyclopedia/d-edge-shortest-path-monge)


---

## [G - Bar Cover](https://atcoder.jp/contests/abc383/tasks/abc383_g)

If we let $\displaystyle B_i = \sum_{j=i}^{i+K−1} A_j$, the problem can be restated as follows:

---

Given a sequence $B = (B_1, \dots, B_{N−K+1})$ of length $N-K+1$, select $i$ elements such that the distance between any two selected elements is at least $K$, and maximize the total sum of the selected elements.

---

We solve this problem using divide-and-conquer. Define $dp[l][r][x][y][i]$ as the maximum sum of $i$ selected elements from the subarray $(B_l, B_{l+1}, \dots, B_{r−1})$, under the constraints that $x$ elements cannot be selected from the left end and $y$ elements cannot be selected from the right end.

The value of $dp[l][r][x][y]$ can be computed using $dp[l][m][x][*]$ and $dp[m][r][*][y]$, where $m = \lfloor (l + r) / 2 \rfloor$, in the following manner:

- For $j = 0, \dots, K−1$, merge $dp[l][m][x][j]$ and $dp[m][r][K−1−j][y]$. The maximum value obtained from these merges gives $dp[l][r][x][y]$.

The merging process needs optimization to avoid high computational costs. The key observation is that $dp[l][r][x][y]$ is concave with respect to $i$. Two concave functions can be merged in linear time by sorting their slopes in descending order. This approach enables efficient merging by managing slopes appropriately.

The time complexity of this approach is $O(NK^2 \log N)$.

---

### Important Supplement to the Official Explanation

This problem heavily relies on the concavity of the solution with respect to $i$. However, as of now, the [official explanation](https://atcoder.jp/contests/abc383/editorial/11500) does not provide a proof of this concavity.

Here is a brief proof:

The goal is to show the following:

> **Lemma**  
> Let $f(i)$ be the optimal solution. Then, for any integer $1 \leq i < \lfloor NK \rfloor$, the inequality $f(i) + f(i+2) \leq 2f(i+1)$ holds.

Let $g(i)$ denote the sequence of leftmost indices of the tiles that achieve the optimal solution $f(i)$. That is, $g(i) = (a_{i,1}, a_{i,2}, \dots, a_{i,i})$, where $a_{i,j+K} \leq a_{i, j+1}$.

Merge $g(i)$ and $g(i+2)$, and sort the resulting sequence to form $A = (A_1, A_2, \dots, A_{2i+2})$.

Now, divide $A$ into two subsequences:
- $B = (A_1, A_3, \dots, A_{2i+1})$
- $C = (A_2, A_4, \dots, A_{2i+2})$

Both $B$ and $C$ are sorted in ascending order, and the distance between adjacent elements is at least $K$. Thus, both sequences represent valid configurations of leftmost indices.

Let the sums corresponding to $B$ and $C$ be $b$ and $c$, respectively. From the following trivial inequality, the lemma is proven:

$$
f(i) + f(i+2) = b + c \leq 2\max(b, c) \leq 2f(i+1).
$$

For reference, see Lemma 1 in the following link:  
[Here](https://noshi91.github.io/algorithm-encyclopedia/d-edge-shortest-path-monge).
