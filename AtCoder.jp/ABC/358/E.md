## [E - Alphabet Tiles](https://atcoder.jp/contests/abc358/tasks/abc358_e)

<details><summary><b>Japanese Editorial</b></summary><br>

問題文と同様に辞書順で $i$ 番目の英大文字を $a_i$ とおきます。

文字列のうち `z` が出現する個数ごとに条件を満たす文字列の個数を求め、これらを足し合わせることで答えを求めることを考えます（説明の都合上 `z` の個数ごとに考えていますが、`z` であることは本質ではなく、$1$ つのアルファベットを使う個数ごとに考えると捉えてよいです）。

長さ $s$ の文字列中に `z` が $t$ 個存在するとします。このとき、`z` の位置の決め方が ${s \choose t}$ 通りあります。`z` 以外の部分については、`z` を除いた長さ $s-t$ の文字列を考えることによって ${s \choose t}$ 通りそれぞれに対し、 `z` を含まない長さ $s-t$ の文字列であって $a_i$ が $0$ 個以上 $C_i$ 個以下であるものが対応していることがわかります。

したがって `a`, `b`, $\dots$, `z` について考えていたものを `a`, `b`, $\dots$, `y` について帰着できることがわかりました。

同様に考えると、`a`, `b`, $\dots$, `y` についての問題は `a`, `b`, $\dots$, `x` について帰着でき、これを繰り返すことにより本問題を解くことができそうだと考えられます。

このように小さいサイズに問題を帰着できたときには dp が有効なことが多いです。

実際、$dp_{i, j}$ を $a_1, a_2, \dots, a_i$ からなる長さ $j$ の文字列であって、各 $1 \le k \le i$ に対して $a_k$ が $0$ 個以上 $C_k$ 個以下であるものの個数とおくと、上の考察から $dp_{i+1, j} = \sum_{k=0}^{\min(j, C_{i+1})} dp_{i, j-k} {j \choose k}$ となります（$a_{i+1}$ の個数を $k$ として $k$ ごとに足し合わせています）。

答えは $\sum_{j=1}^{K} dp_{26, j}$ であり、dp は $j \le K$ の範囲で計算すれば十分であることに注意してください。

二項係数を階乗およびその逆元の前計算、あるいはパスカルの三角形の要領で二項係数自体を前計算することでこの dp は文字の種類数を $\sigma$ とおいて（本問題では $\sigma = 26$ です）時間計算量 $O(\sigma K^2)$ で計算することができ、本問題の制約下では十分高速です。

