## [G - AtCoder Office](https://atcoder.jp/contests/abc365/tasks/abc365_g) 

<details style="border: 1px solid black; padding: 10px;"><summary>Japanese editorial</summary><br>

まず、それぞれの高橋くんに対してオフィスの中にいた時間の区間の集合 $S_i$ を求めることができます。

ある閾値 $C$ を定め、$S_i$ の大きさが $C$ 以下であるかによって $2$ つのアルゴリズムを使い分けることを考えます。

* $S_A, S_B$ の大きさがどちらも $C$ 以下の場合
* $S_A, S_B$ のうち少なくとも一方の大きさが $C$ より大きい場合

### $S_A, S_B$ の大きさがどちらも $C$ 以下の場合

区間の右端が小さいほうから見ていくことで $O(C)$ 時間で答えを求めることができます。

### $S_A, S_B$ のうち少なくとも一方の大きさが $C$ より大きい場合

このような組 $(A,B)$ はたかだか $\dfrac{N^2}{C}$ 個あります。 これらすべてに対する答えを求めておくことで、質問に対して $O(1)$ 時間で答えることができます。

$S_i$ の大きさが $C$ より大きいような $i$ はたかだか $\dfrac{N}{C}$ 個あります。 それぞれの $i$ に対して、すべての入退室記録を $O(M)$ 時間で走査してすべての高橋くんに対する答えを求めることができます。
この前計算は時間計算量 $O(\dfarc{MN}{C})$ 、空間計算量 $O(\dfrac{N^2}{C})$ で行うことができます。

全体の時間計算量は $O(QC+\dfrac{MN}{C})$ となるので、$C=O(\sqrt{\dfarc{MN}{Q}})$ とすることで時間計算量を $O(\sqrt{QMN})$ とすることができ、これは十分高速です。

実装例は以下のようになります。

```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <map>
#include <algorithm>

int main() {
    using namespace std;
    unsigned N, M;
    cin >> N >> M;
    vector<pair<unsigned, unsigned>> records(M);
    for (auto &&[T, P]: records) {
        cin >> T >> P;
        --P;
    }
    vector<vector<pair<unsigned, unsigned>>> inside_office(N);
    {
        vector<unsigned> in(N);
        for (const auto &[T, P]: records) {
            if (in[P]) {
                inside_office[P].emplace_back(in[P], T);
                in[P] = 0;
            } else
                in[P] = T;
        }
    }
    constexpr unsigned large_limit{1000};
    map<pair<unsigned, unsigned>, unsigned> memo;

    // 集合のサイズが大きいほうに対する答えを求める
    for (unsigned i{}; const auto &Si : inside_office) {
        if (size(Si) > large_limit) {
            vector<unsigned> sum(N);
            // i 番目の高橋くんがこれまで合計何分いたかを求める
            unsigned prev_i{}, i_sum{};
            bool i_inside{false};
            // 累積和で P 番目の高橋くんが i 番目の高橋くんと同時にいた時刻を求める
            for (const auto &[T, P]: records) {
                if (P == i) {
                    i_sum += i_inside * (T - prev_i);
                    prev_i = T;
                    i_inside ^= true;
                }
                sum[P] = i_sum + i_inside * (T - prev_i) - sum[P];
            }
            for (unsigned j{}; j < N; ++j)
                memo[minmax(i, j)] = sum[j];
        }
        ++i;
    }

    // 両方が小さい場合の答えを求める
    const auto query{[&inside_office, &memo](unsigned a, unsigned b) {
        if (memo.contains({a, b}))
            return memo[{a, b}];
        const auto &Sa{inside_office[a]};
        const auto &Sb{inside_office[b]};
        // どちらかが空なら、答えは 0
        if (empty(Sa) || empty(Sb))
            return memo[{a, b}] = 0;
        unsigned ans{};
        // a, b の区間を昇順に見て共通部分の長さを合計する
        for (unsigned i{}; const auto &[l, r] : Sa){
        ans += clamp(Sb[i].second, l, r) - clamp(Sb[i].first, l, r);
        while (i + 1 < size(Sb) && Sb[i + 1].first <= r) {
            ++i;
            ans += clamp(Sb[i].second, l, r) - clamp(Sb[i].first, l, r);
        }
    }
        return memo[{a, b}] = ans;
    }};

    unsigned Q;
    cin >> Q;

    for (unsigned i{}, a, b; i < Q; ++i) {
        cin >> a >> b;
        --a;
        --b;
        cout << query(a, b) << endl;
    }
    return 0;
}
```

