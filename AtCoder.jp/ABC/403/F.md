## [F - Shortest One Formula](https://atcoder.jp/contests/abc403/tasks/abc403_f)


値がそれぞれ $a, b$ であるような $2$ つの数式 $s, t$ に対して，次のような文字列も数式として有効です．（+ は文字列の結合を表します．）

* `(` + $s$ + `)` （値は $a$）
* $s$ + `+` + $t$ （値は $a+b$）
* $s$ + `*` + $t$ （値は $a\times b$，ただし $s, t$ はともに `<term>` である必要がある）

これらの構成ルールをもとに，値が $N$ になるような最短の数式を dp で求めます．ここで

* $dp_1[i]$ を値が $i$ となる数式のうち，長さが最小のもの
* $dp_2[i]$ を値が $i$ でとなる `<term>` を満たす数式のうち，長さが最小のもの

と定義します．

まず，`1` のみで表現できる値については，次のように初期化できます：

* $dp_1[i] = dp_2[i] =$ `11...1`

遷移は以下の通りです（$\gets$ は，矢印の左辺の数式を，右辺の数式で更新できる場合を表します．すなわち，右辺の方が文字列として短い場合に更新します）：

* $dp_1[i]\gets dp_1[j] + $ `+` $ + dp_1[k](j+k = i)$
* $dp_1[i] \gets dp_2[j] +$ `*` $ + dp_2[k](j \times k = i, j \ne 1, k \ne 1)$
* $dp_2[i] \gets $ `(` $+ dp_1[j] +$ `+` $+ dp_1[k] +$ `)` $(j + k = i)$
* $dp_2[i] \gets dp_2[j] +$ `*` $+ dp_2[k](j \times k = i,j \ne 1,k \ne 1)$

各数式の長さは $O(\log⁡ N)$ であることが証明できるので，この $dp$ は $O(N^2 \log ⁡N)$ で動作します．また，dp で文字列そのものではなく長さの最小値を持つと計算量は $O(N^2)$ になります．



**数式の長さがlogオーダーになることの略証**

---

$N$ を表す数式の長さの最小値を $f(N)$ とします。

* $f(1)=1$ です
* `(n)*(1+1)` で $2n$ を作ることができるため、$f(2n) \le f(n)+8$ です
* `(n)*(1+1)+1` で $2n+1$ を作ることができるため、$f(2n+1) \le f(n)+10$ です

よって以上より、

$
f(N)\le f\left(\left\lfloor \dfrac{N}{2} \right\rfloor\right) + 10 \\ 
\le f\left(\left\lfloor \dfrac{N}{4}\right\rfloor \right) + 20 \\
\le \dots \\
\le 1+10\lceil \log_2 N \rceil = O(\log ⁡N)
$

---

For two valid formulas $s, t$ whose values are $a, b$ respectively, the following strings are also valid formulas. (Here “+” denotes string concatenation.)

- `(` + $s$\, + `)`  
  (value remains $a$)
- $s$\, + `+`\,+ $t$  
  (value is $a + b$)
- $s$\, + `*`\,+ $t$  
  (value is $a \times b$, but both $s$ and $t$ must satisfy the `<term>` grammar)

Using these construction rules, we find by dynamic programming the shortest formula whose value equals $N$. Define

- $\displaystyle dp_1[i]$ = the shortest formula (by string length) whose value is $i$.
- $\displaystyle dp_2[i]$ = the shortest formula whose value is $i$ and which also satisfies `<term>`.

First, any number representable using only the digit `1` can be initialized as:

$$
dp_1[i] = dp_2[i] = \underbrace{\mathtt{11\cdots1}}_{i\text{ times}}
$$

The DP transitions (where “$\gets$” means “update if the right-hand side gives a strictly shorter string”) are:

1. Addition into $dp_1$:
   $$
   dp_1[i] \;\gets\; dp_1[j] \;+\;\text{`+`}\;+\;dp_1[k]
   \quad\bigl(j + k = i\bigr)
   $$
2. Multiplication into $dp_1$:
   $$
   dp_1[i] \;\gets\; dp_2[j] \;+\;\text{`*`}\;+\;dp_2[k]
   \quad\bigl(j \times k = i,\; j\neq1,\; k\neq1\bigr)
   $$
3. Addition into $dp_2$ (with parentheses to form a `<term>`):
   $$
   dp_2[i] \;\gets\; \text{`(`}\;+\;dp_1[j]\;+\;\text{`+`}\;+\;dp_1[k]\;+\;\text{`)`}
   \quad\bigl(j + k = i\bigr)
   $$
4. Multiplication into $dp_2$:
   $$
   dp_2[i] \;\gets\; dp_2[j] \;+\;\text{`*`}\;+\;dp_2[k]
   \quad\bigl(j \times k = i,\; j\neq1,\; k\neq1\bigr)
   $$

Each formula’s length can be shown to be $O(\log N)$. Therefore the above DP runs in $O(N^2 \log N)$, and if you store only the minimum lengths (rather than the full strings), the time becomes $O(N^2)$.

---

### Sketch of why the formula length is $O(\log N)$

Let $f(N)$ be the minimum length of a formula representing $N$.

- Clearly $f(1) = 1$.
- Since you can form $2n$ as `(<formula for n>)*(1+1)`,  
  $$
    f(2n)\;\le\; f(n)\;+\;8.
  $$
- Since you can form $2n+1$ as `(<formula for n>)*(1+1)+1`,  
  $$
    f(2n+1)\;\le\; f(n)\;+\;10.
  $$

Hence, repeatedly halving $N$,

$$
\begin{aligned}
f(N) 
&\le f\!\bigl(\lfloor N/2\rfloor\bigr) + 10\\
&\le f\!\bigl(\lfloor N/4\rfloor\bigr) + 20\\
&\;\;\vdots\\
&\le 1 + 10\lceil \log_2 N\rceil
= O(\log N).
\end{aligned}
$$
