## [D - Souvenirs](https://atcoder.jp/contests/abc358/tasks/abc358_d)

<details><summary><b>Japanese Editorial</b></summary><br>

人 $1, 2, \dots, M$ の順に渡す箱を確定させることを考えます。

$i = 1, 2, \dots, M$ の順に以下のようにする貪欲法が正当です。

* $B_i$ 個以上のお菓子が入った箱であって、まだ誰にも渡すことを決めていない箱のうち入っているお菓子の数が最小である箱を人 $i$ に渡すと決める（以下この渡し方を $(\star)$ とおきます）。

この解法が正当でないと仮定して矛盾を導きます。

最適解を $1$ つとります。

この最適解においては、ある $i$ について $(\star)$ を満たさない渡し方をしています。そのようなものの中で最小の $i$ をとります。$1, 2, \dots, i-1$ について$(\star)$ を満たしているときに人 $i$ に対して渡す箱を箱 $X$ とおきます（正確には箱自体は一意には定まりませんが、箱に入っているお菓子の数は一意に定まります）。とった最適解において箱 $X$ が誰にも渡されない場合には、人 $i$ に箱 $X$ を渡すことにより解が改善するので最適解であることに矛盾します。したがって、ある人 $j$ に対して箱 $X$ を渡すことになりますが、この場合は人 $i$ と人 $j$ に渡す箱を交換する操作を行います。このような操作を行っても最適解である状態は保たれますが、この操作によって $(\star)$ を満たさない最小の $i$ は真に増加するため、操作を繰り返すことによって矛盾が得られます。よって貪欲法の正当性が示されました。

したがってこの貪欲法を十分高速にシミュレーションできればよいです。これは C++ における `std::multiset` などのデータ構造を利用して素朴に行うか、$A$ および $B$ は sort しても答えが変わらないことを利用して尺取り法の要領で行うこともできます。

実装例

</details><br>


Let's consider determining the boxes to be given to people in the order of 1, 2, ..., M.

It is valid to use the following greedy approach in the order $i = 1, 2, \dots, M$:

* For each person $i$, assign them the box that has at least $B_i$ candies and has the smallest number of candies among the boxes that have not yet been assigned to anyone (we will refer to this method as $(\star)$).

We will prove the correctness of this method by contradiction.

Let's consider an optimal solution.

In this optimal solution, suppose for some $i$, the assignment does not follow $(\star)$. Let's take the smallest such $i$. Assume that the assignments for people 1, 2, ..., $i-1$ follow $(\star)$. Let $X$ be the box given to person $i$ (specifically, the exact box may not be unique, but the number of candies in it is unique). If in this optimal solution, box $X$ is not given to anyone else, then assigning box $X$ to person $i$ improves the solution, contradicting the assumption that it was optimal. Therefore, box $X$ must be given to some other person $j$. In this case, we can swap the boxes given to person $i$ and person $j$. This swap maintains the optimal state, but it increases the smallest $i$ that does not follow $(\star)$, leading to a contradiction when the process is repeated. Hence, the correctness of the greedy method is proven.

Therefore, it is sufficient to simulate this greedy method efficiently. This can be done naively using data structures like `std::multiset` in C++, or by using the two-pointer technique (sliding window method) taking advantage of the fact that sorting $A$ and $B$ does not change the answer.

Implementation Example:

```cpp
#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
using namespace std;
using ll = long long;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);
    rep(i, n) cin >> a[i];
    rep(i, m) cin >> b[i];
    multiset<int> st;
    rep(i, n) st.insert(a[i]);
    ll ans = 0;
    rep(i, m) {
        auto v = st.lower_bound(b[i]);
        if (v == st.end()) {
            cout << -1 << '\n';
            return 0;
        }
        ans += *v;
        st.erase(v);
    }
    cout << ans << '\n';
}
```
