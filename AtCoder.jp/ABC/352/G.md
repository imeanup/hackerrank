## [G - Socks 3](https://atcoder.jp/contests/abc352/tasks/abc352_g)

<!-- 
**解説**

---

以下、$S = A_1 + A_2 + \cdots + A_N$ とおきます。まず、タンスから靴下を取り出す回数は鳩の巣原理より $N+1$ 回以下です。

$i = 1, \cdots, N$ について、タンスから靴下を取り出す回数が $i$ 回 **以上**である確率を $P_i$ とおきます。求める期待値は $P_1 + P_2 + \cdots + P_N$ です。

<details open=""><summary>簡単な証明</summary>

タンスから靴下を取り出す回数が $i$ 回 **ちょうど**である確率を $Q_i$ とおくと、求める期待値は $1. Q_1 + 2.Q_2 + \cdots + (N+1).Q_(N+1)$ です。$Q_i = P_i - P_{i+1}$ を用いてこの式を変形すると、$P_1 + P_2 + \cdots +P_{N+1}$ が得られます。

</details>

$P_{i+1}$ は「タンスから靴下を $i$ 枚取り出した段階でまだ同じ色の靴下の組が存在しない確率」と言い換えることができます。したがって、$S$ 枚の中から色が相異なる $i$ 枚の靴下を選ぶ方法の数を $f_i$ とおくと、$P_{i+1} = \dfrac{f_i}{S \choose i}$ です。${S \choose 0}, {S \choose 1}, \cdots , {S \choose N}$ を求めることは容易なため、あとは各 $i = 0, 1, \cdots, N$ について $f_i の値が求まれば良いことになります。

多項式 $F$ を $F = \sum_{i=0}^{S} f_i x^i$ と定義します。ここで、

$$f_i = \sum_{1\le K_1 < k_2 < \cdots \le k_i \le N} \prod_{l=1}^{i} A_{k_l}$$

ですから、$F = (1 + A_i x)$ と定義すると、$F$ は $F_1, F_2, \cdots, F_N$ の総積になります。よって、本問題は以下の問題に帰着されます。

* $1$ 次多項式が $N$ 個与えられるので、その総積を求めよ。

これは有名な問題であり、シンプルな分割統治法によって $O(N \log^2 N)$ で解くことができます。具体的には、$f(l, r)$ を $F_l, F_{l+1}, \cdots, F_{r-1}$ の総積と定義した上で、$f(l,r) = f(l,m) \times f(m, r) \Big(m = \left\lfloor \dfrac{l+r}{2} \right\rfloor \Big)$ を用いて再帰的に解いていけばよいです。$f(l, m) \times f(m, r)$ の計算に NTT を用いれば全体の計算量が $O(N \log^2 N)$ になります。

実装例 (C++): -->

**Explanation**

---

Let's denote $S = A_1 + A_2 + \cdots + A_N$. First, by the pigeonhole principle, the number of times socks are taken out of the drawer is at most $N+1$.

Let's denote the probability that socks are taken out of the drawer at least $i$ times for $i = 1, \cdots, N$ as $P_i$. The expected value we seek is $P_1 + P_2 + \cdots + P_N$.

<details open=""><summary>Proof</summary>

Let's denote the probability that socks are taken out of the drawer exactly $i$ times as $Q_i$. Then, the expected value we seek is $1 \cdot Q_1 + 2 \cdot Q_2 + \cdots + (N+1) \cdot Q_(N+1)$. Using $Q_i = P_i - P_{i+1}$ and rearranging this expression, we obtain $P_1 + P_2 + \cdots +P_{N+1}$.

</details>

$P_{i+1}$ can be interpreted as the probability that "there are still no pairs of socks of the same color after taking out $i$ pairs of socks from the drawer". Therefore, if we let $f_i$ be the number of ways to choose $i$ socks of different colors from $S$ socks, then $P_{i+1} = \dfrac{f_i}{S \choose i}$. Since calculating ${S \choose 0}, {S \choose 1}, \cdots , {S \choose N}$ is straightforward, we only need to determine the values of $f_i$ for each $i = 0, 1, \cdots, N$.

Let's define the polynomial $F$ as $F = \sum_{i=0}^{S} f_i x^i$. Here,

$$f_i = \sum_{1\le K_1 < k_2 < \cdots \le k_i \le N} \prod_{l=1}^{i} A_{k_l}$$

so if we define $F = (1 + A_i x)$, then $F$ becomes the product of $F_1, F_2, \cdots, F_N$. Therefore, this problem is reduced to the following problem.

* Given $N$ first-degree polynomials, find their product.

This is a well-known problem and can be solved using a simple divide and conquer algorithm in $O(N \log^2 N)$ time. Specifically, by defining $f(l, r)$ as the product of $F_l, F_{l+1}, \cdots, F_{r-1}$, we can recursively solve it using $f(l,r) = f(l,m) \times f(m, r) \Big(m = \left\lfloor \dfrac{l+r}{2} \right\rfloor \Big)$. By using NTT for the calculation of $f(l, m) \times f(m, r)$, the overall time complexity becomes $O(N \log^2 N)$.

Implementation Example (C++):

```cpp
#include <bits/stdc++.h>
#include <atcoder/modint>
#include <atcoder/convolution>

using namespace std;
using namespace atcoder;

using mint = modint998244353;

// \prod_{i=l}^{r-1} (1+a[i]x)
vector<mint> prod(const vector<int> &a, int l, int r) {
    if (r - l == 1) return {1, a[l]};
    int m = (l + r) / 2;
    return convolution(prod(a, l, m), prod(a, m, r));
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    int s = 0;
    for (int &i: a) {
        cin >> i;
        s += i;
    }
    vector<mint> f = prod(a, 0, n);
    mint ans = 0;
    mint sCi = 1;
    for (int i = 0; i <= n; i++) {
        ans += f[i] / sCi;
        sCi *= s - i;
        sCi /= i + 1;
    }
    cout << ans.val() << endl;
}
```
