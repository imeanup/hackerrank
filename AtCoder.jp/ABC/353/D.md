# [D - Another Sigma Problem](https://atcoder.jp/contests/abc353/tasks/abc353_d)

<!-- $f(x, y)$ を扱いやすい形に言い換えます。$y$ を文字列として解釈したときの長さを $len(y)$ とすると、$f(x, y) = 10^{len(y)} x + y$ です。

各 $i$ について、$f(\star, A_i)$ という形での $A_i$ の寄与と $f(A_i, \star)$ という形での $A_i$ の寄与を求めましょう。

前者は簡単です。$f(\star, A_i)$ では $A_i$ はそのまま加算されるので、答えには $(i-1) A_i$ 寄与します。

後者を考えます。$i < j$ かつ $len(A_j) = k$ なる $j$ の個数を $d_k$ とすると、寄与は $\sum_{k=1}^{10} d_k10^k A_i$ です。

$d_k$ の更新は各 $i$ について定数時間で行える（実装例も参考にしてください）ので、$A$ の最大値を $M$ とすれば 後者の寄与も各 $i$ について $O(\log M)$ で計算できます。

以上より、答えを $O(N\log M)$ で求めることができました。

実装例(C++): -->

Let's rephrase $f(x, y)$ into a more manageable form. When interpreting $y$ as a string, let $len(y)$ denote its length. Then, $f(x, y) = 10^{len(y)} x + y$.

For each $i$, let's determine the contribution of $A_i$ in the form $f(\star, A_i)$ and $f(A_i, \star)$.

The former is straightforward. In $f(\star, A_i)$, $A_i$ is added as it is, so its contribution to the answer is $(i-1) A_i$.

Now, consider the latter. Let $d_k$ be the number of $j$ such that $i < j$ and $len(A_j) = k$. The contribution is $\sum_{k=1}^{10} d_k 10^k A_i$.

Updating $d_k$ can be done in constant time for each $i$ (refer to the implementation example), so if $M$ is the maximum value in $A$, the latter contribution can also be calculated in $O(\log M)$ time for each $i$.

Therefore, the answer can be computed in $O(N\log M)$ time.

Implementation example (C++):

```cpp
#include <bits/stdc++.h>
#include "atcoder/modint"

using namespace std;
using ll = long long;
using mint = atcoder::modint998244353;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for(auto &v : a) cin >> v;
  vector<int> d(11);
  for(int i = 0; i < n; i++) {
    d[to_string(a[i]).size()]++;
  }
  mint res = 0;
  vector<mint> p10(11, 1);
  for(int i = 1; i <= 10; i++) p10[i] = p10[i - 1] * 10;
  for(int i = 0; i < n; i++) {
    res += mint(a[i]) * i;
    d[to_string(a[i]).size()]--;
    for(int j = 1; j <= 10; j++) {
      res += p10[j] * a[i] * d[j];
    }
  }
  cout << res.val() << endl;
}
```