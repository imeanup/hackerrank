<!-- 再帰関数でも解けます。 
$g(k)$ を $\max (f(0),f(1), \cdots ,f(k))$ として $g(K)$ を求めたいです。
あらかじめ $2^i$ の bit が立っている $A_j$ の数を全ての $i$ について求めておきます。この値を $c_i$ とします。 $O(N\log A)$ でこれは求まります。

$k=0$ のとき $g$ は $A_i$ の総和で、これは $O(N)$ で求められます。
$k>0$ において $2^d \le k < 2^{d+1}$ なる非負整数 $d$ が存在します。ここで $[0,k]$ は $[0,2^d−1]$ と $[2^d ,k]$ の和として表されます。

$[0,2^d−1] における $f$ の最大値は $g(2^d−1)$ です。 $[2^d,k]$ における $f$ の最大値は $g(k−2^d)+2^d (N−2c_d)$ です。後者は $2^d$ の bit の寄与を考えると導かれます。
  
$g$ をメモ化再帰して上の遷移を実装することで全体として $O(N \log A)$ で解けます。 -->

This problem can also be solved using recursion. Let $g(k)$ be the maximum of $f(0), f(1), \ldots, f(k)$, and we want to find $g(K)$.

First, we calculate the number of $A_j$ where the bit $2^i$ is set for all $i$. Let's denote this value as $c_i$. This can be calculated in $O(N \log A)$.

When $k = 0$, $g$ is simply the sum of $A_i$, which can be calculated in $O(N)$.

For $k > 0$, there exists a non-negative integer $d$ such that $2^d \leq k < 2^{d+1}$. Here, $[0, k]$ can be represented as the sum of $[0, 2^d - 1]$ and $[2^d, k]$.

The maximum value of $f$ in $[0, 2^d - 1]$ is $g(2^d - 1)$. The maximum value of $f$ in $[2^d, k]$ is $g(k - 2^d) + 2^d(N - 2c_d)$. The latter is derived considering the contribution of the $2^d$ bit.

By implementing memoized recursion for $g$ and using the above transitions, the problem can be solved in $O(N \log A)$ overall.

<details><summary>C++</summary><br>

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = int64_t;

map<ll, ll> seen, mp, cnt;

ll solve(int n, ll k, vector<ll> &A){
    if (seen[k]) return mp[k];

    if (k == 0){
        ll res = accumulate(A.begin(), A.end(), 0ll);
        seen[k] = 1;
        mp[k] = res;
        return res;
    }
    ll g = 1;
    while (2 * g <= k) g *= 2;

    ll res = solve(n, g-1, A);
    res = max(res, solve(n, k-g, A) + g * (n-2*cnt[g]));
    seen[k] = 1;
    mp[k] = res;

    return res;
}

