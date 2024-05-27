## [G - Baseball](https://atcoder.jp/contests/abc355/tasks/abc355_g)

<details><summary><b>Japanese</b></summary><br>

$S := \sum_{i=1}^N P_i$ とします．

### グラフによる表現と DP の定式化

本問題をグラフの問題として表現します．$0, 1, \cdots, N+1$ のラベルがついた $N+2$ 頂点のグラフに，以下のように有向辺を張ります．

* 辺 $(0, j) (1\le j \le N)$ の重みを $\sum_{y=1}^{j-1} P_y \times (j-y)$ とする
* 辺 $(i, j) (1 \le i < j \le N)$ の重みを $\sum_{y=i}^{j-1} P_y \times \min(y-i, j-y)$ とする
* 辺 $(i, N+1) (1\le i \le N)$ の重みを $\sum_{y=i}^N P_y \times (y-i)$ とする

高橋君が $x_1, x_2, \cdots, x_K$ を選んだとき，青木君が得るスコアの期待値の $S$ 倍は，このグラフの長さ $K+1$ のパス $0 \to x_1 \to \cdots \to x_K \to N+1$ の重みになります．青木君が得るスコアの期待値の最小値を求める問題は，このグラフでちょうど $K+1$ 辺を使ったときの頂点 $0$ から頂点 $N+1$ への最短路を求める問題に帰着します．

グラフは DAG なので，この問題は DP により解くことができます． $dp[k][j]$ を，「$k$ 本の辺を使ったときの頂点 $0$ から頂点 $j$ への最短路長」とします．$dp[K+1][N+1]$ が求める答えです． 遷移は次のように行います．

$$
dp[k][j] = \min_{i<j}\{dp[k-1][i] + c(i, j)\} (\star)
$$

ここで， $c(i, j)$ は辺 $(i, j)$ の重みです．$c(i, j)$ は， $P_y$ と $P_y \times y$ の累積和を前計算しておくことにより，クエリあたり $O(1)$ 時間で計算できます．

ところが，この DP を素直に実装すると， $O(N^2K)$ 時間かかってしまいます．

### コストの Monge 性と Alien DP による高速化

式 $(\star)$ で表される DP は，遷移のコスト $c(i, j)$ が **Monge 性** と呼ばれる性質を満たすときに， **Alien DP** と呼ばれる手法を用いることで高速に計算できます．

コスト $c(i, j)$ が Monge であるとは，以下の条件を満たすことです．

$$
\forall i, j, k, l, \ 0 \le i < j < k < l \le N + 1 \implies c(i, l) + c(j, k) \ge c(i, k) + c(j, l)
$$

本問題のコストが Monge 性を満たすことは，直感的には以下の図より理解できます．$c(x, y)$ は $x$ と $y$ を結ぶ三角形領域の面積にだいたい対応していると思ってください． $c(i, l) + c(j, k) = (A+B+C+D) + C = A+B+2C+D, c(i, k) + (j, l) = (B+C) + (C+D) = B+2C+D$  となり， Monge 性の条件の不等式が成り立ちます．

