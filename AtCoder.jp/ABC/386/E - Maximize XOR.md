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

ただし，この方法では $K$ が大きいとき実行時間に間に合うことができません．なぜなら，関数 func が呼び出される回数が $\displaystyle \sum_{i = 0}^K \binom{N}{i}$ 回程度となり，$\binom{N}{K}$ の値は小さくても $\binom{N}{\lfloor N/2\rfloor}$ の値が大きくなってしまうことがあるからです．

例えば，$(N, K) = (100,98)$ のとき，$\binom{N}{K} = 4950 < 10^6$ で制約を満たしますが，$\binom{100}{50}$ は約 $10^{29}$ と非常に大きくなってしまいます．

これを回避するためには，$K$ が大きいときには選ばれる $K$ 個を考える代わりに選ばれない $N−K$ 個を考えることで 実行時間に間に合わせることができます．具体的には，以下のような場合分けによって答えを計算することができます．

* $K \le N−K$ のとき：上のコードのように愚直に全探索をすればよいです．
* $K > N−K$ のとき：あらかじめすべての要素の XOR を計算しておき，選ばない $N − K$ 個を全探索することで $K$ 個選んだときの総 XOR を高速に求めることができます．

計算量は $O(\binom{N}{K} \min⁡(K, N−K))$ です．$\binom{N}{K} \le 10^6$ という制約では $\min⁡(K, N − K) \le 11$ が成り立つのでこれで間に合います．

Python であれば，長さ $N$ の列 $A$ のうち長さが $K$ である部分列の列挙が itertools.combinations を用いることで容易にできます．

---

**公式解説の計算量解析についての補足**

---

公式解説には以下のようなコードが載っており、なぜこれで $O(\binom{N}{K} \min⁡(N, N−K))$ になるのか疑問に思うかもしれません。 この計算量解析は自明ではないと考えています。

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

公式解説にある工夫で $K \le \frac{N}{2}$ となっていることを前提にすると、実はこの関数が呼び出される回数は合計で $O(K\binom{N}{K})$ 回です。以下はこのことの証明となります。

この関数の呼び出しは $2$ つに分けられます

* $\text{len}(x) = K$ であるような呼び出し(=4行目でreturnされる呼び出し)
* それ以外の呼び出し

前者が合計でちょうど $\binom{N}{K}$ 回なのはよいでしょう。
後者の呼び出しのうち、引数の `i` が $i$ であるようなものは、$0, 1, 2, \dots, i−1$ から $K$ 個未満選ぶ方法の数だけあります(そして、$K$ 個未満選ぶ実際の選び方がそれぞれ引数の `x` に入って呼び出されます)。よって呼び出し回数の合計は $\sum_{i=0}^N \sum_{k=0}^{\min⁡(i,K−1)} \binom{i}{k} = \sum_{k=0}^{K−1} \sum_{i=k}^N \binom{i}{k}$ となります。

ここで、$\sum_{i=k}^N \binom{i}{k} = \binom{N+1}{k+1}$ です。$N+1$ 人から $k+1$ 人選ぶときに、最も番号の若い $1$ 人で場合分けすると左辺の和が出てきます。

結局後者の呼び出し回数は $\displaystyle\sum_{k=0}^{K−1}\binom{N+1}{k+1} = \sum_{k=1}^K\binom{N+1}{k} = \sum_{k=1}^K\left(\binom{N}{k} + \binom{N}{k−1}\right) \le 2 \sum_{k=1}^K \binom{N}{k} \le 2K\binom{N}{K}$ となります。(範囲外の二項係数は $0$ とします)

なお、同じようでも以下のようなコードでは同様の解析で計算量は $\displaystyle\sum{k=1}^{K+1}\binom{N+1}{k}$ となりTLE します。$(N,K)=(10^6,1)$ のときなど)

```py
def func(x: list[int], i: int):
    if i == N:
        if len(x) == K:
            # 長さが K であるようなインデックスの列 x がここで列挙される
        return
    func(x, i + 1)
    if len(x) < K: func(x + [i], i + 1)

func([], 0)
```

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

However, this approach won’t work efficiently when $K$ is large. This is because the number of times the function `func` is called is roughly $\displaystyle\sum_{i=0}^K \binom{N}{i}$, and even though $\displaystyle\binom{N}{K}$ may be small, $\displaystyle\binom{N}{\lfloor N/2 \rfloor}$ can be large.

For example, when $(N, K) = (100, 98)$, $\binom{N}{K} = 4950 < 10^6$, which satisfies the constraint, but $\binom{100}{50}$ is approximately $10^{29}$, which is extremely large.

To avoid this, when $K$ is large, instead of thinking about the $K$ selected items, we can focus on the $N-K$ items that are not selected, which allows us to stay within the time limit. Specifically, the answer can be calculated using the following case distinctions:

* When $K \le N - K$: We can simply perform an exhaustive search like the code above.
* When $K > N - K$: Precompute the XOR of all elements and perform an exhaustive search over the $N-K$ unselected items to efficiently calculate the total XOR when selecting $K$ items.

