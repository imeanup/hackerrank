## [D - Permutation Subsequence](https://atcoder.jp/contests/abc352/tasks/abc352_d)

<!-- 
**解説**

---

問題文中における $a$ の値を全探索することを考えます。 すなわち、$a = 1, 2, \cdots, N-K+1$ それぞれについて以下の値を求めたいです。

* $\{P_{i_1}, P_{i_2}, \cdots, P_{i_K}\} = \{a, a+1, \cdots, a + K -1\}$ となるように $i_1 < i_2 <\cdots <i_K$ を選んだときの $i_K-i_1$ の値

ここで、数列 $Q = (Q_1, Q_2, \cdots , Q_N)$ を、$Q_j = (P_j = j$ を満たす $i$ の値 $)$ と定義します。 $P$ が  $(1, 2, \cdots, N)$ の順列であるとき、 $Q$ もまた  $(1, 2, \cdots, N)$ の順列です。 すると、上記の値は以下のように言い換えられます。

* $\{ Q_a, Q_{a+1}, \cdots, Q_{a+K-1}\}$ の最大値と最小値の差

$a$ の昇順にこの値を求めることを考えます。集合 $\{ Q_a, Q_{a+1}, \cdots, Q_{a+K-1}\}$ は $a$ を $1$ 増やしたとき $1$ 要素分しか変化しない（$Q_a$ が抜けて $Q_{a+K}$ が入る）ことから、以下のようなデータ構造 $D$ があれば良いことがわかります。

* $D$ は集合を管理するデータ構造であり、以下の操作を高速に $O(N)$ より速く）処理できる。
  * $D$ に要素を $1$ つ追加する。
  * $D$ から要素を $1$ つ削除する。
  * $D$ に現在含まれる要素の最大値と最小値を取得する。

これらの要件を満たせるデータ構造の一つが平衡二分探索木であり、C++ の `std::set` などが該当します。`std::set` を用いた場合の実装の詳細は下記の実装例を参考にしてください。他の言語における実装については各言語のリファレンス等を参照してください。

実装例 (C++): -->


**Explanation**

---

Let's consider exhaustive search for the value of $a$ in the problem statement. In other words, we want to find the following value for each $a = 1, 2, \cdots, N-K+1$:

* The value of $i_K-i_1$ when we select $i_1 < i_2 < \cdots < i_K$ such that $\{P_{i_1}, P_{i_2}, \cdots, P_{i_K}\} = \{a, a+1, \cdots, a + K -1\}$.

Here, we define a sequence $Q = (Q_1, Q_2, \cdots , Q_N)$, where $Q_j$ represents the value of $i$ satisfying $P_j = j$. If $P$ is a permutation of $(1, 2, \cdots, N)$, then $Q$ is also a permutation of $(1, 2, \cdots, N)$. Therefore, the above value can be rephrased as follows:

* The difference between the maximum and minimum values of $\{ Q_a, Q_{a+1}, \cdots, Q_{a+K-1}\}$.

Let's compute this value in ascending order of $a$. Since the set $\{ Q_a, Q_{a+1}, \cdots, Q_{a+K-1}\}$ changes only by one element (where $Q_a$ is removed and $Q_{a+K}$ is added) when $a$ is increased by $1$, it becomes clear that we need a data structure $D$ with the following properties:

* $D$ is a data structure that manages sets and can perform the following operations quickly (in $O(N)$ or faster):
  * Add one element to $D$.
  * Remove one element from $D$.
  * Retrieve the maximum and minimum elements currently in $D$.

One data structure that meets these requirements is a balanced binary search tree, and in C++, `std::set` would be appropriate. Please refer to the implementation example below for details on implementing this with `std::set`. For implementations in other languages, please consult the respective language's documentation.

Implementation Example (C++):

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> q(n);
    for (int i = 0; i < n; i++) {
        int p;
        cin >> p;
        --p;
        q[p] = i;
    }
    set<int> st;
    for (int i = 0; i < k; i++) {
        st.insert(q[i]);
    }
    // *st.rbegin() : Get the maximum value
    // *st.begin() : Get the minimum value
    int ans = *st.rbegin() - *st.begin();
    for (int i = k; i < n; i++) {
        st.erase(q[i - k]);
        st.insert(q[i]);
        ans = min(ans, *st.rbegin() - *st.begin());
    }
    cout << ans << endl;
}

```
