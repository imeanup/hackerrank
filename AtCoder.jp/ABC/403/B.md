## [B - Four Hidden](https://atcoder.jp/contests/abc403/tasks/abc403_b)


### 解法1

$T$ の `?` に具体的な `a` から `z` の文字を当てはめて得られる $S$ の候補をすべて探索し，$S$ が $U$ を連続部分文字列として含むか判定すればよいです．

$S$ としてあり得る候補は $26^4=456976$ 個であり，4重の for ループにより高速に列挙することができます．

$S$ が $U$ を連続部分文字列として含むかどうかの判定も2重の for ループにより行えます．$S$ が $U$ を連続部分文字列として含む位置の候補は $∣S∣−∣U∣+1$ 通りあり，それらをすべて全探索して，対応する位置にある文字が一致するかどうか判定すればよいです．

また，言語によっては，連続部分文字列があるか判定する標準機能が実装されている場合があります．C++ の場合は `find` 関数を，Python の場合は `in` 演算子を用いることができます．

[実装例 (C++)](https://atcoder.jp/contests/abc403/submissions/65217735)

[実装例 (Python)](https://atcoder.jp/contests/abc403/submissions/65217678)

### 解法2

$S$ を具体的に決めなくても，2重の for 文のみで問題を解くことができます．

$S$ が $U$ を連続部分文字列として含む位置の候補 $∣S∣−∣U∣+1$ 通りを全探索し，$S$ の $i$ 文字目から $i+∣U∣−1$ 文字目が $U$ に一致しうるか判定します．一致する条件は以下の通りです．

* $j = 1,2, \dots,∣U∣$ について，$T_{i+j}=$ `?` または $T_{i+j}= U_j$

この条件を満たしているとき， $T_{i+j}=$ `?` を $U_j$ で置き換えることで $S_{i+j} = U_j$ とできるので，部分文字列を一致させられます．よってこの条件は十分条件です．

また，ある $j$ について $T_{i+j} \ne $ `?` かつ $T_{i+j} \ne U_j$ ならば，必ず $S_{i+j} \ne U_j$ となり，部分文字列が一致することはありません．よってこの条件は必要条件です．

[実装例 (C++)](https://atcoder.jp/contests/abc403/submissions/65217904)

[実装例 (Python)](https://atcoder.jp/contests/abc403/submissions/65217889)

---

### Solution 1

We can brute-force every possible string $S$ obtained by replacing each `?` in $T$ with one of the letters `a` through `z`, and check whether $U$ appears as a contiguous substring of $S$.

There are $26^4 = 456{,}976$ possible candidates for $S$, which we can efficiently enumerate with four nested loops (one for each `?`).  For each candidate $S$, we check in $O(|S| - |U| + 1)$ time whether $U$ occurs as a substring—either by a double loop comparing characters at each possible alignment, or using your language’s built-in substring search (e.g.\ C++’s `find` or Python’s `in` operator).

This runs easily within the time limits.

- [C++ implementation example](https://atcoder.jp/contests/abc403/submissions/65217735)  
- [Python implementation example](https://atcoder.jp/contests/abc403/submissions/65217678)

---

### Solution 2

We can solve the problem with only two nested loops, without ever constructing all of $S$.

There are $\lvert S\rvert - \lvert U\rvert + 1$ possible starting positions in $S$ where $U$ might match.  Fix a position $i$, and check whether $S_{i+j}$ can match $U_j$ for each $j=1,2,\dots,|U|$.  Since $S$ is formed by replacing each `?` in $T$, the necessary and sufficient condition for a match at offset $j$ is:

- Either $T_{i+j}$ is `?`, or $T_{i+j} = U_j$.

If this holds for all $j$, then we can choose to replace each `?` at $T_{i+j}$ by $U_j$, making $S_{i+j}=U_j$ and hence embedding $U$ as a substring of $S$.  If for some $j$, $T_{i+j}$ is neither `?` nor $U_j$, then no replacement can make $S_{i+j}=U_j$, so the substring cannot match at that position.

Thus, we simply scan all possible $i$ in $O((|T|-|U|+1)\cdot|U|)$ time, checking the above condition.

- [C++ implementation example](https://atcoder.jp/contests/abc403/submissions/65217904)  
- [Python implementation example](https://atcoder.jp/contests/abc403/submissions/65217889)
