## [D - Gomamayo Sequence](https://atcoder.jp/contests/abc346/tasks/abc346_d)

<details><summary>Japanese Editorial</summary><br>

問題の性質を利用して前後から文字列を扱う方法について解説しています。

dp により前からのみ文字列を扱う方法は[こちら](https://atcoder.jp/contests/abc346/editorial/9640)で紹介しています。

---

$T$ の $i$ 文字目と $i+1$ 文字目が一致するような $i$ を固定します。すると、$1$ 文字目から $i$ 文字目および $i+1$ 文字目から $N$ 文字目は `...0101010101...` のように `0` と `1` が交互に並ぶ文字列となります。

したがって、各 $i$ に対して以下の値が計算できればよいです。

* $S$ の $1$ 文字目から $i$ 文字目を `01010101...` のような `0` から始まり `0` と `1` が交互に並ぶ文字列にするために必要なコストの総和の最小値
* $S$ の $1$ 文字目から $i$ 文字目を `10101010...` のような `1` から始まり `0` と `1` が交互に並ぶ文字列にするために必要なコストの総和の最小値
* $S$ の $i+1$ 文字目から $N$ 文字目を `...10101010` のような `0` で終わり `0` と `1` が交互に並ぶ文字列にするために必要なコストの総和の最小値
* $S$ の $i+1$ 文字目から $N$ 文字目を `...01010101` のような `1` で終わり `0` と `1` が交互に並ぶ文字列にするために必要なコストの総和の最小値

上 $2$ つは $i$ での計算結果から $i+1$ での計算結果が簡単にわかるため $i$ の昇順、下 $2$ つは $i$ での計算結果から $i-1$ での計算結果が簡単にわかるため $i$ の降順に計算することで答えを求めることができます。

具体的に $1$ 番上に書いたものの計算を例にして説明します。

$i+1$ 文字目は $i+1$ が奇数のとき `0` に、偶数のとき `1` にするべきですが、これが元の $S_{i + 1}$ と一致している場合には $i$ での計算結果と $i+1$ での計算結果は一致します。そうでない場合は、$i$ での計算結果に $C_{i + 1}$ を足すことにより $i+1$ での計算結果が得られます。

実装の際には、`0` で終わる / `1` で終わるというような扱いではなく、($N$ 文字全体のうちの) 偶数文字目が `0` で奇数文字目が `1` の文字列 / 偶数文字目が `1` で奇数文字目が `0` の文字列というような扱いをすると考えるべきことが減ると考えられます。

実装例

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<ll> c(n);
    for (int i = 0; i < n; i++) cin >> c[i];
    vector<ll> f0(n + 1), f1(n + 1), g0(n + 1), g1(n + 1);
    for (int i = 0; i < n; i++) {
        f0[i + 1] = f0[i];
        f1[i + 1] = f1[i];
        if (i % 2 == 0) {
            if (s[i] == '0') f1[i + 1] += c[i];
            else f0[i + 1] += c[i];
        }
        else {
            if (s[i] == '0') f0[i + 1] += c[i];
            else f1[i + 1] += c[i];
        }
    }
    for (int i = n - 1; i >= 0; i--) {
        g0[i] = g0[i + 1];
        g1[i] = g1[i + 1];
        if (i % 2 == 0) {
            if (s[i] == '0') g0[i] += c[i];
            else g1[i] += c[i];
        }
        else {
            if (s[i] == '0') g1[i] += c[i];
            else g0[i] += c[i];
        }
    }
    ll ans = 1'000'000'000'000'000'000;
    for (int i = 1; i < n; i++) ans = min(ans, f0[i] + g0[i]);
    for (int i = 1; i < n; i++) ans = min(ans, f1[i] + g1[i]);
    cout << ans << '\n';
}
```

dp により前からのみ文字列を扱う方法を解説します。

問題の性質を利用して前後から文字列を扱う方法は[こちら](https://atcoder.jp/contests/abc346/editorial/9639)で紹介しています。

---

$dp_{i, j, k}$ を $S$ の $1$ 文字目から $i$ 文字目までを ($i$ 文字目まででの) 隣接する文字が同じであるものが $j$ 箇所であり、$i$ 文字目が $k$ であるような文字列に置き換えるために必要なコストの最小値として定義します（$k$ の値では `0` や `1` を単に整数の $0$ や $1$ と同様に扱っていることに注意してください）。

答えは $\min(dp_{N, 1, 0}, dp_{N, 1, 1})$ です。

$dp_{i, j, k}$ の具体的な計算について説明します。

説明の簡略化のため、$k = 0$ とします。$k = 1$ でも同様に計算できます。

$i-1$ 文字目の文字に注目して場合分けを行います。

$i-1$ 文字目の文字が `0` であるときは $i-1$ 文字目と $i$ 文字目が一致しており、$i-1$ 文字目の文字が `1` であるときは $i-1$ 文字目と $i$ 文字目が一致していません。

したがって、$S_i = $ `0` のとき $dp_{i, j, 0} = \min(dp_{i-1, j-1, 0}, )dp_{i-1, j, 1}, S_i =$ `1` のとき $dp_{i, j, 0} = \min(dp_{i-1, j-1, 0}, dp_{i-1, j, 1}) + C_i$ です（$j = 0$ のときは $j-1$ は負になるので、その際は min を取る対象から外してください）。

$j \le 1$ であるもののみ管理すればよいため dp の状態数は $O(N)$ 個でよく、遷移は $O(1)$ 通りであるため答えは時間計算量 $O(N)$ で計算できます。

実装例

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll INF = 1'000'000'000'000'000'000;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<ll> c(n);
    for (int i = 0; i < n; i++) cin >> c[i];
    vector dp(n, vector(2, vector(2, INF)));
    dp[0][0][s[0] - '0'] = 0;
    dp[0][0][(s[0] - '0') ^ 1] = c[0];
    for (int i = 1; i < n; i++) {
        int r = s[i] - '0';
        for (int k = 0; k < 2; k++) {
            dp[i][0][k] = dp[i - 1][0][k ^ 1] + (r == k ? 0 : c[i]);
            dp[i][1][k] = min(dp[i - 1][0][k], dp[i - 1][1][k ^ 1]) + (r == k ? 0 : c[i]);
        }
    }
    ll ans = min(dp[n - 1][1][0], dp[n - 1][1][1]);
    cout << ans << '\n';
}
```

