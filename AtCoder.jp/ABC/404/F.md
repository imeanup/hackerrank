## [F - Lost and Pound](https://atcoder.jp/contests/abc404/tasks/abc404_f)

以下、手順 1,2,3 を 1 回行う一連の流れを 1 ターンと表現します。

$DP[t][k]$ を「$t$ ターン目が終わった時点で当たりのボタンが $k$ 回押された状態からゲームを続け、最適な行動をしたときの勝率」と定め、$t$ の降順に求めます。

$DP[t+1][∗]$ から $DP[t][k]$ を求める方法を考えます。$t+1$ ターン目に各 $i = 1, \dots,N$ についてボタン $i$ を $c_i$ 回押すとき、どのボタンがあたりであるかはそれぞれ $\dfrac{1}{N}$ なので、勝率は $\dfrac{1}{N} \displaystyle \sum_{i=1}^N DP[t+1][k+c_i]$ となります。よって、どのボタンを何回押すかを全て考慮することで以下の漸化式を得ます。

$$DP[t][k] = \max_{⁡c_1 + \dots + c_N = M} \dfrac{1}{N} \sum_{i=1}^N DP[t+1][k+c_i]$$

これを高速に求めることを考えます。$t,k$ を固定し、

$$DP_{t,k}'[n][s] = \max_{⁡c_1 + \dots + c_n = s} \sum_{i=1}^n DP[t+1][k+c_i]$$

と定めると定義より $DP[t][k]=\dfrac{1}{N} DP_{t,k}'[N][M]$ です。$DP_{t,k}'[N][M]$ を求めるにあたって、$c$ の順序は影響しないことから、$(c_i = 0 \wedge i \le i') \Rightarrow c_i' = 0$ すなわち「$c_i = 0$ であるような $i$ は全て後ろに固まっている」というような $c$ のみを考慮するとしてよいです。これを踏まえ、$c$ に $0$ でない要素がいくつあるかを考えることで、

$$DP_{t,k}^{′′}[n][s] = \max_{⁡c_1 + \dots + c_n = s \\ c_i > 0} \sum_{i=1}^n DP[t+1][k+c_i]$$

と定めると、$DP_{t,k}'[N][M] = \max_{⁡1\le n\le \min⁡(M,N)} (DP_{t,k}^{′′}[n][M]+(N−n)DP[t+1][k])$ を得、$1\le n \le \min⁡(M,N)$ の範囲で $DP′′[n][M]$ が 求まれば $DP_{t,k}'[N][M]$ を求めることができます。$DP^{′′}$ を求める $DP$ は状態数 $O(M^2)$、遷移 $O(M)$ であることから $O(M^3)$ 時間で行えます。

以上を全ての $t,k$ に対して行うことで、$O(TKM^3)$ でこの問題を解くことができました。

---


Below, we call one complete execution of steps 1, 2, and 3 a single **turn**.

Define $DP[t][k]$ to be “the probability of winning if, at the end of turn $t$, you have already pressed the ‘winning’ button $k$ times, and from that state you play optimally thereafter.”  We compute these values in decreasing order of $t$.

---

### Recurrence from $DP[t+1]$ to $DP[t]$

Suppose on turn $t+1$ you press button $i$ exactly $c_i$ times (for $i=1,\dots,N$).  Since each button is equally likely to be the winning one (probability $1/N$), your resulting win probability is

$$\frac1N \sum_{i=1}^N DP[t+1][\,k + c_i\,].$$

Therefore, if you must allocate a total of $M$ presses among the $N$ buttons, you obtain the recurrence

$$DP[t][k] = \max_{\;c_1 + \cdots + c_N = M\;} \;\frac1N\sum_{i=1}^N DP[t+1][\,k + c_i\,].$$

---

### Efficient Computation via Nested DP

Fix $t$ and $k$.  To speed up the maximization over all $(c_1,\dots,c_N)$ summing to $M$, introduce an auxiliary DP:

$$DP'_{t,k}[n][s] = \max_{\;c_1 + \cdots + c_n = s\;} \sum_{i=1}^n DP[t+1][\,k + c_i\,].$$

By definition,

$$DP[t][k] = \frac1N \,DP'_{t,k}[N][M].$$

Observe that the order of the $c_i$ doesn’t matter; we may assume all the zeroes are “pushed to the back.”  Let

$$DP''_{t,k}[n][s] = \max_{\substack{c_1 + \cdots + c_n = s\\c_i>0}} \sum_{i=1}^n DP[t+1][\,k + c_i\,],$$

i.e.\ the best sum when exactly $n$ of the $c_i$ are positive and sum to $s$.  Then one shows

$$DP'_{t,k}[N][M] = \max_{1 \le n \le \min(M,N)} \Bigl( DP''_{t,k}[n][M] \;+\; (N-n)\,DP[t+1][k] \Bigr).$$

Thus once we can compute $DP''_{t,k}[n][M]$ for all $1\le n\le\min(M,N)$, we recover $DP'_{t,k}[N][M]$ in $O(N)$ time.

---

### Complexity and Final Result

Computing the table $DP''_{t,k}[\,\cdot\,][\,\cdot\,]$ itself is a DP over two dimensions of size up to $M$, with an $O(M)$ inner transition—overall $O(M^3)$ per $(t,k)$.  Since there are $O(TK)$ distinct $(t,k)$ states, the total time is $O\bigl(T \times K \times M^3\bigr),$ which suffices to solve the problem.
