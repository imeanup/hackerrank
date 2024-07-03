## [E - Random Swaps of Balls](https://atcoder.jp/contests/abc360/tasks/abc360_e)



<details><summary>Japanese Editorial</summary><br>

操作の対称性を考えると、ある時点で黒いボールが最も左にある確率を $p$ としたとき、左から $2, 3, \dots, N$ 番目にある確率はどれも $\dfrac{1-p}{N_!}$ です。そのため、 $K$ 回操作をした後に黒いボールが最も左にある確率が求まれば、この問題を解けます。これは動的計画法で求められます。

* $dp[i] := i$ 回操作をしたとき黒いボールが最も左にある確率

と定義します。求めたいものは $dp[K]$ です。遷移には、以下の $2$ つの確率が必要です。

* 黒いボールが最も左にある状態から $1$ 回操作して、黒いボールが最も左以外のどこかに移動する確率
* 黒いボールが最も左以外のどこかにある状態から $1$ 回操作して、黒いボールが最も左に移動する確率

それぞれ $p, q$ とします。DP の遷移は以下の通りです。

* $dp[0] = 1$
* $dp[i+1] = (1-p) dp[i] + q(1-dp[i])$

$p, q$ は単純な場合の数の計算で

* $p = \dfrac{2(n-1)}{n^2}$
* $q =  \dfrac{2}{n^2}$

とわかります。これを素直に実装すると計算量 $O(K)$ の解法が得られます。整理すると $2$ 項間線形漸化式の形になり、一般項を簡単な形で表現できます (高校数学の典型的な問題です) 。累乗の計算がボトルネックとなり、 $dp[K]$ は計算量 $O(\log K)$ で求まります。

[実装例 (C++)](https://atcoder.jp/contests/abc360/submissions/54963919)

より一般に、線形漸化式の第 $N$ 項を求める高速な方法として、行列累乗や Fiduccia のアルゴリズムがあります。

</details><br>

Considering the symmetry of operations, if the probability of the black ball being the leftmost at any given time is $p$, then the probability of it being at the $2^{nd}, 3^{rd}, \dots, N^{th}$ position from the left is each $\dfrac{1-p}{N-1}$. Therefore, if we can determine the probability of the black ball being the leftmost after $K$ operations, we can solve this problem. This can be calculated using dynamic programming.

* Define $dp[i] :=$ the probability of the black ball being the leftmost after $i$ operations.

The value we seek is $dp[K]$. For the transitions, we need the following two probabilities:

* The probability that the black ball moves from the leftmost position to any other position after one operation.
* The probability that the black ball moves from any other position to the leftmost position after one operation.

Let these probabilities be $p$ and $q$, respectively. The DP transition is as follows:

* $dp[0] = 1$
* $dp[i+1] = (1-p) dp[i] + q(1-dp[i])$

The probabilities $p$ and $q$ can be calculated with simple combinatorics:

* $p = \dfrac{2(n-1)}{n^2}$
* $q =  \dfrac{2}{n^2}$

By implementing this directly, we get a solution with a time complexity of $O(K)$. When simplified, it forms a linear recurrence relation of two terms, allowing us to express the general term in a simpler form (a typical problem in high school mathematics). The bottleneck is the computation of powers, and $dp[K]$ can be obtained with a time complexity of $O(\log K)$.

[Example implementation (C++)](https://atcoder.jp/contests/abc360/submissions/54963919)

More generally, for quickly computing the $N$th term of a linear recurrence relation, methods such as matrix exponentiation and Fiduccia's algorithm can be used.
