## [E - Toward 0](https://atcoder.jp/contests/abc350/tasks/abc350_e)

<!-- この問題はメモ化再帰により解くことができます。

#### 問題1

まずは次の問題を考えます。

> 設定は元の問題と同じ。ただし、操作は次の1種類である。
>
> * $Y$ 円払う。$2$ 以上 $6$ 以下の整数が等確率で出るサイコロを振る。その出目を $b$ としたとき、$N$ を $\left\lfloor \frac{N}{b} \right\rfloor$ に置き換える。

求める期待値を $f(N)$ とします。このとき、

$ f(N) = Y + \frac{1}{5} f(\left\lfloor \frac{N}{2} \right\rfloor)+ \frac{1}{5} f(\left\lfloor \frac{N}{3} \right\rfloor)+ \frac{1}{5} f(\left\lfloor \frac{N}{4}\right\rfloor )+ \frac{1}{5} f(\left\lfloor \frac{N}{5}\right\rfloor)+ \frac{1}{5} f(\left\lfloor\frac{N}{6}\right\rfloor)$

となります。よってメモ化再帰により求めることができます。（計算量については後述）

#### 問題2

続いて次の問題を考えます。

> 設定は元の問題と同じ。ただし、操作は次の1種類である。
>
> * $Y$ 円払う。$1$ 以上 $6$ 以下の整数が等確率で出るサイコロを振る。その出目を $b$ としたとき、$N$ を $\left\lfloor \frac{N}{b} \right\rfloor$ に置き換える。

求める期待値を $𝑓(𝑁)$ とします。このとき、

$ f(N) = Y + \frac{1}{6} f(\left\lfloor \frac{N}{1} \right\rfloor)+ \frac{1}{6} f(\left\lfloor \frac{N}{2} \right\rfloor)+ \frac{1}{6} f(\left\lfloor \frac{N}{3}\right\rfloor )+ \frac{1}{6} f(\left\lfloor \frac{N}{4}\right\rfloor)+ \frac{1}{6} f(\left\lfloor\frac{N}{5}\right\rfloor) + \frac{1}{6} f(\left\lfloor \frac{N}{6} \right \rfloor)$

となります。右辺にも $𝑓(𝑁)$ があるため再帰で計算することはできないように見えますが、左辺に移項し全体に $\frac{6}{5}$ を掛けることで

$ f(N) = \frac{6}{5}Y + \frac{1}{5} f(\left\lfloor \frac{N}{2} \right\rfloor)+ \frac{1}{5} f(\left\lfloor \frac{N}{3} \right\rfloor)+ \frac{1}{5} f(\left\lfloor \frac{N}{4}\right\rfloor )+ \frac{1}{5} f(\left\lfloor \frac{N}{5}\right\rfloor)+ \frac{1}{5} f(\left\lfloor\frac{N}{6}\right\rfloor)$

となり、メモ化再帰により求めることができます。（計算量については後述）

#### 元の問題

元の問題を考えます。求める期待値を $𝑓(𝑁)$ とします。操作が $2$ 種類あるので、期待値が小さい方を採用するのが最適です。すなわち

$f(N) = \min⁡(X + f(\left\lfloor\frac{N}{A}\right\rfloor),\frac{6}{5} Y + \frac{1}{5} f(\left\lfloor\frac{N}{2}\right\rfloor) + \frac{1}{5} f(\left\lfloor\frac{N}{3}\right\rfloor) + \frac{1}{5} f(\left\lfloor\frac{N}{4}\right\rfloor) + \frac{1}{5} f(\left\lfloor\frac{N}{5}\right\rfloor) +\frac{1}{5} f(\left\lfloor\frac{N}{6}\right\rfloor))$


となり、メモ化再帰により求めることができます。

$𝑓(𝑁)$ を求めるために計算する必要がある ものは、$\Bigg\lfloor\dfrac{\left\lfloor\frac{N}{b}\right\rfloor}{b}\Bigg\rfloor$ に注意すると、$m = 2^p3^q5^r$ と書けるような整数 $m$ によって $f\Big(\left\lfloor \frac{N}{m} \right\rfloor\Big)$ と書かれるものに限ります。

このような $m$ は高々 $𝑂((\log ⁡N)^3)$ 個しか存在しないため、全体の計算量は $𝑂((log⁡𝑁)^3)$ となります。
 -->

