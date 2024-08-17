## [F - Rearrange Query](https://atcoder.jp/contests/abc367/tasks/abc367_f) 

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese editorial</b></summary><br>

$\{A_l,A_{l+1}, \dots ,A_r\}$ と $\{B_L,B_{L+1}, \dots,B_R\}$ が多重集合として一致しているか？というクエリを処理する問題です．

$2$ つの集合が一致しているかどうかを高速に確率的に判定する方法として Zobrist Hash が有名です．多重集合の一致判定も同様にハッシュを用いることで高速に解くことができます．

ハッシュ関数 $H$ として，以下の要件が満たされていると良いです．

* 多重集合 $S$ のハッシュ値 $H(S)$ が高速に計算できる
* 二つの多重集合 $S,T$ が一致しているならば $H(S) = H(T)$
* 二つの多重集合 $S,T$ が一致していないならば，高確率で $H(S) \ne H(T)$

例えば，$1$ 以上 $N$ 以下の各整数に適当なハッシュ値を割り当てて，$S$ のハッシュ関数を「$S$ に含まれる各要素のハッシュ値の総和 $\mod P$ ($P$ は適当な大きい素数)」とすることで上を満たすことができます．

$1$ つ目の要件について，$\{A_l,A_{l+1}, \dots ,A_r\}$ および $\{B_L,B_{L+1}, \dots ,B_R\}$ のハッシュ値は，あらかじめハッシュ値の累積和を計算しておくことで $O(1)$ で求めることができます．$2$ つ目の要件について，二つの多重集合 $S,T$ が一致しているならば $H(S) = H(T)$ となるのは容易にわかります．$3$ つ目の要件を示すのは難しいですが，二つの多重集合 $S,T$ が一致していないならば，高確率で $H(S)\ne H(T)$ となっています（Schwartz–Zippel lemma を用いて証明ができるようです．[参考 (noshi さんの記事)](https://github.com/noshi91/blog/blob/master/pages/hash.pdf)）．

以上で述べたように，$1$ 以上 $N$ 以下の各整数にハッシュ関数をランダムに設定し，累積和を前計算することで，各クエリに対して $O(1)$ で高確率で正しい答えを求めることができます．全体の計算量は $O(N+Q)$ です．

</details><br>

This is a problem about processing queries that ask whether the multisets $\{A_l,A_{l+1}, \dots ,A_r\}$ and $\{B_L,B_{L+1}, \dots,B_R\}$ are identical.

Zobrist Hash is a well-known method for efficiently and probabilistically determining whether two sets are identical. Similarly, the problem of determining if two multisets are identical can be solved quickly using hashing.

The hash function $H$ should satisfy the following requirements:

* The hash value $H(S)$ of a multiset $S$ can be computed quickly.
* If two multisets $S$ and $T$ are identical, then $H(S) = H(T)$.
* If two multisets $S$ and $T$ are not identical, then with high probability, $H(S) \ne H(T)$.

For example, by assigning a suitable hash value to each integer between $1$ and $N$, and defining the hash function of $S$ as "the sum of the hash values of all elements in $S$ modulo $P$ (where $P$ is a suitably large prime number)," the above requirements can be satisfied.

Regarding the first requirement, the hash values of $\{A_l,A_{l+1}, \dots ,A_r\}$ and $\{B_L,B_{L+1}, \dots ,B_R\}$ can be calculated in $O(1)$ time by precomputing the cumulative sums of the hash values. As for the second requirement, it is easy to see that if two multisets $S$ and $T$ are identical, then $H(S) = H(T)$. Demonstrating the third requirement is more difficult, but if two multisets $S$ and $T$ are not identical, then with high probability, $H(S) \ne H(T)$ (this can be proven using the Schwartz–Zippel lemma; see [reference (noshi's article)](https://github.com/noshi91/blog/blob/master/pages/hash.pdf)).

As described above, by randomly assigning a hash function to each integer between $1$ and $N$ and precomputing the cumulative sums, you can obtain the correct answer with high probability in $O(1)$ time for each query. The overall computational complexity is $O(N+Q)$.

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
import random
mod = (1 << 61) - 1

N, Q = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))

hash = [random.randint(1, mod - 1) for i in range(N)]
cumA = [0] * (N + 1)
cumB = [0] * (N + 1)
for i in range(N):
    cumA[i + 1] = (cumA[i] + hash[A[i]]) % mod
    cumB[i + 1] = (cumB[i] + hash[B[i]]) % mod

for i in range(Q):
    l, r, L, R = map(int, input().split())
    if (cumA[r] - cumA[l - 1]) % mod == (cumB[R] - cumB[L - 1]) % mod:
        print("Yes")
    else:
        print("No")

```

</details><br>
