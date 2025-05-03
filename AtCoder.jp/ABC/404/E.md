## [E - Bowls and Beans](https://atcoder.jp/contests/abc404/tasks/abc404_e)

まず、豆の移動は「現在最も後ろにある豆を動かす」を繰り返すものとして構いません。
理由: 前にある豆を先に動かしてから後ろにある豆を動かすとき、これらの操作を逆にしても損しません。
また、豆を動かす際、複数の茶碗に分けて入れる必要もありません。
理由: 豆を分けて入れる操作をひとつ選び、豆をどこかひとつにまとめて入れても損しません。

このもとで本問題を考察しましょう。
まず、一番前にある豆を茶碗 $0$ に落とすまでに何手かかるかを考えます。
豆を移動するにあたって、次の性質が成り立ちます。

> ある豆を連続して移動させることを考える。
> 茶碗 $r$ から始めて $k$ 手連続で豆を移動させると、移動後に豆が存在する茶碗は区間を成す。
> 厳密には、ある $l$ が存在して、移動後に豆が存在しうのは茶碗 $l,l+1,\dots,r$ となる。

一番前にある豆が茶碗 $x$ にあるとき、この豆を茶碗 $0$ に移動させるための最短手数は次のように求められます。

* 最初、豆が存在しうる茶碗の区間は $[x,x]$ である。
* $k$ 手で豆が存在しうる茶碗の区間が $[l,r]$ のとき、 $k+1$ 手で豆が存在しうる茶碗の区間は $\displaystyle[\min_{i = l}^r(i−C_i),r]$ となる。
* これを、豆が茶碗 $0$ に到達しうる状態になるまで続ける。

これで、一番前にある豆に必要な移動回数は分かりました。
では、一番前にある豆以外に必要な移動回数はどう考えれば良いでしょうか?
この場合、豆を「ひとつ前の豆が存在する茶碗」まで到達させればよいです。というのも、その豆を動かしてひとつ前の豆が存在する茶碗まで到達させれば、そこにある豆とまとめてひとつの豆だと思って動かせばその豆のことを忘れることができます。

移動回数は高々 $N−1$ 回 (一番後ろの茶碗から豆を除去することを繰り返せば達成可能です) であることに注意すると答えは高々 $N−1$ となり、愚直にシミュレーションしても時間計算量 $O(N^2)$ でこの問題に正解できます。
segment tree 等で高速化すれば時間計算量 $O(N\log⁡ N)$ で解けます。

---

First, without loss of generality we can assume that each move consists of “taking the bean that is currently furthest back and moving it.”
**Reason:** If you ever move a bean that is further forward before moving one that is further back, you can swap those two moves and not do any worse.

Also, when you move a bean, there is no need ever to split it across multiple bowls.
**Reason:** If you were to split a single bean’s moves among several bowls, you could instead choose one of those bowls and dump the entire bean there without increasing your number of moves.

Under those simplifications, we analyze the problem as follows.

---

### Moving the frontmost bean to bowl 0

Suppose the frontmost bean is currently in bowl $x$.  We want the minimum number of moves to get it down to bowl 0.  Observe this property:

> **Claim.** If you move **the same** bean for $k$ consecutive moves, starting from bowl $r$, then after those $k$ moves the bean will occupy a contiguous range of bowls.
> More precisely, there exists some $l$ such that the bean could be in any bowl in the interval $[l,\,r]$.

We can compute how that interval evolves:

1. Initially, with 0 moves, the bean’s possible interval is $[x,\,x]$.
2. If after $k$ moves the interval is $[l,\,r]$, then after one more move it becomes

$$
  \bigl[\min_{i=l}^r\,(i - C_i),\;\,r\bigr],
$$

because from any bowl $i\in[l,r]$ you can move the bean to $i - C_i$.
3.  Continue until the interval includes 0—i.e. until it becomes $[\,0,\;r]$ or lower.

This gives the minimum number of moves needed to bring the frontmost bean to bowl 0.

---

### Moving each subsequent bean

For every other bean, you don’t need to bring it all the way to bowl 0.  Instead, you only need to move it until it reaches the bowl where the **previous** (i.e. one-rank-ahead) bean ended up.  Once it reaches that bowl, you can think of “merging” it with the earlier bean and forget about it.

---

### Overall complexity

Each bean requires at most $N-1$ moves (you can always repeatedly remove the bean from the very back), so the total answer is at most $N-1$.  A straightforward simulation runs in $O(N^2)$ time, which passes.  If you speed up the interval–minimum queries with a segment tree (or similar), you get $O(N\log N)$.