![](https://img.atcoder.jp/abc355/3ccf746e9e2be2a73d06c90e03f79ceb.png)

次に，Alien DP を説明します．アルゴリズムの正当性などの細かい議論は以下の参考文献にゆずり，ここではアルゴリズムのみ述べます．

* noshi91 さんによる記事: [Monge グラフ上の $d$-辺最短路長を計算するアルゴリズム](https://noshi91.github.io/algorithm-encyclopedia/d-edge-shortest-path-monge)

まず，関数 $f(\lambda)$ を次のように定義します．

* コスト $c(i, j)$ に一様に $\lambda$ を足した上で， **使う辺の本数の制約を無視したときの** 頂点 $0$ から頂点 $N+1$ への最短路長を $d$ とする． $f(\lambda) := d - \lambda(K+1)$ とする．

$\max_{\lambda \in \Z} f(\lambda)$ が求める答えとなります．$\lambda$ は辺を1本使うことに対するペナルティであり，このアルゴリズムは，使用する辺の本数がちょうど$K+1$本となるようなペナルティ $\lambda$ の値を探索しているとみなせます．

$f(\lambda)$ は $\lambda$ に関して上に凸であること，また最適な $\lambda$ は $0 \le \lambda \le 3 \max_{i, j} c(i, j) \le 3NS$  の範囲にあることが示せます．よって，この最大化問題は，傾きの二分探索，三分探索，または黄金分割探索により $O(\log (NS))$ 回の $f(\lambda)$ の評価により解くことができます．この最大化問題を解く各手法は以下の記事で比較されています．

* noshi91 さんによる記事: [Aliens DP における二分探索の色々](https://noshi91.hatenablog.com/entry/2023/11/20/052227)

あとは，与えられた $\lambda$ に対して $f(\lambda)$ を高速に求めることができればよいです． これはふたたび DP によって計算することができます．遷移は以下のとおりです．

$$
dp[j] = \min_{i<j}\{dp[i] + c(i, j) + \lambda\} \ \ (\star\star)
$$

DP の次元が一つ落ちましたが，これを素直に実装すると $O(N^2 \log (NS))$ 時間となり，依然として間に合いません． しかし，式 $(\star \star)$ で表される DP は，コスト $c(i, j)$ が Monge であるときに高速に計算できることが知られています．

### Monge な辺重みを持つグラフの最短路問題

式 $(\star \star)$ の DP を高速に実行する方法をいくつか紹介します．解法1から3は，以下の資料で詳しく説明されています．

* tatyam さんによるスライド: [Monge の手引書](https://speakerdeck.com/tatyam_prime/monge-noshou-yin-shu)

#### 解法1. 分割統治 + monotone minima $O(N (\log N)^2)$ 時間

$(N+2)\times (N+2)$ 行列 $A$ を，$A_{ij} = dp[j] + c(i, j) + \lambda$ として定義します．すると，DP $(\star \star)$ は $A$ の各行の最小値を求める問題になります．$c(i, j)$ が Monge であるとき，行列 $A$ は **totally monotone** という性質を持ちます．**Monotone minima** は，totally monotone な行列の各行の最小値を $O(N\log N)$ 時間で求めることのできるアルゴリズムです．

Monotone minima は $A$ の要素に任意の順番でアクセスできることを要求します．ところが，今回の設定では $dp[j]$ の値を知るまで $A_{ij}$ の値を知ることができず，$dp[j]$ の値を知るには， $A$ の $j$ 行目の最小値を知っている必要があります．このように，要素にアクセスできる順番に制限があるため，今回は monotone minima を直接適用することができません．

そこで，分割統治を行います．$solve(l, r)$ を，$dp[l], \cdots, dp[r-1]$ を求める処理として，次のようにします．

1. $m := \Big\lfloor \dfrac{(l+r)}{2}\Big \rfloor$ として， $solve(l, m)$ を再帰的に実行する．
2. $dp[l], \cdots, dp[m-1]$ から $dp[m], \cdots, dp[r-1]$ への遷移を処理する．このとき，必要な $dp$ の値はすべてわかっているから， monotone minima が使える．
3. $solve(m, r)$ を再帰的に実行する．

こうして $O(N (\log N)^2)$ 時間のアルゴリズムが得られます．全体では $O(N (\log N)^2 \log (NS))$ 時間となります．高速な言語であれば AC を得ることができます．

#### 解法2. 分割統治 + SMAWK $O(N\log N)$ 時間

解法1の monotone minima を **SMAWK アルゴリズム**に置き換えることで，log を1つ落とすことができます．SMAWK アルゴリズムは，totally monotone な行列の各行の最小値を $O(N)$ 時間で求めるアルゴリズムです．ただし，SMAWK アルゴリズムは定数倍が比較的重いため，本問題の制約下では monotone minima とほとんど区別できないと思います．

#### 解法3. LARSCH $O(N)$ 時間

解法2をさらに工夫することにより，**LARSCH アルゴリズム** という $O(N)$ 時間のアルゴリズムが得られます．LARSCH アルゴリズムの実装は少々複雑ですが，シンプルな $O(N\log N)$ 時間の実装が noshi91 さんにより以下の記事で提案されています．時間計算量は悪化しますが，定数倍が軽いため， writer の実装では $O(N)$ 時間の LARSCH よりも高速でした．

* noshi91 さんによる記事: [簡易版 LARSCH Algorithm](https://noshi91.hatenablog.com/entry/2023/02/18/005856)

#### 解法4. convex hull trick $O(N\log N)$ 時間

Totally monotone 行列 $A$ の任意の2列に対して，要素の大小関係は単調になっています．すなわち，$A$ の $j$ 列目を $i$ の関数と見ると，これらの関数は互いにたかだか1回しか交わりません．

互いにたかだか1回しか交わらない関数群の最小値は，**convex hull trick**を応用することで求めることができます．Convex hull trickは本来，1次関数群の最小値を求めるアルゴリズムですが，関数群が互いにたかだか1回しか交わらないという性質を持てば，同様のアルゴリズムで処理することができます．2つの関数の交点を求めるときに二分探索を用いることで，$O(N\log N)$ 時間で $(\star \star)$ を解くことができます．

また，一次関数群の最小値を求めるデータ構造である **Li-Chao tree** も同様に，互いにたかだか1点しか交わらない関数群を扱うことができます．Li-Chao tree を利用しても $O(N\log N)$ 時間のアルゴリズムが得られます．

### 実装例

writer の実装では，2番目の実装が最も高速でした．

* [黄金分割探索 + 分割統治 + monotone minima](https://atcoder.jp/contests/abc355/submissions/53788275)
* [黄金分割探索 + 簡易版 LARSCH](https://atcoder.jp/contests/abc355/submissions/53788299)
* [黄金分割探索 + convex hull trick](https://atcoder.jp/contests/abc355/submissions/53788285)

</details><br>

Let $S := \sum_{i=1}^N P_i$.

### Graph Representation and DP Formulation

We can represent this problem as a graph problem. In a graph with $N+2$ vertices labeled $0, 1, \ldots, N+1$, we add directed edges as follows:

* For edge $(0, j)$ where $1 \le j \le N$, the weight is $\sum_{y=1}^{j-1} P_y \times (j-y)$.
* For edge $(i, j)$ where $1 \le i < j \le N$, the weight is $\sum_{y=i}^{j-1} P_y \times \min(y-i, j-y)$.
* For edge $(i, N+1)$ where $1 \le i \le N$, the weight is $\sum_{y=i}^N P_y \times (y-i)$.

When Takahashi chooses $x_1, x_2, \ldots, x_K$, the expected score that Aoki obtains, multiplied by $S$, corresponds to the weight of the path $0 \to x_1 \to \ldots \to x_K \to N+1$ with $K+1$ edges. Thus, finding the minimum expected score for Aoki reduces to finding the shortest path from vertex 0 to vertex $N+1$ using exactly $K+1$ edges in this graph.

Since the graph is a Directed Acyclic Graph (DAG), we can solve this problem using Dynamic Programming (DP). Let $dp[k][j]$ represent the shortest path length from vertex 0 to vertex $j$ using $k$ edges. The desired answer is $dp[K+1][N+1]$. The transitions are given by:

$$
dp[k][j] = \min_{i<j} \{dp[k-1][i] + c(i, j)\} \quad \ (\star)
$$

where $c(i, j)$ is the weight of edge $(i, j)$. By precomputing the cumulative sums of $P_y$ and $P_y \times y$, $c(i, j)$ can be computed in $O(1)$ time per query.

However, a straightforward implementation of this DP takes $O(N^2K)$ time, which is too slow.

### Monge Property and Speeding Up Using Alien DP

The DP expressed in equation $(\star)$ can be computed more efficiently if the transition cost $c(i, j)$ satisfies the **Monge property**. The Monge property states that for all $i, j, k, l$ such that $0 \le i < j < k < l \le N + 1$, the following inequality holds:

$$
c(i, l) + c(j, k) \ge c(i, k) + c(j, l) 
$$

In this problem, the Monge property can be understood intuitively by considering the cost $c(i, j)$ as corresponding roughly to the area of a triangular region connecting $x$ and $y$.

![](https://img.atcoder.jp/abc355/3ccf746e9e2be2a73d06c90e03f79ceb.png)

Next, we use the Alien DP approach. For details on the algorithm's correctness, refer to the following resource:

* Article by noshi91: [Algorithm for calculating the shortest path with $d$ edges on a Monge graph](https://noshi91.github.io/algorithm-encyclopedia/d-edge-shortest-path-monge)

Define a function $f(\lambda)$ as follows:

* Add $\lambda$ uniformly to the cost $c(i, j)$, then find the shortest path from vertex 0 to vertex $N+1$ without the constraint on the number of edges used. Let $d$ be the shortest path length. Define $f(\lambda) := d - \lambda(K+1)$.

The answer to the problem is $\max_{\lambda \in \mathbb{Z}} f(\lambda)$. The value $\lambda$ acts as a penalty for using an edge. The algorithm seeks the penalty $\lambda$ such that exactly $K+1$ edges are used.

The function $f(\lambda)$ is concave, and the optimal $\lambda$ lies in the range $0 \le \lambda \le 3 \max_{i, j} c(i, j) \le 3NS$. The maximum of $f(\lambda)$ can be found using methods like binary search, ternary search, or golden-section search, requiring $O(\log(NS))$ evaluations of $f(\lambda)$.

To efficiently compute $f(\lambda)$ for a given $\lambda$, we use DP again. The transitions are:

$$
dp[j] = \min_{i<j} \{dp[i] + c(i, j) + \lambda\} \quad (\star\star) 
$$

This DP has one fewer dimension, but a straightforward implementation still takes $O(N^2 \log(NS))$ time, which is impractical. However, it is known that the DP in equation $(\star\star)$ can be sped up when $c(i, j)$ is Monge.

### Fast Algorithms for Shortest Path with Monge Weights

Several methods can speed up the DP in equation $(\star\star)$:

* **Divide and Conquer + Monotone Minima $O(N (\log N)^2)$**

  Define a $(N+2) \times (N+2)$ matrix $A$ with $A_{ij} = dp[j] + c(i, j) + \lambda$. The DP in equation $(\star\star)$ becomes a problem of finding the minimum in each row of $A$. When $c(i, j)$ is Monge, matrix $A$ is totally monotone. The **Monotone Minima** algorithm finds the minimum of each row in $O(N \log N)$ time.

  However, because $A$'s elements depend on previous DP values, we cannot directly apply Monotone Minima. Instead, use a divide and conquer approach: recursively solve $solve(l, m)$ for $dp[l]$ to $dp[m-1]$, use Monotone Minima to handle transitions from $dp[l]$ to $dp[m-1]$ to $dp[m]$ to $dp[r-1]$, and then solve $solve(m, r)$ recursively.

  This approach yields $O(N (\log N)^2)$ time complexity. Overall, it takes $O(N (\log N)^2 \log(NS))$ time, which is feasible with a fast enough language.

* **Divide and Conquer + SMAWK $O(N \log N)$**

  Replace Monotone Minima with the **SMAWK algorithm**, which finds the minimum of each row in a totally monotone matrix in $O(N)$ time. Though SMAWK has a higher constant factor, under certain constraints, it performs similarly to Monotone Minima.

* **LARSCH $O(N)$**

  By refining the approach in divide and conquer with SMAWK, we get the **LARSCH algorithm** with $O(N)$ time complexity. This method, though complex, can be optimized to run faster in practice. A simpler $O(N \log N)$ version by noshi91 can be found here: [Simplified LARSCH Algorithm](https://noshi91.hatenablog.com/entry/2023/02/18/005856).

* **Convex Hull Trick $O(N \log N)$**

  Since any two functions in the totally monotone matrix cross at most once, we can use the **convex hull trick** to find the minimum in $O(N \log N)$ time. The **Li-Chao tree**, a data structure for finding the minimum of linear functions, also works here.

### Implementation Examples

In the writer's implementation, the second approach was the fastest:

* [Golden-section search + Divide and Conquer + Monotone Minima](https://atcoder.jp/contests/abc355/submissions/53788275)
* [Golden-section search + Simplified LARSCH](https://atcoder.jp/contests/abc355/submissions/53788299)
* [Golden-section search + Convex Hull Trick](https://atcoder.jp/contests/abc355/submissions/53788285)

<!-- 
$$
\rho, \sigma, \Sigma, \tau, \theta, \Theta, \upsilon, \Upsilon, \varDelta, \varepsilon, \varGamma \\
\varLambda, \varOmega, \varphi, \varPhi, \varpi, \varPi, \xi, \zeta \\
\Lambda, \lambda, \mu, \omega, \Omega, \phi, \Phi, \pi, \Pi, \psi, \Psi
$$ 
-->