The time complexity is $O(\binom{N}{K} \min(K, N-K))$. Given the constraint $\binom{N}{K} \le 10^6$, it follows that $\min(K, N-K) \le 11$, so this approach will work within the time limits.

<details style="border: 1px solid black; padding: 10px;"><summary><b>CPP</b></summary><br>

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}
const ll MAXN = 1e18;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<ll> a(n);
    rep(i, n) cin >> a[i];

    ll ans = 0;
    
    function<void(ll, int, int)>f = [&](ll curr, int idx, int c) -> void {
        if (c == 0) {
            chmax(ans, curr);
            return;
        }
        if (idx == n) return;
        f(curr^a[idx], idx+1, c-1);
        f(curr, idx+1, c);
    };

    if (k <= n-k) 
        f(0, 0, k);
    else{
        ll now = 0;
        for (const auto &x : a){
            now ^= x;
        }
        f(now, 0, n-k);
    }
    cout << ans << endl;
    return 0;
}
```

</details><br>

<details style="border: 1px solid black; padding: 10px;"><summary><b>Python</b></summary><br>

```py
import sys

sys.setrecursionlimit(3 * 10**5)

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0


def func(xor, idx, c):
    global ans
    if c == 0:
        ans = max(ans, xor)
        return
    if idx == N:
        return
    func(xor ^ A[idx], idx + 1, c - 1)
    func(xor, idx + 1, c)


if K <= N - K:
    func(0, 0, K)
else:
    all_xor = 0
    for i in range(N):
        all_xor ^= A[i]
    func(all_xor, 0, N - K)

print(ans)
```

</details><br>

In Python, using `itertools.combinations`, it’s easy to enumerate all length-$K$ subsequences from a list $A$ of length $N$.

<details style="border: 1px solid black; padding: 10px;"><summary><b>Python</b></summary><br>

```py
import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

if K <= N - K:
    for a in itertools.combinations(A, K):
        xor = 0
        for i in a:
            xor ^= i
        ans = max(ans, xor)
else:
    all_xor = 0
    for i in range(N):
        all_xor ^= A[i]
    for a in itertools.combinations(A, N - K):
        xor = all_xor
        for i in a:
            xor ^= i
        ans = max(ans, xor)

print(ans)
```

</details><br>


**Supplement on the Computational Complexity Analysis in the Official Explanation**

---

The official explanation includes the following code. You might wonder why its time complexity is $O\left(\binom{N}{K} \min(N, N-K)\right)$. I consider this computational complexity analysis non-trivial.

```py
def func(x: list[int], i: int):
    if len(x) == K:
        # An index sequence `x` of length K is enumerated here
        return
    if i == N:
        return
    func(x, i + 1)
    func(x + [i], i + 1)

func([], 0)
```

Assuming the optimization mentioned in the official explanation, where $K \le \frac{N}{2}$, the total number of calls to this function is actually $\displaystyle O(K\binom{N}{K})$. Below is the proof of this result.

The function calls can be divided into two types:

1. Calls where $\text{len}(x) = K$ (these return at line 4).
2. All other calls.

The total number of type 1 calls is exactly $\displaystyle\binom{N}{K}$, which is straightforward.

For type 2 calls, those where the argument `i` equals $i$, there are as many such calls as there are ways to choose fewer than $K$ elements from $\{0, 1, 2, \dots, i-1\}$ (and these chosen elements are passed in the argument `x` in each call). Therefore, the total number of calls is:

$$
\sum_{i=0}^N \sum_{k=0}^{\min(i, K-1)} \binom{i}{k} = \sum_{k=0}^{K-1} \sum_{i=k}^N \binom{i}{k}.
$$

Here, $\displaystyle\sum_{i=k}^N \binom{i}{k} = \binom{N+1}{k+1}$. This is derived by considering how to select $k+1$ people from $N+1$ people, breaking it down by the smallest-numbered person. 

Thus, the total number of type 2 calls is:

$$
\sum_{k=0}^{K-1}\binom{N+1}{k+1} = \sum_{k=1}^K\binom{N+1}{k}.
$$

Expanding further, this equals:

$$
\sum_{k=1}^K\left(\binom{N}{k} + \binom{N}{k-1}\right) \le 2 \sum_{k=1}^K \binom{N}{k} \le 2K\binom{N}{K}.
$$

(Note: Binomial coefficients outside their valid range are treated as 0.)

On the other hand, for similar code as shown below, the computational complexity would be $\displaystyle\sum_{k=1}^{\color{red}{K+1}} \binom{N+1}{k}$, which results in TLE (time limit exceeded) for cases like $(N, K) = (10^6, 1)$.

```py
def func(x: list[int], i: int):
    if i == N:
        if len(x) == K:
            # An index sequence `x` of length K is enumerated here
        return
    func(x, i + 1)
    if len(x) < K: func(x + [i], i + 1)

func([], 0)
```
