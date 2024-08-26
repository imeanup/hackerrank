
## [B - Decrease 2 max elements](https://atcoder.jp/contests/abc368/tasks/abc368_b)

<details><summary>Japanese editorial</summary><br>

**より高速な解法**

---

考察を進めることで、より大きな制約でも高速に解ける解法を導くことができます。

まず、$\sum_{i=1}^N A_i$ が操作のたびに $2$ だけ減少するので、答えは $\Big\lfloor \dfrac{1}{2} \sum_{i = 1}^N A_i \Big\rfloor$ 以下です。

次に、$\max_{i \le \le N} A_i$ が操作のたびにたかだか $1$ だけ減少するので、$\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$ は $1$ 回の操作で $1$ もしくは $2$ 減少し、答えは $\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$ 以下です。

以上より、答えは $\min\Big\{ \Big\lfloor \dfrac{1}{2} \sum_{i=1}^N A_i\Big\rfloor, \sum_{i=1}^N A_i - \max_{1\le i \le N} A_i \Big\}$ 以下です。 実は、この上界が達成されることを示せます。


$\lfloor \dfrac{1}{2} \sum_{i=1}^N A_i\rfloor$ と $\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$ の大小関係について場合分けを行います。

<details style="border: 1px solid black; padding: 10px;" ><summary><b>証明</b></summary><br>

#### $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor > \sum_{i=1}^N A_i - \max_{1\le i\le N} A_i$ のとき

このとき、$A_i$ が最大になる $i$ がただひとつ存在します。これが $1$ として一般性を失いません。このような $A$ からはじめたとき、操作は常に $A_1$ と $A_i (i \ne 1)$ に対して行われ、操作回数は $\sum_{i=1}^N A_i - \max_{1 \le \le N} A_i$ 回です。

---

#### $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i -\max_{1 \le i \le N} A_i$  のとき

まず、$\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i -\max_{1\le i\le N} A_i$  が成り立っている状態から（操作ができるなら）操作を行っても $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i -\max_{1\le i\le N} A_i$  が成り立つことを示します。

$A_1 = \max_{1\le \le N} A_i$ として一般性を失わないため、そうします。

1. $A_1=A_i$ なる $1< i \le N$ がたかだか $1$ つのとき、操作の前後で $\max_{1\le i \le N} A_i$ は $1$ 減少しています。よって、$\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor , \sum_{i=1}^N A_i -\max_{1 \le i \le N} A_i$ のどちらも $1$ だけ減少しているため、大小関係は変化しません。
2. $A_1=A_i$ なる $1< i \le N$ が $2$ つ以上存在するとき、$\sum_{i=1}^N A_i \ge 3A_1$ なので、$\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor < \sum_{i=1}^N A_i - \max_{1\le i\le N} A_i$ が成り立ちます。操作の前後で $\max_{1\le i \le N} A_i$ は変化しないため、$\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor$ は $1$ 、$\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$ は $2$ だけ減少し、$\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i -\max_{1\le i \le N} A_i$  が成り立ちます。

よって、操作のたびに $\min\Big\{ \Big\lfloor \dfrac{1}{2} \sum_{i=1}^N A_i\Big\rfloor, \sum_{i=1}^N A_i - \max_{1\le i \le N} A_i \Big\} = \Big\lfloor \dfrac{1}{2} \sum_{i=1}^N A_i\Big\rfloor$ は $1$ ずつ減少し、操作回数は $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor$ 回です。

</details><br>

あとは、これを実装することで $N \le 10^6, A_i \le 10^{18}$ のような制約でも十分高速に問題を解くことができます。

実装例は以下のようになります。

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    int sum_A = 0, max_A = 0;
    for (int i = 0; i < N; ++i) {
        int A;
        cin >> A;
        // A の合計と A の最大値を更新
        sum_A += A;
        max_A = max(A, max_A);
    }
    // 答えは min(合計 / 2, 合計 - 最大値)
    cout << min(sum_A / 2, sum_A - max_A) << endl;
    return 0;
}

```

</details><br>

</details><br>

**Faster Solution**

---

By advancing the consideration, we can derive a solution that can solve the problem more quickly even with larger constraints.

First, since $\sum_{i=1}^N A_i$ decreases by 2 with each operation, the answer is at most $\Big\lfloor \dfrac{1}{2} \sum_{i = 1}^N A_i \Big\rfloor$.

Next, because $\max_{i \le N} A_i$ decreases by at most 1 with each operation, $\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$ decreases by 1 or 2 with each operation, so the answer is at most $\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$.

Thus, the answer is at most $\min\Big\{ \Big\lfloor \dfrac{1}{2} \sum_{i=1}^N A_i\Big\rfloor, \sum_{i=1}^N A_i - \max_{1\le i \le N} A_i \Big\}$. In fact, it can be shown that this upper bound can be achieved.

Let's consider the relationship between $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big\rfloor$ and $\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$.

<details style="border: 1px solid black; padding: 10px;"><summary><b>Proof</b></summary><br>

#### When $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor > \sum_{i=1}^N A_i - \max_{1\le i\le N} A_i$

In this case, there is only one index $i$ where $A_i$ is the maximum. We can assume without loss of generality that this is $i = 1$. Starting from such an array $A$, the operations are always performed between $A_1$ and $A_i (i \ne 1)$, and the number of operations is $\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$.

---

#### When $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$

First, we show that starting from a state where $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i - \max_{1\le i\le N} A_i$ holds, and if an operation can be performed, $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i - \max_{1\le i\le N} A_i$ will continue to hold.

We assume without loss of generality that $A_1 = \max_{1\le i \le N} A_i$.

1. When there is at most one $i > 1$ such that $A_1 = A_i$, $\max_{1\le i \le N} A_i$ decreases by 1 before and after the operation. Therefore, both $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor$ and $\sum_{i=1}^N A_i -\max_{1 \le i \le N} A_i$ decrease by 1, so the relationship between them does not change.
2. When there are two or more indices $i > 1$ such that $A_1 = A_i$, since $\sum_{i=1}^N A_i \ge 3A_1$, $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor < \sum_{i=1}^N A_i - \max_{1\le i\le N} A_i$ holds. Since $\max_{1\le i \le N} A_i$ does not change before and after the operation, $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor$ decreases by 1 and $\sum_{i=1}^N A_i - \max_{1 \le i \le N} A_i$ decreases by 2, so $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor \le \sum_{i=1}^N A_i -\max_{1\le i \le N} A_i$ holds.

Therefore, with each operation, $\min\Big\{ \Big\lfloor \dfrac{1}{2} \sum_{i=1}^N A_i\Big\rfloor, \sum_{i=1}^N A_i - \max_{1\le i \le N} A_i \Big\} = \Big\lfloor \dfrac{1}{2} \sum_{i=1}^N A_i\Big\rfloor$ decreases by 1, and the number of operations is $\Big \lfloor \dfrac{1}{2} \sum_{i=1}^N A_i \Big \rfloor$.

</details><br>

Finally, by implementing this approach, we can solve the problem efficiently even with constraints like $N \le 10^6$ and $A_i \le 10^{18}$.

An example implementation is as follows:

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    int sum_A = 0, max_A = 0;
    for (int i = 0; i < N; ++i) {
        int A;
        cin >> A;
        // Update the sum of A and the maximum value of A
        sum_A += A;
        max_A = max(A, max_A);
    }
    // The answer is min(sum / 2, sum - max)
    cout << min(sum_A / 2, sum_A - max_A) << endl;
    return 0;
}
```

</details><br>
