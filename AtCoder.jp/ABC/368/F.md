## [F - Dividing Game](https://atcoder.jp/contests/abc368/tasks/abc368_f)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese</b></summary><br>

本解説では、 Grundy 数についての理解を前提とします。知らない方は、 [ABC255-G の解説](https://atcoder.jp/contests/abc255/editorial/4104) やインターネット検索をご利用ください。

各 $i$ についての Grundy 数を求めるために、操作を観察します。$A_i$ を $A_i$ 自身でない正の約数で置き換えるという操作は、言い換えると $A_i$ の重複を含めた素因数を $1$ つ以上減らす操作です。

$A_i$ の重複を含めた素因数の個数を $x_i$ とします。このゲームは結局、 $i$ 番目の山には $x_i$ 個の石があり、 $1$ つ以上の石を取り除いて取り除けなくなった方が負けのゲームと考えてよいです。これは Nim そのもので、 $A_i$ の Grundy 数は $x_i$ です。

$A$ の最大値を $T$ とすると、エラトステネスの篩を用いることで時間計算量が $O(N+T\log \⁡log ⁡T)$ のアルゴリズムを得られます。愚直に素因数分解を行う $O(N \sqrt{T})$ のアルゴリズムでも十分高速です。

</details><br>

This explanation assumes an understanding of Grundy numbers. If you're unfamiliar with them, please refer to the [ABC255-G editorial](https://atcoder.jp/contests/abc255/editorial/4104) or search the internet for more information.

To determine the Grundy number for each $i$, let's observe the operation. Replacing $A_i$ with a positive divisor of $A_i$ that is not equal to $A_i$ itself can be rephrased as reducing the number of prime factors (with repetition) of $A_i$ by at least one.

Let $x_i$ be the number of prime factors (including repetitions) of $A_i$. Essentially, this game can be thought of as a game where the $i$th pile has $x_i$ stones, and the players take turns removing one or more stones. The player who cannot make a move loses. This is exactly a Nim game, and the Grundy number for $A_i$ is $x_i$.

If we let $T$ be the maximum value of $A$, we can use the Sieve of Eratosthenes to obtain an algorithm with a time complexity of $O(N + T \log \log T)$. Alternatively, an $O(N \sqrt{T})$ algorithm that performs prime factorization straightforwardly is also sufficiently fast.
