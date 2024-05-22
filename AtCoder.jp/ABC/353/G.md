# [G - Merchant Takahashi](https://atcoder.jp/contests/abc353/tasks/abc353_g)

高橋君の移動は、高橋君が参加する市場が開催される町を順に移動するものだけを考えて構いません（そうでない移動に対して、余計な停止を取り除くことで最終的な所持金が減ることはありません）。

よって、$dp[i] :=$ 高橋君が最後に参加した市場が町 $i$ で行われたときの所持金の最大値 のように定め、これを更新していくことを考えます。 はじめ、$dp[1] = 10^{10^{100}}, dp[i] = 0 (i \ne 1)$ です（便宜上、はじめに $(T_i, P_i) = (1, 0)$ なる市場に参加したとします）。

市場の情報 $(T_i, P_i)$ に対して、更新は次のように行われます。

$$
dp[T_i] = P_i + \max_{1 \le j < N} \{dp[j] - C|j - T_i|\}
$$

この式を整理します。

$$
\begin{align}
dp[T_i] &= P_i + \max_{1 \le j < N} \{dp[j] - C|j - T_i|\} \\
&= P_i + \max \Big\{ \max_{1 \le j <T_i} \{ dp[j] - C|j - T_i|\}, \max_{T_i \le j < N} \{dp[j] - C|j-T_i| \} \Big\} \\
&= P_i + \max \Big\{ \max_{1 \le j <T_i} \{ dp[j] - C(T_i - j)\}, \max_{T_i \le j < N} \{dp[j] - C(j-T_i) \} \Big\} \\
&= P_i + \max \Big\{ -CT_i + \max_{1 \le j <T_i} \{ dp[j] - Cj\}, CT_i + \max_{T_i \le j < N} \{dp[j] - Cj\} \Big\} \\
\end{align}
$$


よって、数列に対して

* 一点更新（chmax）
* prefix max を求める

が高速にできれば、この問題を解くことができます $\Big((dp[j] - Cj)_{1 \le j < N}$ の列は前後反転しているとみればよいです $\Big)$。

これは、セグメント木や fenwick 木などを用いるとクエリ $O(\log N)$ で、prefix max が切り替わる点列を平衡二分探索木などで管理するとクエリ $O(\log \min\{N, M\})$ で処理することができます。

実装例は以下のようになります。セグメント木を用いるものと、prefix max が切り替わる点列を管理するものの両方を示します。

実装の際には、$10^{10^{100}}$ は少々大きいため、計算結果に影響がない範囲で初期値を調節する必要があります。

```cpp
#include <iostream>
#include <atcoder/segtree>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;
    unsigned long C;
    cin >> C;
    unsigned M;
    cin >> M;

    // range max を求めるセグメント木
    using range_max = atcoder::segtree<unsigned long, [](auto a, auto b){return max(a, b);}, []{return 0UL;}>;

    // (i, dp[i] + Ci) の prefix max を管理するセグメント木と、
    // (i, dp[i] - Ci) の suffix max を管理するセグメント木
    range_max prefix(N), suffix(N);
    
    // 初期値をオーバーフローを起こさない程度の値に設定
    constexpr unsigned long offset{2000000000000000000};
    
    // dp[0] = offset に対応
    prefix.set(0, offset);
    suffix.set(0, offset);
    
    // これまでの所持金の最大値
    unsigned long ans{offset};
    
    for (unsigned i{}; i < M; ++i) {
        unsigned T;
        unsigned long P;
        cin >> T >> P;
        --T;
        
        // dp[i] + Ci のうち i が T 以下であるような最大のものと、
        // dp[i] - Ci のうち i が T 以上であるような最小のものをとる
        // 前者の値 - CT と後者の値 + CT の小さくないほうを求めて、更新に用いる
        const auto best{max(prefix.prod(0, T + 1) - C * T, suffix.prod(T, N) + C * T) + P};
        
        // 所持金の最大値を更新
        ans = max(ans, best);
        
        // 更新
        prefix.set(T, best + C * T);
        suffix.set(T, best - C * T);
    }
    
    // 初期値を引いた値が求める答え
    cout << ans - offset << endl;
    return 0;
}
```

