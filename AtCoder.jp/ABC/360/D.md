## [D - Ghost Ants](https://atcoder.jp/contests/abc360/tasks/abc360_d)

<details><summary><b>Japanese Editorial</b></summary>

条件を整理すると、 $1$ 以上 $N$ 以下の整数 $i, j (i \ne j)$ が $S_i =$ `1` かつ $S_j =$ `0` かつ $0 < X_j - X_i \le 2 \times T$ を満たすとき、蟻 $i$ と蟻 $j$ はすれ違います。 このような $(i, j)$ の組の個数を求める必要があります。

$X$ を昇順に並び替え、同時に対応する $S$ も並び替えても答えは変わらないため、並び替えたとします。$S_i = $ `1` である $i$ の $X_i$ を取り出した列を $A$ とし、$S_i = $ `0`である $i$ の $X_i$ を取り出した列を $B$ とします。 このとき、$A$ も $B$ も昇順とします。

ある $i$ に対して $B_j > A_i$ なる$j$ の最小値は $i$ が増加するにつれて単調に増加します。また、同時に $B_j - A_i \le 2 \times T$ を満たす $j$ の最大値も $i$ が増加するにつれて単調に増加します。以上から尺取り法を用いることで、各 $i$ に対して条件を満たす $j$ の数を求めることができます。そして、これらの総和を求めることで答えを得られます。

実装例(C++):

</details><br>

To summarize the conditions, ants $i$ and $j$ will pass each other if there exist integers $i, j$ (where $1 \leq i, j \leq N$ and $i \ne j$) such that $S_i = 1$, $S_j = 0$, and $0 < X_j - X_i \leq 2 \times T$. We need to find the number of such pairs $(i, j)$.

By sorting $X$ in ascending order and simultaneously sorting the corresponding $S$, the answer does not change. Therefore, we can assume the arrays are sorted. Let $A$ be the sequence of $X_i$ where $S_i = 1$, and $B$ be the sequence of $X_i$ where $S_i = 0$. Both $A$ and $B$ will be in ascending order.

For a given $i$, the smallest $j$ such that $B_j > A_i$ increases monotonically as $i$ increases. Similarly, the largest $j$ such that $B_j - A_i \leq 2 \times T$ also increases monotonically as $i$ increases. Using the two-pointer technique, we can determine the number of $j$'s satisfying the conditions for each $i$. Summing these counts gives the final answer.

Example implementation (C++):

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    ll t;
    cin >> n >> t;
    string s;
    cin >> s;
    vector<ll> x1, x2;
    for (int i = 0; i < n; ++i) {
        ll x;
        cin >> x;
        if (s[i] == '1')
            x1.push_back(x);
        else
            x2.push_back(x);
    }
    sort(x1.begin(), x1.end());
    sort(x2.begin(), x2.end());
    int l = 0, r = 0;
    ll ans = 0;
    for (int i = 0; i < (int)x1.size(); ++i) {
        while (l < (int)x2.size() && x2[l] < x1[i]) l++;
        while (r < (int)x2.size() && x2[r] <= x1[i] + 2 * t) r++;
        ans += r - l;
    }
    cout << ans << '\n';
}
```
