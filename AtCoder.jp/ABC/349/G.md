## [G - Palindrome Construction](https://atcoder.jp/contests/abc349/tasks/abc349_g)


<!-- ### グラフの問題としての表現

まず，計算量を意識せずに解法を考えます．

$N$ 頂点のグラフを考えます． $S_i = S_j$ となる必要があるとき頂点 $i, j$ 間に **青** の辺を， $S_i \ne S_j$ となる必要があるとき頂点 $i, j$ 間に **赤** の辺を張ります．

まず，各 $i$ について， $(S_{i-A_i}, S_{i-A_i +1}, \cdots, S_{i+A_i})$ が回文になっているという条件から，青の辺 $(i-A_i, i+A_i), (i - A_i + 1, i + A_i -1), \cdots, (i-1, i+1)$ を張ります．

次に，各 $i$ について， $2 \le i - A_i, i + A_i \le N-1$ ならば， $(S_{i-A_i-1}, S_{i-A_i+1}, \cdots, S_{i+A_i + 1})$ が回文でないという条件から $S_{i-A_i-1} \ne S_{i+A_i + 1}$ が必要です．よって，赤の辺 $(i-A_i - 1, i+A_i+1)$ を張ります．

青の辺でつながった連結成分に含まれる頂点はすべて同じ値を取る必要があります．そこで，青の辺でつながった連結成分を縮約します．そして，赤の辺の両端の頂点が異なる値を取るように，それぞれの連結成分に値を割り当てればよいです．

縮約後，赤の辺からなる自己ループが存在すれば，連結成分への値の割り当ては不可能であり，条件を満たす $S$ は存在しません．

赤の辺からなる自己ループが存在しない場合，番号の小さい頂点を含む連結成分から順番に見ていって，赤の辺で隣接している連結成分でまだ使用されていない値のうちできるだけ小さいものを貪欲に割り当てていけばよいです．

以上の解法の問題点は，青の辺が最大で $O(N^2)$ 本張られるという点にあります．そこで，**青の辺に関する連結性を保ったまま，張る必要のある青の辺の本数を減らす**必要があります．

### Manacher のアルゴリズムによる高速化

**Manacher のアルゴリズム**を応用することで，青の辺の本数を $O(N)$ 本に減らすことができます．Manacher のアルゴリズムは，与えられた文字列の各 index を中心とした極大な回文部分文字列の長さを $O(N)$ 時間で求めるアルゴリズムです．

Manacher のアルゴリズムのアイデアは，「 **すでに計算したものを利用して，調べるまでもなく回文になるとわかっている部分の計算を省略する** 」というものです．アルゴリズムの詳細な説明は以下の文献に譲ります．

