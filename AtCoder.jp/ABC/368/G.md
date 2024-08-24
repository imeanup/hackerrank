## [G - Add and Multiply Queries](https://atcoder.jp/contests/abc368/tasks/abc368_g)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese</b></summary><br>

タイプ $3$ のクエリについて考えます。$A$ の最大値を $M$ とします。

まず、 $i = l$ のとき $v = 0$ なので必ず $v$ を $v+A[i]$ で置き換えるべきです。制約より、この時点で $v$ が正になります。重要な考察は、ここから $v$ を $v \times B[i]$ で置き換える操作を選ぶ回数は、雑に見積もっても $\log⁡_2 M (<60)$ 回しかないことです。なぜなら、 $2^{60} > 10^{18}$ なので $60$ 回以上この操作をできる入力が与えられないからです。

よって、以下のアルゴリズムで `while true:` 以下のループが回るのはたかだか $59$ 回です。

```py
v = A[l]
while true:
    next_l = min(r, l + 1 以降で B[i] >= 2 であるような最小の i)
    v += sum_a(l + 1, next_l)
    v = max(v + A[next_l], v * B[next_l])
    l = next_l
    if (l == r):
        break
output(v)
```

Segment Tree などを適切に使用することで計算量が $O(N+Q \log ⁡N\log ⁡M)$ になります。定数倍が非常に軽く、十分高速です。

</details><br>

Consider queries of type $3$. Let the maximum value of $A$ be $M$.

Firstly, when $i = l$, $v = 0$, so we should replace $v$ with $v + A[i]$. Due to the constraints, $v$ will be positive at this point. An important observation is that the number of times you can choose to replace $v$ with $v \times B[i]$ is at most $\log_2 M (<60)$, since $2^{60} > 10^{18}$, so no input will allow this operation more than 60 times.

Thus, the `while true:` loop in the following algorithm will run at most 59 times.

```python
v = A[l]
while true:
    next_l = min(r, smallest i >= l + 1 such that B[i] >= 2)
    v += sum_a(l + 1, next_l)
    v = max(v + A[next_l], v * B[next_l])
    l = next_l
    if (l == r):
        break
output(v)
```

By appropriately using data structures like Segment Trees, the time complexity is $O(N + Q \log N \log M)$. The constant factor is very small, making it sufficiently fast.
