## [G - Many LCS](https://atcoder.jp/contests/abc391/tasks/abc391_g)


$T,S$ の最長共通部分列 (LCS) の長さを求める方法を軽く振り返っておきます．

> $(|T| + 1)\times (|S| + 1)$ の配列 dp を用意し，$dp[i][j]$ を $T[:i]$ と $S[:j]$ の LCS の長さとする．dp の遷移は以下の $3$ つである．
>
> 1. $dp[i][j] \gets dp[i−1][j]$
> 2. $dp[i][j] \gets dp[i][j−1]$
> 3. もし $T[i]=S[j]$ なら $dp[i][j] \gets dp[i−1][j−1]+1$

この遷移を観察すると，dp 配列には以下の性質が成り立つことが分かります．

* $dp[i][0] = 0$
* $0 \le dp[i][j+1]− dp[i][j] \le 1$

すなわち， $dp[i]$ は広義単調増加列であり，隣接する項の差は高々 $1$ です．よって，$dp[i]$ としてあり得る状態は高々 $2^{|S|}$ 通りしかないことが分かります．

この性質を利用して元の問題を解きます．$DP[i][dp\_array]$ を「長さ $i$ の文字列 $T$ であって，$T$ と $S$ の LCS を求めるときの dp 配列における $dp[i]$ が $dp\_array$ であるようなものの個数」とします．$i$ を増やしたときの $dp\_array$ の遷移先については，上で述べた LCS の dp の遷移にしたがって求めればよいです．$DP[i]$ の状態数が $O(2^N)$ であり，$dp\_array$ の遷移の計算に $O(\sigma N)$ かかるため，計算量は $O(NM\sigma 2^N)$ になります．（$\sigma$ は文字の種類数です．）また，あらかじめ遷移を前計算しておくことで計算量を $O(NM2^N)$ に減らすことも可能です．

```cpp
from collections import defaultdict

mod = 998244353

N, M = map(int, input().split())
A = [ord(i) - ord("a") for i in input()]
K = 26
dp = defaultdict(int)
dp[tuple([0] * (N + 1))] = 1
for _ in range(M):
    ndp = defaultdict(int)
    for arr, c in dp.items():
        for i in range(K):
            narr = [0] * (N + 1)
            for j in range(N):
                narr[j + 1] = max(narr[j], arr[j + 1])
                if A[j] == i:
                    narr[j + 1] = max(narr[j + 1], arr[j] + 1)
            ndp[tuple(narr)] = (ndp[tuple(narr)] + c) % mod
    dp = ndp
ans = [0] * (N + 1)
for arr, c in dp.items():
    ans[arr[N]] += c
print(*[i % mod for i in ans])

```

---


Let's briefly review how to determine the length of the longest common subsequence (LCS) of $T$ and $S$.

> Prepare a $(|T| + 1) \times (|S| + 1)$ array $dp$, where $dp[i][j]$ represents the length of the LCS of $T[:i]$ and $S[:j]$. The transitions for $dp$ are as follows:
>
> 1. $dp[i][j] \gets dp[i-1][j]$
> 2. $dp[i][j] \gets dp[i][j-1]$
> 3. If $T[i] = S[j]$, then $dp[i][j] \gets dp[i-1][j-1] + 1$

By observing these transitions, we can see that the $dp$ array satisfies the following properties:

- $dp[i][0] = 0$
- $0 \leq dp[i][j+1] - dp[i][j] \leq 1$

In other words, $dp[i]$ is a non-decreasing sequence, where the difference between adjacent elements is at most 1. Therefore, the number of possible states for $dp[i]$ is at most $2^{|S|}$.

Using this property, we solve the original problem. Define $DP[i][dp\_array]$ as "the number of strings $T$ of length $i$ such that the $dp$ array when computing the LCS of $T$ and $S$ is $dp\_array$." The possible transitions of $dp\_array$ when increasing $i$ can be determined based on the LCS $dp$ transitions mentioned above. 

Since the number of states of $DP[i]$ is $O(2^N)$, and computing the transitions of $dp\_array$ requires $O(\sigma N)$, the overall time complexity is $O(NM\sigma 2^N)$ (where $\sigma$ is the number of distinct characters). Additionally, by precomputing the transitions in advance, the complexity can be reduced to $O(NM2^N)$.
