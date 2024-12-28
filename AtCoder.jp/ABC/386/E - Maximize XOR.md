## [E - Maximize XOR](https://atcoder.jp/contests/abc386/tasks/abc386_e) 

特殊な制約 $\binom{N}{K} \le 10^6$ に注目します．$A$ から異なる $K$ 個の項を選ぶ方法が $10^6$ 通り以下であることが保証されているので，探索方法を工夫することでそのような選び方を全探索できます．

全探索をする方法として，以下のようなコードを書くことができそうです．

```py
def func(x: list[int], i: int):
    if len(x) == K:
        # 長さが K であるようなインデックスの列 x がここで列挙される
        return
    if i == N:
        return
    func(x, i + 1)
    func(x + [i], i + 1)

func([], 0)
```

ただし，この方法では $K$ が大きいとき実行時間に間に合うことができません．なぜなら，関数 func が呼び出される回数が $\displaystyle\sum_{i = 0}^K\binom{N}{i}$ 回程度となり，$\binom{N}{K}$ の値は小さくても $\binom{N}{\lfloor N/2\rfloor}$ の値が大きくなってしまうことがあるからです．

例えば，$(N, K) = (100,98)$ のとき，$\binom{N}{K} = 4950 < 10^6$ で制約を満たしますが，$\binom{100}{50}$ は約 $10^{29}$ と非常に大きくなってしまいます．

これを回避するためには，$K$ が大きいときには選ばれる $K$ 個を考える代わりに選ばれない $N−K$ 個を考えることで 実行時間に間に合わせることができます．具体的には，以下のような場合分けによって答えを計算することができます．

* $K \le N−K$ のとき：上のコードのように愚直に全探索をすればよいです．
* $K > N−K$ のとき：あらかじめすべての要素の XOR を計算しておき，選ばない $N − K$ 個を全探索することで $K$ 個選んだときの総 XOR を高速に求めることができます．

計算量は $O(\binom{N}{K} \min⁡(K, N−K))$ です．$\binom{N}{K} \le 10^6$ という制約では $\min⁡(K, N − K) \le 11$ が成り立つのでこれで間に合います．



Python であれば，長さ $N$ の列 $A$ のうち長さが $K$ である部分列の列挙が itertools.combinations を用いることで容易にできます．

---


Let’s focus on the special constraint $\binom{N}{K} \le 10^6$. Since the number of ways to select $K$ distinct items from $A$ is guaranteed to be at most $10^6$, we can explore all such selections by designing a suitable search method.

As a way to perform exhaustive search, we can write the following code:

```py
def func(x: list[int], i: int):
    if len(x) == K:
        # Here, we enumerate the index sequence x that has length K
        return
    if i == N:
        return
    func(x, i + 1)
    func(x + [i], i + 1)

func([], 0)
```

However, this approach won’t work efficiently when $zK$ is large. This is because the number of times the function `func` is called is roughly $\sum_{i=0}^K \binom{N}{i}$, and even though $\binom{N}{K}$ may be small, $\binom{N}{\lfloor N/2 \rfloor}$ can be large.

For example, when $(N, K) = (100, 98)$, $\binom{N}{K} = 4950 < 10^6$, which satisfies the constraint, but $\binom{100}{50}$ is approximately $10^{29}$, which is extremely large.

To avoid this, when $K$ is large, instead of thinking about the $K$ selected items, we can focus on the $N-K$ items that are not selected, which allows us to stay within the time limit. Specifically, the answer can be calculated using the following case distinctions:

* When $K \le N - K$: We can simply perform an exhaustive search like the code above.
* When $K > N - K$: Precompute the XOR of all elements and perform an exhaustive search over the $N-K$ unselected items to efficiently calculate the total XOR when selecting $K$ items.

The time complexity is $O(\binom{N}{K} \min(K, N-K))$. Given the constraint $\binom{N}{K} \le 10^6$, it follows that $\min(K, N-K) \le 11$, so this approach will work within the time limits.

In Python, using `itertools.combinations`, it’s easy to enumerate all length-$K$ subsequences from a list $A$ of length $N$.
