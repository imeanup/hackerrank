## [G - Divisible by 3](https://atcoder.jp/contests/abc370/tasks/abc370_g)

<details><summary><b>Japanese </b></summary><br>

この問題は、乗法的関数の prefix sum を計算するアルゴリズムを利用することで解くことが出来る問題です。

## 乗法的関数とは？

正整数を引数に取る関数 $f(n)$ が次の条件を満たす時、$f(n)$ は **乗法的** であると呼びます。

* 任意の $\gcd(a, b) = 1$ である正整数 $a, b$ に対して $f(ab)=f(a)f(b)$ が成り立つ。

言い換えると、正整数 $n$ が素数 $p_1,p_2,\dots,p_k$ を用いて $n = p_1^{e_1}p_2^{e_2} \dots p_k^{e_k}$ と表せる時、乗法的関数 $f$ について $f(n)$ が $f(p_1^{e_1}),f(p_2^{e_2}),\dots ,f(p_k^{e_k})$ の積として表せる、という解釈が出来ます。

乗法的関数に関する問題としてしばしば登場するものとして prefix sum の計算が挙げられます。すなわち次の問題です。

> #### 乗法的関数の prefix sum
>
> 乗法的関数 $f(n)$ が与えられる。(素数 $p$ に対して $F(p^e)$ は $O(1)$ で計算できると考えてよい。) 次の式を計算せよ。
>
> $$ \sum_{1 \le n \le N} f(n)$$

今回の問題は、実は乗法的関数の prefix sum の計算に帰着させることが出来ます。

はじめにいくつかの事実を確認します。

> #### 事実 1
>
> $\sigma(n)$ を $n$ の約数の総和を返す関数とする。$\sigma(n)$ は乗法的関数である。

この事実は、$n = p_1^{e_1}p_2^{e_2}\dots p_k^{e_k}$ における $\sigma(n)$ が

$$
\sigma(n) = \prod_{i=1}^k (1 + p_i + \dots + p_i^{e_i})
$$

と表せるという公式から従います。

> #### 事実 2
>
> 正整数 $M$ が与えられる。$g(n)$ を総積が $n$ である長さ $M$ の正整数列の個数を返す関数とする。$g(n)$ は乗法的関数である。

この事実は、いくらかの組合せ的解釈により $n = p_1^{e_1}p_2^{e_2}\dots p_k^{e_k}$ において

$$
g(n) = \prod_{i=1}^k {{e_i+M−1}\choose{M−1}}
$$

になることを証明することで確認できます。(証明は練習問題とします, 青~黄 diff 程度)

以上より、今回の問題は次のように言い換えられます。

> #### 今回の問題の言い換え
>
> 乗法的関数 $g(n)$ が与えられる。(素数 $p$ に対して $g(p^e)$ は $O(1)$ で計算できると考えてよい。) 次の式を計算せよ。
>
> $$\sum_{1 \le n \le N , sigma(n) \mod 3 = 0} g(n)$$

この問題内の $\sigma(n) \mod 3 = 0$ の部分を取り除くと乗法的関数の prefix sum を計算する問題となります。この部分を上手く取り除いてみましょう。

乗法的関数 $h(n)$ を素数 $p$ に対して次式が成り立つように置きます。

$$
h(pe) = \begin{cases} 0 & \sigma(p^e) \mod 3 = 0 \\ g(p^e) & \text{ otherwise} \end{cases}
$$

すると、 $\sigma(n)$ の乗法性により次式が成り立ちます。

$$
h(n)= \begin{cases} 0 & \sigma(n) \mod 3 = 0 \\ g(n) & \sigma(n) \mod 3 \ne 0\end{cases}
$$

よって、今回の問題は次のように言い換えられます。

> #### 今回の問題の言い換え(2)
>
> 乗法的関数 $g(n),h(n)$ が与えられる。(素数 $p$ に対して $g(p^e),h(p^e)$ は $O(1)$ で計算できると考えてよい。) 次の式を計算せよ。
>
> $$\sum_{n=1}^N (g(n) − h(n))$$

もちろん上式は

$$ \sum_{n=1}^N g(n) − \sum_{n=1}^N h(n)$$

と変形できるため、$g(n)$ の prefix sum から $h(n)$ の prefix sum を引いたものを計算できればよいです。
以上より今回の問題を乗法的関数の prefix sum を計算する問題に帰着させることが出来ました。

乗法的関数の prefix sum の計算方法はいくつかありますが、ここでは

* **Lucy DP** , および
* **black algorithm** あるいは **Min_25 篩**

と呼ばれるアルゴリズムを利用した解法を説明します。

<details><summary><b> Lucy DP </b></summary> <br>

以降では乗法的関数 $f(n)$ の $1 \le n \le N$ における prefix sum を考えます。また、関数 $F(n),F_{prime}(n)$ と整数集合 $Q_n$ を次のように定義します。

$$
\begin{align*}
F(n) &= \sum_{1 \le m \le n} f(m) \\

