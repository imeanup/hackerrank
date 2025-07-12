## [F - Jump Traveling](https://atcoder.jp/contests/abc414/tasks/abc414_f)


一回の移動を $K$ 歩とみなすことにします．次のような dp を考えます．

dp[(u, v)][k]：頂点 $u$ から $v$ へ，一回の移動の中の $k$ 歩目で移る場合を考えたとき，これが起きうるような頂点 $v$ までの歩数の最小値

頂点 $1$ に隣接する頂点 $v$ に対して，$dp[(1, v)][1] = 1$ と初期化できます．（あるいは仮想の頂点 $X$ を作って $dp[(X, 1)][K] = 0$ としても良いです．）dp の遷移は次のようになります．

* $k \ne K$ のとき： 頂点 $v$ に隣接する頂点 $w$（ただし $w \ne u$）ついて，$dp[(v, w)][k+1] \gets dp[(u, v)][k] + 1$
* $k = K$ のとき： 頂点 $v$ に隣接する頂点 $w$ について，$dp[(v, w)][1] \gets dp[(u, v)][k] + 1$

これは BFS で計算することができますが，このままでは TLE してしまいます．なぜなら，ある $v$ に対して $dp[(v, w)][k+1] \gets dp[(u, v)][k] + 1$ という遷移が起きる回数を考えると，$v$ の次数を $d$ としたときに， $u$,$w$ がそれぞれ $d$ 通り，$k$ が $k$ 通りあるため，最悪で $O(N^2K)$ 回になってしまうからです．

ここで重要な考察として，ある頂点 $v$ に対して，$dp[(v, w)][k+1] \gets dp[(u, v)][k] + 1$ という遷移は $2$ つの $u$ に対してのみ行えば十分です．言い換えると，頂点 $v$ に $(k+1)$ 歩目で踏み入れるのは $2$ 回まで考慮すればそれで十分です．

その理由を次の図で説明します．

