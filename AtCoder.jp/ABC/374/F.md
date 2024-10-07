## [F - Shipping](https://atcoder.jp/contests/abc374/tasks/abc374_f)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese</b></summary><br>

$T_N \le 10 ^{12}$ である (暦に存在する日数が非常に大きい) ので、「今何日か?」を愚直に管理する解法ではこの問題に正解することができなさそうです。

そこで、着目する日の数を減らしてみましょう。

実は、出荷を行うタイミングとして考えるべきものは以下の式で記述できるものだけです。

* $T_i + k X$
  * 但し、 $1 \le i \le N, 0 \le k \le N$

略証:
注文 $i,j (i < j)$ について、 $j$ を $i$ より先に出荷しても不満度が減少することはない (注文の順番に出荷する最適解が常に存在する) 。
このとき、同時に出荷する注文の集合を固定した時、起こることは以下の $2$ つのうち $1$ つである。

* 同時に出荷する注文のうち最も遅いものを待って出荷する。
* 前の出荷の $X$ 日後の時点で出荷したい注文が全て揃っているので、その日に直ちに出荷する。

前者はある $i$ を用いて $T_i$ 日、後者は前の出荷の $X$ 日後と表現されるため、最初の結論を得る。

これで、着目する日の個数が $O(N^2)$ 個になりました。

このもとで、この問題は以下の動的計画法により解くことができます。

着目する日をイベント $1,2, \cdots$ と呼ぶことにします。

$dp$ [ イベント $i$ ][ 最後に出荷した注文 $j$ ] = { 現時点で出荷された注文に対する不満度の総和の最小値 $x$ }

遷移は次の通りです。

* $dp[i+1][j]$ に $x$ を遷移する ( イベント $i$ の日に何も出荷しない )
* イベント $i$ から $X$ 日以降経過した最初のイベントを $d$ とする。このとき、 $dp[d][j+m]$ に $x$ + ( イベント $i$ の日に $j+1$ 個目から $j+m$ 個目までの注文を出荷した場合の不満度の総和 ) を遷移する。

この動的計画法は、時間計算量 $O(N^3K)$ で動作します。 実行時間制限が余裕をもって設定されているため、もうひとつ計算量にかかる文字が多い解法でも定数倍が十分高速であれば正解できる可能性があります。

</details><br>

Since $T_N \leq 10^{12}$ (the number of days in the calendar is extremely large), a straightforward solution that directly tracks "what day it is now" will likely not lead to a correct answer for this problem.

Therefore, let's try to reduce the number of days to focus on.

In fact, the only timings for shipping that need to be considered can be described by the following formula:

- $T_i + k \cdot X$
  - where $1 \leq i \leq N, 0 \leq k \leq N$

Brief proof:
For orders $i, j$ (with $i < j$), shipping $j$ before $i$ will not reduce the dissatisfaction (an optimal solution always exists where orders are shipped in the order they were placed).
In this case, when fixing the set of orders to be shipped simultaneously, one of the following two situations will occur:

- Wait for the latest order among the ones being shipped together to ship them all at once.
- If all the orders that should be shipped are ready exactly $X$ days after the previous shipment, then ship them immediately on that day.

The former case can be represented as $T_i$ days using some $i$, and the latter as shipping exactly $X$ days after the previous shipment, leading to the conclusion given above.

Thus, the number of days to focus on has been reduced to $O(N^2)$.

Now, the problem can be solved using the following dynamic programming approach.

Let's call the focused days "events" $1, 2, \cdots$.

Define:

$$
dp[\text{event } i][\text{last shipped order } j] = \{\text{minimum total dissatisfaction up to the current shipped orders}\}
$$

The transitions are as follows:

- Transition to $dp[i+1][j]$ with $x$ (i.e., no orders are shipped on event $i$).
- Let $d$ be the first event that occurs at least $X$ days after event $i$. Then, transition to $dp[d][j+m]$ with $x +$ (the total dissatisfaction if orders $j+1$ through $j+m$ are shipped on event $i$).

This dynamic programming solution runs in $O(N^3K)$ time. Since the time limit is set with some leeway, even an approach with a high constant factor in its time complexity may still be able to solve the problem correctly if it runs efficiently enough.

<details style="border: 1px solid black; padding: 10px;"><summary><b>Suisen</b></summary><br>

$O(N^2)$ **時間解法**

---

不満度の総和は $(\sum_i S_i)−(\sum_i T_i)$ です。第二項は定数なので、第一項を最小化します。以降、$S_i$ をコストと呼びます。

以下の $dp$ テーブルを $i$ の降順に埋めていきます。

$$
dp(i) := 時刻 T_i に出荷して注文 iまでを処理した状態から、\\ 注文 i+1 以降を処理するコスト和の最小値.
$$

$dp(i)$ の計算を考えます。いま、時刻 $T_i$ に出荷して注文 $i$ までを処理した状態とします。この後の出荷時刻は $T_i + X, T_i+ 2X, \dots ,T_i+kX, T_j, \dots$ のような形になっているとしてよいです。更に、時刻 $T_j$ における出荷で注文 $j$ までを処理した状態となるように $j$ を取ることが出来ます (ただし、$T_{N + 1} = \infty$ (十分大きな数) として $j = N+1$ も許すことにします)。

