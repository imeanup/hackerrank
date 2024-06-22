## [E - Water Tank](https://atcoder.jp/contests/abc359/tasks/abc359_e)

<details><summary>Japanese Editorial</summary><br>

$n = 1, 2, \dots, N$ について、$A_n$ がはじめて正になるような操作の直前に $A_i (i < n)$ の値がどのようになっているかを考えます。

<details><summary>論証による導出</summary><br>

本問の操作について、次の $2$ つが成り立つことを示します。

$1 \le i \le N$ なる整数 $i$ に対して、条件 $P(i)$ で $A_{i-1} \le \max\{H_i, A_i\}$ を表すこととします。

1. 操作の直後、$i = 1, 2, \dots, N$ のすべてについて $P(i)$ が成り立つ
2. 操作は、次のように言い換えることができる。
   * $i_C$ を $A_{i-1} < \max\{H_i, A_i\}$ が成り立つ最小の $i (1 \le i \le N)$（存在しなければ $N+1$）と定める。
   * $A_{i_C - 1}$ の値を $1$ 増やす。

まず、$1 \implies 2$ を示します。

<details><summary>証明</summary><br>

$P(i)$ は ¬ $(A_{i-1} > A_i \wedge A_{i-1} > H_i)$ と同値であることに注意します。

操作が始まる前、$1 \le i \le i_C$ においては $A_{i-1} = \max\{H_i, A_i\}$ が成り立っています。 $i$ に対する $2$ 番の操作を行う時点では、$1$ 番の操作もしくは $i-1$ に対する $2$ 番の操作によって $A_{i-1}$ の値が $1$ 増加しているので、$A_{i-1} > A_i$ および $A_{i-1} > H_i$ が成り立ちます。

$1$ 番の操作と $1 \le i \le i_C$ に対する $2$ 番の操作が行われた直後、$A_{^iC - 1}$ の値だけ $1$ 増加しています。 $i_C$ の取り方から、$i = i_C$ に対する $2$ 番の操作を行う直前にも $P(i_C)$ が成り立っています。 よって、$A_{i_C}$ の値は変化しません。 仮定よりどの $i_C < i$ に対しても $P(i)$ が成り立っているので、$i_C < i$ に対する $2$ 番の操作の条件が満たされることはありません。

よって、$1 \implies 2$ が示されました。

</details><br>

次に、$1$ を示します。 操作回数に対する帰納法を行います。

<details><summary>証明</summary><br>

はじめ、$A_0 = A_1 = \dots = A_N = 0$ なので、成り立っています。

条件が成り立っている状態から $1$ 回だけ操作を行っても条件が成り立つことを示します。

上の証明から、条件が成り立っている状態から操作を行うと、$A_{i-1} < \max\{H_i, A_i\}$ が成り立つ最小の $i$（存在しなければ $N+1$）に対する $A_{i-1}$ の値のみが $1$ だけ増加します。

よって、$i \ne i_C - 1, i_C$ に対しては $A_{i-1}, A_i$ の値は変化せず、$P(i)$ が変わらず成り立ちます。

$i = i_C - 1$ に対しては、$A_i$ の値が増加するため $\max\{H_i, A_i\}$ が減少することはなく、$P(i_C-1)$ が成り立ちます。

$i_C \le N$ のとき、$i = i_C$ に対しては、$i_C$ の取り方から操作が始まる前には $A_{i-1} = \max\{H_i, A_i\}$ が成り立っているため、$A_{i-1}$ の値を $1$ 増やしても $P(i_C)$ が成り立ちます。

以上より、$1$ が示されました。

</details><br>

$2$ の言い換えにより、$A_n$ がはじめて正になるような操作では、$i_C = n$ となる必要があることがわかります。 つまり、この操作の直前において、すべての $i \le i < n$ に対して $A_{i-1} = \max\{H_i, A_i\}$ が成り立っています。

ここから $i = n-1, n-2, \dots, 1, 0$ の順に $A_i$ の値を定めることができ、$A_{i-1} = \max_{i < j \le n} H_j (0 \le i < n)$ と書けることがわかります。

</details><br>

丁寧に条件を考察したり実験して観察をしたりすることで、$A_n$ がはじめて正になるような操作の直前には $A_i = \max_{i < j < n} H_j (0 \le i < n)$ が成り立っていることがわかります。

はじめ $\sum_{i=0}^N A_i = 0$ であり、操作を一度行うごとに $\sum_{i=0}^N A_i$ の値は $1$ ずつ増加するので、