![](https://img.atcoder.jp/abc414/017489a049e850d996064cba9adfb777.png)

1. 初めて $v$ に $a$ から訪れたとき，$v\to b, v\to c, v\to d$ の遷移が起きます．
2. 次に $v$ に $b$ から訪れたとき，更新される可能性があるのは $v \to a$ のみです．$v\to c$ や $v\to d$ は $1$ 回目に $a$ から訪れたときにすでに遷移が起きています．
3. $v$ に $3$ 回目以降訪れたとき，$1$ 回目と $2$ 回目ですべて遷移は網羅しているため，新しい遷移は起きません．

よって，$v$ に $k$ 歩目に踏み入れたのが何回か？を持っておき， $3$ 回目以降の処理をスキップすることで，計算量は $O(Nk)$ になります．

実装についてですが，各辺について双方向の有向辺があるとみなし，元のグラフで $i$ 番目（0-indexed）の辺に対応する有向辺を $2i, 2i+1$ と番号付けると連想配列等を使わずに実装できます．

```py
from collections import deque


def solve():
    N, K = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(N - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        G[u].append((v, 2 * i))
        G[v].append((u, 2 * i + 1))

    dp = [[-1] * (2 * N - 2) for i in range(K)]
    ans = [-1] * N
    cnt = [[0] * N for i in range(K)]
    dq = deque([(0, 0, -1)]) # (総歩数，頂点番号，有向辺の番号)
    while dq:
        d, v, e = dq.popleft()
        if d % K == 0 and ans[v] == -1:
            ans[v] = d // K
        if cnt[d % K][v] == 2:
            continue
        cnt[d % K][v] += 1
        for u, e2 in G[v]:
            if e ^ e2 == 1 and d % K != 0:
                continue
            if dp[(d + 1) % K][e2] == -1:
                dp[(d + 1) % K][e2] = d + 1
                dq.append((d + 1, u, e2))

    print(*ans[1:])


for _ in range(int(input())):
    solve()

```



---

We regard a single “move” as consisting of $K$ steps.  Consider the following DP:

$$
\text{dp}[(u, v)][k] = \text{the minimum total number of steps needed to reach vertex }v,\text{ in the situation where you move from }u\text{ to }v\text{ on the \(k\)th step of a move.}
$$

You can initialize for every vertex $v$ adjacent to $1$:

$$
\text{dp}[(1, v)][1] = 1.
$$

(Alternatively, you could introduce a virtual vertex $X$ and set $\text{dp}[(X,1)][K] = 0$.)

The transitions of this DP are:

* **If** $k \neq K$:
  For each neighbor $w$ of $v$ (with $w \neq u$),

  $$
    \text{dp}[(v, w)][k+1] \;\Longleftarrow\; \text{dp}[(u, v)][k] + 1.
  $$

* **If** $k = K$:
  For each neighbor $w$ of $v$,

  $$
    \text{dp}[(v, w)][1] \;\Longleftarrow\; \text{dp}[(u, v)][k] + 1.
  $$

You could compute this by BFS, but as stated it will TLE.  The reason is that for a given vertex $v$ of degree $d$, there are $d$ possibilities for $u$, $d$ for $w$, and $K$ for $k$, giving up to $O(N^2 K)$ transitions in the worst case.

---

### Key Observation

For each vertex $v$, it suffices to perform the transition

$$
  \text{dp}[(v, w)][k+1] \;\Longleftarrow\; \text{dp}[(u, v)][k] + 1
$$

for **at most two distinct** predecessors $u$.  Equivalently, it’s enough to consider at most two visits when entering $v$ on the $(k+1)$th step.

The intuition is illustrated below:

1. **First time** you visit $v$ coming from $a$, you trigger transitions $v\to b$, $v\to c$, and $v\to d$.
2. **Second time** you visit $v$ coming from $b$, the only new transition that might update is $v\to a$.  The edges $v\to c$ and $v\to d$ were already processed during the first visit.
3. **Third and subsequent visits** to $v$ add no new transitions, because all neighbor-to-neighbor moves have already been covered in the first two visits.

Hence, if you keep track of how many times you’ve entered each $v$ at a given step mod $K$, and skip processing upon the third and later entries, the overall complexity falls to $O(NK)$.

---

### Implementation Details

Treat each undirected edge as two directed edges.  If the $i$­‑th (0­‑indexed) undirected edge in the original graph corresponds to directed edges numbered $2i$ and $2i+1$, you can avoid using associative arrays.  Here is one possible Python implementation:

```py
from collections import deque

def solve():
    N, K = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        # label the two directions of edge i as 2*i and 2*i+1
        G[u].append((v, 2*i))
        G[v].append((u, 2*i + 1))

    # dp[step_mod_K][directed_edge_id] = minimum total steps (or -1 if unseen)
    dp = [[-1] * (2 * (N - 1)) for _ in range(K)]
    ans = [-1] * N
    # cnt[step_mod_K][vertex] = number of times vertex visited at this step_mod_K
    cnt = [[0] * N for _ in range(K)]
    dq = deque([(0, 0, -1)])  # (total_steps, current_vertex, incoming_directed_edge)

    while dq:
        d, v, e = dq.popleft()
        # Whenever d % K == 0 and ans[v] is unset, record the number of moves
        if d % K == 0 and ans[v] == -1:
            ans[v] = d // K
        # Skip further processing if we've already visited v twice at this step_mod_K
        if cnt[d % K][v] == 2:
            continue
        cnt[d % K][v] += 1

        for u, e2 in G[v]:
            # Prevent immediately reversing a step unless you're at a move boundary
            if (e ^ e2) == 1 and d % K != 0:
                continue
            if dp[(d + 1) % K][e2] == -1:
                dp[(d + 1) % K][e2] = d + 1
                dq.append((d + 1, u, e2))

    # Output the answer for vertices 2..N
    print(*ans[1:])

for _ in range(int(input())):
    solve()
```
