## [G - Specified Range Sums](https://atcoder.jp/contests/abc404/tasks/abc404_g)

唐突ですが、 $\displaystyle \sum_{j = l}^r A_j = S_i$ という制約は扱いづらいため、 $\displaystyle B(k) = \sum_{i = 1}^k A_i$ と置き換えましょう。
すると、 $\displaystyle\sum_{j=l}^r A_j = S_i$ という制約は $B_r−B_{l−1}=S$ という形に置き換わります。

ここで、改めて数列に課されている制約を $B$ を使って整理します。

> * $B_{R_i} − B_{L_i} − 1 = S_i (1\le i \le M)$
> * $B_j−B_{j−1} \ge 1 (1\le j \le N)$

この制約を更に加工し、等号を不等号にします。

> * $B_{R_i} − B_{L_i−1}\ge S_i (1\le i \le M)$
> * $B_{R_i} − B_{L_i−1} \le S_i (1\le i\le M)$
> * $B_j − B_{j−1} \ge 1 (1\le j\le N) $

さて、解くべき問題は、次の線形計画問題として表現されます。

$$
\begin{align*}
\text{minimize}\quad & B_N \\
\text{subject to}\quad & B_{R_i} − B_{L_i−1} \ge S_i (1\le i \le M) \\
& B_{R_i} − B_{L_i−1} \le S_i (1\le i \le M) \\
& B_j−B_{j−1} \ge 1 (1\le j \le N) \\
\end{align*}
$$

ここで、全ての制約式が $B_i+c \ge B_j$ の形で表現されることに注目します。これは特別な解きやすい形の線形計画問題で、 **牛ゲー** と呼ばれます。[解説1](https://tjkendev.github.io/procon-library/python/graph/difference-constraints-ushi.html) [解説2](https://ei1333.github.io/luzhiled/snippets/memo/ushi-game.html) [解説3](https://qiita.com/horiso/items/ca818df8ddbc5be58ec1) [解説4](https://zenn.dev/masutech/articles/compro-cowgame-theory) [解説5](https://qiita.com/tanabe13f/items/6c723c29a121de760790)
( これが 牛ゲー と呼ばれている理由は、このテクニックが浸透するに至った問題が「牛を並べる問題」であったからです。 [移植1](http://poj.org/problem?id=3169) [移植2](https://www.acmicpc.net/problem/7040) )

牛ゲーそのものの目的関数は「特定の変数の最大化」ですが、線形計画問題を以下のように設定すれば問題ありません。
この問題の答えは以下の線形計画問題の最適解の目的関数の $−1$ 倍となります。
$$
\begin{align*}
\text{maximize}\quad & B_0 \\
\text{subject to}\quad & B_{R_i} − B_{L_i−1} \ge S_i (1\le i \le M) \\
& B_{R_i} − B_{L_i−1} \le S_i (1\le i \le M) \\
& B_j−B_{j−1} \ge 1 (1\le j \le N) \\
& B_N = 0 
\end{align*}
$$

あとは、この問題の形に従い適切なグラフを構築して Bellman-Ford 法で最短経路問題を解くと、この問題に正解できます。

---

It may seem sudden, but the constraint $\displaystyle\sum_{j = l}^r A_j = S_i$ is a bit awkward to work with, so let us define $\displaystyleB(k) = \sum_{i = 1}^k A_i$.

Then $\displaystyle\sum_{j = l}^r A_j = S_i$ is equivalent to $B_r - B_{l-1} = S_i.$

---

## Rewriting the constraints in terms of $B$

Originally the sequence $\{A_j\}$ is subject to the constraints

> * $\displaystyle\sum_{j = L_i}^{R_i} A_j = S_i$ for $1 \le i \le M$,
> * $A_j \ge 1$ for $1 \le j \le N$.

In terms of $B$, these become

> * $B_{R_i} - B_{L_i-1} = S_i$ \quad $(1 \le i \le M)$
> * $B_j - B_{j-1} \ge 1$ \quad $(1 \le j \le N)$.

We can split each equality into a pair of inequalities:

> * $B_{R_i} - B_{L_i-1} \ge S_i$ \quad $(1 \le i \le M)$
> * $B_{R_i} - B_{L_i-1} \le S_i$ \quad $(1 \le i \le M)$
> * $B_j - B_{j-1} \ge 1$ \quad $(1 \le j \le N)$.

---

## Formulating as a special LP (“Cow Game”)

The problem we now want to solve is the following linear program:

$$
\begin{aligned}
\text{minimize}\quad   & B_N,\\
\text{subject to}\quad & B_{R_i} - B_{L_i-1} \ge S_i && (1\le i \le M),\\
                      & B_{R_i} - B_{L_i-1} \le S_i && (1\le i \le M),\\
                      & B_j - B_{j-1} \ge 1       && (1\le j \le N).
\end{aligned}
$$

Notice that **every** constraint is of the form

$$
B_i + c \;\ge\; B_j,
$$

which is a classic “difference‐constraints” system often called the **Cow Game**.
The name comes from the first widely–circulated problem using this trick, which was about arranging cows (see “port” problems on POJ 3169 and BOJ 7040).

For more on the Cow Game technique, see these write‑ups:

* [解説1](https://tjkendev.github.io/procon-library/python/graph/difference-constraints-ushi.html)
* [解説2](https://ei1333.github.io/luzhiled/snippets/memo/ushi-game.html)
* [解説3](https://qiita.com/horiso/items/ca818df8ddbc5be58ec1)
* [解説4](https://zenn.dev/masutech/articles/compro-cowgame-theory)
* [解説5](https://qiita.com/tanabe13f/items/6c723c29a121de760790)

---

## Adjusting the objective to match the Cow Game framework

The standard Cow Game LP asks you to **maximize** a certain variable.  We can easily adapt our formulation by fixing $B_N = 0$ and instead maximizing $B_0$.  In fact, the maximum value of $B_0$ in

$$
\begin{aligned}
\text{maximize}\quad   & B_0,\\
\text{subject to}\quad & B_{R_i} - B_{L_i-1} \ge S_i && (1\le i \le M),\\
                      & B_{R_i} - B_{L_i-1} \le S_i && (1\le i \le M),\\
                      & B_j - B_{j-1} \ge 1       && (1\le j \le N),\\
                      & B_N = 0,
\end{aligned}
$$

is exactly $-$ (the minimum value of $B_N$ in our original problem).  Hence, solving this and taking the negative of the optimal objective gives the answer.

---

## Implementation sketch

1. **Build a directed graph** whose nodes are $0,1,2,\dots,N$.
2. **Add edges** encoding each constraint $B_u - B_v \ge c$ as an edge $v \to u$ with weight $c$.
3. **Run Bellman–Ford** (or any shortest‐path algorithm that handles negative weights) from node $N$ (where we fix $B_N=0$).
4. The computed distances $d[i]$ satisfy $d[i] = B_i$; the answer to the original problem is $-\,d[0]$.