$$\sum_{i=0}^N A_i = 1 + \sum_{i=0}^{n-1} \max_{i < j \le n} H_j$$

の値が $i = n$ に対する答えになります。

$n$ が増えるとき $X_i := \max_{i < j \le n} H_j$ がどのように変化するかを考えることで、次のような問題に言い換えることができます。

> 長さ $N$ の数列 $X = (X_1, X_2,\dots, X_N)$ がある。はじめ、$X_1 = X_2 = \dots = X_N = 0$ である。 $i = 1, 2, \dots, N$ に対して順に次の操作を行う。
>
> * $1\le j \le i$ に対し、$X_j \gets \max\{X_j, H_i\}$ と更新する。
>
> それぞれの操作の直後の $1 + \sum_{i=1}^N X_i$ を求めよ。

この問題を解く方針はいくつかあります。

* stack を用いて $(H_i, (X_j = H_i$ となる $j$ の個数 $))$ となる列を管理する
  * $X_j \gets \max\{X_j, H_i\}$ では、stack の先頭の組 $(v, c)$ に対して $v \le H_i$ である限り先頭を取り出すことを繰り返し、$(H_i$ (取り出した $c$ の合計 $+1$)$)$ を追加する
  * $\sum X_i$ も stack の操作と同時に更新
* 遅延セグメント木を用いて区間更新・区間和クエリにする
  * $X$ が単調減少列になるので、更新すべき区間は二分探索で求めることができる
* segment tree beats を用いて区間 chmax ・区間和クエリを処理する

$1$ つめの方針では時間・空間計算量が $O(N)$ 、$2$ つめと $3$ つめの方針では $O(N\log N)$ 時間と $O(N)$ 空間になります。

実装例は以下のようになります。 この実装例では $1$ つめの方針で解いています。

```cpp
#include <iostream>
#include <utility>
#include <vector>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;
    // 高さについて単調減少になるように (高さ, 個数) を管理する
    vector<pair<unsigned, unsigned>> rectangles;

    // 1 + ∑ 高さ × 個数
    unsigned long ans = 1;

    for (unsigned i = 0, H; i < N; ++i) {
        cin >> H;
        // 高さは H 、はじめ個数は 1
        unsigned count = 1;

        // H より低いものがある限り更新
        while (!empty(rectangles) && rectangles.back().first <= H) {
            const auto &[h, c] = rectangles.back();
            // 合計から h × c を引いて
            ans -= static_cast<unsigned long>(h) * c;
            // 個数を増やして
            count += c;
            // 列から取り除く
            rectangles.pop_back();
        }

        // 合計に H × count を足す
        ans += static_cast<unsigned long>(H) * count;
        rectangles.emplace_back(H, count);
        cout << ans << " ";
    }
    cout << endl;
    return 0;
}
```

</details><br>


Consider the values of $A_i$ (for $i < n$) just before the operation when $A_n$ becomes positive for the first time, for $n = 1, 2, \dots, N$.

<details><summary>Derivation by Proof</summary><br>

For the operation in this problem, we demonstrate the following two points:

Let condition $P(i)$ represent $A_{i-1} \le \max\{H_i, A_i\}$ for an integer $i$ such that $1 \le i \le N$.

1. Immediately after the operation, $P(i)$ holds for all $i = 1, 2, \dots, N$.
2. The operation can be rephrased as follows:
   * Define $i_C$ as the smallest $i$ for which $A_{i-1} < \max\{H_i, A_i\}$ holds (if no such $i$ exists, let $i_C = N+1$).
   * Increase the value of $A_{i_C - 1}$ by 1.

First, we show $1 \implies 2$.

<details><summary>Proof</summary><br>

Note that $P(i)$ is equivalent to ¬ $(A_{i-1} > A_i \wedge A_{i-1} > H_i)$.

Before the operation starts, for $1 \le i \le i_C$, $A_{i-1} = \max\{H_i, A_i\}$ holds. When performing the second type of operation for $i$, the value of $A_{i-1}$ has been increased by 1 either by the first type of operation or by the second type of operation for $i-1$, so $A_{i-1} > A_i$ and $A_{i-1} > H_i$ hold.

Immediately after performing the first type of operation and the second type of operation for $1 \le i \le i_C$, the value of $A_{i_C - 1}$ increases by 1. From the definition of $i_C$, $P(i_C)$ also holds just before performing the second type of operation for $i = i_C$. Therefore, the value of $A_{i_C}$ does not change. Since $P(i)$ holds for all $i_C < i$ by assumption, the condition for the second type of operation for $i_C < i$ is not met.

