## [E - Guess the Sum](https://atcoder.jp/contests/abc355/tasks/abc355_e)

<details><summary><b>Japanese </b></summary><br>

質問できる区間がセグメント木のような区間になっている点で [ABC349-D Divide Interval](https://atcoder.jp/contests/abc349/tasks/abc349_d) と似ています．本問題との違いは引き算が行えることです．例えば $N = 3, L = 1, R = 7$ のとき，質問する区間を ABC349-D の方法で区間を分割すると $A_1, A_2 + A_3, A_4+A_5+A_6+A_7$ の $3$ 回の質問が必要になります．一方で，本問題では一回目に $A_0 + A_1 + A_2 + A_3 + A_4 + A_5 + A_6 + A_7$ を，二回目に $A_0$ を質問し，一回目の値から二回目の値を引くことで答えを求めることができます．

---

以下では，合同式の法を $100$ とします．

整数 $x, y (0 \le x, y \le 2^N)$ に対して，$S(x, y)$ を次で定めます．

$$
S(x, y) = 
\begin{cases} 
0 & \text{if } x = y \\
\sum_{i=x}^{y-1} A_i & \text{if } x < y \\
-S(y, x) & \text{if } x > y 
\end{cases}
$$

求めるものは $S(L, R+1)$，質問できるものは $S(2^i j, 2^i(j+1))$ です．また，$S(2^i(j+1), 2^ij) \equiv -S (2^i(j+1), 2^ij)$ であるため，$S(2^i(j+1), 2^ij)$ も質問できるものとみなします．$S(x, y)$ と $S(y, z)$ が分かってるとき， $S(x, z)$ は $S(x, y) + S(y, z)$ として求めることができます．

ここで，頂点が $0, 1, \dots, 2^N$ の $2^N + 1$ 頂点であり，$S(x, y)$ が質問できるような $x, y$ に対して頂点 $x$ と $y$ の間に辺を貼ってあるようなグラフ $G$ を考えます．

$G$ 上での距離が $2$ であるような頂点 $x, y$ に対して，$G$ における $x$ から $y$ までの最短経路上の頂点を $v_0(=x), v_1, v_2(=y)$ として $S(v_0, v_1)$ および $S(v_1, v_2)$ を質問することで $S(x, y)$ を $2$ 回の質問で特定することができます．

同様に．$G$ 上での距離が $3$ であるような頂点 $x, y$ に対して，$G$ における $x$ から $y$ までの最短経路上の頂点を $v_0(=x), v_1, v_2, v_3(=y)$ として $S(v_1, v_2)$ および $S(v_1, v_2)$ を質問することで $S(x, y)$ を $3$ 回の質問で特定することができます．

より一般に．$G$ 上での距離が $d$ であるような頂点 $x, y$ に対して，$S(x, y)$ を $d$ 回の質問で求めることができます．

よって，グラフ $G$ 上で $L$ から $R$ の最短経路が（復元付きで）求められれば良いです．グラフ $G$ の頂点数は $2^N+1$，辺数は $2^{N+1}-1$ であるため，BFS を用いることで計算量 $O(2^N)$ で最短経路を求めることができます．

</details><br>

---

The intervals where questions can be asked are similar to the intervals in [ABC349-D Divide Interval](https://atcoder.jp/contests/abc349/tasks/abc349_d), resembling a segment tree. The difference with this problem is that subtraction is possible. For example, when $N = 3, L = 1, R = 7$, using the method from ABC349-D to divide the intervals, you would need to ask three questions: $A_1$, $A_2 + A_3$, and $A_4 + A_5 + A_6 + A_7$. In contrast, in this problem, you can first ask for $A_0 + A_1 + A_2 + A_3 + A_4 + A_5 + A_6 + A_7$ and then ask for $A_0$ in the second question. By subtracting the value obtained in the second question from the value obtained in the first question, you can find the answer.

---

Below, the modulus for the congruence is set to 100.

For integers $x$ and $y$ ( $0 \le x, y \le 2^N$ ), $S(x, y)$ is defined as follows:

$$
S(x, y) = 
\begin{cases} 
0 & \text{if } x = y \\
\sum_{i=x}^{y-1} A_i & \text{if } x < y \\
-S(y, x) & \text{if } x > y 
\end{cases}
$$

What we seek is $S(L, R+1)$. The questions we can ask are $S(2^i j, 2^i (j+1))$. Moreover, since $S(2^i (j+1), 2^i j) \equiv -S(2^i (j+1), 2^i j)$, we can also consider $S(2^i (j+1), 2^i j)$ as a valid question. When $S(x, y)$ and $S(y, z)$ are known, $S(x, z)$ can be determined as $S(x, y) + S(y, z)$.

Now, consider a graph $G$ with vertices labeled $0, 1, \ldots, 2^N$, where an edge is placed between vertices $x$ and $y$ if $S(x, y)$ can be questioned. 

For vertices $x$ and $y$ with a distance of 2 in $G$, you can determine $S(x, y)$ in two questions by asking about the vertices $v_0 (=x), v_1, v_2 (=y)$ on the shortest path from $x$ to $y$ in $G$, querying $S(v_0, v_1)$ and $S(v_1, v_2)$.

Similarly, for vertices $x$ and $y$ with a distance of 3 in $G$, you can determine $S(x, y)$ in three questions by asking about the vertices $v_0 (=x), v_1, v_2, v_3 (=y)$ on the shortest path from $x$ to $y$ in $G$, querying $S(v_1, v_2)$ and $S(v_2, v_3)$.

More generally, for vertices $x$ and $y$ with a distance of $d$ in $G$, $S(x, y)$ can be determined with $d$ questions.

Thus, if you can find the shortest path from $L$ to $R$ (with recovery) in graph $G$, you can solve the problem. The graph $G$ has $2^N + 1$ vertices and $2^{N+1} - 1$ edges, so using BFS, the shortest path can be found in $O(2^N)$ time complexity.

<details><summary>Python <b>Code</b></summary><br>

```py
from collections import deque

N, L, R = map(int, input().split())
n = 1 << N
edge = [[] for i in range(n + 1)]
for i in range(N + 1):
    for l in range(0, n, 1 << i):
        r = l + (1 << i)
        edge[l].append(r)
        edge[r].append(l)

parent = [None] * (n + 1)
parent[R + 1] = -1
dq = deque([R + 1])
while dq:
    v = dq.popleft()
    for u in edge[v]:
        if parent[u] == None:
            parent[u] = v
            dq.append(u)

ans = 0
now = L
while parent[now] != -1:
    p = parent[now]
    sgn = 1
    l, r = now, p
    if l > r:
        sgn = -1
        l, r = r, l
    i = (r - l).bit_length() - 1
    j = l >> i
    print("?", i, j, flush=True)
    T = int(input())
    ans += sgn * T
    now = p

print("!", ans % 100)
```

</details><br>