## [G - Sum of (XOR^K or 0)](https://atcoder.jp/contests/abc367/tasks/abc367_g) 


<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese editorial</b></summary><br>

この解説では xor 畳み込みおよび hadamard 変換が登場します ．[ABC の過去問](https://atcoder.jp/contests/abc212/tasks/abc212_h) の解説も参考にしてください．

---

$L=20$とします．$i = 0,1, \dots ,2^L−1$ に対して $C_i$ を「$A$ の部分列のうち，長さが $M$ の倍数であり，総 xor が $i$ に等しいものの個数」として定めます．答えは $\sum_{i=0}^{2^L-1} C_i$ と表されるので，$C_0,C_1, \dots ,C_{2^L−1}$ が求められれば良いです．

長さが $2^L$ であり，各項が多項式であるような列の集合を $S$ とします．

$v_i \in S (i=1,2, \dots ,N)$ を次で定めます．

* $v_i$ の第 $0$ 項は $1$，第 $A_i$ 項は $x$，それ以外は $0$
  * ただし $A_i = 0$ のときは第 $0$ 項は $1+x$，それ以外は $0$

また $a,b \in S$ に対して，xor 畳み込み $a∗b\in S$ を次で定めます（$×$ は通常の多項式の積です）．

$$
(a*b)_k = \sum_{i\oplus j = k} a_i \times b_j
$$

$N$ 個の列 $v_1,v_2, \dots ,v_N$ の xor 畳み込みを $V = v_1∗v_2∗ \dots ∗v_N$ とします．このとき，$V$ の第 $i$ 項の $x_j$ の係数 $([x^j]V_i)$ は「$A$ の長さ $j$ の部分列であって，総 xor が $i$ であるものの個数」と等しくなります．したがって，$C_i = [x^0]V_i + [x^M]V_i + [x^{2M}]V_i+ \cdots = [x^0]V_i (\mod 1 − x^M)$ です．

xor 畳み込みを高速に行う方法として hadamard 変換が有名です．hadamard 変換を $H$ とすると，$a,b \in S$ に対して以下が成り立ちます．

$$
H(a∗b)_i = H(a)_i \times H(b)_i
$$

上の式を複数回適用することで $H(V)_i = H(v_1)_i \times H(v_2)_i \times \dots \times H(v_N)_i$ となります．ここで $H(v_i)$ の構造について考察してみましょう．

hadamard 行列の $(i,j)$ 成分は $(−1)^{\text{popcount}(i \text{AND} j)}$ です．一つの項のみ $1$ であり，それ以外が $0$ であるような列を hadamard 変換すると，変換後の各項は $1$ または $−1$ になります（例えば $H((0,0,0,1,0,0,0,0))=(1,−1,−1,1,1,−1,−1,1)$）．特に，第 $0$ 項のみが $1$ である列を hadamard 変換すると，変換後はすべての項が $1$ になります．$v_i$ は第 $0$ 項が $1$，第 $A_i$ 項が $x$ であるような列でしたから，$H(v_i)$ の各項は $1+x$ または $1−x$ になることが分かります（例えば $H((1,0,0,x,0,0,0,0))=(1+x,1−x,1−x,1+x,1+x,1−x,1−x,1+x)$)．$H(V)$ は $H(v_1),H(v_2), \dots ,H(v_N)$ の各点積になるので，$H(V)_i$ はある整数 $B_i$ を用いて $(1+x)^{B_i}(1−x)^{N−B_i}$ と表すことができます．

この $B$ は hadamard 変換の定義に従って愚直に計算すると $O(4^L)$ かかりますが，分割統治によって $O(L2^L)$ で計算することができます．あるいは，$A$ に含まれる $i$ の個数を $cnt_i$ とすると $B_i = \dfrac{H(cnt)_i + N}{2}$ が成り立つため，これを利用してもよいです．

$B$ を求めた後は，$[x^0](1+x)^{B_i}(1−x)^{N−B_i}(\mod 1−x^M)$ を求め，それを hadamard 変換することによって $C$ を求めることができます．$[x^0](1+x)^{B_i}(1−x)^{N−B_i}(\mod 1 − x^M)$ は $(1+x)^n,(1−x)^n(\mod 1 − x^M)$ を計算しておくことで全体で $O(NM)$ で求まります．

以上より，この問題を $O(NM+2^L(L+\log ⁡K))$ で解くことができます．

</details><br>