</details><br>

The text explains a method for handling strings from both ends by utilizing the nature of the problem.

The method for handling strings from the front using dynamic programming (dp) is introduced [here](https://atcoder.jp/contests/abc346/editorial/9640).

---

We fix an index $i$ such that the $i$-th and $i+1$-th characters of $T$ are the same. Then, the substring from the 1st to the $i$-th character and the substring from the $i+1$-th to the $N$-th character will be strings where `0` and `1` alternate like `...0101010101...`.

Therefore, for each $i$, we need to calculate the following values:

* The minimum total cost required to transform the substring from the 1st to the $i$-th character of $S$ into a string starting with `0` and alternating `0` and `1` like `01010101...`.
* The minimum total cost required to transform the substring from the 1st to the $i$-th character of $S$ into a string starting with `1` and alternating `0` and `1` like `10101010...`.
* The minimum total cost required to transform the substring from the $i+1$-th to the $N$-th character of $S$ into a string ending with `0` and alternating `0` and `1` like `...10101010`.
* The minimum total cost required to transform the substring from the $i+1$-th to the $N$-th character of $S$ into a string ending with `1` and alternating `0` and `1` like `...01010101`.

The top two values can be easily calculated in ascending order of $i$ because the calculation result for $i+1$ can be obtained from the result for $i$. Similarly, the bottom two values can be calculated in descending order of $i$ because the calculation result for $i-1$ can be obtained from the result for $i$.

Let's explain the calculation of the first value as an example.

The $(i+1)$-th character should be `0` if $(i+1)$ is odd, and `1` if $(i+1)$ is even. If this matches the original $S_{i+1}$, the calculation result for $i+1$ will be the same as the result for $i$. Otherwise, the result for $i+1$ can be obtained by adding $C_{i+1}$ to the result for $i$.

In implementation, instead of considering the end characters as `0` or `1`, it is simpler to consider strings where even-indexed characters are `0` and odd-indexed characters are `1`, or even-indexed characters are `1` and odd-indexed characters are `0`.

Implementation Example

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<ll> c(n);
    for (int i = 0; i < n; i++) cin >> c[i];
    vector<ll> f0(n + 1), f1(n + 1), g0(n + 1), g1(n + 1);
    for (int i = 0; i < n; i++) {
        f0[i + 1] = f0[i];
        f1[i + 1] = f1[i];
        if (i % 2 == 0) {
            if (s[i] == '0') f1[i + 1] += c[i];
            else f0[i + 1] += c[i];
        }
        else {
            if (s[i] == '0') f0[i + 1] += c[i];
            else f1[i + 1] += c[i];
        }
    }
    for (int i = n - 1; i >= 0; i--) {
        g0[i] = g0[i + 1];
        g1[i] = g1[i + 1];
        if (i % 2 == 0) {
            if (s[i] == '0') g0[i] += c[i];
            else g1[i] += c[i];
        }
        else {
            if (s[i] == '0') g1[i] += c[i];
            else g0[i] += c[i];
        }
    }
    ll ans = 1'000'000'000'000'000'000;
    for (int i = 1; i < n; i++) ans = min(ans, f0[i] + g0[i]);
    for (int i = 1; i < n; i++) ans = min(ans, f1[i] + g1[i]);
    cout << ans << '\n';
}
```

```cpp
// snuke
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, n) for(int i = 0; i < (n); i++)
int main(){
    int n; 
    string s;
    cin >> n >> s;
    vector<int> c(n);
    rep(i, n) cin >> c[i];
    // flip the bits in even position (or odd)
    rep(i, n) if(i%2 == 1) s[i] ^= '1'^'0'; 

    ll ans = 1e18;
    rep(_, 2){
        // 
        vector<ll> l(n+1), r(n+1);

        rep(i, n) {
            l[i+1] = l[i];
            if (s[i] == '1') l[i+1] += c[i];
        }

        for (int i = n-1; i >= 0; i--){
            r[i] = r[i+1];
            if (s[i] == '0') r[i] += c[i];
        }
        for (int i = 1; i < n; i++){
            ans = min(ans, l[i] + r[i]);
        }
        rep(i, n) s[i] ^= '1' ^ '0';
    }
    cout << ans << endl;

    return 0;
}
```

```cpp
// snuke
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, n) for(int i = 0; i < (n); i++)
int main(){
    int n; 
    string s;
    cin >> n >> s;
    vector<int> c(n);
    rep(i, n) cin >> c[i];
    rep(i, n) if (i%2 == 0) s[i] ^= '1' ^ '0';
    ll ans = 1e18;
    rep(_, 2){
        ll now = 0;
        rep(i, n) if (s[i] == '0') now += c[i];
        rep(i, n-1){
            if (s[i] == '0') now -= c[i];
            else now += c[i];
            ans = min(ans, now);
        }
        rep(i, n) s[i] ^= '1' ^ '0';
    }
    cout << ans << endl;
    return 0;
}
```


We will explain the method for handling strings from the front using dp.

The method for handling strings from both ends by utilizing the nature of the problem is introduced [here](https://atcoder.jp/contests/abc346/editorial/9639).

---

We define $dp_{i, j, k}$ as the minimum cost required to transform the substring from the 1st to the $i$-th character of $S$ into a string where the $i$-th character is $k$ and there are $j$ positions where adjacent characters are the same (note that $k$ is treated as a simple integer $0$ or $1$).

The answer is $\min(dp_{N, 1, 0}, dp_{N, 1, 1})$.

Let's explain the specific calculation of $dp_{i, j, k}$.

For simplicity, we consider the case where $k = 0$. The calculation for $k = 1$ is similar.

We divide into cases based on the character at the $(i-1)$-th position.

If the $(i-1)$-th character is `0`, the $(i-1)$-th and $i$-th characters are the same. If the $(i-1)$-th character is `1`, they are not the same.

Therefore, when $S_i = 0$, $dp_{i, j, 0} = \min(dp_{i-1, j-1, 0}, dp_{i-1, j, 1})$, and when $S_i = 1$, $dp_{i, j, 0} = \min(dp_{i-1, j-1, 0}, dp_{i-1, j, 1}) + C_i$ (if $j = 0$, $j-1$ is negative, so exclude it from the min).

Since we only need to manage states with $j \le 1$, the number of dp states is $O(N)$, and each transition is $O(1)$, allowing us to compute the answer in $O(N)$ time.

Implementation Example

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll INF = 1'000'000'000'000'000'000;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<ll> c(n);
    for (int i = 0; i < n; i++) cin >> c[i];
    vector dp(n, vector(2, vector(2, INF)));
    dp[0][0][s[0] - '0'] = 0;
    dp[0][0][(s[0] - '0') ^ 1] = c[0];
    for (int i = 1; i < n; i++) {
        int r = s[i] - '0';
        for (int k = 0; k < 2; k++) {
            dp[i][0][k] = dp[i - 1][0][k ^ 1] + (r == k ? 0 : c[i]);
            dp[i][1][k] = min(dp[i - 1][0][k], dp[i - 1][1][k ^ 1]) + (r == k ? 0 : c[i]);
        }
    }
    ll ans = min(dp[n - 1][1][0], dp[n - 1][1][1]);
    cout << ans << '\n';
}
```

```cpp
//snuke
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, n) for(int i = 0; i < (n); i++)

void chmin(ll & a, ll b){
    a = min(a, b);
}

const ll INF = 1e18;
ll dp[200005][2][2];

int main(){
    int n; string s;
    cin >> n >> s;
    vector<ll> c(n); rep(i, n) cin >> c[i];
    rep(i, n+1)rep(j, 2)rep(k, 2) dp[i][j][k] = INF;
    rep(j, 2){
        int cost = 0;
        if (s[0] != '0' + j) cost = c[0];
        dp[1][j][0] = cost;
    }

    for (int i = 1; i < n; ++i){
        rep(j, 2) rep(k, 2){
            rep(nj, 2){
                int nk = k;
                if (j == nj) nk++;
                if (nk >= 2) continue;
                int cost = 0;
                if (s[i] != '0' + nj) cost = c[i];
                chmin(dp[i+1][nj][nk], dp[i][j][k] + cost);
            }
        }
    }
    ll ans = INF;
    rep(j, 2) chmin(ans, dp[n][j][1]);
    cout << ans << endl;
    return 0;
}
```