[実装例](https://atcoder.jp/contests/abc358/submissions/54548837) (C++)

</details><br>

Let's denote the $i$-th uppercase English letter in lexicographical order as $a_i$, as in the problem statement.

We consider finding the number of strings that satisfy the conditions based on the number of occurrences of the letter `z` in the string. By summing these counts, we can find the answer. (For the sake of explanation, we are considering the count of `z`, but the same logic applies to any other letter.)

Suppose there are $t$ occurrences of `z` in a string of length $s$. The number of ways to determine the positions of `z` is given by $\binom{s}{t}$. For the remaining part of the string, excluding `z`, we consider a string of length $s-t$ without `z`. For each of the $\binom{s}{t}$ ways, there are strings of length $s-t$ that do not contain `z` and have between 0 and $C_i$ occurrences of $a_i$.

Therefore, the problem of counting the occurrences of each letter from 'a' to `z` can be reduced to considering only the letters from `a` to `y`.

By applying the same logic, the problem for the letters from `a` to `y` can be reduced to the letters from `a` to `x`, and so on. By repeating this process, we can solve the problem.

When the problem can be reduced to smaller sizes like this, dynamic programming (dp) is often effective.

Let $dp_{i,j}$ be the number of strings of length $j$ that can be formed using the letters $a_1, a_2, \ldots, a_i$ with each letter $a_k$ (for $1 \leq k \leq i$) appearing between 0 and $C_k$ times. From the above discussion, we can derive that $dp_{i+1, j} = \sum_{k=0}^{\min(j, C_{i+1})} dp_{i, j-k} \binom{j}{k}$, where we sum over the number of occurrences $k$ of $a_{i+1}$.

The answer is $\sum_{j=1}^{K} dp_{26, j}$, and it is sufficient to compute the dp values for $j \leq K$.

By precomputing the binomial coefficients using factorials and their inverses, or using Pascal's triangle, this dp can be computed in $O(\sigma K^2)$ time complexity, where $\sigma$ is the number of different letters (which is $26$ for this problem). This is efficient given the constraints of the problem.

[Implementation Example](https://atcoder.jp/contests/abc358/submissions/54548837) (C++)

<details><summary>Atcode Admin Code</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/modint>
using namespace atcoder;

using ll = int64_t;
using mint = modint998244353;

#define rep(i, n) for(int i = 0; i < n; i++)
#define all(n) (n).begin(),(n).end()

struct modinv {
  int n; vector<mint> d;
  modinv(): n(2), d({0,1}) {}
  mint operator()(int i) {
    while (n <= i) d.push_back(-d[mint::mod()%n]*(mint::mod()/n)), ++n;
    return d[i];
  }
  mint operator[](int i) const { return d[i];}
} invs;
struct modfact {
  int n; vector<mint> d;
  modfact(): n(2), d({1,1}) {}
  mint operator()(int i) {
    while (n <= i) d.push_back(d.back()*n), ++n;
    return d[i];
  }
  mint operator[](int i) const { return d[i];}
} facts;
struct modfactinv {
  int n; vector<mint> d;
  modfactinv(): n(2), d({1,1}) {}
  mint operator()(int i) {
    while (n <= i) d.push_back(d.back()*invs(n)), ++n;
    return d[i];
  }
  mint operator[](int i) const { return d[i];}
} ifacts;
mint comb(int n, int k) {
  if (n < k || k < 0) return 0;
  return facts(n)*ifacts(k)*ifacts(n-k);
}

int main(){
    int n = 26;
    int K; cin >> K;
    vector<int> C(n);
    rep(i, n) cin >> C[i];
    vector<mint> dp(K+1);
    dp[0] = 1;
    rep(i, n){
        vector<mint> old(K+1);
        swap(old, dp);
        rep(j, K+1){
            rep(a, C[i] + 1){
                int nj = j + a;
                if (nj > K) break;
                dp[nj] += old[j] * comb(nj, a);
            }
        }
    }
    mint ans;
    rep(i, K) ans += dp[i+1];
    cout << ans.val() << "\n";
    return 0;
}
```

</details><br>

---
### Another approach 

<details><summary>Japanese editorial</summary><br>

DP を経由せず多項式を利用して数えます。


各文字 $i$ の個数が丁度 $a_i$ 個であるような文字列の個数は多項係数 $\binom{a_1 + a_2 + \dots + a_{26}}{a_1, a_2, \dots, a_{26}} = \dfrac{(a_1 + a_2 + \dots + a_{26})!}{a_1! \times a_2! \times \dots \times a_{26}!}$ なので答えは 

$$
\sum_{l=1}^{K} l! \left[ x^l \right] \prod_{i=1}^{26} \left( \sum_{j=0}^{C_{i}} \frac{1}{j!} x^j \right) 
$$

と表せます。ここで $\left[ x^l \right] f(x)$ は多項式 $f$ の $l$ 次の係数です。

従って 

$$
\prod_{i=1}^{26} \left( \sum_{j=0}^{C_{i}} \frac{1}{j!} x^j \right) 
$$

の $K$ 次以下の部分を計算できればよいですが、これは $O(\sigma K^2)$ 時間で可能です。また、多項式乗算に FFT を利用すれば $O(\sigma K \log K)$ 時間に削減されます (公式解説の DP も FFT を用いた畳み込みで同様の計算時間が達成されます)。なお $\sigma$ は文字種数であり、本問では $\sigma = 26$ に固定されています。

</details><br>

---

Counting is done using polynomials without going through dynamic programming (DP).

The number of strings where the number of each character $i$ is exactly $a_i$ can be represented by the multinomial coefficient $\binom{a_1 + a_2 + \dots + a_{26}}{a_1, a_2, \dots, a_{26}} = \dfrac{(a_1 + a_2 + \dots + a_{26})!}{a_1! \times a_2! \times \dots \times a_{26}!}$. Therefore, the answer is 

$$
\sum_{l=1}^{K} l! \left[ x^l \right] \prod_{i=1}^{26} \left( \sum_{j=0}^{C_{i}} \frac{1}{j!} x^j \right)
$$

where $\left[ x^l \right] f(x)$ represents the coefficient of $x^l$ in the polynomial $f$.

Thus,

$$
\prod_{i=1}^{26} \left( \sum_{j=0}^{C_{i}} \frac{1}{j!} x^j \right)
$$

needs to be calculated for terms up to the $K$-th degree. This can be done in $O(\sigma K^2)$ time. Furthermore, if polynomial multiplication is done using FFT, the time can be reduced to $O(\sigma K \log K)$ (the same calculation time is achieved in the official explanation's DP using convolution with FFT). Note that $\sigma$ is the number of character types, which is fixed at $\sigma = 26$ in this problem.

<details><summary>C++</summary><br>

```cpp
#include <bits/stdc++.h>
#include <atcoder/modint>
#include <atcoder/convolution>
using namespace std;
using namespace atcoder;

using mint = modint998244353;

#define rep(i, n) for(int i = 0; i < n; i++)

template <typename T, typename U = T>
struct factorial {
    factorial() = default;
    factorial(int n) { ensure(n); }

    static void ensure(const int n) {
        int sz = _fac.size();
        if (n + 1 <= sz) return;
        int new_size = max(n + 1, sz * 2);
        _fac.resize(new_size), _fac_inv.resize(new_size);
        for (int i = sz; i < new_size; ++i){
            _fac[i] = _fac[i-1]*i;
        }
        _fac_inv[new_size - 1] = U(1) / _fac[new_size - 1];
        for (int i = new_size - 1; i > sz; --i){
            _fac_inv[i - 1] = _fac_inv[i] * i;
        }
    }

    T fac(const int i) {
        ensure(i);
        return _fac[i];
    }

    T operator()(int i) {
        return fac(i);
    }

    U fac_inv(const int i) {
        ensure(i);
        return _fac_inv[i];
    }

    U binom(const int n, const int r) {
        if (n < 0 or r < 0 or n < r) return 0;
        ensure(n);
        return _fac[n] * _fac_inv[r] * _fac_inv[n - r];
    }

    template <typename ...Ds, enable_if_t<conjunction_v<is_integral<Ds>...>, nullptr_t> = nullptr>
    U polynom(const int n, const Ds& ...ds) {
        if (n < 0) return 0;
        ensure(n);
        int sumd = 0;
        U res = _fac[n];
        for (int d : { ds... }){
            if (d < 0 or d > n) return 0;
            sumd += d;
            res *= _fac_inv[d];
        }
        if (sumd > n) return 0;
        res *= _fac_inv[n - sumd];
        return res;
    }

    U perm(const int n, const int r) {
        if (n < 0 or r < 0 or n < r) return 0;
        ensure(n);
        return _fac[n] * _fac_inv[n - r];
    }

private:
    static vector<T> _fac;
    static vector<U> _fac_inv;
};


template <typename T, typename U>
vector<T> factorial<T, U>::_fac{ 1 };

template <typename T, typename U>
vector<U> factorial<T, U>::_fac_inv{ 1 };

int main() {
    int k; 
    cin >> k;
    constexpr int n = 26;
    vector<int> c(n);
    rep(i, n) cin >> c[i];

    factorial<mint> fac(k);

    vector<mint> pd(k + 1);
    pd[0] = 1;
    rep(i, n) {
        vector<mint> g(c[i] + 1);
        rep(v, c[i] + 1) {
            g[v] = fac.fac_inv(v);
        }
        auto dp = convolution(pd, g);
        dp.resize(k + 1);
        dp.swap(pd);
    }

    mint ans = 0;
    rep(x, k + 1) ans += pd[x] * fac.fac(x);
    cout << ans.val()-1 << endl;

    return 0;
}
```

</details><br>
