## [F - SSttrriinngg in StringString](https://atcoder.jp/contests/abc346/tasks/abc346_f)

<details><summary>Japanese Editorial</summary>

解説

---

まずは $k$ に関して二分探索をします。以降、ある $k$ に対して、$g(T, k)$ が $f(S, N)$ の部分文字列であるかどうか判定する方法について考えます。

以下、$S$ の長さを $s$、$T$ の長さを $t$ とし、文字列 $X$ の先頭 $i$ 文字のことを $X[:i]$ と表記します。また、$T$ に含まれる各文字が $S$ にもまた含まれていることを仮定します（そうでない場合答えは明らかに $0$ です）。

$i = 1, 2, \dots, t$ の順に以下の値を求めることを考えます。

* $iter_i : g(T[:i], k)$ が $f(S, N)[:j]$ の部分文字列であるような最小の $j$

最終的には $iter_t$ と $N \times s$ の大小を比較することで答えが求まります。$iter_i$ から $iter_{i+1}$ を求めるのは $f(S, N)$ の $iter_{i} + 1$ 文字目以降で $T$ の $i+1$ 文字目が $k$ 回目に現れる場所を求めることと一致するので、本問題は、以下の形式のクエリを $N$ 回処理する問題に帰着されます。

* $query(a, b, c)$：正整数 $a, b$、文字 $c$ が与えられる。$f(S, N)$ の $a$ 文字目以降で $c$ が $b$ 回目に現れるのは何文字目か。

$S$ の中に $c$ が現れる回数を $cnt_c$ とおきます。$a$ が $s$ より大きい場合、$query(a, b, c) = query(a-s, b, c) + s$ を用いて $a \le s$ の場合に帰着できます。また、$b$ が $cnt_c$ より大きい場合、$query(a, b, c) = query(a + s, b - cnt_c, c)$ を利用して $b \le cnt_c$ の場合に帰着できます。

よって、$a\le s, b\le cnt_c$ の条件のもとでクエリを処理できればよいことがわかりました。これらの条件が満たされるとき $query(a, b, c)$ の答えは $2s$ 以下になるので、各英小文字に対してその文字が $f(S, 2)$ 内で現れる位置のリストを前計算で求めておけば、二分探索などを用いて各クエリを高速に処理することができます。

よって、最初の $k$ に関する二分探索を含め、全体で $O(s\sigma + t\log N s)$ や $O(s + \sigma + t\log s \log N s)$ （$\sigma$ は文字の種類数）などの計算量で本問題を解くことができます。

実装例 (C++) :

</details>

---
---

**Explanation**

First, we perform binary search on $k$. Next, we consider how to determine if $g(T, k)$ is a substring of $f(S, N)$ for a given $k$.

Let the length of $S$ be $s$, the length of $T$ be $t$, and denote the first $i$ characters of a string $X$ as $X[:i]$. We also assume that each character in $T$ is also present in $S$ (if not, the answer is obviously 0).

We aim to find the following values for $i = 1, 2, \dots, t$:

* $iter_i$: The minimum $j$ such that $g(T[:i], k)$ is a substring of $f(S, N)[:j]$.

Finally, we compare $iter_t$ with $N \times s$ to determine the answer. To find $iter_{i+1}$ from $iter_i$, we need to find where the $i+1$-th character of $T$ appears for the $k$-th time in $f(S, N)$ after the $iter_i$-th character. Therefore, this problem reduces to processing the following type of query $N$ times:

* $query(a, b, c)$: Given positive integers $a$ and $b$ and character $c$, determine the position of the $b$-th occurrence of $c$ in $f(S, N)$ after the $a$-th character.

Let $cnt_c$ be the number of times $c$ appears in $S$. If $a$ is greater than $s$, we can reduce the problem to the case where $a \le s$ using $query(a, b, c) = query(a-s, b, c) + s$. If $b$ is greater than $cnt_c$, we use $query(a, b, c) = query(a + s, b - cnt_c, c)$ to reduce the problem to the case where $b \le cnt_c$.

Thus, we need to process the query under the conditions $a \le s$ and $b \le cnt_c$. When these conditions are met, the answer to $query(a, b, c)$ will be within $2s$. Therefore, we can precompute the positions of each lowercase letter in $f(S, 2)$ and use binary search to process each query quickly.

Including the initial binary search on $k$, the overall complexity of the solution is $O(s\sigma + t\log N s)$ or $O(s + \sigma + t\log s \log N s)$, where $\sigma$ is the number of distinct characters.

Example implementation (C++):

```cpp
#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const ll inf = 1LL << 60;

int main() {
    ll n;
    string s, t;
    cin >> n >> s >> t;
    int sl = s.size(), tl = t.size();
    vector<vector<int>> pos(26);
    for (int i = 0; i < sl * 2; i++) {
        pos[s[i % sl] - 'a'].push_back(i);
    }
    vector pre(sl + 1, vector<int>(26)); // S の最初の i 文字に j が何回現れるか (How many times does j appear in the first i characters of S?)
    for (int i = 0; i < sl; i++) {
        pre[i + 1] = pre[i];
        ++pre[i + 1][s[i] - 'a'];
    }
    vector<int> cnt(26);
    for (int i = 0; i < 26; i++) cnt[i] = pos[i].size() / 2;
    ll ok = 0, ng = inf;
    auto f = [&](ll x) -> bool {
        ll iter = 0;
        for (int i = 0; i < tl; i++) {
            int c = t[i] - 'a';
            if (!cnt[c]) return false;
            ll r = (x - 1) % cnt[c] + 1;
            ll q = (x - r) / cnt[c];
            if (q > inf / sl) return false;
            iter += sl * q;
            int nx = pos[c][pre[iter % sl][c] + r - 1]; // iter % sl 以降で r 番目に c が現れる場所 (the rth occurrence of c after iter % sl)
            iter += nx + 1 - iter % sl;
            if (iter > n * sl) return false;
        }
        return true;
    };
    while (ng - ok > 1) {
        ll mid = (ok + ng) / 2;
        if (f(mid)) ok = mid;
        else ng = mid;
    }
    cout << ok << endl;
}

```
