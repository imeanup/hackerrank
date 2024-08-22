<details><summary><b> Japanese </b></summary><br>

# ダブリングの基本概念とその応用


ダブリングは、全体の要素数がN個あって1回移動した時にどの要素に到達するのか定まっているとき、「K個先の要素を求めるのに **𝑂**(**𝐾**) かかる」ような状況において

* 前処理：**𝑂**(**𝑁**log**𝐾**) 時間, **𝑂**(**𝑁**log**𝐾**) 空間
* クエリ：**𝑂**(**log**𝐾**)**

で行うことができるようにするアルゴリズムです。

[繰り返し二乗法](https://algo-logic.info/calc-pow/)もダブリングの一種と捉えることができ、[最近共通祖先(LCA)](https://algo-logic.info/lca/)の計算にも利用されます。


## アルゴリズム

**ダブリングによるK個先の要素の求め方：**

* 前処理：「doubling[k][i] : **𝑖** 番目の要素から **2**𝑘 先の要素は何か」を以下の式を利用して計算
  * doubling[k+1][i] = doubling[k][doubling[k][i]]
* クエリ：前処理した結果を利用して K 個先の要素を求める
  * 現在地を now として、**𝐾** を2進数として見た時の全ての桁について以下を行う
    * **𝐾** の **𝑘** 桁目 が 1 ならば now = doubling[k][now] とする

※前処理では以下のような計算をします。

* それぞれの要素について 1 個先の要素が何か記録
* 前の結果を利用して、それぞれの要素について 2 個先の要素が何か記録
* 前の結果を利用して、それぞれの要素について 4 個先の要素が何か記録
* 前の結果を利用して、それぞれの要素について 8 個先の要素が何か記録
* 前の結果を利用して、それぞれの要素について 16 個先の要素が何か記録
* …

**2**𝑘 先の要素が分かっていれば「 “**2**𝑘 先の要素" の**2**𝑘 先」を簡単に求めることができるので、「**2**𝑘**+**1 先の要素が何か」を高速に求めることができます。

※クエリでは、前処理した結果を利用しています。[繰り返し二乗法](https://algo-logic.info/calc-pow/)について見るとイメージしやすいと思います。

### 計算量

K個先の要素を求めたい時の計算量は以下のようになります。

* 前処理：**𝑂**(**𝑁**log**𝐾**) 時間, **𝑂**(**𝑁**log**𝐾**) 空間
* クエリ：**𝑂**(**log**𝐾**)**

## 問題例: [ABC167 D – Teleporter](https://atcoder.jp/contests/abc167/tasks/abc167_d)

*町が **𝑁** 個ある。町 **𝑖** から町 **𝐴**𝑖 に移動することを K 回繰り返す。*
*町 1 から始めた時、最終的にどの町にたどり着くか？*

### 制約

* **2**≤**𝑁**≤**2**×**10**5
* **1**≤**𝐴**𝑖**≤**𝑁
* **1**≤**𝐾**≤**10**18

### 考え方

単純にシミュレーションすると、O(K) の計算量になって間に合いません。

そこで、ダブリングの考え方が使えます。

* doubling[k][i] : 町 **𝑖** から **2**𝑘 先の町はどこか？

という情報を前計算することで、

* 前処理：**𝑂**(**𝑁**log**𝐾**) 時間, **𝑂**(**𝑁**log**𝐾**) 空間
* クエリ：**𝑂**(**log**𝐾**)**

計算することができます。

他にも、周期性を利用した解法などもあります。詳しくは [D – Teleporter 解説 (AtCoder Beginner Contest 167)](https://algo-logic.info/abc167d/) を見て下さい。

### C++ での実装例


## 練習問題

* [AtCoder Beginner Contest 167 D – Teleporter](https://atcoder.jp/contests/abc167/tasks/abc167_d) ([解説](https://algo-logic.info/abc167d/))
* [[AOJ] NTL_1 Power ](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_B&lang=ja): 繰り返し二乗法
* [AOJ GRL_5_C Lowest Common Ancestor](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C&lang=ja) : LCA 

</details><br><br>

# Basic Concept of Doubling and Its Applications

Doubling is an algorithm that allows you to find the element $K$ steps ahead in situations where moving one step at a time takes $O(K)$ time. It can be performed with:

- Preprocessing: $O(N \log K)$ time and $O(N \log K)$ space
- Query: $O(\log K)$ time

This technique can be applied to problems where you need to calculate something like "$K$ steps ahead" efficiently, and it is also used in calculations like [exponentiation by squaring](https://algo-logic.info/calc-pow/) and [Lowest Common Ancestor (LCA)](https://algo-logic.info/lca/).

## Algorithm

**Finding the $K^{th}$ element ahead using Doubling:**

- Preprocessing: Calculate " $\text{doubling}[k][i]$ : What is the element $2^k$ steps ahead from the $i^{th}$ element?" using the following formula:
  - $\text{doubling}[k+1][i] = \text{doubling}[k][\text{doubling}[k][i]]$
- Query: Use the preprocessed results to find the element $K$ steps ahead.
  - Set the current position to `now`, and for every bit in the binary representation of $K$, do the following:
    - If the $k^{th}$ bit of $K$ is $1$, then set $\text{now} = \text{doubling}[k][now]$.

During preprocessing, the following steps are performed:

- Record the element $1$ step ahead for each element.
- Using the previous results, record the element $2$ steps ahead for each element.
- Using the previous results, record the element $4$ steps ahead for each element.
- Using the previous results, record the element $8$ steps ahead for each element.
- $\cdots$

If you know the element $2^k$ steps ahead, you can easily find the element $2^{(k+1)}$ steps ahead by computing the element that is " $2^k$ steps ahead of the element that is $2^k$ steps ahead." This allows for quick calculations of elements that are a large number of steps ahead.

For queries, the preprocessed results are utilized. Refer to [exponentiation by squaring](https://algo-logic.info/calc-pow/) for an easier understanding.

### Time Complexity

The time complexity for finding the element K steps ahead is as follows:

- Preprocessing: $O(N\log K)$ time, $O(N\log K)$ space
- Query: $O(\log K)$ time

## Example Problem: [ABC167 D – Teleporter](https://atcoder.jp/contests/abc167/tasks/abc167_d)

*There are $N$ towns. Starting from town $1$, you move to town $A_i$ for $K$ times. Which town will you end up in?*

### Constraints

- $2 \le N \le 2 \times 10^5$
- $1 \le A_i \le N$
- $1 \le K \le 10^{18}$

### Approach

If you simulate the process naively, the time complexity would be O(K), which is infeasible.

This is where the concept of Doubling comes in handy.

By precomputing:

- $\text{doubling}[k][i]$ : Which town is $2^k$ steps ahead from town $i$ ?

You can solve the problem with:

- Preprocessing: $O(N\log K)$ time, $O(N\log K)$ space.
- Query: $O(\log K)$ time.

Other approaches, like utilizing cyclic patterns, are also possible. For more details, see the [D – Teleporter Explanation (AtCoder Beginner Contest 167)](https://algo-logic.info/abc167d/).

### Example Implementation in C++

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        A[i]--;  // Convert to 0-indexed
    }
  
    int logK = 1;
    while ((1LL << logK) <= K) logK++;
  
    // doubling[k][i] : Town you reach after 2^k steps from town i
    vector<vector<int>> doubling(logK, vector<int>(N));
    for (int i = 0; i < N; i++) {
        doubling[0][i] = A[i];
    }
  
    // Preprocessing for doubling
    for (int k = 0; k < logK - 1; k++) {
        for (int i = 0; i < N; i++) {
            doubling[k + 1][i] = doubling[k][doubling[k][i]];
        }
    }
  
    int now = 0;
    for (int k = 0; K > 0; k++) {
        if (K & 1) now = doubling[k][now];
        K >>= 1;
    }
  
    cout << now + 1 << endl;
}
```

</details><br>

## Practice Problems

- [AtCoder Beginner Contest 167 D – Teleporter](https://atcoder.jp/contests/abc167/tasks/abc167_d) ([Explanation](https://algo-logic.info/abc167d/))
- [[AOJ] NTL_1 Power](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_B&lang=ja): Exponentiation by Squaring
- [AOJ GRL_5_C Lowest Common Ancestor](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C&lang=ja): LCA

<details><summary><b> Japanese editorial  </b></summary><br>

# ダブリング

## アルゴリズムの概要

全体の要素数が$N$個あって、それぞれの要素について、その要素から1回遷移(移動)したときの移動先が定まっているとする。
このとき、「$K$回遷移したときの到達点」を高速に求めるアルゴリズムの1つがダブリングである。

このような問題を愚直に求めようとすると$\mathcal{O}(K)$になるが、ダブリングを用いることにより$\mathcal{O}(N\log{K})$で計算できるようになる。

## アルゴリズムの詳細

一般的なダブリングでは、動的計画法で用いるDPテーブルに似た以下のようなテーブルを事前に計算する。

$dp[i][j]$: $j$番目の要素から$2^i$回遷移したときの到達地点。ただし、$1 \leq j \leq N, 0 \leq i \leq \lceil \log_{2} {K} \rceil$。

このテーブルの初期条件は以下のようになる。ここで、集合$S = \{1, 2, \ldots, N\}$に対して、「$j$番目の要素から1回遷移したときの到達地点」を表す関数$f: S \rightarrow S$を$f(j)$ $(1 \leq j \leq N)$と定める。

$$
\begin{cases}
\text{初期条件: } &dp[0][j] = f(j) \quad (1 \leq j \leq N) \\
\text{漸化式: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (0 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)
\end{cases}
$$

:::details 初期条件と漸化式について補足

初期条件$(i = 0)$については、$2 ^ 0 = 1$回遷移したときの到達点は$f(j)$の値をそのまま入れておけばよいというだけである。

漸化式の方については、以下のように導出すればよい。

全ての$j$と$i - 1$以下について$dp[i - 1][j]$が求まっている状態で、$j$番目の要素から$2 ^ i$回遷移したときの到達点を求めたい。
これを求めるには、$j$番目の要素から$2 ^ {i - 1}$回遷移した後、更にもう$2 ^ {i - 1}$回遷移した結果が得られればよい。
「$j$番目の要素から$2 ^ {i - 1}$回遷移したときの到達点」は$dp[i - 1][j]$に入っているので、そこから更に$2^{i - 1}$回遷移した結果は$dp[i - 1][dp[i - 1][j]]$に格納されている。これを$dp[i][j]$に格納すればよい。
:::

事前計算によってこのテーブルを計算できれば、$K$を2進数とみなし、$K$の各ビットを下位から見ていき、テーブルを用いて結果を更新していけばよい。
すなわち、$K = 2^{c_1} + 2^{c_2} + 2^{c_3} + \cdots + 2^{c_k} \quad (0 \leq c_1 \leq c_2 \cdots c_k)$と表したとき、$c_1$から順に、答え$A$を$A = dp[c_l][A] \quad (1 \leq l \leq k)$と更新していくことで解を得られる。

計算量は、事前計算で$\mathcal{O}(N\log{K})$、解の計算で$\mathcal{O}(\log{K})$となる。

## 類題

ダブリングを使って解くことのできる類題をいくつか挙げる。

### AtCoder Beginner Contest 167 D - Teleporter

#### 問題

[AtCoderのページ](https://atcoder.jp/contests/abc167/tasks/abc167_d)より引用する。

> ### 問題文
>
> 高橋王国には$N$個の町があります。町は$1$から$N$まで番号が振られています。
>
> それぞれの町にはテレポーターが$1$台ずつ設置されています。町$i (1 \leq i \leq N)$のテレポーターの転送先は町$A_i$です。
>
> 高橋王は正の整数$K$が好きです。わがままな高橋王は、町$1$から出発してテレポーターをちょうど$K$回使うと、どの町に到着するかが知りたいです。
>
> 高橋王のために、これを求めるプログラムを作成してください。
>
> ### 制約
>
> - $2 \leq N \leq 2 \times 10^5$
> - $1 \leq A_i \leq N$
> - $1 \leq K \leq 10^{18}$

#### 解答例

ダブリングを使って簡単に解くことができる。

テーブルを以下のように定義する。

$dp[i][j]$: 町$j$から$2^i$回テレポートして到達した町の番号 $(0 \leq i \leq \log_2 K, 1 \leq j \leq N)$

初期条件と漸化式は以下のようになる。

$$
\begin{cases}
\text{初期条件: } &dp[0][j] = A_{j} \quad (1 \leq j \leq N) \\
\text{漸化式: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)
\end{cases}
$$

Pythonによるコード例を以下に示す。尚、$K$が最大で$10^{18}$であるため$\log K$を60程度に取らないといけないが、$N$は最大で$2 \times 10^5$であり、計算量が$10^7$オーダーになる場合がある。そのため、Pythonでは`PyPy3`で提出しないと[TLEになる](https://atcoder.jp/contests/abc167/submissions/33148942)ので注意。

```py
from typing import List


def main():
    # 入力受け取り
    N, K = map(int, input().split())
    # 0-indexedで受け取っておく
    A: List[int] = list(map(lambda x: int(x) - 1, input().split()))

    # ダブリングのテーブル
    dp: List[List[int]] = [[0 for j in range(N)] for i in range(61)]
    # 初期条件
    for j in range(N):
        dp[0][j] = A[j]

    # 遷移
    for i in range(1, 61):
        for j in range(N):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # 解を求める
    answer: int = 0
    # 現在見ているビットの下位からの桁
    i: int = 0
    # Kを2進数とみなして計算する
    while K:
        # Kの下位からi桁目が1なら遷移する
        if K & 1:
            answer = dp[i][answer]
        # 1つビットシフトする
        K >>= 1
        # iを進める
        i += 1

    # 解の出力(1-indexedに戻す)
    print(answer + 1)


if __name__ == "__main__":
    main()
```

実際の提出は[こちら](https://atcoder.jp/contests/abc167/submissions/33148930)。

### 競プロ典型90問 058 - Original Calculator (★4)

#### 問題

[AtCoderのページ](https://atcoder.jp/contests/typical90/tasks/typical90_bf)より引用する。

> ### 問題文
>
> あなたは奇妙な電卓を持っています。この電卓は$0$以上$10^5-1$以下の整数を$1$つ表示できます。この電卓には**ボタンA**と呼ばれるボタンがあります。整数$x$が表示されているときに ボタンA を$1$回押すと、次の処理が順番に行われます。
>
> 1. $x$を十進法で表したときの各桁の和を計算し、$y$とする。
> 1. $x+y$を$10^5$で割ったあまりを計算し、$z$とする。
> 1. 表示されている整数を$z$に変更する。
>
> 例えば、$99999$が表示されているときに ボタンA を$1$回押すと、$99999+(9+9+9+9+9)=100044$なので、表示される整数は$44$に変更されます。
>
> 今、この電卓に$N$が表示されています。 ボタンA を$K$回押した後に表示されている整数を求めて下さい。
>
> ### 制約
>
> - $0 \leq N \leq 10^5-1$
> - $1 \leq K \leq 10^{18}$
> - 入力はすべて整数

#### 解答例

ダブリングテーブルを以下のように定義する。

$dp[i][j]$: 整数$j$が表示されている状態から$2^i$回ボタンを押した後に表示される整数$(0 \leq i \leq \log_2 K, 0 \leq j < 10^5)$

整数$x$が表示されているときにボタンを1回押した後表示される数値$z$を求める関数を$f(x)$と表記することにする。
このとき、初期条件と漸化式は以下のようになる。

$$
\begin{cases}
\text{初期条件: } &dp[0][j] = f(j) \quad (0 \leq j < 10^5) \\
\text{漸化式: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 0 \leq j < 10^5)
\end{cases}
$$

Pythonによる実装例を以下に示す。こちらは`PyPy3`でなくても[TLEにはならない](https://atcoder.jp/contests/typical90/submissions/33149195)様子。

```py
from typing import List
import math


def f(x: int) -> int:
    # 整数xを文字列として解釈して計算する
    y: int = sum(map(lambda s: ord(s) - ord("0"), str(x)))
    return (x + y) % 100000


def main():
    # 入力受け取り
    N, K = map(int, input().split())

    # log_2 KをMとおく。
    M: int = math.ceil(math.log2(K))

    # ダブリングテーブル
    dp: List[List[int]] = [[0 for j in range(100000)] for i in range(M + 1)]

    # 初期条件
    for j in range(100000):
        dp[0][j] = f(j)

    # 遷移
    for i in range(1, M + 1):
        for j in range(100000):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # 解を求める
    answer: int = N
    i: int = 0
    while K:
        if K & 1:
            answer = dp[i][answer]
        K >>= 1
        i += 1

    print(answer)


if __name__ == "__main__":
    main()
```

実際の提出は[こちら](https://atcoder.jp/contests/typical90/submissions/33149167)。

### AtCoder Beginner Contest 241 E - Putting Candies

#### 問題

問題文を[AtCoderのページ](https://atcoder.jp/contests/abc241/tasks/abc241_e)より引用する。

> ### 問題文
>
> 長さ$N$の数列$A=(A_0,A_1,\ldots,A_{N-1})$が与えられます。  
> 最初の時点では空の皿があり、高橋君は次の操作を$K$回繰り返します。
>
> - 皿の中のアメの個数を$X$とする。皿に$A_{(X\bmod N)}$個のアメを追加する。
>   ただし、$X\bmod N$で$X$を$N$で割った余りを表す。
>
> $K$回の操作の後で、皿の中には何個のアメがあるか求めてください。
>
> ### 制約
>
> - $2 \leq N \leq 2\times 10^5$
> - $1 \leq K \leq 10^{12}$
> - $1 \leq A_i\leq 10^6$
> - 入力はすべて整数である。

#### 解答例

ダブリングテーブルを以下のように定義する。

$dp[i][j]$: 皿の上のアメの数が$j (= X \mod N)$個のとき、そこから$2^i$回操作を繰り返すことで追加されるアメの総数 $(0 \leq j \leq N, 0 \leq i \leq \lceil \log_2 K \rceil)$

アメの数が$j (=X \mod N)$のとき、その状態から$2^i$回操作を行ったときに追加されるアメの総数は、「皿の上のアメの数が$j$個のときから$2^{i - 1}$回操作を繰り返したときに追加されるアメの個数」$+$「そこから更にもう$2^{i - 1}$回操作を繰り返したときに追加されるアメの個数」である。
後者の項の解釈：皿の上には元々$j$個乗っていて、その状態で$2^{i - 1}$回操作を繰り返す(前者の項の操作)と、皿の上には$dp[i - 1][j]$個のアメが**追加される**。そこから更に$2^{i - 1}$回操作を繰り返すとき、皿の上には$j + dp[i - 1][j]$個のアメがあることになるので、$dp[i - 1][(j + dp[i - 1][j]) \mod N]$となる。

従って、初期条件と漸化式は以下のようになる。

$$
\begin{cases}
\text{初期条件: } &dp[0][j] = A_j \quad (1 \leq j \leq N) \\
\text{漸化式: } &dp[i][j] = dp[i - 1][j] + dp[i - 1][dp[i - 1][j]] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 0 \leq j \leq N)
\end{cases}
$$

Pythonによる実装例を以下に示す。この問題も$K$の最大値が$10^12$なので、$i$の値はせいぜい40まででよい。そうしないと全体の計算量が$10^7$オーダーになり、Pythonだと時間制限が厳しくなるので注意。

```py
from typing import List


def main():
    # 入力受け取り
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    # ダブリングテーブル
    dp: List[List[int]] = [[0 for j in range(N)] for i in range(41)]
    # 初期条件
    for j in range(N):
        dp[0][j] = A[j]

    # 遷移
    for i in range(1, 41):
        for j in range(N):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][(j + dp[i - 1][j]) % N]

    # 答えを格納する変数
    answer: int = 0
    i: int = 0
    while K:
        if K & 1:
            # dp[i][j]は「操作によって追加されるアメの数」であるので、
            # 答えの数に加算していく。
            answer += dp[i][answer % N]
        K >>= 1
        i += 1

    # 回答出力
    print(answer)


if __name__ == "__main__":
    main()


```

実際の提出は[こちら](https://atcoder.jp/contests/abc241/submissions/33166702)。

### AtCoder Beginner Contest 258 E - Packing Potatoes

#### 問題

問題文を[AtCoderのページ](https://atcoder.jp/contests/abc258/tasks/abc258_e)より引用する。

> ### 問題文
>
> ベルトコンベアに載って$10^{100}$個のじゃがいもが$1$個ずつ流れてきます。流れてくるじゃがいもの重さは長さ$N$の数列$W = (W_0, \dots, W_{N-1})$で表され、$i \, (1 \leq i \leq 10^{100})$番目に流れてくるじゃがいもの重さは$W_{(i-1) \bmod N}$です。ここで、$(i-1) \bmod N$は$i - 1$を$N$で割った余りを表します。
>
> 高橋君は、まず空の箱を用意し、次のルールに従ってじゃがいもを順番に箱に詰めていきます。
>
> - じゃがいもを箱に入れる。箱に入っているじゃがいもの重さの総和が$X$以上になったら、その箱には蓋をし、新たに空の箱を用意する。
>
> $Q$個のクエリが与えられます。$i \, (1 \leq i \leq Q)$番目のクエリでは、正整数$K_i$が与えられるので、$K_i$番目に蓋をされた箱に入っているじゃがいもの個数を求めてください。問題の制約下で、蓋をされた箱が$K_i$個以上存在することが証明できます。
>
> ### 制約
>
> - $1 \leq N, Q \leq 2 \times 10^5$
> - $1 \leq X \leq 10^9$
> - $1 \leq W_i \leq 10^9 \, (0 \leq i \leq N - 1)$
> - $1 \leq K_i \leq 10^{12} \, (1 \leq i \leq Q)$
> - 入力は全て整数

#### 解答例

公式解説に倣い、各$i = 1, 2, \ldots, 10^{100}$に対して$j = (i - 1) \mod N$をそのじゃがいもの「種類」と呼ぶこととする。
また、配列$C = (C_1, C_2, \ldots, C_N)$の要素$C_j$を「種類$j$のじゃがいもから始めて順番に箱詰めを行ったとき、何個入れた時点で蓋をされるか？」を表す数とする。

ダブリングテーブルを以下のように定義する。

$dp[i][j]$: 種類$j$のじゃがいもから始めて順番に箱詰めを行っていき、$2^{i}$個の箱の蓋が閉じられたときの、次に箱詰めする対象となるじゃがいもの種類。$(0 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)$

$K$が与えられたとき、ダブリングテーブルを使うことで、$K - 1$個の箱の蓋が閉じられた後最初に入れるじゃがいもの種類がわかることになる($K$番目の箱に最初に入れるじゃがいもの種類がわかるということである)。
配列$C$が既知であるなら、これらの情報より、$K$番目の箱に入るじゃがいもの個数を求めることができる。

##### 配列$C$の求め方

まずは配列$C$を求める。これがわからないとダブリングテーブルの漸化式が求まらない。

愚直に求めるならば、各$j$からスタートして$j$を1つずつインクリメントしながら$W_{(j - 1) \mod N}$を加算していき、初めて重さの和が$X$以上になったところでストップする。
このときの添字を$l$としたとき、$C_j = l - j + 1$と計算することができる。

しかし、この計算だと例えば$X = 10^9, W_j = 1$のような条件では$10^9$オーダーの計算が必要になってしまう。
そこで、次のように考える。$W = (W_1, W_2, \ldots, W_N)$の総和を$S$とおく。種類$j$のじゃがいもから始めて順番に箱詰めしていったとき、$S < X$が成り立つならば、1周してきて種類$j$に戻ってからまたいくつかのじゃがいもを入れて蓋をすることになる。
これを考えると、種類$j$から始めて蓋をするまでに、$\lfloor \frac{X}{S} \rfloor$周してからもう数個じゃがいもを入れることになる。
$\lfloor \frac{X}{S} \rfloor$周したとき、残りの許容重量は$X \mod S$となるから、種類$j$から始めて重さが初めて$X \mod S$以上になったときの種類を$l$とすればよいことがわかる。

これを踏まえると、配列$C$は次のように求められる。

- $C$の各要素は$\lfloor \frac{X}{S} \rfloor \times N$で初期化しておく。
- $W$を2周繋げた配列の累積和を取った配列$V$を用意しておき、各$j$について以下のように$l$を求める。
  - $V_l \geq  X + V_j$を満たす最小の添字$l$を二分探索法によって見つける。
  - $C_j$に$(l - j)$を加算する。

これで配列$C_i$を求めることができた。

##### ダブリングテーブルの初期条件と漸化式

ダブリングテーブルの初期条件と漸化式は以下のようになる。

$$
\begin{cases}
\text{初期条件: } &dp[0][j] = (j + C_j) \mod N \quad (1 \leq j \leq N) \\
\text{漸化式: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)
\end{cases}
$$

あとは$K - 1$回遷移したときの添字$l$を求め、$C_l$を出力すればよい。

Pythonによる実装例を以下に示す。

```py
from typing import List
import sys
import itertools
import bisect


input = sys.stdin.readline


def main():
    # 入力受け取り
    N, Q, X = map(int, input().split())
    W: List[int] = list(map(int, input().split()))
    K: List[int] = [int(input()) for i in range(Q)]

    # Wの総和
    S: int = sum(W)
    # 配列C
    # 各要素は「何周するか×1周の個数」で初期化しておく
    C: List[int] = [(X // S) * N] * N

    # ダブリングテーブル
    dp: List[List[int]] = [[0 for j in range(N)] for i in range(41)]

    # 周回分はすでに加算しているので残った余りについて計算する
    X %= S
    # Wを2周分繋げて累積和を取った配列V
    V: List[int] = [0] + list(itertools.accumulate(W * 2))
    # 二分探索で配列Cの各要素の値を求める
    for j in range(N):
        l: int = bisect.bisect_left(V, X + V[j])
        C[j] += l - j

    # aダブリングテーブルの初期条件
    for j in range(N):
        dp[0][j] = (j + C[j]) % N

    # 遷移
    for i in range(1, 41):
        for j in range(N):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # 各クエリの解を求める
    for k in K:
        # K - 1番目の箱の蓋を締め終わったとき、
        # 次に入れるじゃがいもの種類が知りたい
        k -= 1
        index: int = 0
        i: int = 0
        while k:
            if k & 1:
                index = dp[i][index]
            k >>= 1
            i += 1

        # 解の出力
        print(C[index])


if __name__ == "__main__":
    main()
```

実際の提出は[こちら](https://atcoder.jp/contests/abc258/submissions/33167588)。

</details><br><br>

# Doubling

## Overview of the Algorithm

Consider a scenario where there are $N$ elements, and for each element, there is a defined destination when transitioning (or moving) from that element once. Doubling is an algorithm used to efficiently determine the destination after $K$ transitions.

Without any optimizations, solving this problem directly would take $\mathcal{O}(K)$ time. However, by using the doubling technique, the time complexity can be reduced to $\mathcal{O}(N\log{K})$.

## Detailed Algorithm

In a typical doubling approach, a table similar to a DP table in dynamic programming is precomputed.

Let $dp[i][j]$ represent the destination after transitioning $2^i$ times from the $j$-th element, where $1 \leq j \leq N$ and $0 \leq i \leq \lceil \log_{2} {K} \rceil$.

### Initial Condition and Recurrence Relation

The initial condition is defined as follows. Let the function $f: S \rightarrow S$ represent the destination after one transition from the $j$-th element, where $S = \{1, 2, \ldots, N\}$.

$$
\begin{cases}
\text{Initial Condition: } &dp[0][j] = f(j) \quad (1 \leq j \leq N) \\
\text{Recurrence Relation: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (0 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)
\end{cases}
$$

### Explanation

For the initial condition $(i = 0)$, the destination after $2^0 = 1$ transition is simply $f(j)$.

To derive the recurrence relation, consider that $dp[i - 1][j]$ has already been computed for all $j$ and $i - 1$. To find the destination after $2^i$ transitions from the $j$-th element, we first transition $2^{i - 1}$ times, then transition another $2^{i - 1}$ times from the new position. The destination after $2^{i - 1}$ transitions is stored in $dp[i - 1][j]$, and transitioning another $2^{i - 1}$ times from this point gives us $dp[i - 1][dp[i - 1][j]]$. This value is then stored in $dp[i][j]$.

### Calculating the Final Answer

Once the table is precomputed, treat $K$ as a binary number, and update the result by iterating through the bits of $K$ from least significant to most significant, using the precomputed table.

If $K$ is represented as $K = 2^{c_1} + 2^{c_2} + 2^{c_3} + \cdots + 2^{c_k}$, update the answer by iterating over each $c_l$ and setting $A = dp[c_l][A]$ for each $l$ from $1$ to $k$.

The time complexity is $\mathcal{O}(N\log{K})$ for precomputation and $\mathcal{O}(\log{K})$ for computing the result.

## Related Problems

Here are some problems that can be solved using the doubling method.

### AtCoder Beginner Contest 167 D - Teleporter

#### Problem

Quoted from the [AtCoder page](https://atcoder.jp/contests/abc167/tasks/abc167_d):

> ### Problem Statement
>
> In the Kingdom of Takahashi, there are $N$ towns, numbered from 1 to $N$.
>
> Each town has one teleporter. The teleporter in town $i$ (1 ≤ $i$ ≤ $N$) sends you to town $A_i$.
>
> King Takahashi loves positive integers, particularly $K$. He wants to know which town he would end up in after using the teleporter exactly $K$ times, starting from town 1.
>
> Please write a program to solve this problem for King Takahashi.
>
> ### Constraints
>
> - $2 \leq N \leq 2 \times 10^5$
> - $1 \leq A_i \leq N$
> - $1 \leq K \leq 10^{18}$

#### Solution Example

This problem can be easily solved using the doubling method.

Define the table as follows:

- $dp[i][j]$: The town number reached after teleporting $2^i$ times from town $j$ $(0 \leq i \leq \log_2 K, 1 \leq j \leq N)$

The initial conditions and the recurrence relation are as follows:

$$
\begin{cases}
\text{Initial Condition: } &dp[0][j] = A_{j} \quad (1 \leq j \leq N) \\
\text{Recurrence Relation: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)
\end{cases}
$$

Below is an example code in Python. Note that since $K$ can be as large as $10^{18}$, you need to set $\log K$ to around 60. Since $N$ can be as large as $2 \times 10^5$, the computation can reach the order of $10^7$. Therefore, it's important to submit using `PyPy3` to avoid [TLE (Time Limit Exceeded)](https://atcoder.jp/contests/abc167/submissions/33148942).

<details style="border: 1px solid black; padding: 10px;"><summary>Python</summary>

```py
from typing import List

def main():
    # Read input
    N, K = map(int, input().split())
    # Convert to 0-indexed
    A: List[int] = list(map(lambda x: int(x) - 1, input().split()))

    # Doubling table
    dp: List[List[int]] = [[0 for j in range(N)] for i in range(61)]
    # Initial condition
    for j in range(N):
        dp[0][j] = A[j]

    # Transitions
    for i in range(1, 61):
        for j in range(N):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # Find the answer
    answer: int = 0
    # Bit index starting from the least significant bit
    i: int = 0
    # Calculate based on the binary representation of K
    while K:
        # If the i-th bit from the least significant bit is 1, transition
        if K & 1:
            answer = dp[i][answer]
        # Shift right by 1 bit
        K >>= 1
        # Move to the next bit
        i += 1

    # Output the result (convert back to 1-indexed)
    print(answer + 1)

if __name__ == "__main__":
    main()
```

</details><br>

The actual submission can be found [here](https://atcoder.jp/contests/abc167/submissions/33148930).

### Typical 90 Problems 058 - Original Calculator (★4)

#### Problem

Quoted from the [AtCoder page](https://atcoder.jp/contests/typical90/tasks/typical90_bf):

> ### Problem Statement
>
> You have a peculiar calculator that can display a single integer between 0 and $10^5 - 1$. The calculator has a button called **Button A**. When an integer $x$ is displayed, pressing Button A once performs the following steps in order:
>
> 1. Calculate $y$, the sum of the digits of $x$ when expressed in decimal.
> 2. Calculate $z$, the remainder when $x + y$ is divided by $10^5$.
> 3. Update the displayed integer to $z$.
>
> For example, if 99999 is displayed and you press Button A once, $99999 + (9 + 9 + 9 + 9 + 9) = 100044$, so the displayed integer will change to 44.
>
> Now, suppose $N$ is initially displayed on this calculator. Determine the integer displayed after pressing Button A $K$ times.
>
> ### Constraints
>
> - $0 \leq N \leq 10^5 - 1$
> - $1 \leq K \leq 10^{18}$
> - All inputs are integers

#### Solution Example

Define the doubling table as follows:

- $ dp[i][j] $: The integer displayed after pressing the button $ 2^i $ times when $ j $ is currently displayed $ (0 \leq i \leq \log_2 K, 0 \leq j < 10^5) $

Let $ f(x) $ denote the function that calculates the value $ z $ displayed after pressing the button once when $ x $ is currently displayed. Then, the initial condition and the recurrence relation are as follows:

$$
\begin{cases}
\text{Initial Condition: } &dp[0][j] = f(j) \quad (0 \leq j < 10^5) \\
\text{Recurrence Relation: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 0 \leq j < 10^5)
\end{cases}
$$

Below is an implementation example in Python. It appears that [TLE (Time Limit Exceeded)](https://atcoder.jp/contests/typical90/submissions/33149195) does not occur even if `PyPy3` is not used.

<details style="border: 1px solid black; padding: 10px;"><summary>Python</summary>

```py
from typing import List
import math

def f(x: int) -> int:
    # Calculate by interpreting the integer x as a string
    y: int = sum(map(lambda s: ord(s) - ord("0"), str(x)))
    return (x + y) % 100000

def main():
    # Read input
    N, K = map(int, input().split())

    # Let log_2 K be M
    M: int = math.ceil(math.log2(K))

    # Doubling table
    dp: List[List[int]] = [[0 for j in range(100000)] for i in range(M + 1)]

    # Initial condition
    for j in range(100000):
        dp[0][j] = f(j)

    # Transitions
    for i in range(1, M + 1):
        for j in range(100000):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # Find the answer
    answer: int = N
    i: int = 0
    while K:
        if K & 1:
            answer = dp[i][answer]
        K >>= 1
        i += 1

    print(answer)

if __name__ == "__main__":
    main()
```

</details><br>

The actual submission can be found [here](https://atcoder.jp/contests/typical90/submissions/33149167).

### AtCoder Beginner Contest 241 E - Putting Candies

#### Problem

Quoted from the [AtCoder page](https://atcoder.jp/contests/abc241/tasks/abc241_e):

> ### Problem Statement
>
> You are given a sequence $A = (A_0, A_1, \dots, A_{N-1})$ of length $N$.  
> Initially, there is an empty dish, and Takahashi will repeat the following operation $K$ times:
>
> - Let $X$ be the number of candies in the dish. Add $A_{(X \bmod N)}$ candies to the dish.
>   Here, $X \bmod N$ represents the remainder when $X$ is divided by $N$.
>
> Determine the number of candies in the dish after $K$ operations.
>
> ### Constraints
>
> - $2 \leq N \leq 2 \times 10^5$
> - $1 \leq K \leq 10^{12}$
> - $1 \leq A_i \leq 10^6$
> - All inputs are integers.

#### Solution Example

Define the doubling table as follows:

- $ dp[i][j] $: The total number of additional candies after performing the operation $2^i$ times starting from $j$ candies in the dish, where $j = X \bmod N$ $ (0 \leq j \leq N, 0 \leq i \leq \lceil \log_2 K \rceil) $

When there are $j$ candies in the dish, the total number of additional candies after performing the operation $2^i$ times can be calculated as the sum of:

1. The total number of candies added after performing the operation $2^{i-1}$ times starting from $j$ candies, and
2. The total number of candies added after performing the operation $2^{i-1}$ times starting from $j + dp[i-1][j]$ candies.

Hence, the initial conditions and recurrence relations are as follows:

$$
\begin{cases}
\text{Initial Condition: } &dp[0][j] = A_j \quad (0 \leq j < N) \\
\text{Recurrence Relation: } &dp[i][j] = dp[i-1][j] + dp[i-1][(j + dp[i-1][j]) \bmod N] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 0 \leq j < N)
\end{cases}
$$

Below is an implementation example in Python. Since the maximum value of $K$ is $10^{12}$, the value of $i$ can be at most 40. Otherwise, the overall computation will be on the order of $10^7$, which could cause a time limit issue with Python.

<details style="border: 1px solid black; padding: 10px;"><summary>Python</summary>

```py
from typing import List

def main():
    # Input
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    # Doubling table
    dp: List[List[int]] = [[0 for j in range(N)] for i in range(41)]
    # Initial condition
    for j in range(N):
        dp[0][j] = A[j]

    # Transitions
    for i in range(1, 41):
        for j in range(N):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][(j + dp[i - 1][j]) % N]

    # Variable to store the answer
    answer: int = 0
    i: int = 0
    while K:
        if K & 1:
            # dp[i][j] represents the number of additional candies, so add it to the answer.
            answer += dp[i][answer % N]
        K >>= 1
        i += 1

    # Output the result
    print(answer)

if __name__ == "__main__":
    main()
```

</details><br>

The actual submission can be found [here](https://atcoder.jp/contests/abc241/submissions/33166702).

### AtCoder Beginner Contest 258 E - Packing Potatoes

#### Problem Statement

The problem statement is quoted from the [AtCoder page](https://atcoder.jp/contests/abc258/tasks/abc258_e).

> ### Problem Statement
>
> There are $10^{100}$ potatoes coming one by one on a conveyor belt. The weight of each potato is represented by a sequence $W$ of length $N$ where $W = (W_0, \dots, W_{N-1})$. The weight of the $i$-th potato (where $1 \leq i \leq 10^{100}$) is $W_{(i-1) \bmod N}$. Here, $(i-1) \bmod N$ denotes the remainder when $i - 1$ is divided by $N$.
>
> Takahashi prepares an empty box and packs the potatoes into the box one by one according to the following rule:
>
> - Put the potato into the box. If the total weight of the potatoes in the box reaches or exceeds $X$, close the box and prepare a new empty box.
>
> There are $Q$ queries. For the $i$-th query (where $1 \leq i \leq Q$), given a positive integer $K_i$, find the number of potatoes in the $K_i$-th box. It is guaranteed that under the given constraints, there will be at least $K_i$ closed boxes.
>
> ### Constraints
>
> - $1 \leq N, Q \leq 2 \times 10^5$
> - $1 \leq X \leq 10^9$
> - $1 \leq W_i \leq 10^9 \, (0 \leq i \leq N - 1)$
> - $1 \leq K_i \leq 10^{12} \, (1 \leq i \leq Q)$
> - All inputs are integers.

#### Solution Example

Following the official explanation, let’s call $j = (i - 1) \mod N$ for each $i = 1, 2, \dots, 10^{100}$ the "type" of that potato. Define an array $C = (C_1, C_2, \ldots, C_N)$ where each element $C_j$ represents "the number of potatoes packed when starting from type $j$ before the box is closed."

Define a doubling table as follows:

$dp[i][j]$: The type of potato to be packed next after $2^{i}$ boxes have been closed, starting from type $j$. $(0 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)$.

When $K$ is given, using the doubling table, it is possible to determine the type of potato to be packed first in the $K$-th box after closing $K - 1$ boxes. If the array $C$ is known, the number of potatoes in the $K$-th box can be determined from this information.

##### Finding Array $C$

First, calculate array $C$. Without this, the recurrence relation for the doubling table cannot be determined.

A brute-force approach would involve starting from each $j$, incrementing $j$ by one while adding $W_{(j - 1) \mod N}$, and stopping when the sum of weights first reaches or exceeds $X$. If the index at this point is $l$, then $C_j = l - j + 1$.

However, with conditions like $X = 10^9$ and $W_j = 1$, this requires calculations on the order of $10^9$. Instead, consider this: let $S$ be the sum of $W = (W_1, W_2, \ldots, W_N)$. If $S < X$ holds when packing starting from type $j$, after making one complete round and returning to type $j$, more potatoes will be added before the box is closed. This means after $\lfloor \frac{X}{S} \rfloor$ rounds, the remaining allowable weight will be $X \mod S$. The first type at which the weight reaches or exceeds $X \mod S$ starting from $j$ is $l$.

With this understanding, array $C$ can be calculated as follows:

- Initialize each element of $C$ with $\lfloor \frac{X}{S} \rfloor \times N$.
- Prepare an array $V$ which is the cumulative sum of $W$ repeated twice, and for each $j$, find $l$ as follows:
  - Find the smallest index $l$ such that $V_l \geq X + V_j$ using binary search.
  - Add $(l - j)$ to $C_j$.

This will calculate array $C$.

##### Initial Conditions and Recurrence Relation of the Doubling Table

The initial conditions and recurrence relation for the doubling table are as follows:

$$
\begin{cases}
\text{Initial Condition: } &dp[0][j] = (j + C_j) \mod N \quad (1 \leq j \leq N) \\
\text{Recurrence Relation: } &dp[i][j] = dp[i - 1][dp[i - 1][j]] \quad (1 \leq i \leq \lceil \log_2 K \rceil, 1 \leq j \leq N)
\end{cases}
$$

Finally, find the index $l$ after $K - 1$ transitions and output $C_l$.

Here’s a Python implementation:

<details style="border: 1px solid black; padding: 10px;"><summary>Python</summary>

```py
from typing import List
import sys
import itertools
import bisect


input = sys.stdin.readline


def main():
    # Input
    N, Q, X = map(int, input().split())
    W: List[int] = list(map(int, input().split()))
    K: List[int] = [int(input()) for i in range(Q)]

    # Total sum of W
    S: int = sum(W)
    # Array C
    C: List[int] = [(X // S) * N] * N

    # Doubling table
    dp: List[List[int]] = [[0 for j in range(N)] for i in range(41)]

    # Calculate the remaining part after full rounds
    X %= S
    # Cumulative sum array V for W repeated twice
    V: List[int] = [0] + list(itertools.accumulate(W * 2))
    # Binary search to find each element of C
    for j in range(N):
        l: int = bisect.bisect_left(V, X + V[j])
        C[j] += l - j

    # Initialize doubling table
    for j in range(N):
        dp[0][j] = (j + C[j]) % N

    # Transitions
    for i in range(1, 41):
        for j in range(N):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # Answer queries
    for k in K:
        k -= 1
        index: int = 0
        i: int = 0
        while k:
            if k & 1:
                index = dp[i][index]
            k >>= 1
            i += 1

        # Output result
        print(C[index])


if __name__ == "__main__":
    main()
```

</details><br>

The actual submission can be found [here](https://atcoder.jp/contests/abc258/submissions/33167588).