```cpp
#include <iostream>
#include <set>

int main() {
    using namespace std;
    unsigned N;
    unsigned long C;
    unsigned M;
    cin >> N >> C >> M;

    // (i, dp[i] + Ci) の prefix max を管理する set と、
    // (i, dp[i] - Ci) の suffix max を管理する set
    set<pair<unsigned, unsigned long>> prefix_max, suffix_max;

    // 初期値をオーバーフローを起こさない程度の値に設定
    constexpr unsigned long offset{2000000000000000000};

    // dp[0] = offset に対応
    prefix_max.emplace(0, offset);
    suffix_max.emplace(0, offset);

    // これまでの所持金の最大値
    unsigned long ans{offset};

    for (unsigned i{}; i < M; ++i) {
        unsigned T;
        unsigned long P;
        cin >> T >> P;
        --T;

        // (i, dp[i] + Ci) のうち i が T 以下であるような最大の i と、
        // (i, dp[i] - Ci) のうち i が T 以上であるような最小の i をとる
        // 前者の値 - CT と後者の値 + CT の小さくないほうを求めて、更新に用いる
        const auto best{max([C, T, &prefix_max]{
                                if(const auto it{prefix_max.lower_bound({T + 1, 0})}; it != begin(prefix_max))
                                    return prev(it)->second - C * T;
                                return 0UL;
                            }(), [C, T, &suffix_max]{
                                if(const auto it{suffix_max.lower_bound({T, 0})}; it != end(suffix_max))
                                    return it->second + C * T;
                                return 0UL;
                            }()) + P};

        // 所持金の最大値を更新
        ans = max(ans, best);

        // T 以降でより大きくないものを削除して、新しい値を追加
        auto prefix_upper{prefix_max.lower_bound({T, 0})};
        while (prefix_upper != end(prefix_max) && prefix_upper->second <= best + C * T)
            prefix_upper = prefix_max.erase(prefix_upper);
        prefix_max.emplace_hint(prefix_upper, T, best + C * T);

        // T 以前でより大きくないものを削除して、新しい値を追加
        auto suffix_lower{suffix_max.lower_bound({T + 1, 0})};
        while (suffix_lower != begin(suffix_max) && prev(suffix_lower)->second <= best - C * T)
            suffix_max.erase(prev(suffix_lower));
        suffix_max.emplace_hint(suffix_lower, T, best - C * T);
    }

    // 初期値を引いた値が求める答え
    cout << ans - offset << endl;
    return 0;
}

```

---
---

Takahashi's movement only needs to consider moving to the towns where the markets he participates in are held sequentially (for other movements, removing unnecessary stops does not decrease his final possession).

Therefore, we define $dp[i]$ as the maximum amount of money Takahashi can have when the last market he participated in was held in town $i$, and we will update this value. Initially, we set $dp[1] = 10^{10^{100}}$ and $dp[i] = 0$ for $i \ne 1$ (for convenience, we assume he first participates in a market with $(T_i, P_i) = (1, 0)$).

The updates for the market information $(T_i, P_i)$ are done as follows:

$$
dp[T_i] = P_i + \max_{1 \le j < N} \{dp[j] - C|j - T_i|\}
$$

Let's break down this formula:

$$
\begin{align}
dp[T_i] &= P_i + \max_{1 \le j < N} \{dp[j] - C|j - T_i|\} \\
&= P_i + \max \Big\{ \max_{1 \le j < T_i} \{ dp[j] - C|j - T_i|\}, \max_{T_i \le j < N} \{dp[j] - C|j - T_i| \} \Big\} \\
&= P_i + \max \Big\{ \max_{1 \le j < T_i} \{ dp[j] - C(T_i - j)\}, \max_{T_i \le j < N} \{dp[j] - C(j - T_i) \} \Big\} \\
&= P_i + \max \Big\{ -CT_i + \max_{1 \le j < T_i} \{ dp[j] - Cj\}, CT_i + \max_{T_i \le j < N} \{dp[j] - Cj\} \Big\} \\
\end{align}
$$

