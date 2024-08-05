## [E - Xor Sigma Problem](https://atcoder.jp/contests/abc365/tasks/abc365_e)

<details><summary>Japanese editorial</summary><br>

XOR を扱う問題では、各bit 毎に分けて考えることが有効である場合が多いです。

$j = 0, 1, \dots, 27$ に対して、$A_i$ の $j$ bit 目が $1$ ならば $B_i = 1$ 、$0$ ならば $B_i = 0$ として長さ $N$ の数列 $B$ を定義します。（ここで $j < 27$ なのは $\text{MAX}_A = 10^8 < 2^{27}$ であるからです。）

各 $j$ について、$B$ に対して本問題を解き、答えに $2^j$ を掛けたものの総和が $A$ に対する答えとなります。

このようにすると、$A$ は様々な値を取るのに対し、$B$ は $0$ または $1$ しか取らないため、考えやすくなります。

次に、$\sum_{i=1}^{N-1} \sum_{j=i+1}^{N} (B_i \oplus B_{i+1}\oplus \dots \oplus B_j)$ という形では ある区間の総 XOR が必要とされていますが、これは区間の和を計算する時累積和を使うのと同様に、累積XORを用いることで高速に計算できます。

具体的には、$C_0 = 0, C_i = B_1 \oplus \dots \oplus B_i$ として累積 XOR の配列 $C$ を定めます。

このとき、$B_i \oplus B_{i+1} \oplus \dots \oplus B_j = C_{i-1} \oplus C_j$ という等式が分かります。このことを用いると、計算する対象を以下の形で書くことが出来ます。

$$
\sum_{i=1}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j) = \sum_{i=0}^{N-2} \sum_{j=i+2}^{N} (C_i \oplus C_j)
$$

ここで $j$ の添え字が $i+2$ から始まっている点が厄介です。そのため、以下の方法で添え字が $i+1$ から始まるように変形します。

$$
\begin{align}
\sum_{i=0}^{N-2} \sum_{j=i+2}^{N} (C_i \oplus C_j) & = \sum_{i=0}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j) - \sum_{i=0}^{N-1} (C_i\oplus C_{i+1}) \\
& = \sum_{i=0}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j) - \sum_{i=0}^{N-1} B_i
\end{align}
$$

このとき、$\sum_{i=0}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j)$ の部分は $C$ で値が異なる組の個数と等しいです。これは、$C$ に含まれる $0$ の個数と $C$ に含まれる $1$ の個数の積で求まります。

よって、計算したい値は、$B$ の総和と、累積 XOR により得られる配列の $0, 1$ の個数を使用することで簡単に求められます。以上より、この問題を $O(N\log \text{MAX}_A)$ 時間で解くことができました。

</details><br>

> English

When dealing with problems involving XOR, it is often effective to consider each bit separately.

For $j = 0, 1, \dots, 27$, define a sequence $B$ of length $N$ where $B_i = 1$ if the $j$-th bit of $A_i$ is $1$, and $B_i = 0$ if it is $0$. (Here, $j < 27$ because $\text{MAX}_A = 10^8 < 2^{27}$.)

For each $j$, solve the problem for $B$, and the answer for $A$ will be the sum of the results multiplied by $2^j$.

By doing this, $A$ can take various values, whereas $B$ can only be $0$ or $1$, making the problem easier to handle.

Next, the problem requires the total XOR for some intervals, $\sum_{i=1}^{N-1} \sum_{j=i+1}^{N} (B_i \oplus B_{i+1}\oplus \dots \oplus B_j)$. This can be efficiently calculated using cumulative XOR, similar to how cumulative sums are used for interval sums.

Specifically, define the cumulative XOR array $C$ as $C_0 = 0$ and $C_i = B_1 \oplus \dots \oplus B_i$.

Then, we can see that $B_i \oplus B_{i+1} \oplus \dots \oplus B_j = C_{i-1} \oplus C_j$. Using this, we can rewrite the target sum as follows:

$$
\sum_{i=1}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j) = \sum_{i=0}^{N-2} \sum_{j=i+2}^{N} (C_i \oplus C_j)
$$

Here, the fact that $j$ starts from $i+2$ is troublesome. Therefore, we transform it so that $j$ starts from $i+1$ using the following method:

$$
\begin{align}
\sum_{i=0}^{N-2} \sum_{j=i+2}^{N} (C_i \oplus C_j) & = \sum_{i=0}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j) - \sum_{i=0}^{N-1} (C_i \oplus C_{i+1}) \\
& = \sum_{i=0}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j) - \sum_{i=0}^{N-1} B_i
\end{align}
$$

At this point, the term $\sum_{i=0}^{N-1} \sum_{j = i+1}^{N} (C_i \oplus C_j)$ corresponds to the number of distinct pairs in $C$. This can be determined by the product of the number of $0$'s and $1$'s in $C$.

Therefore, the desired value can be easily calculated using the total sum of $B$ and the count of $0$'s and $1$'s in the cumulative XOR array. Hence, this problem can be solved in $O(N\log \text{MAX}_A)$ time.