Thus, $1 \implies 2$ is demonstrated.

</details><br>

Next, we show $1$ by induction on the number of operations.

<details><summary>Proof</summary><br>

Initially, $A_0 = A_1 = \dots = A_N = 0$ holds.

We show that if the condition holds before performing one operation, it still holds after performing one operation.

From the above proof, starting from the state where the condition holds, performing an operation will increase the value of $A_{i-1}$ by 1 for the smallest $i$ (if no such $i$ exists, let $i_C = N+1$) for which $A_{i-1} < \max\{H_i, A_i\}$ holds.

Therefore, the values of $A_{i-1}$ and $A_i$ do not change for $i \ne i_C - 1, i_C$, and $P(i)$ continues to hold.

For $i = i_C - 1$, as the value of $A_i$ increases, $\max\{H_i, A_i\}$ does not decrease, so $P(i_C-1)$ holds.

When $i_C \le N$, for $i = i_C$, since $A_{i-1} = \max\{H_i, A_i\}$ holds before the operation due to the definition of $i_C$, $P(i_C)$ still holds even after increasing the value of $A_{i-1}$ by 1.

Thus, $1$ is demonstrated.

</details><br>

From the rephrasing in $2$, it is understood that $i_C = n$ must hold for the operation just before $A_n$ becomes positive for the first time. This means that just before this operation, $A_{i-1} = \max\{H_i, A_i\}$ holds for all $i \le n$.

Thus, the values of $A_i$ can be determined in the order $i = n-1, n-2, \dots, 1, 0$, and we can write $A_{i-1} = \max_{i < j \le n} H_j$ (for $0 \le i < n$).

</details><br>

By carefully considering the conditions or experimenting and observing, it can be understood that just before the operation when $A_n$ becomes positive for the first time, $A_i = \max_{i < j < n} H_j$ holds for $0 \le i < n$.

Initially, $\sum_{i=0}^N A_i = 0$, and each operation increases the value of $\sum_{i=0}^N A_i$ by 1. Therefore,

$$ \sum_{i=0}^N A_i = 1 + \sum_{i=0}^{n-1} \max_{i < j \le n} H_j $$

is the answer for $i = n$.

By considering how $X_i := \max_{i < j \le n} H_j$ changes as $n$ increases, we can rephrase the problem as follows:

> Given a sequence $X = (X_1, X_2, \dots, X_N)$ of length $N$. Initially, $X_1 = X_2 = \dots = X_N = 0$. For $i = 1, 2, \dots, N$, perform the following operation in order:
>
> * For each $1 \le j \le i$, update $X_j \gets \max\{X_j, H_i\}$.
>
> Find the value of $1 + \sum_{i=1}^N X_i$ immediately after each operation.

There are several approaches to solve this problem:

* Use a stack to manage the sequence as $(H_i, \text{number of elements } X_j = H_i)$:
  * For $X_j \gets \max\{X_j, H_i\}$, keep removing the top of the stack as long as $v \le H_i$ for the top element $(v, c)$, and add $(H_i, \text{total count of removed elements} + 1)$ to the stack.
  * Update $\sum X_i$ along with the stack operations.
* Use a lazy segment tree for range updates and range sum queries:
  * Since $X$ is a monotonically decreasing sequence, the range to be updated can be found by binary search.
* Use segment tree beats for range chmax and range sum queries.

The first approach has a time and space complexity of $O(N)$, while the second and third approaches have $O(N\log N)$ time and $O(N)$ space complexity.

An example implementation using the first approach is as follows:

```cpp
#include <iostream>
#include <utility>
#include <vector>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;
    // Manage (height, count) to ensure monotonic decrease in height
    vector<pair<unsigned, unsigned>> rectangles;

    // 1 + ∑ (height × count)
    unsigned long ans = 1;

    for (unsigned i = 0, H; i < N; ++i) {
        cin >> H;
        // Initial height is H, and count is 1
        unsigned count = 1;

        // Update while there are elements lower than H
        while (!empty(rectangles) && rectangles.back().first <= H) {
            const auto &[h, c] = rectangles.back();
            // Subtract h × c from the total
            ans -= static_cast<unsigned long>(h) * c;
            // Increase count
            count += c;
            // Remove from the sequence
            rectangles.pop_back();
        }

        // Add H × count to the total
        ans += static_cast<unsigned long>(H) * count;
        rectangles.emplace_back(H, count);
        cout << ans << " ";
    }
    cout << endl;
    return 0;
}
```
