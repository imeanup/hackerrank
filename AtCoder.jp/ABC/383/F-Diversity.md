## [F - Diversity](https://atcoder.jp/contests/abc383/tasks/abc383_f)

以下では商品 $i$ は $i$ 個目の商品を指すとします。

この問題は動的計画法を用いることで解くことができます。具体的には、

$dp[c][p]=$ 色が $c$ 以下の商品から $p$ 円分購入したときの満足度の最大値

として、最終的な答えは $dp[N][0], dp[N][1], \dots, dp[N][X]$ の最大値となるようなDPを考えます。

このDPを色ごとにまとめて更新することを考えます。$dp[c−1]$ まで計算が終わっていて $dp[c]$ の計算するとき、色が $c$ である商品を $1$ 個ずつ見て以下のように $dp[c]$ の更新をします。商品が $j$ であるとき、$p = X, X−1, \dots, P_j$ の順番で

$dp[c][p] = \max⁡(\{dp[c−1][p − P_j] + U_j + K, dp[c][p − P_j] + U_j, dp[c][p]\})$

と更新することで色 $c$ の商品全てについて更新した後は

$dp[c][i]=$ (色が $c$ 以下の商品から 色 $c$ の商品を $1$ 個以上購入して $i$ 円分購入したときの満足度の最大値)

となっています。最後に、各 $p$ に対して $dp[c][p] = \max⁡(dp[c][i],dp[c−1][p])$ と更新することで色が $c$ 以下の商品から $p$ 円分購入したときの満足度の最大値が $dp[c][p]$ に格納されます。

まとめると、以下の要領でDPテーブルが計算できます

* はじめ、$dp[0][0] = 0$ でそれ以外は $-\infty$ で初期化されているとします。
* $c = 1, 2, \dots, N$ の順で以下を行います
  * 色 $c$ の商品 $i_1, i_2, \dots, i_k$ であるとき、 $j = 1, 2, \dots ,k$ の順番で以下の更新をする
    * $p = X, X−1, \dots ,P_{ij}$ の順番で $dp[c][p] = \max⁡(\{dp[c−1][p−P_{ij}]+U_{ij} + K, dp[c][p−P_{ij}] + U_{ij}, dp[c][p]\})$ と更新する
  * $p = 0, 1, \dots , X$ に順で、$dp[c][p] = \max⁡(dp[c][p],dp[c−1][p])$ と更新する

商品の個数も色の種類数も $N$ で更新には $O(X)$ かかるため、全体で計算量は $O(NX)$ となり、十分高速です。

実装例(C++):

---

Below, let product $i$ refer to the $i$-th product.

This problem can be solved using dynamic programming (DP). Specifically:

Let $dp[c][p]$ denote the maximum satisfaction achievable by purchasing products costing up to $p$ yen from among products with colors up to $c$.

The final answer will be the maximum value among $dp[N][0], dp[N][1], \dots, dp[N][X]$.

The DP updates are done by grouping products by their colors. Assuming $dp[c-1]$ has already been calculated, when calculating $dp[c]$, process the products with color $c$ one by one. For a product $j$, update $dp[c]$ for $p = X, X-1, \dots, P_j$ in the following way:

$$
dp[c][p] = \max\left(dp[c-1][p - P_j] + U_j + K, \, dp[c][p - P_j] + U_j, \, dp[c][p]\right)
$$

After processing all products with color $c$, the following holds:

$$
dp[c][i] = \text{(Maximum satisfaction achievable by spending $i$ yen to purchase at least one product of color $c$ from products with colors up to $c$)}
$$

Finally, update for all $p$ as follows:

$$
dp[c][p] = \max(dp[c][p], dp[c-1][p])
$$

This ensures $dp[c][p]$ contains the maximum satisfaction achievable by purchasing products costing up to $p$ yen from products with colors up to $c$.

### Summary of the DP Table Computation:

1. Initialize $dp[0][0] = 0$, and all other entries as $-\infty$.
2. For $c = 1, 2, \dots, N$:
   - For each product $i_1, i_2, \dots, i_k$ of color $c$, update for $j = 1, 2, \dots, k$:
     - For $p = X, X-1, \dots, P_{ij}$, update:
       
       $$
       dp[c][p] = \max\left(dp[c-1][p-P_{ij}] + U_{ij} + K, \, dp[c][p-P_{ij}] + U_{ij}, \, dp[c][p]\right)
       $$
       
   - For $p = 0, 1, \dots, X$, update:

     $$
     dp[c][p] = \max(dp[c][p], dp[c-1][p])
     $$

### Complexity:

Since the number of products and color types is $N$, and each update takes $O(X)$, the overall complexity is $O(NX)$, which is efficient enough.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
static constexpr ll inf = 2e18;

int main() {
    int n, x;
    ll k;
    cin >> n >> x >> k;
    vector<int> p(n);
    vector<ll> u(n), c(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i] >> u[i] >> c[i];
    }
    vector<vector<int>> id(n);
    for (int i = 0; i < n; ++i) {
        id[c[i] - 1].push_back(i);
    }
    vector<vector<ll>> dp(n + 1, vector<ll>(x + 1, -inf));
    dp[0][0] = 0;
    for (int i = 0; i < n; ++i) {
        for (auto& idx : id[i]) {
            for (int j = x; j >= p[idx]; --j) {
                if (dp[i][j - p[idx]] != -inf)
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - p[idx]] + u[idx] + k);
                if (dp[i + 1][j - p[idx]] != -inf)
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i + 1][j - p[idx]] + u[idx]);
            }
        }
        for (int j = 0; j <= x; ++j)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
    }
    cout << *max_element(dp[n].begin(), dp[n].end()) << endl;
}
```
