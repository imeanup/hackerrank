## [G - Compress Strings](https://atcoder.jp/contests/abc343/tasks/abc343_g)

<details><summary><b> Japanese Editorial </b></summary><br>

**解説**

---

まず、$S_i$ が $S_j$ の部分文字列であるような $i, j$ が存在する場合、「$S_i$ を部分文字列として含む」という条件は「$S_j$ を部分文字列として含む」という条件に完全に包含されているので、$S_i$ の存在は抹消してしまって問題ありません。以下、そのような $i, j$ が存在しないことを仮定します。

また、$2$ つの文字列 $X, Y$ について、$X$ の末尾 $k$ 文字と$Y$ の先頭 $k$ 文字が一致するような最大の $k$ を $f(X, Y)$ と表記します。

$S_1, S_2, \dots, S_N$ 全てを部分文字列として含むような文字列のうち長さが最小となるものを $1$ つ取り、この文字列の $l_i$ 文字目から $r_i - 1$ 文字目までが $S_i$ に対応するように $l_i, r_i$ を $1$ 組取ります。

一般性を失わず $l_1 \le l_2 \le \dots \le l_N$ を仮定します。このとき、$i = 1, 2, \dots, N-1$ 全てについて以下が成り立ちます。

* $l_i < l_{i+1} \le r_i$
* $r_i - l_{i+1} = f(S_i, S_{i+1})$

これらが成り立たない場合、1 段落目で置いた仮定や 2 段落目で取った文字列の長さの最小性に矛盾します。

従って、$S_1, S_2, \dots, S_N$ 全てを部分文字列として含むような文字列の長さの最小値を求める上では、以下のような文字列についてのみ考えても問題ありません。

* $(1, 2, \dots N)$ のある順列 $(p_1, p_2, \dots, p_N)$ について、$S_{p_{1}}, S_{P_{2}}$ の末尾 $|S_{p2}| - f(S_{p1}, S_{p2})$ 文字、$S_{p3}$ の末尾 $|S_{p3}| - f(S_{p2}, S_{p3})$ 文字、$\dots, S_{PN} の末尾 $|S_{PN}| - f(S_{PN_1}, S_{PN})$ 文字をこの順に連結してできる文字列

よって本問題は、全ての $(1, 2, \dots N)$ の順列 $(p_1, p_2, \dots, p_N)$ に対する $\sum_{i=1}^{N-1} f(S_{p_{i}}, S_{p_{i+1}})$ の最小値を求める問題に帰着されます。

Z algorithm、KMP 法、rolling hash 等の文字列アルゴリズムを使って全ての $i, j$ の組に対する $f(S_i, S_j)$ の値を予め求めておけば、上記の問題は巡回セールスマン問題と同様の bit DP によって解くことができます。

以上により、本問題を $O(N\sum |S_i| + 2^N N^2)$ などの計算量で解くことができました。

実装例 (C++) :

</details><br>

### Explanation

---

First, if there exist $i, j$ such that $S_i$ is a substring of $S_j$, the condition "includes $S_i$ as a substring" is entirely covered by the condition "includes $S_j$ as a substring". Therefore, the existence of $S_i$ can be eliminated without any problem. Henceforth, we assume no such $i, j$ exist.

Also, for two strings $X, Y$, let $f(X, Y)$ denote the maximum length $k$ such that the last $k$ characters of $X$ match the first $k$ characters of $Y$.

We take one string that includes all $S_1, S_2, \dots, S_N$ as substrings and has the minimum possible length. For this string, we determine a set of $l_i, r_i$ such that the substring from the $l_i$th character to the $(r_i - 1)$th character corresponds to $S_i$.

Without loss of generality, we assume $l_1 \le l_2 \le \dots \le l_N$. In this case, for all $i = 1, 2, \dots, N-1$, the following holds:

* $l_i < l_{i+1} \le r_i$
* $r_i - l_{i+1} = f(S_i, S_{i+1})$

If these do not hold, it contradicts the assumptions made in the first paragraph or the minimality of the string length taken in the second paragraph.

Therefore, to find the minimum length of a string that includes all $S_1, S_2, \dots, S_N$ as substrings, it is sufficient to consider the following type of string:

* For some permutation $(p_1, p_2, \dots, p_N)$ of $(1, 2, \dots, N)$, concatenate the last $|S_{p2}| - f(S_{p1}, S_{p2})$ characters of $S_{p2}$, the last $|S_{p3}| - f(S_{p2}, S_{p3})$ characters of $S_{p3}$, and so on, up to the last $|S_{pN}| - f(S_{pN-1}, S_{pN})$ characters of $S_{pN}$.

Hence, the problem reduces to finding the minimum value of $\sum_{i=1}^{N-1} f(S_{p_{i}}, S_{p_{i+1}})$ over all permutations $(p_1, p_2, \dots, p_N)$.

By using string algorithms like the Z algorithm, KMP method, or rolling hash, we can precompute the values of $f(S_i, S_j)$ for all pairs $i, j$. Then, the above problem can be solved using bit DP, similar to the Traveling Salesman Problem (TSP).

Thus, this problem can be solved with a time complexity of $O(N\sum |S_i| + 2^N N^2)$.

Example implementation (C++):


```cpp
#include <bits/stdc++.h>
#include <atcoder/string>

using namespace std;
using namespace atcoder;

// Does s contain t as a substring?
bool contains(const string &s, const string &t) {
    int n = s.size(), m = t.size();
    vector<int> za = z_algorithm(t + s);
    for (int i = m; i <= n; i++) {
        if (za[i] >= m) return true;
    }
    return false;
}

int main() {
    int n;
    cin >> n;
    vector<string> s(n);
    for (int i = 0; i < n; i++) cin >> s[i];
    for (auto it = s.begin(); it < s.end();) {
        bool flag = false;
        for (auto jt = s.begin(); jt < s.end(); jt++) {
            if (jt != it) flag |= contains(*jt, *it);
        }
        if (flag) it = s.erase(it);
        else ++it;
    }
    n = s.size();
    vector d(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        string now = s[i];
        for (int j = 0; j < n; j++) {
            if (j != i) now += s[j];
        }
        vector<int> za = z_algorithm(now);
        int cur = s[i].size();
        for (int j = 0; j < n; j++) {
            if (j == i) continue;
            d[j][i] = s[i].size();
            for (int k = 0; k < s[j].size(); k++) {
                if (za[cur + k] >= s[j].size() - k) {
                    d[j][i] = k + s[i].size() - s[j].size();
                    break;
                }
            }
            cur += s[j].size();
        }
    }
    vector dp(1 << n, vector<int>(n, 1 << 30));
    for (int i = 0; i < n; i++) dp[1 << i][i] = s[i].size();
    for (int bit = 1; bit < (1 << n) - 1; bit++) {
        for (int i = 0; i < n; i++) {
            if (~bit >> i & 1) continue;
            for (int j = 0; j < n; j++) {
                if (bit >> j & 1) continue;
                dp[bit | 1 << j][j] = min(dp[bit | 1 << j][j], dp[bit][i] + d[i][j]);
            }
        }
    }
    cout << *min_element(dp.back().begin(), dp.back().end()) << endl;
}
```