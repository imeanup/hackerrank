<!-- 良い数列は，セグメント木の区間に対応しています．例えば入力例 $1$ の $S(3, 19)$ を良い数列に分割する方法は，下の図の赤い区間で表現することができます． -->

A good sequence corresponds to intervals in a segment tree. For example, the method of partitioning the good sequence in example 1, $S(3, 19)$, can be represented by the red intervals in the figure below.

![](https://img.atcoder.jp/abc349/58acfeba45a3cbb1726442d669e1e966.png)

<!-- 左から順番に分割する方法を決めていくことにします．個数が最小になるようにするとき，できるだけ長い区間を貪欲に取っていくことが最善です．

入力例 $1 S(3, 19)$ を例にとってみます．

1. 現在の残っている数列は $S(3, 19)$ である．$3$ を左端とする良い数列は $S(3, 4)$ のみなので $S(3, 4)$ を選択する．残りの数列は $S(4, 19)$ である．
2. 現在の残っている数列は $S(4, 19)$ である．$4$ を左端とする良い数列は $S(4, 5), S(4, 6), S(4, 8)$ なので最も長いの $(4, 8)$ を選択する．残りの数列は $S(8,19)$ である．
3. 現在残っている数列は $S(8,19)$ である．$8$ を左端とする良い数列は $(8,9), (8,10),S(8,12),S(8,16)$ なので最も長い $(8,16)$ を選択する．残りの数列は $S(16,19)$ である．
4. 現在残っている数列は $S(16,19)$ である．$16$ を左端とする良い数列は $S(16,17), S(16,18), S(16,20)$ である．$S(16,20)$ は残っている数列を超えているので，それ以外のうち最も長い $(16,18)$ を選択する．残りの数列は $S(18,19)$ である．
5. 現在残っている数列は $S(18,19)$ である．$18$ を左端とする良い数列は $S(18,19), S(18,20)$ である．$S(18,20)$ は残っている数列を超えているので，それ以外のうち最も長い $S(18,19)$ を選択する．残りの数列はない．

左端が $l$ のとき，あり得る数列の長さは $2$ べき（非負整数 $i$ を用いて $2^i$ と表わされる整数）のうち $l$ を割り切るものです．よって，左端が $l$ のときに選択するべき数列は

* $l \iff 0(\mod 2^i)$
* $l + 2^i \le R$ （残っている区間を超えないための条件）

を同時に満たすような最大の $i$ を $i_0$ としたとき $S(l, l + 2^i_0)$ になります．

実装例 (Python) -->

We will decide the method of partitioning from left to right. When minimizing the number of segments, it is best to greedily take as long intervals as possible.

Let's take Sample Input 1, $S(3, 19)$, as an example:

1. The current remaining sequence is $S(3, 19)$. The only good sequence starting with $3$ is $S(3, 4)$, so we choose $S(3, 4)$. The remaining sequence is $S(4, 19)$.
2. The current remaining sequence is $S(4, 19)$. The good sequences starting with $4$ are $S(4, 5)$, $S(4, 6)$, and $S(4, 8)$. We select the longest one, $(4, 8)$. The remaining sequence is $S(8, 19)$.
3. The current remaining sequence is $S(8, 19)$. The good sequences starting with $8$ are $(8, 9)$, $(8, 10)$, $S(8, 12)$, and $S(8, 16)$. We choose the longest one, $(8, 16)$. The remaining sequence is $S(16, 19)$.
4. The current remaining sequence is $S(16, 19)$. The good sequences starting with $16$ are $S(16, 17)$, $S(16, 18)$, and $S(16, 20)$. Since $S(16, 20)$ exceeds the remaining sequence, we select the longest one among the others, $(16, 18)$. The remaining sequence is $S(18, 19)$.
5. The current remaining sequence is $S(18, 19)$. The good sequences starting with $18$ are $S(18, 19)$ and $S(18, 20)$. Since $S(18, 20)$ exceeds the remaining sequence, we choose the longest one among the others, $S(18, 19)$. There is no remaining sequence.

When the left endpoint is $l$, the possible length of the sequence is any power of $2$ (an integer expressed as $2^i$, where $i$ is a non-negative integer) that divides $l$. Therefore, the sequence to be selected when the left endpoint is $l$ is $S(l, l + 2^{i_0})$, where $i_0$ is the maximum $i$ that simultaneously satisfies:

* $l \equiv 0 (\mod 2^i)$
* $l + 2^i \leq R$ (to not exceed the remaining interval)

Implementation (Python)

```py
L, R = map(int, input().split())
ans = []
while L != R:
    i = 0
    while L % pow(2, i+1) == 0 and L+pow(2, i+1) <= R:
        i += 1
    ans.append([L, L+pow(2, i)])
    L += pow(2, i)
print(len(ans))
for l, r in ans:
    print(l, r)
```

<!-- また，よい数列に分割する方法をセグメント木の区間に対応させるとき，区間は山型（右上がり→右下がり）になるという性質があります（すなわち，良い数列を $S(l_1, r_1) = (2^i_1 j_1, 2^i_1(j_1+1)) , \cdots, S(l_M, r_M) = (2^i_M j_M, 2^i_M(j_M+1))$ としたとき，ある整数 $k$ が存在して $i_1 < \cdots < i_k > \cdots > i_M $ になっています）．これを利用して解くこともできます． -->

Also, when correlating the method of partitioning a good sequence with intervals in a segment tree, there is a property that the intervals become mountain-shaped (rising rightward → falling rightward). In other words, when representing a good sequence as $S(l_1, r_1) = (2^{i_1} j_1, 2^{i_1}(j_1+1)), \cdots, S(l_M, r_M) = (2^{i_M} j_M, 2^{i_M}(j_M+1))$, there exists an integer $k$ such that $i_1 < \cdots < i_k > \cdots > i_M$. This property can also be utilized to solve the problem.

実装例 (Python)

```py
L, R = map(int, input().split())
ans = []
for i in range(61):
    if L % (pow(2, i+1)) == pow(2, i) and L+pow(2, i) <= R:
        ans.append([L, L+pow(2, i)])
        L += pow(2, i)
for i in range(60, -1, -1):
    if L+pow(2, i) <= R:
        ans.append([L, L+pow(2, i)])
        L += pow(2, i)
print(len(ans))
for l, r in ans:
    print(l, r)
```


<!-- さらに別の方法として，下から決めていくこともできます．多くのセグメント木の実装では区間クエリを下側から順番に見ていきながら処理していますが，それと同じことをすればよいです．下から順番に見ていって，左側と右側それぞれで長さ $2^i$ の数列を選択するかを決めていきます．左側で長さ $2^i$ の数列を選択する条件は

* $L$ の $i$ bit 目が立っている．
* $L < R$

です．右側も同様です． -->

Another method is to determine from the bottom up. Many implementations of segment trees process interval queries from the bottom up, examining them in order. We can do the same. We start from the bottom and decide whether to select a sequence of length $2^i$ on the left and right sides respectively. The condition to select a sequence of length $2^i$ on the left side is:

* The $i$-th bit of $L$ is set.
* $L < R$

The condition for the right side is similar.

実装例 (Python)

```py
L, R = map(int, input().split())
ans_left, ans_right = [], []
i = 0
while L < R:
    if (L >> i) & 1:
        ans_left.append([L, L+(1 << i)])
        L += 1 << i
    if (R >> i) & 1:
        ans_right.append([R-(1 << i), R])
        R -= 1 << i
    i += 1
ans = ans_left+ans_right[::-1]
print(len(ans))
for l, r in ans:
    print(l, r)
```

### Improvements

<details><summary>1. C++ </summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = int64_t;

int main(){
    ll L, R;
    cin >> L >> R;
    vector<pair<ll, ll>> ans;
    
    while (L != R){
        int i = 0;
        while (L % (1LL << (i+1)) == 0 && (L + (1LL << (i+1)) <= R)) {
            i++;
        }
        ans.emplace_back(L, L + (1LL << i));
        L += (1LL << i);
    }
    cout << ans.size() << "\n";

    for (auto &[x, y] : ans){
        cout << x << " " << y << "\n";
    }
    return 0;
}

```

</details>

<details><summary>2. C++ </summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;

int main(){
    ll L, R; cin >> L >> R;
    vector<pair<ll, ll>> ans;
    while (L < R){
        for (int i = 60; i >= 0; i--){
            ll w = 1ll << i;
            if (L % w) continue;
            if (L+w > R) continue;
            ans.emplace_back(L, L+w);
            L += w;
            break;
        }
    }
    cout << ans.size() << "\n";
    for (auto [l, r] : ans){
        cout << l << " " << r << "\n";
    }
    return 0;
}
```

</details>

<details><summary>3. C++ </summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;

int main(){
    ll L, R; cin >> L >> R;
    vector<pair<ll, ll>> ans;
    auto f = [&] (auto f, ll l, ll r) -> void {
        if (L <= l && r <= R){
            ans.emplace_back(l, r);
            return;
        }
        ll c = (l + r) >> 1;
        if (L < c) f(f, l, c);
        if (c < R) f(f, c, r);
    };
    f(f, 0, 1ll << 60);
    cout << ans.size() << "\n";
    for (auto [l, r] : ans){
        cout << l << " " << r << "\n";
    }
    return 0;
}
```

</details>


<details><summary>4. C++ </summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;

int main(){
    ll L, R; cin >> L >> R;
    vector<pair<ll, ll>> ans;
    int i = 0;
    while (L < R){
        if (L & 1) ans.emplace_back(L << i, (L+1) << i), L++;
        if (R & 1) ans.emplace_back((R-1) << i, R << i), R--;
        L >>= 1, R >>= 1, i++;
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << "\n";
    for (auto [l, r] : ans){
        cout << l << " " << r << "\n";
    }
    return 0;
}
```

</details>