### Solution 1: Recursion + Memoization 

#### Problem 1

First, let's consider the following problem:

> The setup is the same as the original problem. However, there is only one type of operation:
>
> * Pay $Y$ yen. Roll a fair six-sided die, where integers from $2$ to $6$ are equally likely to appear. Let $b$ be the outcome of the roll. Replace $N$ with $\left\lfloor \frac{N}{b} \right\rfloor$.

Let $f(N)$ denote the expected value we seek. Then, we have:

$f(N) = Y + \frac{1}{5} f(\left\lfloor \frac{N}{2} \right\rfloor) + \frac{1}{5} f(\left\lfloor \frac{N}{3} \right\rfloor) + \frac{1}{5} f(\left\lfloor \frac{N}{4}\right\rfloor ) + \frac{1}{5} f(\left\lfloor \frac{N}{5}\right\rfloor) + \frac{1}{5} f(\left\lfloor\frac{N}{6}\right\rfloor)$

Therefore, we can solve it using recursion with memoization. (Regarding computational complexity, see below).

#### Problem 2

Next, let's consider the following problem:

> The setup is the same as the original problem. However, there is only one type of operation:
>
> * Pay $Y$ yen. Roll a fair six-sided die, where integers from $1$ to $6$ are equally likely to appear. Let $b$ be the outcome of the roll. Replace $N$ with $\left\lfloor \frac{N}{b} \right\rfloor$.

Let $f(N)$ denote the expected value we seek. Then, we have:

$f(N) = Y + \frac{1}{6} f(\left\lfloor \frac{N}{1} \right\rfloor) + \frac{1}{6} f(\left\lfloor \frac{N}{2} \right\rfloor) + \frac{1}{6} f(\left\lfloor \frac{N}{3}\right\rfloor ) + \frac{1}{6} f(\left\lfloor \frac{N}{4}\right\rfloor) + \frac{1}{6} f(\left\lfloor\frac{N}{5}\right\rfloor) + \frac{1}{6} f(\left\lfloor \frac{N}{6} \right \rfloor)$


<!-- We seem to be stuck in a recursion since $f(N)$ appears on the right-hand side. However, by rearranging the equation and multiplying both sides by $\frac{6}{5}$, we obtain: -->

Although it appears recursive due to $f(N)$ appearing on the right side, by shifting to the left and multiplying the entire equation by $\frac{6}{5}$, we get:

$f(N) = \frac{6}{5}Y + \frac{1}{5} f(\left\lfloor \frac{N}{2} \right\rfloor) + \frac{1}{5} f(\left\lfloor \frac{N}{3}\right\rfloor ) + \frac{1}{5} f(\left\lfloor \frac{N}{4}\right\rfloor) + \frac{1}{5} f(\left\lfloor\frac{N}{5}\right\rfloor) + \frac{1}{5} f(\left\lfloor \frac{N}{6} \right \rfloor)$


Now, we can solve it using recursion with memoization. (Regarding computational complexity, see below).

#### Original Problem

Now, let's consider the original problem. Let $f(N)$ denote the expected value we seek. Since there are two types of operations, we choose the one with the smaller expected value. That is,

$f(N) = \min⁡\left(X + f\left(\left\lfloor\frac{N}{A}\right\rfloor\right), \frac{6}{5} Y + \frac{1}{5} f\left(\left\lfloor\frac{N}{2}\right\rfloor\right) + \frac{1}{5} f\left(\left\lfloor\frac{N}{3}\right\rfloor\right) + \frac{1}{5} f\left(\left\lfloor\frac{N}{4}\right\rfloor\right) + \frac{1}{5} f\left(\left\lfloor\frac{N}{5}\right\rfloor\right) +\frac{1}{5} f\left(\left\lfloor\frac{N}{6}\right\rfloor\right)\right)$

Thus, it can be solved using recusrion with memoization.

To compute $f(N)$, we only need to consider $\Bigg\lfloor\dfrac{\left\lfloor\frac{N}{a}\right\rfloor}{b}\Bigg\rfloor = \left\lfloor\dfrac{N}{ab}\right\rfloor$. Note that we only need to consider those $m$ that can be represented as $m = 2^p3^q5^r$. Since there are at most $O((\log ⁡N)^3)$ such values, the overall computational complexity is $O((\log ⁡N)^3)$.