* 日本語：[文字列の頭良い感じの線形アルゴリズムたち２](https://snuke.hatenablog.com/entry/2014/12/02/235837)
* 英語：[Manacher’s Algorithm - Finding all sub-palindromes in $O(N)$](https://cp-algorithms.com/string/manacher.html)

Manacher のアルゴリズムを応用することで， **条件を満たす $S$ が存在するとき** ，以下の疑似コードにより青の辺を正しく張ることができます． -->

### Representation as a Graph Problem

First, let's consider the solution without worrying about computational complexity.

We consider a graph with $N$ vertices. We create **blue** edges between vertices $i$ and $j$ when $S_i = S_j$, and **red** edges between vertices $i$ and $j$ when $S_i \neq S_j$.

First, for each $i$, based on the condition that $(S_{i-A_i}, S_{i-A_i +1}, \cdots, S_{i+A_i})$ forms a palindrome, we create blue edges $(i-A_i, i+A_i), (i - A_i + 1, i + A_i -1), \cdots, (i-1, i+1)$.

Next, for each $i$, if $2 \leq i - A_i, i + A_i \leq N-1$, then we need $S_{i-A_i-1} \neq S_{i+A_i + 1}$ based on the condition that $(S_{i-A_i-1}, S_{i-A_i+1}, \cdots, S_{i+A_i + 1})$ is not a palindrome. Therefore, we create red edges $(i-A_i - 1, i+A_i+1)$.

All vertices in connected components connected by blue edges must have the same value. Thus, we contract the connected components connected by blue edges. Then, we assign values to each connected component such that the vertices at the ends of the red edges have different values.

After contraction, if there exist self-loops formed by red edges, it's impossible to assign values to the connected components, and there exists no $S$ satisfying the conditions.

If there are no self-loops formed by red edges, we can greedily assign the smallest possible values to the connected components, starting from the connected component containing the vertex with the smallest index and proceeding to the connected components adjacent via red edges.

The main issue with this solution is that the number of blue edges can be as large as $O(N^2)$. Therefore, it's necessary to reduce the number of blue edges while preserving the connectivity.

### Speeding Up with Manacher's Algorithm

By applying **Manacher's Algorithm**, we can reduce the number of blue edges to $O(N)$. Manacher's Algorithm efficiently computes the lengths of maximal palindrome substrings centered at each index of a given string in $O(N)$ time.

The key idea behind Manacher's Algorithm is to "utilize previously computed results to skip unnecessary computations for parts that are already known to be palindromic." For detailed explanations of the algorithm, please refer to the following resources:

* Japanese: [文字列の頭良い感じの線形アルゴリズムたち２](https://snuke.hatenablog.com/entry/2014/12/02/235837)
* English: [Manacher’s Algorithm - Finding all sub-palindromes in $O(N)$](https://cp-algorithms.com/string/manacher.html)

By applying Manacher's Algorithm, when **there exists an $S$ satisfying the conditions**, we can correctly construct the blue edges using the pseudo code provided below.

```py
i = j = 0
while i < N:
    while j < A[i] + 1:
        unite(i - j, i + j)
        j += 1

    k = 1
    while i - k >= 0 and k + A[i - k] + 1 < j:
        k += 1
    i += k
    j -= k
```

<!-- ここで， $A$ の添字や頂点の番号は 0-indexed であることに注意してください．また，関数 `unite(u, v)` は，頂点 $u, v$ 間に青の辺を張る処理です．

このアルゴリズムの時間計算量を解析します．一見，二重ループなので $O(N^2)$ に見えますが，実は $O(N)$ になっていることを示します．

まず，3行目の while ループ `while j < A[i] + 1` が実行される回数を解析します．$i+j$ の値に注目すると，

* 10行目と11行目をまとめて考えると，ここで $i+j$ は不変
* $i+j$ が変化するのは5行目のみで，実行されるたびに $1$ 増える
* 3行目の while ループの条件式から， $i+j \le i + A[i] \le i + (N-i-1) < N$

が成り立ちます．これらより，3行目の while ループはたかだか $N$ 回程度実行されます．

次に，8行目の while ループ `while i - k >= 0 and k + A[i - k] + 1 < j` が実行される回数を解析します． $i$ の値に注目すると，

* $k$ は，8行目の while ループがそのステップで実行された回数
* $i$ は $k$ の総和だから，アルゴリズム全体で8行目の while ループが実行された回数
* 2行目の while ループの条件式から， $i < N$

が成り立ちます．これらより， 8行目の while ループはたかだか $N$ 回程度実行されます．

以上より，このアルゴリズムが $O(N)$ 時間で動作することが確認できました．

以上のアルゴリズムは，「条件を満たす $S$ が存在するとき」という条件付きで動作します．よって，得られた $S$ が実際に条件を満たすことの確認が必要です．これは，再び Manacher のアルゴリズムにより $O(N)$ 時間で確認できます． -->

Here, please note that the indices of $A$ and vertex numbers are 0-indexed. Also, the function `unite(u, v)` is the process of creating a blue edge between vertices $u$ and $v$.

Let's analyze the time complexity of this algorithm. At first glance, it seems to have a nested loop, so it appears to be $O(N^2)$, but we will show that it is actually $O(N)$.

First, let's analyze the number of executions of the while loop on line 3 `while j < A[i] + 1`. If we focus on the value of $i+j$:

- Combining lines 10 and 11, $i+j$ remains unchanged here.
- $i+j$ changes only in line 5, and it increases by $1$ each time it is executed.
- Based on the condition of the while loop on line 3, $i+j \leq i + A[i] \leq i + (N-i-1) < N$ holds.

From these, we can see that the while loop on line 3 is executed at most about $N$ times.

Next, let's analyze the number of executions of the while loop on line 8 `while i - k >= 0 and k + A[i - k] + 1 < j`. If we focus on the value of $i$:

- $k$ is the number of times the while loop on line 8 is executed in its step.
- Since $i$ is the sum of $k$, the while loop on line 8 is executed a total of $N$ times throughout the algorithm.
- Based on the condition of the while loop on line 2, $i < N$ holds.

From these, we can see that the while loop on line 8 is executed at most about $N$ times.

Therefore, we have confirmed that this algorithm operates in $O(N)$ time.

This algorithm operates conditionally on the existence of an $S$ satisfying the conditions. Therefore, it is necessary to verify that the obtained $S$ actually satisfies the conditions. This can be verified in $O(N)$ time again using Manacher's Algorithm.