int main(){
    int n; ll k;
    cin >> n >> k;
    vector<ll> A(n);
    for (int i = 0; i < n; i++){
        cin >> A[i];
        ll g = 1;
        for (int d = 0; d < 41; d++){
            if (g & A[i]) cnt[g]++;
            g = g * 2;
        }
    }    
    cout << solve(n, k, A) << "\n";
    return 0;
}
```

</details>
<br>

---
---
<!-- 
$0 \le X \le K$ なる $X$ 全てについて $f(X)$ を計算し、最大値を出力する方法では、$O(NK)$ となり計算に $10$ 年以上かかりそうです。そこで、より高速に求める必要があります。

$X < k + 1$ なので $K+1 = (K_{39} K_{38} \cdots K_{0})_2, X = (X_{39}X_{38} \cdots X_0)_2$ と $2$ 進数で表したとき $^{*1}$ に、

$$

\begin{align*}
X_{39} &= K_{39} \\
&\vdots \\
X_{i+1} &= K_{i+1} \\
X_i &< K_i
\end{align*}

$$

を満たす $i$ が存在します。このとき、$X_i = 0, K_i = 1$ です。
逆に、ある $i$ について

$$
\begin{align*}
X_{39} &= K_{39} \\
&\vdots \\
X_{i+1} &= K_{i+1} \\
X_i &< K_i
\end{align*}
$$

であるような $X$ は、$X_{i−1}, X_{i−2}, \cdots, X_0$ の値に関わらず $X < K$ が成り立ちます。
そこで、このような $i(0 \le i < 40)$ を全探索することを考えます。各 i に対する $f(X)$ の最大値を $a_i$ とす れば、解は $\max\{a_0, a_1, \cdots, a_{39}\}$ になります。
各 $i$ に対する $f(X)$ の最大値を考えます。$X_{39}, X_{38}, \cdots, X_i$ は条件より

$$
\begin{align*}
X_{39} &= K_{39} \\
&\vdots \\
X_{i+1} &= K_{i+1} \\
X_i &= 0
\end{align*}
$$

です。上でも述べたとおり $X_{i−1}, X_{i−2}, \cdots, X_0$ を決める際には $X < K$ を無視しても構いません。$f$ は ビットごとに考えることができるため、$X_{i−1}, X_{i−2}, \cdots, X_0$ を独立に決めることができます。具体的には、$X_k (0 \le k \le i − 1)$ について、$A_1, A_2, \cdots, A_N$ の中で下から $k$ ビット目が立っているものの数を $c_k$ とすると、$X_k = 0$ とすればこのビットが $f$ に貢献する値は $2^kc_k$ となり、$X_k = 1$ とすれば $2^k(n − c_k)$ となります。し たがって、$c_k > n − c_k$ の場合は $_X_k = 0$ とし、そうでない場合は $X_k = 1$ とするのが最適です。これを $i$ の 小さい順または大きい順に探索することで、$X$ を高々 $2$ ビットずつ変化させて探索でき、$O(N \log K)$ で求め ることができます。
別解として、$X$ の上位ビットから順に決める桁 $DP$ による $O(N\log K)$ の解法もあります。 -->

To compute $f(X)$ for all $X$ such that $0 \le X \le K$ and find the maximum value, it would take more than 10 years with $O(NK)$ calculations. Therefore, a faster approach is needed.

Since $X < K + 1$, we can express $K+1 = (K_{39} K_{38} \cdots K_{0})_2$ and $X = (X_{39}X_{38} \cdots X_0)_2$ in binary, denoted as $^{*1}$, such that:

$$
\begin{align*}
X_{39} &= K_{39} \\
&\vdots \\
X_{i+1} &= K_{i+1} \\
X_i &< K_i
\end{align*}
$$

There exists an $i$ that satisfies these conditions. In this case, $X_i = 0$ and $K_i = 1$. Conversely, for a given $i$, if:

$$
\begin{align*}
X_{39} &= K_{39} \\
&\vdots \\
X_{i+1} &= K_{i+1} \\
X_i &< K_i
\end{align*}
$$

then, for such $X$, regardless of the values of $X_{i-1}, X_{i-2}, \cdots, X_0$, $X < K$ holds. Therefore, we consider exhaustive search for such $i$ ($0 \le i < 40$). Let $a_i$ be the maximum value of $f(X)$ for each $i$, then the solution is $\max\{a_0, a_1, \cdots, a_{39}\}$.

Now, consider the maximum value of $f(X)$ for each $i$. From the conditions, $X_{39}, X_{38}, \cdots, X_i$ satisfy:

$$
\begin{align*}
X_{39} &= K_{39} \\
&\vdots \\
X_{i+1} &= K_{i+1} \\
X_i &= 0
\end{align*}
$$

As mentioned earlier, we can ignore $X < K$ when determining $X_{i−1}, X_{i−2}, \cdots, X_0$. Since $f$ can be considered bitwise, we can independently determine $X_{i−1}, X_{i−2}, \cdots, X_0$. Specifically, for $X_k (0 \le k \le i − 1)$, if we denote the count of numbers in $A_1, A_2, \cdots, A_N$ with the $k$-th bit set from the bottom as $c_k$, then if $c_k > n - c_k$, setting $X_k = 0$ contributes $2^kc_k$ to $f$, otherwise, setting $X_k = 1$ contributes $2^k(n - c_k)$. Therefore, it's optimal to set $X_k = 0$ when $c_k > n - c_k$ and $X_k = 1$ otherwise. By searching in ascending or descending order of $i$, we can explore $X$ by changing it by at most $2$ bits at a time, and solve it in $O(N \log K)$.

Alternatively, there is a $DP$ solution that determines $X$ from the most significant bit downward, providing an $O(N\log K)$ solution.

---
$^{*1}$ The constraint $X, K ≤ 10^{12} ≤ 2^{40}$ implies that $X$ and $K$ can be represented with $40$ bits.