In this explanation, XOR convolution and Hadamard transform will be introduced. Please refer to the [ABC past question](https://atcoder.jp/contests/abc212/tasks/abc212_h) explanation as well.

---

Let $L=20$. Define $C_i$ for $i = 0,1, \dots ,2^L−1$ as "the number of subsequences of $A$ that have a length that is a multiple of $M$ and have a total XOR equal to $i$". The answer can be expressed as $\sum_{i=0}^{2^L-1} C_i$, so it is sufficient to determine $C_0,C_1, \dots ,C_{2^L−1}$.

Let $S$ be the set of sequences of length $2^L$, where each term is a polynomial.

Define $v_i \in S (i=1,2, \dots ,N)$ as follows:

* The 0th term of $v_i$ is 1, the $A_i$-th term is $x$, and all other terms are 0.
  * However, if $A_i = 0$, the 0th term is $1+x$, and all other terms are 0.

Also, define the XOR convolution $a∗b\in S$ for $a,b \in S$ as follows (where $×$ denotes the usual polynomial product):

$$
(a*b)_k = \sum_{i\oplus j = k} a_i \times b_j
$$

Let $V = v_1∗v_2∗ \dots ∗v_N$ be the XOR convolution of the $N$ sequences $v_1,v_2, \dots ,v_N$. Then, the coefficient $([x^j]V_i)$ of $x_j$ in the $i$-th term of $V$ is equal to "the number of subsequences of $A$ of length $j$ with a total XOR equal to $i$". Therefore, $C_i = [x^0]V_i + [x^M]V_i + [x^{2M}]V_i+ \cdots = [x^0]V_i (\mod 1 − x^M)$.

The Hadamard transform is a well-known method for performing XOR convolution quickly. If we denote the Hadamard transform by $H$, the following holds for $a,b \in S$:

$$
H(a∗b)_i = H(a)_i \times H(b)_i
$$

By applying the above equation multiple times, we have $H(V)_i = H(v_1)_i \times H(v_2)_i \times \dots \times H(v_N)_i$. Now, let's consider the structure of $H(v_i)$.

The $(i,j)$ element of the Hadamard matrix is $(−1)^{\text{popcount}(i \text{AND} j)}$. When the Hadamard transform is applied to a sequence with only one term equal to 1 and the others equal to 0, each term after the transformation becomes either 1 or −1 (for example, $H((0,0,0,1,0,0,0,0))=(1,−1,−1,1,1,−1,−1,1)$). In particular, if only the 0th term is 1, after the Hadamard transform, all terms will be 1. Since $v_i$ was a sequence where the 0th term is 1 and the $A_i$-th term is $x$, we can see that each term of $H(v_i)$ becomes $1+x$ or $1−x$ (for example, $H((1,0,0,x,0,0,0,0))=(1+x,1−x,1−x,1+x,1+x,1−x,1−x,1+x)$). Since $H(V)$ is the pointwise product of $H(v_1),H(v_2), \dots ,H(v_N)$, $H(V)_i$ can be expressed as $(1+x)^{B_i}(1−x)^{N−B_i}$ using some integer $B_i$.

Calculating this $B$ directly according to the definition of the Hadamard transform would take $O(4^L)$, but it can be computed in $O(L2^L)$ using divide-and-conquer. Alternatively, if $cnt_i$ denotes the number of $i$ in $A$, then $B_i = \dfrac{H(cnt)_i + N}{2}$ holds, and this can also be utilized.

After determining $B$, $C$ can be obtained by calculating $[x^0](1+x)^{B_i}(1−x)^{N−B_i}(\mod 1−x^M)$ and then performing the Hadamard transform. The computation of $[x^0](1+x)^{B_i}(1−x)^{N−B_i}(\mod 1 − x^M)$ can be done in $O(NM)$ overall by precomputing $(1+x)^n,(1−x)^n(\mod 1 − x^M)$.

Therefore, this problem can be solved in $O(NM+2^L(L+\log ⁡K))$.

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
mod = 998244353


def hadamard(a, m):
    for k in range(m):
        i = 1 << k
        for j in range(1 << m):
            if not i & j:
                a[j], a[i | j] = (a[j] + a[i | j]), (a[j] - a[i | j])


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
L = 20
cnt = [0] * (1 << L)
for i in range(N):
    cnt[A[i]] += 1

F = [[0] * M for i in range(N + 1)]  # (1 + x) ^ n (mod 1 - x ^ M)
G = [[0] * M for i in range(N + 1)]  # (1 - x) ^ n (mod 1 - x ^ M)
F[0][0] = 1
G[0][0] = 1

for i in range(N):
    for j in range(M):
        F[i + 1][j] = (F[i][j] + F[i][j - 1]) % mod
        G[i + 1][j] = (G[i][j] - G[i][j - 1]) % mod

# [x ^ 0] (1 + x) ^ i * (1 - x) ^ (N - i) (mod 1 - x ^ M)
FG = [sum(F[i][j] * G[N - i][-j] for j in range(M)) % mod for i in range(N + 1)]

hadamard(cnt, L)
B = [(cnt[i] + N) // 2 for i in range(1 << L)]
C = [FG[B[i]] for i in range(1 << L)]
hadamard(C, L)

inv = pow(1 << L, mod - 2, mod)
ans = 0
for i in range(1 << L):
    C[i] = C[i] % mod * inv % mod
    ans += C[i] * pow(i, K, mod)
    ans %= mod

print(ans)
```

</details><br>
