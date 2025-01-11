## [B - Heavy Snake](https://atcoder.jp/contests/abc388/tasks/abc388_b) 

太さが $T_i$、長さが $L_i$ のヘビの長さが $k$ 伸びたときのヘビの重さは $T_i(L_i+k)$ です。

したがって、各 $k = 1, 2, \cdots ,D$ に対して $T_i(L_i+k)$ の最大値を求め、出力すればよいです。

実装例

---

When a snake with thickness $T_i$ and length $L_i$ grows by $k$ in length, its weight becomes $T_i(L_i + k)$.

Therefore, for each $k = 1, 2, \cdots, D$, we need to find and output the maximum value of $T_i(L_i + k)$.

### Implementation Example

---

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, d;
	cin >> n >> d;
	vector<int> t(n), l(n);
	for (int i = 0; i < n; i++) cin >> t[i] >> l[i];
	for (int k = 1; k <= d; k++) {
		int ans = 0;
		for (int i = 0; i < n; i++) ans = max(ans, t[i] * (l[i] + k));
		cout << ans << '\n';
	}
}

```
