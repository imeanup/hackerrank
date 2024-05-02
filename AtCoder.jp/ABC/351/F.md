## [F - Double Sum](https://atcoder.jp/contests/abc351/tasks/abc351_f)

<!-- 
この問題は平面走査と呼ばれるアルゴリズムの基本問題です。この問題を解けなかった人は平面走査について学習するとよいでしょう。

求めたい二重和は

$$
\sum_{i = 1}^{N} \sum_{i<j} \max(A_j - A_i, 0)
$$

です。ここで、$i$ を固定したときの二重和への寄与は

$$
\begin{align}
\sum_{i < j} \max(A_j - A_i, 0) \\
=& \sum_{i < j, A_i \le A_j} A_j - A_i \\
=& (i < j かつ A_i \le A_j である A_j の総和) \\
-& (i < j A_i \le A_j である A_j の個数) \times A_i
\end{align}
$$


と言い換えることが出来ます。 この事実を利用すると、次の手順で平面走査をすることでこの問題を解くことが出来ます。

* 次の 2 種類の値を管理するデータ構造を用意する。
  * 「要素の追加」「$x$ 以上の要素の個数」の 2 種類のクエリを処理できる多重集合 $S_0$
  * 「要素の追加」「$x$ 以上の要素の総和」の 2 種類のクエリを処理できる多重集合 $S_1$
* また、答えを格納する変数 $ans$ を用意する。はじめ $ans = 0$ とする。
* $i = N, N-1, \cdots, 2, 1$の順に次の処理を行う。
  * $c$ を $S_0$ に $x = A_i$ でクエリを投げたときの返り値とする。
  * $s$ を $S_1$ に $x = A_i$ でクエリを投げたときの返り値とする。
  * $ans$ に $s - c \times A_i$ を加算する。
  * $S_0, S_1$ に $A_i$ を追加する。
* 最終的な $ans$ の値を出力する。

$S_0, S_1$ については、座標圧縮した Fenwick Tree を持てば 1 回の処理あたり $O(\log N)$ の計算量で処理出来ます。

以上よりこの問題を $O(N \log N)$ で解くことが出来て、これは十分高速です。

* 実装例 (Python) -->

This problem is a fundamental problem in an algorithm called "plane sweep" (or "sweep line"). Those who couldn't solve this problem might benefit from learning about plane sweep.

The double summation we want to find is:

$$
\sum_{i = 1}^{N} \sum_{i < j} \max(A_j - A_i, 0)
$$

Here, the contribution to the double summation when $i$ is fixed can be expressed as:

$$
\begin{align}
\sum_{i < j} \max(A_j - A_i, 0) \\
=& \sum_{i < j, A_i \le A_j} A_j - A_i \\
=& (\text{sum of } A_j \text{ where } i < j \text{ and } A_i \le A_j) \\
-& (\text{count of } A_j \text{ where } i < j \text{ and } A_i \le A_j) \times A_i
\end{align}
$$

Using this fact, we can solve this problem using the following steps in the plane sweep algorithm:

* Prepare a data structure to manage two types of values:
  * A multiset $S_0$ that can handle queries of "add element" and "count elements greater than or equal to $x$".
  * A multiset $S_1$ that can handle queries of "add element" and "sum of elements greater than or equal to $x$".
* Also, prepare a variable $ans$ to store the answer. Initially, set $ans = 0$.
* Iterate over $i = N, N-1, \cdots, 2, 1$ and perform the following steps:
  * Let $c$ be the result of querying $S_0$ with $x = A_i$.
  * Let $s$ be the result of querying $S_1$ with $x = A_i$.
  * Add $s - c \times A_i$ to $ans$.
  * Add $A_i$'s (count, $1$, and element, $A[i]$) to both $S_0$ and $S_1$.
* Output the final value of $ans$.

Using a Fenwick Tree with coordinate compression for $S_0$ and $S_1$, each operation can be performed in $O(\log N)$ time.

By following these steps, this problem can be solved in $O(N \log N)$ time, which is sufficiently fast.

* Implementation (Python)

```py
from atcoder.fenwicktree import FenwickTree
import bisect

N = int(input())
A = list(map(int, input().split()))
B = sorted([x for x in set(A)])
M = len(B)
sum0 = FenwickTree(M)
sum1 = FenwickTree(M)
ans = 0
for i in reversed(range(N)):
    k = bisect.bisect_left(B, A[i])
    c = sum0.sum(k, M)
    s = sum1.sum(k, M)
    ans += s - c * A[i]
    sum0.add(k, 1)
    sum1.add(k, A[i])
print(ans)

```

### Coordinate Compression

> [Here](https://codeforces.com/blog/entry/23180?#comment-561832)

```cpp
#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = int64_t;
#define rep(i, x) for(int i=0;i<(x);i++)

// Coodinate Compression
// https://youtu.be/fR3W5IcBGLQ?t=8550

template<typename T = int>
struct CC {
    bool initialized;
    vector<T> xs;
    CC() : initialized(false) {}
    void add(T x) {
        xs.push_back(x);
    }
    void init() {
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        initialized = true;
    }
    int operator()(T x) {
        if (!initialized) init();
        return upper_bound(xs.begin(), xs.end(), x) - xs.begin() - 1;
    }
    T operator[] (int i) {
        if (!initialized) init();
        return xs[i];
    }
    int size() {
        if (!initialized) init();
        return xs.size();
    }
};

int main(){
    int N; cin >> N;
    vector<int> A(N);
    rep(i, N) cin >> A[i];
    CC<int> cc;
    rep(i, N) cc.add(A[i]);

    fenwick_tree<int> tcnt(N);
    fenwick_tree<ll> tsum(N);
    ll ans = 0;
    rep(i, N){
        int ai = cc(A[i]);
        ans += 1LL * A[i] * tcnt.sum(0, ai);
        ans -= tsum.sum(0, ai);
        tcnt.add(ai, 1);
        tsum.add(ai, A[i]);
    }
    cout << ans << endl;
    return 0;
}

```
