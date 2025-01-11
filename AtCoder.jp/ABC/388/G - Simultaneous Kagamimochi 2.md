## [G - Simultaneous Kagamimochi 2](https://atcoder.jp/contests/abc388/tasks/abc388_g)

E 問題の[この解説](https://atcoder.jp/contests/abc388/editorial/11902)の第二方針を使います。 （与えられた餅列の後に無限に大きな餅が無限に続いているとし、連続する $K$ 個の餅をすべて上段にして $K$ 個の鏡餅を作るために必要な下段のインデックスの最小値について考えます。）

$B_i \mathrel{:=} i$ 番目の餅を上段の餅として使うときの、下段の餅としてありえる最小のインデックス $(1 \le i\le N)$ と定めます。

すると、クエリ $(L,R)$ に対する答えは $L + K − 1 + \displaystyle\max ⁡\left\{\max⁡_{L \le i < L + K}\{B_i−i\}, K \right\} \le R$ を満たす最大の $K$\ です。 左辺は $K$ について単調なので、$B_i−i$ をセグメント木などで管理し、二分探索を行うことでこの問題を解くことができます。

時間計算量は $O(N+Q\log⁡ N)$ などになります。

実装例は以下のようになります。 セグメント木上の二分探索を行っており、時間計算量は $O(N + Q\log ⁡N)$ 時間です。


```cpp
#include <iostream>
#include <vector>
#include <atcoder/segtree>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    vector<unsigned> A(N);
    for (auto&& a : A)
        cin >> a;

    // (区間の長さ, B[i] - i の最大値) を持つセグメント木
    using value_type = pair<unsigned, unsigned>;
    atcoder::segtree<value_type, [](const auto& lhs, const auto& rhs) {
        const auto& [left_length, left_distance_max]{lhs};
        const auto& [right_length, right_distance_max]{rhs};
        return value_type{left_length + right_length, max(left_distance_max, right_distance_max)};
    }, [] { return value_type{}; }> segment_tree{
        [N](const auto& seq) {
            vector<value_type> result(N);
            // B[i] を求める 全体で Θ(N) 時間
            for (unsigned i{}, j{}; i < N; ++i) {
                while (j < N && seq[i] * 2 > seq[j]) ++j;
                result[i] = {1, j - i};
            }
            return result;
        }(A)
    };

    unsigned Q;
    cin >> Q;

    for (unsigned i{}; i < Q; ++i) {
        unsigned L, R;
        cin >> L >> R;
        --L;
        // 右端が R 以下になる最大の [L, L+K) を求める
        cout << segment_tree.max_right(L, [L, R](const auto& itv) {
            const auto& [length, distance]{itv};
            return L + length + max(distance, length) <= R;
        }) - L << endl;
    }

    return 0;
}

```

---

For problem E, we will use the second strategy from the [official editorial](https://atcoder.jp/contests/abc388/editorial/11902). (We assume that after the given sequence of rice cakes, there is an infinitely large number of rice cakes continuing indefinitely. We then consider the smallest possible index of the bottom row rice cakes required to make a set of $K$ mirror cakes, with all $K$ cakes in the top row.)

We define $B_i \mathrel{:=}$ as the smallest index that can be used as the bottom row rice cake when using the $i$-th rice cake as the top row rice cake ($1 \le i \le N$).

Thus, the answer for a query $(L, R)$ is the maximum $K$ such that $L + K − 1 + \displaystyle\max \left\{\max_{L \le i < L + K}\{B_i−i\}, K \right\} \le R$ holds. The left-hand side is monotonically increasing with respect to $K$, so by managing $B_i−i$ with a segment tree and performing binary search, we can solve this problem.

The time complexity is $O(N + Q\log N)$.

The implementation example is as follows. It performs binary search on a segment tree, and the time complexity is $O(N + Q\log N)$.

```cpp
#include <iostream>
#include <vector>
#include <atcoder/segtree>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    vector<unsigned> A(N);
    for (auto&& a : A)
        cin >> a;

    // Segment tree holding (segment length, max value of B[i] - i)
    using value_type = pair<unsigned, unsigned>;
    atcoder::segtree<value_type, [](const auto& lhs, const auto& rhs) {
        const auto& [left_length, left_distance_max]{lhs};
        const auto& [right_length, right_distance_max]{rhs};
        return value_type{left_length + right_length, max(left_distance_max, right_distance_max)};
    }, [] { return value_type{}; }> segment_tree{
        [N](const auto& seq) {
            vector<value_type> result(N);
            // Compute B[i] for each i in Θ(N) time
            for (unsigned i{}, j{}; i < N; ++i) {
                while (j < N && seq[i] * 2 > seq[j]) ++j;
                result[i] = {1, j - i};
            }
            return result;
        }(A)
    };

    unsigned Q;
    cin >> Q;

    for (unsigned i{}; i < Q; ++i) {
        unsigned L, R;
        cin >> L >> R;
        --L;
        // Find the largest [L, L+K) where the right end is <= R
        cout << segment_tree.max_right(L, [L, R](const auto& itv) {
            const auto& [length, distance]{itv};
            return L + length + max(distance, length) <= R;
        }) - L << endl;
    }

    return 0;
}
```

---

長さ $N$ の数列 $C = (C_1, C_2, \dots, C_N)$ を以下のように定義します。

* $C_i$ は $2A_i \le A_{i+a}$ を満たす最小の整数 $a$。ただし、$2A_i > A_N$ のときは $C_i = N + 1 − i$

$i$ 番目のクエリの答えが $k$ 以上であることと、以下の $$ つの条件を満たすことは同値です。

* $2k\le R_i − L_i+1$
* $\max⁡(C_{L_i}, C_{L_i+1}, \dots, C_{L_i+k−1}) \le R_i − L_i + 1 − k$

この $2$ つの条件を用いて、クエリごとに答えを二分探索すれば良いです。

$2$ つめの条件は Sparse Table を用いて、$O(1)$ で判定することができます。よって、時間計算量は $O((N+Q)\log⁡(N))$ です。

[c++ 実装例 140ms](https://atcoder.jp/contests/abc388/submissions/61608867)


---

We define a sequence of length $N$, $C = (C_1, C_2, \dots, C_N)$, as follows:

* $C_i$ is the smallest integer $a$ that satisfies $2A_i \le A_{i+a}$. However, if $2A_i > A_N$, then $C_i = N + 1 - i$.

The answer to the $i$-th query being greater than or equal to $k$ is equivalent to satisfying the following two conditions:

* $2k \le R_i - L_i + 1$
* $\max(C_{L_i}, C_{L_i+1}, \dots, C_{L_i+k-1}) \le R_i - L_i + 1 - k$

Using these two conditions, we can perform a binary search for each query to find the answer.

The second condition can be checked using a Sparse Table in $O(1)$ time. Therefore, the overall time complexity is $O((N+Q) \log(N))$.

[C++ Implementation Example 140ms](https://atcoder.jp/contests/abc388/submissions/61608867)
