## [E - Max/Min](https://atcoder.jp/contests/abc356/tasks/abc356_e)

<details><summary>Japanese Editorial</summary><br>

簡単のため、$A$ が相異なる場合を考えます。$\max A = M$ とします。

和を取るのは $i < j$ を満たす全てのペア $(i, j)$ に対してであり、和を取る対象が $i, j$ に関して対称であるため、数列 $A$ を並び替えても答えは変わりません。よって $A$ は昇順にソートされているとしてよいです。

$A$ が昇順にソートされているとき、$i < j$ ならば $A_i \le A_j$ であることから、$\Big\lfloor\dfrac{\max(A_i, A_j)}{\min(A_i, A_j)}\Big\rfloor = \Big\lfloor\dfrac{A_j}{A_i}\Big\rfloor$ となります。

$i$ を固定したとき、$j$ を動かすのではなく、$\Big\lfloor\dfrac{A_j}{A_i}\Big\rfloor$ の値を動かすことを考えます。すなわち、

$$
\sum_{i=1}^{N-1}\sum_{j=i+1}^{N} \Big\lfloor\dfrac{A_j}{A_i}\Big\rfloor = \sum_{i=1}^{N-1}\sum_{n} n \times f(A_i, n)
$$

と変形します。ここで、$f(d, n)$ は $\Big\lfloor\dfrac{A_j}{d}\Big\rfloor = n$ を満たす $j$ の個数とします。（この変形は、例えば「1+1+1+2+2+2+2+5+5」を「1×3 + 2×4 + 3×0 + 4×0 + 5×2」と計算するものです）

$A_i = X$ となる $i$ の個数を $C_X$ として、あらかじめ $C$ の累積和を計算しておくことで $f(d, n)$ は $O(1)$ で求めることができます。また、$i$ を固定したとき $n$ の動く範囲は $n \le \frac{M}{A_i}$ であることから、和を取る項の個数は $\sum_{i=1}^{N-1} \frac{M}{A_i} \le \sum_{d=1}^{N} \frac{M}{d} = O(M \log N)$ です。（調和級数の和）

よって以上より $O(M \log N)$ でこの問題が解けました。

$A_i$ が同じ要素を持つ場合も、それらを適切にまとめて計算することで同じ計算量で求めることができます。

</details><br>

For simplicity, let's consider the case where all elements in $A$ are distinct. Let $\max A = M$.

The summation is taken over all pairs $(i, j)$ that satisfy $i < j$, and since the summation is symmetric with respect to $i$ and $j$, the answer does not change if we rearrange the sequence $A$. Thus, we can assume that $A$ is sorted in ascending order.

When $A$ is sorted in ascending order, for $i < j$, we have $A_i \le A_j$, which implies $\Big\lfloor \dfrac{\max(A_i, A_j)}{\min(A_i, A_j)}\Big\rfloor = \Big\lfloor\dfrac{A_j}{A_i}\Big\rfloor$.

Instead of varying $j$ for a fixed $i$, we consider varying the value of $\Big\lfloor\dfrac{A_j}{A_i}\Big\rfloor$. In other words,

$$
\sum_{i=1}^{N-1}\sum_{j=i+1}^{N} \Big\lfloor\dfrac{A_j}{A_i}\Big\rfloor = \sum_{i=1}^{N-1}\sum_{n} n \times f(A_i, n)
$$

Here, $f(d, n)$ represents the number of $j$ such that $\Big\lfloor\dfrac{A_j}{d}\Big\rfloor = n$. (This transformation is similar to calculating "1+1+1+2+2+2+2+5+5" as "1×3 + 2×4 + 3×0 + 4×0 + 5×2").

By precomputing the cumulative sum of $C$, where $C_X$ is the number of $i$ such that $A_i = X$, $f(d, n)$ can be obtained in $O(1)$ time. Additionally, for a fixed $i$, the range in which $n$ varies is $n \le \frac{M}{A_i}$, so the number of terms in the summation is $\sum_{i=1}^{N-1} \frac{M}{A_i} \le \sum_{d=1}^{N} \frac{M}{d} = O(M \log N)$ (harmonic series sum).

Therefore, we can solve this problem in $O(M \log N)$ time.

Even if $A_i$ contains duplicate elements, we can calculate the result with the same complexity by appropriately grouping them together.

[C++](https://atcoder.jp/contests/abc356/submissions/53940551) <p>
[Python](https://atcoder.jp/contests/abc356/submissions/53940544)