Thus, for the sequence:

* Point update (chmax)
* Prefix max

If these can be done quickly, this problem can be solved. $\Big((dp[j] - Cj)_{1 \le j < N}$ should be considered in reverse order $\Big)$.

This can be handled with segment trees or Fenwick trees (Binary Indexed Trees) to process queries in $O(\log N)$ time, and managing the sequence of points where the prefix max changes with a balanced binary search tree to process queries in $O(\log \min\{N, M\})$ time.

Here are implementation examples using both segment trees and managing the sequence of points where the prefix max changes.

In the actual implementation, $10^{10^{100}}$ is exceedingly large, so the initial value should be adjusted to a range that does not affect the computation results.

### Segment Tree Implementation Example

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;
    const long long INF = numeric_limits<long long>::max();

    SegmentTree(int size) {
        n = size;
        tree.resize(2 * n, -INF);
    }

    void update(int pos, long long value) {
        pos += n;
        tree[pos] = max(tree[pos], value);
        for (pos /= 2; pos > 0; pos /= 2) {
            tree[pos] = max(tree[2 * pos], tree[2 * pos + 1]);
        }
    }

    long long query(int left, int right) {
        left += n;
        right += n;
        long long result = -INF;
        while (left < right) {
            if (left % 2 == 1) result = max(result, tree[left++]);
            if (right % 2 == 1) result = max(result, tree[--right]);
            left /= 2;
            right /= 2;
        }
        return result;
    }
};

int main() {
    int N;
    long long C;
    cin >> N >> C;
    vector<pair<int, long long>> markets(N);
    for (int i = 0; i < N; ++i) {
        cin >> markets[i].first >> markets[i].second;
    }

    const long long INIT = 1e18;
    vector<long long> dp(N + 1, 0);
    dp[1] = INIT;
    
    SegmentTree segTree(N + 1);
    segTree.update(1, dp[1] - C * 1);

    for (const auto& market : markets) {
        int Ti = market.first;
        long long Pi = market.second;
        long long maxVal = Pi + max(
            segTree.query(1, Ti) - C * Ti,
            segTree.query(Ti, N + 1) + C * Ti
        );
        dp[Ti] = max(dp[Ti], maxVal);
        segTree.update(Ti, dp[Ti] - C * Ti);
    }

    long long answer = *max_element(dp.begin(), dp.end());
    cout << answer << endl;

    return 0;
}
```

### Balanced Binary Search Tree (Using std::map) Implementation Example

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <limits>
#include <algorithm>

using namespace std;

int main() {
    int N;
    long long C;
    cin >> N >> C;
    vector<pair<int, long long>> markets(N);
    for (int i = 0; i < N; ++i) {
        cin >> markets[i].first >> markets[i].second;
    }

    const long long INIT = 1e18;
    map<int, long long> dp;
    dp[1] = INIT;
    
    map<int, long long> prefixMax;
    prefixMax[1] = dp[1] - C * 1;

    for (const auto& market : markets) {
        int Ti = market.first;
        long long Pi = market.second;

        auto it = prefixMax.lower_bound(Ti);
        long long maxVal = Pi;

        if (it != prefixMax.begin()) {
            --it;
            maxVal += it->second + C * Ti;
        }

        it = prefixMax.lower_bound(Ti);
        if (it != prefixMax.end()) {
            maxVal = max(maxVal, Pi + it->second - C * Ti);
        }

        dp[Ti] = max(dp[Ti], maxVal);

        prefixMax[Ti] = max(prefixMax[Ti], dp[Ti] - C * Ti);
    }

    long long answer = 0;
    for (const auto& p : dp) {
        answer = max(answer, p.second);
    }
    
    cout << answer << endl;

    return 0;
}
```

These implementations demonstrate how to handle the updates and queries efficiently using segment trees and balanced binary search trees (with `std::map`). Adjustments may be necessary depending on the specific problem constraints and input sizes.