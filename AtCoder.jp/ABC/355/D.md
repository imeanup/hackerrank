## [D - Intersecting Intervals](https://atcoder.jp/contests/abc355/tasks/abc355_d)

<details><summary><b>Japanese</b></summary><br>

すべての区間の組について共通部分を持つかどうか調べると $O(N^2)$ 時間かかり，実行時間制限に間に合いません．適切なアルゴリズムを用いて高速化する必要があります．

ここで，共通部分を持つ区間の組を数える代わりに，共通部分を持たない区間の組の個数 $x$ を求めて $\frac{N(N-1)}{2}$ から引くことで答えを求めることにします（これは，「 **余事象を考える** 」という典型的な考え方です）．

区間 $i$ の左にあって区間 $i$ と共通部分を持たない区間は， $r_j < l_i$ を満たす区間 $j$ です．よって，各 $i = 1, 2, \dots, N$ について， $r_j < l_i$ なる $j$ の個数を求めると，その総和が求める $x$ です．

これは，**尺取り法**というテクニックによって高速に計算することができます． まず，数列 $L, R$ を，それぞれ $(l_1, l_2, \dots, l_N), (r_1, r_2, \dots, r_N)$ を昇順に並べ替えたものとします． $i = 1, 2, \dots, N$ の順番に，$R_j < L_i$ を満たす $j$ の個数 $c_i$ を求めましょう．$R$ が昇順に並んでいることから，$R_j < L_i$ を満たす $j$ は $1, 2, \dots, c_i$ です． よって，次のようなアルゴリズムが考えられます．

1. $i = 1, 2, \dots, N$ の順番に，次の操作を行う．
   1. $c \gets 1$ とする．
   2. $R_c < L_i$ である間， $c \gets c+1$ とする．
   3. $c_i \gets c-1$ とする．

このアルゴリズムは，各 $i$ についてステップ 1.2 が最大で $N-1$ 回実行されるため，依然として全体で $O(N^2)$ 時間かかってしまいます．高速化にはさらなる考察が必要です．

ここで，重要な性質として， $L$ が昇順に並んでいることから $c_i \le c_{i + 1}$ が各 $i = 1, 2, \dots, N-1$ について成り立ちます なぜならば， $R_{c_i}, R_{c_i + 1}, \dots,$ より， $R$ の少なくとも $c_i$ 個は $L_i + 1$ より小さいからです．

よって， $c_{i+1}$ を求めるときに， $R_1, R_2, \dots,$ と $1$ から順番に調べるのではなく，$R_{c_i}, R_{c_i + 1}, \dots,$ というように，探索を $c_i$ からはじめても良いです．つまり，先程のアルゴリズムを次のように変更することができます．

1. $c \gets 1$ とする．
2. $i = 1, 2, \dots, N$ の順番に，次の操作を行う．
   1. $R_c < L_i$ である間， $c \gets c+1$ とする．
   2. $c_i \gets c-1$ とする．

このアルゴリズムの計算量を調べましょう．ステップ 2.1 が実行されるたびに， $c$ は $1$ 増えます．また， $c$ はたかだか $N$ です．よって，ステップ 2.1 はプログラム全体でたかだか $N-1$ 回しか実行されません．よって，このアルゴリズムの時間計算量は（ソートを除いて）$O(N)$ であり，高速に動作します．

実装例 (Python)

</details><br>


If we check for intersections between all pairs of intervals, it will take $O(N^2)$ time, which will not meet the time constraints. We need to use an appropriate algorithm to speed this up.

Instead of counting pairs of intervals that do intersect, we'll count the number of pairs $x$ that do not intersect and subtract this from $\frac{N(N-1)}{2}$ to get our answer. This is a typical approach known as considering the "complementary event."

An interval $j$ that does not intersect with interval $i$ must satisfy $r_j < l_i$. Therefore, for each $i = 1, 2, \dots, N$, we need to count the number of $j$ that satisfy $r_j < l_i$. The sum of these counts will give us $x$.

This can be efficiently calculated using the **two-pointer technique**. First, sort the sequences $L$ and $R$ in ascending order, where $L = (l_1, l_2, \dots, l_N)$ and $R = (r_1, r_2, \dots, r_N)$. For each $i = 1, 2, \dots, N$, we determine the count $c_i$ of $j$ such that $R_j < L_i$. Given that $R$ is sorted in ascending order, $j$ satisfying $R_j < L_i$ will be among the first $c_i$ elements.

The algorithm can be described as follows:

1. For $i = 1, 2, \dots, N$:
   1. Set $c \gets 1$.
   2. While $R_c < L_i$, increment $c$ by 1.
   3. Set $c_i \gets c - 1$.

However, this still results in $O(N^2)$ time complexity as step 1.2 can be executed up to $N-1$ times for each $i$. We need further optimization.

An important property is that $c_i \le c_{i+1}$ for $i = 1, 2, \dots, N-1$ because $L$ is sorted in ascending order. This means we can start the search for $c_{i+1}$ from $c_i$ instead of from 1, modifying the algorithm as follows:

1. Initialize $c \gets 1$.
2. For $i = 1, 2, \dots, N$:
   1. While $R_c < L_i$, increment $c$ by 1.
   2. Set $c_i \gets c - 1$.

Now, let’s analyze the time complexity. Each increment of $c$ in step 2.1 only happens $N-1$ times in total because $c$ can only increase up to $N$. Hence, this algorithm runs in $O(N)$ time, excluding the sorting step, making it very efficient.

Thus, the overall algorithm, including sorting, operates in $O(N \log N)$ time due to the sorting step, which is efficient and meets the time constraints.

<details><summary><b>Code</b></summary>

```py
N = int(input())
l = [0] * N
r = [0] * N
for i in range(N):
    l[i], r[i] = map(int, input().split())
l.sort()
r.sort()

ans = N * (N - 1) // 2
j = 0
for i in range(N):
    while r[j] < l[i]:
        j += 1
    ans -= j
print(ans)
```

</details>
