# C - Standing On The Shoulders

<!-- $P_N = i$、すなわち巨人 $i$ が一番上にいるときの一番上に立っている巨人の頭の高さは $B_i + \sum_{j \ne i} A_j$ です。

$B_i + \sum_{j \ne i} A_j = B_i - A_i + \sum_{j = 1}^{N} A_j$ であり、答えは $i = 1, 2, \cdots, N$ におけるこの値の最大値ですが、$\sum{j=1}^{N} A_j$ の値は $i$ に依らないことを利用すると $\max(B_j-A_i)$ の値を求めればよいことがわかります。

これは for ループなどを利用することで時間計算量 $O(N)$ で計算可能です。

実装例 -->


When $P_N = i$, that is, when the giant $i$ is at the top, the height of the tallest giant standing on top is $B_i + \sum \limits_{j \ne i} A_j$.

$$B_i + \sum \limits_{j \ne i} A_j = B_i - A_i + \sum \limits_{j = 1}^{N} A_j$$

, and the answer is the maximum value of this for $i = 1, 2, \cdots, N$. However, using the fact that the value of $\sum \limits_{j = 1}^{N} A_j$ does not depend on $i$, it can be understood that we only need to find the value of $\max(B_j-A_i)$.

This can be calculated with a time complexity of $O(N)$ using methods such as a for loop.

Implementation example:

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
	int n;
	cin >> n;
	vector<ll> a(n), b(n);
	for (int i = 0; i < n; i++) cin >> a[i] >> b[i];
	ll m = 0;
	for (int i = 0; i < n; i++) m = max(m, b[i] - a[i]);
	ll ans = m;
	for (int i = 0; i < n; i++) ans += a[i];
	cout << ans << '\n';
}
```