</details><br>

## [G - AtCoder Office](https://atcoder.jp/contests/abc365/tasks/abc365_g) 

First, for each Takahashi, we can determine the set of intervals $S_i$ representing the times they were inside the office.

By defining a threshold $C$, we can use two different algorithms depending on whether the size of $S_i$ is less than or equal to $C$.

* When the sizes of both $S_A$ and $S_B$ are less than or equal to $C$
* When at least one of $S_A$ or $S_B$ has a size greater than $C$

### When the sizes of both $S_A$ and $S_B$ are less than or equal to $C$

We can find the answer in $O(C)$ time by examining the intervals in order of their right endpoints.

### When at least one of $S_A$ or $S_B$ has a size greater than $C$

There are at most $\dfrac{N^2}{C}$ such pairs $(A, B)$. By precomputing the answers for all these pairs, we can answer queries in $O(1)$ time.

There are at most $\dfrac{N}{C}$ such $i$ where the size of $S_i$ is greater than $C$. For each such $i$, we can scan all entry and exit records in $O(M)$ time to find the answer for all Takahashi. This precomputation can be done in $O(\dfrac{MN}{C})$ time and requires $O(\dfrac{N^2}{C})$ space.

Overall, the time complexity is $O(QC+\dfrac{MN}{C})$, so setting $C=O(\sqrt{\dfrac{MN}{Q}})$ gives a time complexity of $O(\sqrt{QMN})$, which is sufficiently fast.

Here is an example implementation:

```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <map>
#include <algorithm>

int main() {
    using namespace std;
    unsigned N, M;
    cin >> N >> M;
    vector<pair<unsigned, unsigned>> records(M);
    for (auto &&[T, P]: records) {
        cin >> T >> P;
        --P;
    }
    vector<vector<pair<unsigned, unsigned>>> inside_office(N);
    {
        vector<unsigned> in(N);
        for (const auto &[T, P]: records) {
            if (in[P]) {
                inside_office[P].emplace_back(in[P], T);
                in[P] = 0;
            } else
                in[P] = T;
        }
    }
    constexpr unsigned large_limit{1000};
    map<pair<unsigned, unsigned>, unsigned> memo;

    // Compute the answers for the larger sets
    for (unsigned i{}; const auto &Si : inside_office) {
        if (size(Si) > large_limit) {
            vector<unsigned> sum(N);
            // Compute the total time the ith Takahashi spent in the office
            unsigned prev_i{}, i_sum{};
            bool i_inside{false};
            // Compute the time intervals when the Pth Takahashi was in the office simultaneously with the ith Takahashi
            for (const auto &[T, P]: records) {
                if (P == i) {
                    i_sum += i_inside * (T - prev_i);
                    prev_i = T;
                    i_inside ^= true;
                }
                sum[P] = i_sum + i_inside * (T - prev_i) - sum[P];
            }
            for (unsigned j{}; j < N; ++j)
                memo[minmax(i, j)] = sum[j];
        }
        ++i;
    }

    // Compute the answers for the smaller sets
    const auto query{[&inside_office, &memo](unsigned a, unsigned b) {
        if (memo.contains({a, b}))
            return memo[{a, b}];
        const auto &Sa{inside_office[a]};
        const auto &Sb{inside_office[b]};
        // If either set is empty, the answer is 0
        if (empty(Sa) || empty(Sb))
            return memo[{a, b}] = 0;
        unsigned ans{};
        // Compute the total overlap between the intervals of a and b
        for (unsigned i{}; const auto &[l, r] : Sa){
            ans += clamp(Sb[i].second, l, r) - clamp(Sb[i].first, l, r);
            while (i + 1 < size(Sb) && Sb[i + 1].first <= r) {
                ++i;
                ans += clamp(Sb[i].second, l, r) - clamp(Sb[i].first, l, r);
            }
        }
        return memo[{a, b}] = ans;
    }};

    unsigned Q;
    cin >> Q;

    for (unsigned i{}, a, b; i < Q; ++i) {
        cin >> a >> b;
        --a;
        --b;
        cout << query(a, b) << endl;
    }
    return 0;
}
```
