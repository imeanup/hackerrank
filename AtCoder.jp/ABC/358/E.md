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

We consider finding the number of strings that satisfy the conditions based on the number of occurrences of the letter 'z' in the string. By summing these counts, we can find the answer. (For the sake of explanation, we are considering the count of 'z', but the same logic applies to any other letter.)

Suppose there are $t$ occurrences of 'z' in a string of length $s$. The number of ways to determine the positions of 'z' is given by $\binom{s}{t}$. For the remaining part of the string, excluding 'z', we consider a string of length $s-t$ without 'z'. For each of the $\binom{s}{t}$ ways, there are strings of length $s-t$ that do not contain 'z' and have between 0 and $C_i$ occurrences of $a_i$.

Therefore, the problem of counting the occurrences of each letter from 'a' to 'z' can be reduced to considering only the letters from 'a' to 'y'.

By applying the same logic, the problem for the letters from 'a' to 'y' can be reduced to the letters from 'a' to 'x', and so on. By repeating this process, we can solve the problem.

When the problem can be reduced to smaller sizes like this, dynamic programming (dp) is often effective.

Let $dp_{i,j}$ be the number of strings of length $j$ that can be formed using the letters $a_1, a_2, \ldots, a_i$ with each letter $a_k$ (for $1 \leq k \leq i$) appearing between 0 and $C_k$ times. From the above discussion, we can derive that $dp_{i+1, j} = \sum_{k=0}^{\min(j, C_{i+1})} dp_{i, j-k} \binom{j}{k}$, where we sum over the number of occurrences $k$ of $a_{i+1}$.

The answer is $\sum_{j=1}^{K} dp_{26, j}$, and it is sufficient to compute the dp values for $j \leq K$.

By precomputing the binomial coefficients using factorials and their inverses, or using Pascal's triangle, this dp can be computed in $O(\sigma K^2)$ time complexity, where $\sigma$ is the number of different letters (which is 26 for this problem). This is efficient given the constraints of the problem.

[Implementation Example](https://atcoder.jp/contests/abc358/submissions/54548837) (C++)