F_{\text{prime}}(n) &= \sum_{1 \le p \le n , p : \text{prime}} f(p) \\

Q_n &= \left\{ m : m = \left\lfloor \dfrac{n}{k} \right\rfloor を満たす正整数 k が存在する \right\}
\end{align*}
$$

乗法的関数の prefix sum を 2 つのステップに分けて計算することにします。

1. $F_{\text{prime}}(n)$ を $n \in Q_n$ において全て計算する
2. $F_{\text{prime}}(n)$ を用いて $F(n)$ を計算する

1 番目のステップとして Lucy DP と呼ばれる DP が、$2$ 番目のステップとして black algorithm あるいは Min_25 篩が登場します。

まずは Lucy DP の説明をします。Lucy DP は [Project Euler: Problem 10](https://projecteuler.net/problem=10) のスレッド(AC すると見られます) にある Lucy_Hedgehog 氏の投稿に由来する DP です。

簡単のため $p$ が素数の場合に $f(p) = 1$ が成り立つ場合を例にとって説明します。この時、$F_{\text{prime}}(n)$ は素数計数関数 $\pi(n)$ と一致するので、ここでは $\pi(n)$ の計算方法として説明します。

$1 \le x \le \lfloor \sqrt{N} \rfloor,n \in Q_N$ の範囲において $S(x,n)$ を次のように定義します。

* $S(x,n) : 2$ 以上 $n$ 以下の整数のうち、エラトステネスの篩のアルゴリズムにおいて $x$ 以下の素数では篩われなかった整数の個数

$\pi(n) = S(\lfloor \sqrt{N} \rfloor, n)$ が成り立つので、$S(\lfloor \sqrt{N} \rfloor, ∗)$ を全て計算できればよいです。

DP の遷移として、$S(x,n)$ を $S(x−1, ∗)$ を用いて表すことを考えます。

* $x$ が素数でない場合

$x$ において篩う処理が発生しないので $S(x,n)=S(x−1,n)$ となります。

* $x$ が素数であり、$n < x^2$ の場合

$n$ 以下の $x$ の倍数はすでに篩われています。よってこちらも $S(x,n) = S(x−1, n)$ となります。

* $x$ が素数であり $n \le x^2$ の場合

$x$ で篩われる数を $mx$ と表すと、$M$ のなす集合は「$x−1$ 以下の素数で篩われなかった数の集合」から「$x−1$ 以下の素数の集合」を除いたものになります。よって

$$
S(x,n) = S(x−1,n)−(S(x−1,\left\lfloor \dfrac{n}{x} \right \rfloor ) − \pi(x−1))
$$

であり、$\pi(x−1) = S(x−1,x−1)$ に注意すると

$$
S(x,n)=S(x−1,n) + S(x−1,\left\lfloor \dfrac{n}{x} \right \rfloor ) +S(x−1,x−1)
$$

が成り立ちます。以上より次式が成り立ちます。

$$
S(x,n) = \begin{cases} S(x−1,n)+S(x−1,\left \lfloor \dfrac{n}{x} \right \rfloor) + S(x−1,x−1) & (x \text{ is prime}) \land x^2 \le n \\
S(x−1, n) & \text{ otherwise} \end{cases}
$$

この DP は $n$ のみを添え字に持って in-place に更新していくことができます。

* Python による $\pi(N)$ を計算する関数の実装例

```py
import math
def Pi(N):
    sqrtN = math.isqrt(N)
    Q = [N // i for i in range(1, sqrtN + 1)]
    Q += list(range(Q[-1] - 1, 0, -1))
    S = {i: i - 1 for i in Q}
    for x in range(2, sqrtN + 1):
        if S[x] > S[x - 1]:
            for n in Q:
                if n < x * x: break
                S[n] -= S[n // x] - S[x - 1]
    return S[N]
```

DP の計算量を考えます。まず、[ABC239Ex 解説](https://atcoder.jp/contests/abc239/editorial/3357) の観察 1, 2, 3 を認めるものとします。例えば $∣Q_N∣ = O(\sqrt{N})$ です。
さて、計算量は `S(v) -= S[v // p] - S[p - 1]`の行が呼び出される回数を考えればよいです。$x$ と $N^{\frac{1}{4}}$ の大小で場合分けして考えます。

* $2 \le x \le N^{\frac{1}{4}}$ のとき

素数は素数定理より $O\left( \dfrac{ N^{\frac{1}{4}} }{ \log⁡ N } \right)$ 個あり、DP テーブルのサイズは $O(\sqrt{N})$ なので合計 $O\left( \dfrac{ N^{\frac{3}{4}} }{ \log⁡ N } \right)$ 回になります。

* $N^{\frac{1}{4}} \le x \le \sqrt{x}$  のとき

各 $x$ について $x^2 \le n \le N$ を満たす部分を更新しますが、$\sqrt{N} \le x^2$ より更新する個数は $O\left(\dfrac{N}{x^2}\right)$ となるのがわかります。よって素数定理と合わせると $O\left( \dfrac{1}{\log⁡ N} \sum_{x = N^{1/4}}^{\sqrt{N}} \dfrac{N}{x^2}\right) = O\left(\dfrac{N^{\frac{3}{4}}}{\log ⁡N} \right)$ 回であることがわかります。

以上より全体の計算量は $O\left(\dfrac{N^{\frac{3}{4}}}{\log ⁡N} \right)$ になります。

ここでは $\pi(n)$ を用いて説明しましたが、このアルゴリズムは他の乗法的関数における $F_{\text{prime}}(n)$ の列挙にも適用することが出来ます。
今回の問題で登場する $g,h$ の素数 $p$ における振る舞いは次の通りです。

$$
\begin{align*}
g(p) &= M \\

h(p) &= \begin{cases} 0 & p \mod 3 = 2 \\
M & \text{otherwise} \end{cases}
\end{align*}
$$

です。$g(p)$ の場合は定数なので $\pi(n)$ を列挙した後に $M$ 倍すれば所望のものを得られます。$h(p)$ の場合は少し難しいですが、$3$ で割って $1$ 余る素数の個数と $2$ 余る素数の個数を Lucy DP で求めることを考えれば所望のものを計算できます。(詳細は略します)

</details><br>

<details><summary><b> black algorithm </b></summary><br>

Lucy DP を用いて $F_{\text{prime}}(n)$ を $n \in Q_N$ において列挙することができました。これらを用いて $F(n)$ を計算するアルゴリズムである black algorithm の概要を説明します。

* [考案者による記事](https://baihacker.github.io/main/2020/The_prefix-sum_of_multiplicative_function_the_black_algorithm.html) にも書かれているように、black algorithm は平易なアルゴリズムである点が特長です。

まず、以下の条件を満たす $n$ 頂点の根付き木を考えます。ここで、$n \ge 2$ に対して $n$ の素因数のうち最大のものを $\rm gpf(n)$ と表します。

* 頂点に $1$ から $n$ までの番号がついている。
* 頂点 $1$ は根であり、頂点 $n \ (n \ge 2)$ の親は $\dfrac{n}{\rm gpf(n)}$ である。

例えば $N = 16$ における木は次の通りです。(葉の頂点を丸で、葉でない頂点を四角で囲っている。また、頂点 $n \ (n \ge 2)$ とその親を結ぶ辺を $\rm gpf(n)$ と対応させた色で塗っている。)

![image](https://img.atcoder.jp/abc370/f8d1f7da34893945f8089ffb9943ae39.png)

この木の特徴として、頂点 $n$ から頂点 $1$ までのパスに $n$ の素因数に対応する辺が素因数の大きい順に並んでいるという点があります。よって、現在の $f(n)$ の値を持ちながらこの木の上を適切に DFS することで $f(1),f(2),\dots ,f(N)$ を $O(N)$ で列挙することが出来ます。そのため prefix sum も $O(N)$ で求められますが、これは低速です。

この DFS アルゴリズムを $F_{\text{prime}}(n)$ を用いて高速化してみましょう。今、葉でない頂点 $n$ にいて、$f(n)$ がわかっているとします。ここで、

* $k$ 番目に小さい素数を $p_k$,
* $p_i = \text{gpf}(n)$,
* $p_j$ を $\dfrac{N}{n}$ 以下の最大の素数

とすると、$n$ の子の頂点を小さい順に並べた列は $np_i,np_{i+1}, \dots,np_j$ のように表せます。そこで、$f(np_i),f(np_{i+1}), \dots ,f(np_j)$ をまとめて足し上げることを考えます。$np_i$ は特殊処理するとして、$p_{i+1}, \dots ,p_j$ は全て $n$ と互いに素なので、$f$ の乗法性を利用すると

$$
\begin{align*}
\sum_{k = i+1}^j f(np_k) &= f(n) \sum_{k=i+1}^j f(p_k) \\ 
&= f(n) \left( F_{\text{prime}}\left( \left\lfloor \dfrac{N}{n} \right\rfloor \right) − F_{\text{prime}}(p_i) \right)
\end{align*}
$$

となり、総和が $F_{\text{prime}}(n)$ を用いて高速に計算できます。この式を利用して、「ある頂点 $n$ に移動するたびに、その頂点の子の $f$ を足し上げる」という操作を行うことにすれば、DFS において葉の頂点に移動する必要が無くなります。(例えば $N=16$ の例だと、$n = 1,2,3,4,8$ 以外の頂点に訪問する必要が無くなります。)

以上の内容を適切に実装することで、$F(n)$ を $O(根付き木の葉でない頂点の個数)$ で計算することが出来ます。具体的に計算量を式として表すと $O(N^{1−\varepsilon})$ ($O(N)$ かつ、任意の $\varepsilon > 0$ に対して $\Omega(N^{1− \varepsilon})$ が成り立つ、の意) になりますが、実際に葉でない頂点の個数を数えてみると $N = 10^{10}$ で $6298637 \simeq 6.3×10^6$ 個と十分少ないため定数倍が非常に軽いことが確認できます。(black algorithm は競技プログラミングにおいて出題される $N \le 10^{12}$ 程度の制約においては十分高速に動作します。)

black algorithm は以上のように平明なアルゴリズムですが、計算量が $O(N^{1− \varepsilon})$ である欠点もあります。そこで別解として Min_25 篩と呼ばれるアルゴリズムも紹介します。

</details><br>

<details><summary><b> Min_25 篩 </b></summary><br>

Min_25 篩とは Min_25 氏によって考案されたアルゴリズムです。Min_25 篩は black algorithm と異なり $O(N^{\frac{2}{3}})$ という $o(N)$ の計算量評価が得られているアルゴリズムです。

また、black algorithm が $F(n)$ のみを計算するのに対して、Min_25 篩は $n \in Q_N$ に対して $F(n)$ の計算結果が得られるという副産物もあります。

ただし、本来の Min_25 篩のアルゴリズムはかなり複雑なので、ここでは簡略化した $O\left(\dfrac{N^{\frac{3}{4}}}{\log ⁡N} \right)$ のアルゴリズムを説明します。

直感的に説明すると、Min_25 篩は Lucy DP の逆をするアルゴリズムです。
$1 \le x \le \lfloor \sqrt{N} \rfloor,n \in Q_N$ の範囲において $S(x,n)$ を次のように定義します。

* $S(x,n) : 2$ 以上 $n$ 以下の整数のうち、エラトステネスの篩のアルゴリズムにおいて $x$ 以下の素数では篩われなかった整数に対する $f(n)$ の総和

すると、明らかに $S(\lfloor \sqrt{N} \rfloor, n ) = F_{\text{prime}}(n)$ であり、求めたいものは $S(1,N)+1$ です。よって、Lucy DP と逆方向に、すなわち $S(\lfloor N \rfloor, ∗)$ から始めて第 1 添え字が小さくなる方向に計算していくことを考えます。

Lucy DP と同様に $S(x,n)$ と $S(x−1,n)$ の差分を考えてみましょう。

* $x$ が素数でない場合

Lucy DP と同様 $S(x,n) = S(x−1,n)$ です。

* $x$ が素数であり、かつ $n < x^2$ である場合

Lucy DP と同様 $S(x,n) = S(x−1,n)$ です。

* $x$ が素数であり、かつ $n \ge x^2$ である場合

$x$ において篩われる数は $x^c m$ ($m$ は $x$ より大きい素数の積で表せる整数) という形をしています。$c$ の値を固定して考えると、$m$ としてあり得るものは

* 『$\dfrac{n}{x^c}$ 以下の「$x$ 以下の素数で篩ったときに残った整数」』の集合から
* 「$x$ 以下の素数」の集合を取り除き、
* さらに $c \ge 2$ の場合は $1$ を加えたもの

になります。この事実を元に立式して整理すると、結局次の式を手に入れられます。

$$
S(x−1,n) = S(x,n) + \sum_{1 \le c, x^{c+1} \le n} f(x^c) \left(S\left(x,\left \lfloor \dfrac{n}{x^c} \right \rfloor \right) − F_{\text{prime}}(x)\right)+f(x^{c+1})
$$

上記の式を元に漸化式を計算すればよく、これは Lucy DP と同様に in-place な DP として高速化できます。計算量もまた Lucy DP と同様の方法で評価できて $O\left(\dfrac{N^{\frac{3}{4}}}{\log ⁡N} \right)$ になります。

また、このアルゴリズムおよび Lucy DP の両方を Fenwick tree を用いて高速化することで $O({N^{\frac{3}{4}}})$ に計算量を落とすことができて、高速化を施したアルゴリズムが本来の Min_25 篩です。(詳細は筆者も知りません…)

以上に説明したアルゴリズム、すなわち Lucy DP および (black algorithm あるいは Min_25 篩) を実装することで $g(n),h(n)$ の prefix sum を計算することができるので今回の問題を解けます。計算量は $O\left(\dfrac{N^{\frac{3}{4}}}{\log ⁡N} \right)$ あるいは定数倍の軽い $O(N^{1− \varepsilon})$ で十分高速です。

* [簡略化した Min_25 篩を用いた実装例(Python)](https://atcoder.jp/contests/abc370/submissions/57434000)

</details><br>

<details><summary><b> 発展的話題: より計算量が良いアルゴリズム </b></summary><br>

本記事では乗法的関数の prefix sum を計算するアルゴリズムとして black algorithm と Min_25 篩を説明しましたが、乗法的関数の prefix sum を計算するアルゴリズムは他にも存在します。特に、中国の競技プログラミング界隈においては研究が盛んな分野で、様々なアルゴリズムが発明されています。
計算量の上では、 zhoukangyang 氏が 2023 年に発表した $\tilde{O}(\sqrt{N})$ のアルゴリズムが最速となっています。([ブログ](https://www.cnblogs.com/zkyJuruo/p/17544928.html), [論文](https://github.com/enkerewpo/OI-Public-Library/blob/master/IOI%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%80%99%E9%80%89%E9%98%9F%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2024%E8%AE%BA%E6%96%87%E9%9B%86.pdf)) また、競技プログラミングでの実用上の最速は朱震霆氏の計算量 $\Theta\left(\dfrac{N^{\frac{3}{4}}}{(\log ⁡N)^{\frac{4}{3}}} \right)$ のアルゴリズムであるようです。
また、乗法的関数が特定の条件を満たす場合は杜教篩や PowerfulNumber 篩と呼ばれるアルゴリズムを適用できます。
このように、乗法的関数の prefix sum は様々な人がアルゴリズムを提案しているので、興味がある方は調べてみると面白いと思います。

参考文献

* [Library Checker : Problem proposal (Sum of Multiplicative Function)](https://github.com/yosupo06/library-checker-problems/issues/1118) : 乗法的関数の prefix sum に関する先行研究がまとまっている。
* [OI-Wiki](https://oi-wiki.org/math/number-theory/min-25/) : 杜教篩, PowerfulNumber 篩などの解説がある。


</details><br>


</details><br>


This problem can be solved using algorithms that calculate the prefix sum of a multiplicative function.

## What is a Multiplicative Function?

A function $f(n)$ that takes a positive integer as an argument is called **multiplicative** if it satisfies the following condition:

- For any pair of integers $a, b$ where $\gcd(a, b) = 1$, the relation $f(ab) = f(a)f(b)$ holds.

In other words, if a positive integer $n$ can be represented as $n = p_1^{e_1} p_2^{e_2} \dots p_k^{e_k}$ using primes $p_1, p_2, \dots, p_k$, then for a multiplicative function $f$, $f(n)$ can be interpreted as the product of $f(p_1^{e_1}), f(p_2^{e_2}), \dots, f(p_k^{e_k})$.

One common problem involving multiplicative functions is the calculation of the prefix sum, which can be framed as follows:

> #### Prefix Sum of a Multiplicative Function
>
> Given a multiplicative function $f(n)$, (and assume that $F(p^e)$ for any prime $p$ can be computed in $O(1)$), calculate the following sum:
>
> $$ \sum_{1 \le n \le N} f(n) $$

This current problem can actually be reduced to the calculation of the prefix sum of a multiplicative function.

Let’s first review a few facts.

> #### Fact 1
>
> Let $\sigma(n)$ be the function that returns the sum of the divisors of $n$. $\sigma(n)$ is a multiplicative function.

This fact follows from the formula for $\sigma(n)$, where if $n = p_1^{e_1} p_2^{e_2} \dots p_k^{e_k}$, then:

$$
\sigma(n) = \prod_{i=1}^k (1 + p_i + \dots + p_i^{e_i})
$$

> #### Fact 2
>
> Given a positive integer $M$, let $g(n)$ be the function that returns the number of sequences of length $M$ whose product is $n$. $g(n)$ is a multiplicative function.

This can be confirmed by proving that if $n = p_1^{e_1} p_2^{e_2} \dots p_k^{e_k}$, then:

$$
g(n) = \prod_{i=1}^k {{e_i + M - 1} \choose {M - 1}}
$$

(The proof is left as an exercise.)

Thus, this problem can be rephrased as follows:

> #### Rephrased Problem
>
> Given a multiplicative function $g(n)$ (where $g(p^e)$ for any prime $p$ can be computed in $O(1)$), calculate the following sum:
>
> $$ \sum_{1 \le n \le N , \sigma(n) \mod 3 = 0} g(n) $$

If we remove the part about $\sigma(n) \mod 3 = 0$, this becomes a problem of calculating the prefix sum of a multiplicative function. Let’s see how to handle this part effectively.

Define another multiplicative function $h(n)$, such that for any prime $p$, the following holds:

$$
h(p^e) = \begin{cases} 0 & \sigma(p^e) \mod 3 = 0 \\ g(p^e) & \text{otherwise} \end{cases}
$$

Then, due to the multiplicativity of $\sigma(n)$, we have:

$$
h(n) = \begin{cases} 0 & \sigma(n) \mod 3 = 0 \\ g(n) & \sigma(n) \mod 3 \ne 0 \end{cases}
$$

Thus, the problem can now be rephrased as:

> #### Rephrased Problem (2)
>
> Given two multiplicative functions $g(n)$ and $h(n)$ (where $g(p^e)$ and $h(p^e)$ for any prime $p$ can be computed in $O(1)$), calculate the following sum:
>
> $$ \sum_{n=1}^N (g(n) − h(n)) $$

Of course, this can be rewritten as:

$$ \sum_{n=1}^N g(n) − \sum_{n=1}^N h(n) $$

Thus, it suffices to compute the prefix sum for $g(n)$ and subtract the prefix sum for $h(n)$.

Now that we have reduced the problem to calculating the prefix sum of multiplicative functions, let’s explore methods for doing so.

Several algorithms can compute the prefix sum of multiplicative functions. Here, we will explain solutions using:

- **Lucy DP**, and
- **black algorithm** or **Min_25 sieve**.

## Lucy DP

Below, we will consider the prefix sum of a multiplicative function $f(n)$ for $1 \leq n \leq N$. We also define functions $F(n), F_{\text{prime}}(n)$, and the integer set $Q_n$ as follows:

$$
\begin{align*}
F(n) &= \sum_{1 \leq m \leq n} f(m) \\

F_{\text{prime}}(n) &= \sum_{1 \leq p \leq n , p : \text{prime}} f(p) \\

Q_n &= \left\{ m : m = \left\lfloor \frac{n}{k} \right\rfloor \text{ where a positive integer } k \text{ exists} \right\}
\end{align*}
$$

We will compute the prefix sum of the multiplicative function in two steps:

1. Calculate $F_{\text{prime}}(n)$ for all $n \in Q_n$.
2. Use $F_{\text{prime}}(n)$ to compute $F(n)$.

In the first step, a DP method called "Lucy DP" is used, while in the second step, methods such as the "black algorithm" or the "Min_25 sieve" are employed.

Let’s start by explaining Lucy DP. This DP method originates from a post by Lucy_Hedgehog in the thread for [Project Euler: Problem 10](https://projecteuler.net/problem=10) (visible upon solving the problem).

For simplicity, we will explain the case where $f(p) = 1$ for prime numbers $p$. In this case, $F_{\text{prime}}(n)$ matches the prime-counting function $\pi(n)$, so we will describe the calculation of $\pi(n)$ here.

For $1 \leq x \leq \lfloor \sqrt{N} \rfloor$ and $n \in Q_N$, we define $S(x, n)$ as follows:

* $S(x, n)$: The number of integers between 2 and $n$ that are not divisible by any prime number less than or equal to $x$, following the sieve of Eratosthenes.

Since $\pi(n) = S(\lfloor \sqrt{N} \rfloor, n)$, it suffices to compute $S(\lfloor \sqrt{N} \rfloor, \ast)$.

The transition of the DP expresses $S(x, n)$ using $S(x-1, \ast)$ as follows:

* If $x$ is not prime:
  * No sieving occurs at $x$, so $S(x, n) = S(x-1, n)$.

* If $x$ is prime and $n < x^2$:
  * All multiples of $x$ up to $n$ have already been sieved. Thus, $S(x, n) = S(x-1, n)$.

* If $x$ is prime and $n \geq x^2$:
  * Let the multiples of $x$ be denoted by $mx$. The set of $M$ is the set of numbers not sieved by primes less than $x-1$, minus the set of primes up to $x-1$. Thus, we have:
  
  $$
  S(x, n) = S(x-1, n) - \left( S(x-1, \left\lfloor \frac{n}{x} \right\rfloor ) - \pi(x-1) \right)
  $$

  Noting that $\pi(x-1) = S(x-1, x-1)$, we get:

  $$
  S(x, n) = S(x-1, n) + S(x-1, \left\lfloor \frac{n}{x} \right\rfloor) + S(x-1, x-1)
  $$

Thus, we arrive at the following expression:

$$
S(x, n) = \begin{cases} 
S(x-1, n) + S(x-1, \left\lfloor \frac{n}{x} \right\rfloor) + S(x-1, x-1) & (\text{if } x \text{ is prime}) \land x^2 \leq n \\
S(x-1, n) & \text{otherwise} 
\end{cases}
$$

This DP can be updated in-place using only $n$ as the index.

* Example implementation of a function to calculate $\pi(N)$ in Python:

```py
import math
def Pi(N):
    sqrtN = math.isqrt(N)
    Q = [N // i for i in range(1, sqrtN + 1)]
    Q += list(range(Q[-1] - 1, 0, -1))
    S = {i: i - 1 for i in Q}
    for x in range(2, sqrtN + 1):
        if S[x] > S[x - 1]:
            for n in Q:
                if n < x * x: break
                S[n] -= S[n // x] - S[x - 1]
    return S[N]
```

Let's consider the time complexity of the DP. First, let's assume Observations 1, 2, and 3 from the [ABC239Ex editorial](https://atcoder.jp/contests/abc239/editorial/3357) are valid. For example, $|Q_N| = O(\sqrt{N})$.

Now, we need to consider the number of times the line `S(v) -= S[v // p] - S[p - 1]` is called. We will split the analysis based on the comparison between $x$ and $N^{\frac{1}{4}}$.

* When $2 \leq x \leq N^{\frac{1}{4}}$:
  The number of primes is $O\left( \dfrac{N^{\frac{1}{4}}}{\log N} \right)$ due to the prime number theorem, and the size of the DP table is $O(\sqrt{N})$, so the total number of calls is $O\left( \dfrac{N^{\frac{3}{4}}}{\log N} \right)$.

* When $N^{\frac{1}{4}} \leq x \leq \sqrt{x}$:
  For each $x$, we update the range $x^2 \leq n \leq N$, but since $\sqrt{N} \leq x^2$, the number of updates is $O\left( \dfrac{N}{x^2} \right)$. Combining this with the prime number theorem, the total number of calls is $O\left( \dfrac{1}{\log N} \sum_{x = N^{1/4}}^{\sqrt{N}} \dfrac{N}{x^2} \right) = O\left( \dfrac{N^{\frac{3}{4}}}{\log N} \right)$.

Thus, the overall time complexity is $O\left( \dfrac{N^{\frac{3}{4}}}{\log N} \right)$.

Although we used $\pi(n)$ as an example here, this algorithm can also be applied to enumerate $F_{\text{prime}}(n)$ for other multiplicative functions. The behavior of the primes $p$ for the functions $g$ and $h$ in this problem is as follows:

$$
\begin{align*}
g(p) &= M \\

h(p) &= \begin{cases} 
0 & p \mod 3 = 2 \\
M & \text{otherwise} 
\end{cases}
\end{align*}
$$

In the case of $g(p)$, it is constant, so after enumerating $\pi(n)$, you can multiply by $M$ to obtain the desired result. For $h(p)$, it's a bit more complex, but if you think of calculating the number of primes congruent to 1 modulo 3 and those congruent to 2 modulo 3 using Lucy DP, you can compute the desired values (details omitted).

## Black Algorithm

Using Lucy DP, we can enumerate $F_{\text{prime}}(n)$ for all $n \in Q_N$. Here, I'll outline the Black Algorithm, which uses these values to calculate $F(n)$.

* As mentioned in the [author's article](https://baihacker.github.io/main/2020/The_prefix-sum_of_multiplicative_function_the_black_algorithm.html), the Black Algorithm is characterized by its simplicity.

First, consider a rooted tree with $n$ vertices that satisfies the following conditions. For $n \geq 2$, let $\text{gpf}(n)$ represent the greatest prime factor of $n$.

* Each vertex is numbered from 1 to $n$.
* Vertex 1 is the root, and for any $n \geq 2$, the parent of vertex $n$ is $\frac{n}{\text{gpf}(n)}$.

For example, here is the tree when $N = 16$. (Leaf vertices are represented by circles, non-leaf vertices by squares, and edges connecting vertex $n$ and its parent are colored according to $\text{gpf}(n)$.)

![image](https://img.atcoder.jp/abc370/f8d1f7da34893945f8089ffb9943ae39.png)

A key feature of this tree is that the path from vertex $n$ to vertex 1 contains edges corresponding to the prime factors of $n$, arranged in decreasing order. Therefore, by performing an appropriate DFS on this tree while keeping track of the current value of $f(n)$, you can enumerate $f(1), f(2), \dots, f(N)$ in $O(N)$ time. This allows you to compute the prefix sum in $O(N)$, but this is slow.

Now, let's speed up this DFS algorithm using $F_{\text{prime}}(n)$. Suppose you are at a non-leaf vertex $n$ and know $f(n)$. Let:

* $p_k$ be the $k$-th smallest prime,
* $p_i = \text{gpf}(n)$,
* $p_j$ be the largest prime less than or equal to $\frac{N}{n}$.

Then, the child vertices of $n$, listed in increasing order, can be expressed as $np_i, np_{i+1}, \dots, np_j$. Now, consider summing $f(np_i), f(np_{i+1}), \dots, f(np_j)$. For $np_i$, you handle it with special processing, but for $p_{i+1}, \dots, p_j$, all are coprime with $n$, so using the multiplicativity of $f$, we get:

$$
\sum_{k = i+1}^j f(np_k) = f(n) \sum_{k=i+1}^j f(p_k) = f(n) \left( F_{\text{prime}}\left( \left\lfloor \frac{N}{n} \right\rfloor \right) - F_{\text{prime}}(p_i) \right)
$$

This allows you to quickly calculate the sum using $F_{\text{prime}}(n)$. By performing this operation each time you move to a vertex $n$, summing the values of its child vertices' $f$ values, you eliminate the need to visit the leaf vertices during DFS. (For example, in the $N = 16$ case, you no longer need to visit vertices other than 1, 2, 3, 4, and 8.)

By implementing this correctly, you can compute $F(n)$ in $O(\text{number of non-leaf vertices in the tree})$. In terms of time complexity, this is $O(N^{1 - \varepsilon})$, meaning it’s $O(N)$ but for any $\varepsilon > 0$, $\Omega(N^{1 - \varepsilon})$ holds. In practice, when you count the non-leaf vertices, for $N = 10^{10}$, there are 6,298,637 vertices, which is small enough that the constant factor is very light. (The Black Algorithm works efficiently for typical competitive programming constraints of $N \leq 10^{12}$.)

Though the Black Algorithm is simple, it has the drawback of having a time complexity of $O(N^{1 - \varepsilon})$. As an alternative, the Min_25 sieve algorithm is also introduced.

## Min_25 Sieve

The Min_25 sieve is an algorithm devised by Min_25. Unlike the black algorithm, the Min_25 sieve achieves a time complexity of $O(N^{\frac{2}{3}})$, which is $o(N)$.

Additionally, while the black algorithm only calculates $F(n)$, the Min_25 sieve also provides the results for $F(n)$ for all $n \in Q_N$ as a byproduct.

However, the original Min_25 sieve algorithm is quite complex, so here I will explain a simplified version of the algorithm with a time complexity of $O\left(\frac{N^{\frac{3}{4}}}{\log N}\right)$.

To intuitively explain, the Min_25 sieve is essentially the reverse of Lucy DP. For $1 \leq x \leq \lfloor \sqrt{N} \rfloor$ and $n \in Q_N$, define $S(x, n)$ as follows:

* $S(x, n)$: The sum of $f(n)$ for integers between 2 and $n$ that were not sieved out by primes less than or equal to $x$ in the Sieve of Eratosthenes.

Clearly, $S(\lfloor \sqrt{N} \rfloor, n) = F_{\text{prime}}(n)$, and what we want is $S(1, N) + 1$. Thus, we calculate starting from $S(\lfloor N \rfloor, ∗)$ and reduce the first index as we go, effectively working in reverse compared to Lucy DP.

Let's now consider the difference between $S(x, n)$ and $S(x-1, n)$, similar to Lucy DP.

* When $x$ is not a prime:  
  $S(x, n) = S(x-1, n)$, same as Lucy DP.

* When $x$ is a prime and $n < x^2$:  
  $S(x, n) = S(x-1, n)$, same as Lucy DP.

* When $x$ is a prime and $n \geq x^2$:  
  The numbers sieved out by $x$ are of the form $x^c m$, where $m$ is an integer represented by the product of primes greater than $x$. Fixing the value of $c$, the possible values of $m$ are:

  * From the set of numbers less than or equal to $\frac{n}{x^c}$ that remained after sieving with primes less than or equal to $x$,
  * Removing the set of primes less than or equal to $x$,
  * Adding 1 if $c \geq 2$.

Based on this, we can derive the following equation:

$$
S(x-1, n) = S(x, n) + \sum_{1 \leq c, x^{c+1} \leq n} f(x^c) \left(S\left(x, \left\lfloor \frac{n}{x^c} \right\rfloor \right) - F_{\text{prime}}(x)\right) + f(x^{c+1})
$$

By calculating this recurrence relation, you can efficiently compute it using in-place DP, similar to Lucy DP. The time complexity is also evaluated in the same way, yielding $O\left(\frac{N^{\frac{3}{4}}}{\log N}\right)$.

Furthermore, by using a Fenwick tree to speed up both this algorithm and Lucy DP, you can reduce the time complexity to $O(N^{\frac{3}{4}})$. The optimized algorithm is the original Min_25 sieve (the author admits they are not fully familiar with the details...).

By implementing the algorithms explained above, namely Lucy DP and (either the black algorithm or the Min_25 sieve), you can compute the prefix sum for $g(n)$ and $h(n)$, thus solving the problem. The time complexity is $O\left(\frac{N^{\frac{3}{4}}}{\log N}\right)$ or a light constant factor $O(N^{1 - \varepsilon})$, which is sufficiently fast.

* [An implementation example using the simplified Min_25 sieve (Python)](https://atcoder.jp/contests/abc370/submissions/57434000)

### Advanced Topic: More Efficient Algorithms

In this article, we explained algorithms like the black algorithm and the Min_25 sieve for calculating the prefix sum of multiplicative functions. However, there are other algorithms available for this task. In particular, this is an area of active research in the competitive programming community in China, where various algorithms have been invented.

In terms of computational complexity, the fastest algorithm was introduced by zhoukangyang in 2023, achieving a complexity of $\tilde{O}(\sqrt{N})$ ([Blog](https://www.cnblogs.com/zkyJuruo/p/17544928.html), [Paper](https://github.com/enkerewpo/OI-Public-Library/blob/master/IOI%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%80%99%E9%80%89%E9%98%9F%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2024%E8%AE%BA%E6%96%87%E9%9B%86.pdf)).

For practical purposes in competitive programming, the fastest known algorithm is by Zhu Zhenting, with a time complexity of $\Theta\left(\dfrac{N^{\frac{3}{4}}}{(\log N)^{\frac{4}{3}}} \right)$.

Additionally, if the multiplicative function meets certain conditions, algorithms like the Du Jiao sieve or the PowerfulNumber sieve can be applied. There are many algorithms proposed by different individuals for calculating the prefix sum of multiplicative functions, so it can be interesting to explore further for those interested.

### References
- [Library Checker: Problem proposal (Sum of Multiplicative Function)](https://github.com/yosupo06/library-checker-problems/issues/1118): A collection of prior research on the prefix sum of multiplicative functions.
- [OI-Wiki](https://oi-wiki.org/math/number-theory/min-25/): Explanation of algorithms like the Du Jiao sieve and the PowerfulNumber sieve.