時刻 $T_i + X,T_i + 2X,\dots $ における操作において、可能な限り多くの注文を処理することにします。このシミュレーションにおいて、時刻 $T_i + pX$ において処理できる注文の個数を $n$ とします。また、時刻 $T_i + (p−1)X$ までの出荷で処理した最大の注文を $l$ とします。

次の出荷は、以下のいずれかのタイミングです。

1. 時刻 $T_i + pX$ に出荷する
2. $l + n \le j \le l+K$ なる $j$ を選んで時刻 $T_j$ に (注文 $j$ までを) 出荷する

1 の場合はそのままシミュレーションを継続することで考慮できます。ただし、 $n = 0$ の場合は出荷の意味が無いので 2 の場合だけ考慮してシミュレーションを終了してよいです。

2 の場合は、時刻 $T_i + (p−1)X$ までのシミュレーションで計算されたコスト和を $C$ として $dp(i)\gets \min \{dp(i), C+ \min_{⁡l + n < j\le l + K}(T_j\cdot (j−l) + dp(j))\}$ と更新することで考慮できます。

以上で $O(N^2 K)$ 時間の解法が得られましたが、更に高速化できます。

ボトルネックは $\min_{⁡l + n < j \le l+K} (T_j\cdot (j − l) + dp(j))$ の計算です。これは $l,n$ にしか依存していないことに注目して $f(l, n) ≔ \min_{⁡l+n<j\le l+K} (T_j \cdot (j−l)+dp(j))$ と定めます。$f$ について、次の漸化式が成り立ちます。

$$
f(l,n) = \min ⁡\{ T_{l+n+1} \cdot (n+1) + dp(l+n+1),f(l,n+1)\}
$$

この漸化式を利用すれば各 $f(l,n)$ は全体で $O(N^2)$ 時間で計算できます。

以上で $O(N^2)$ 時間の解法が得られました。

### 計算量についての補足

シミュレーションのループが回る回数が $O(N)$ であることは非自明ですが、これは $n = 0$ の場合にシミュレーションを終了していることが本質的です。より詳細に言えば、$n > 0$ の場合に $l$ が必ず $1$ 以上増えますが、一方で $l$ は高々 $N$ であることから、ループの回数は高々 $N$ 回であることが分かります。

[実装例](https://atcoder.jp/contests/abc374/submissions/58494784)

</details><br>

### $O(N^2)$ Time Solution

---

The total dissatisfaction is $(\sum_i S_i) - (\sum_i T_i)$. The second term is a constant, so we aim to minimize the first term. From now on, we will refer to $S_i$ as the cost.

We will fill in the following $dp$ table in decreasing order of $i$:

$$
dp(i) := \text{The minimum total cost of handling orders from } i+1 \text{ onward, given that the orders up to } i \text{ have been shipped at time } T_i.
$$

Let's consider how to compute $dp(i)$. Currently, we assume that orders up to $i$ have been shipped at time $T_i$. After this, the next possible shipping times are $T_i + X, T_i + 2X, \dots, T_i + kX, T_j, \dots$, and so on. Furthermore, we can select $j$ such that the orders up to $j$ are shipped at time $T_j$ (with $T_{N+1} = \infty$ as a sufficiently large number, so $j = N+1$ is also allowed).

For operations at times $T_i + X, T_i + 2X, \dots$, we aim to process as many orders as possible. In this simulation, let $n$ be the number of orders that can be processed at time $T_i + pX$, and let $l$ be the largest order processed by the previous shipment at time $T_i + (p-1)X$.

The next shipment can be made at the following times:

1. Ship at time $T_i + pX$
2. Choose some $j$ such that $l + n \leq j \leq l+K$, and ship the orders up to $j$ at time $T_j$

In case 1, we can continue the simulation as usual. However, if $n = 0$, shipping at this time is meaningless, so we can terminate the simulation and only consider case 2.

In case 2, let $C$ be the total cost calculated by the simulation up to time $T_i + (p-1)X$. Then, we update $dp(i)$ as follows:

$$
dp(i) \gets \min \{ dp(i), C + \min_{l+n < j \leq l+K} (T_j \cdot (j-l) + dp(j)) \}
$$

At this point, we have obtained an $O(N^2K)$ time solution, but it can be further optimized.

The bottleneck is the calculation of $\min_{l+n < j \leq l+K} (T_j \cdot (j-l) + dp(j))$. By observing that this depends only on $l$ and $n$, we define:

$$
f(l, n) := \min_{l+n < j \leq l+K} (T_j \cdot (j-l) + dp(j))
$$

Using this, we can derive the following recurrence relation:

$$
f(l, n) = \min \{ T_{l+n+1} \cdot (n+1) + dp(l+n+1), f(l, n+1) \}
$$

With this recurrence relation, we can compute each $f(l, n)$ in a total of $O(N^2)$ time.

Thus, we have obtained an $O(N^2)$ time solution.

### Note on the Time Complexity

It is not immediately obvious why the number of iterations in the simulation loop is $O(N)$. This is due to the fact that the simulation terminates when $n = 0$. More specifically, when $n > 0$, $l$ is guaranteed to increase by at least 1, but since $l$ can be at most $N$, the number of iterations is at most $N$.

[Example Implementation](https://atcoder.jp/contests/abc374/submissions/58494784)
