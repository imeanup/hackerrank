# C: Dice and Coin

<!-- 最初に出たサイコロの目ごとに処理していき、最後にそれぞれの確率を合計します。
それぞれ、何回コインの表を出し続けることで初めて得点が K 以上になるかは、ループで数えることで求
めることができます。この回数だけコインが表を出し続けることが必要です。(途中で裏が出てしまったら得
点は $0$ となるので、勝つことはできません)。
サイコロを $1$ 回振り $i (1 \le i \le N)$ が出る確率は $\frac{1}{N}$ です。そのそれぞれに対し、 $t$ 回コインの表を出し
続ける必要がある場合、成功率は $0.5^t$ となります。$\dfrac{1}{N} \times 0.5^t$ のすべての合計が求める答えになります。
以上の方法で計算すると、計算量は $O(N\log K)$ となり、間に合います。

C++ での実装例は以下の通りです。 -->

First, we process each outcome of the initial roll of the die, and finally, we sum up the probabilities for each outcome. We can determine how many times we need to continue flipping the coin to achieve a score of at least $K$ by counting in a loop. It is necessary to continue flipping the coin this many times. (If tails come up during the process, the score becomes $0$, so winning is not possible).

The probability of rolling the **die** once and getting $i (1 \leq i \leq N)$ is $\frac{1}{N}$. 

For each outcome, if it is necessary to continue flipping the **coin** $t$ times, the success rate is $\Big(\dfrac{1}{2}\Big)^t$ . The sum of all $\dfrac{1}{N} \times \Big(\dfrac{1}{2}\Big)^t$ will be the desired answer.

By calculating in this way, the **time complexity** becomes $O(N\log K)$, which is feasible.

Here is an example of implementation in C++:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, k; cin >> n >> k;
    double r = 0;
    for (int i = 1; i <= n; i++){
        double tmp = 1.0/n;
        int now = i;
        while (now < k) {
            now *= 2;
            tmp /= 2;
        }
        r += tmp;
    }
    cout << setprecision(12) << r << "\n";
    return 0;
}
```

<!-- 制約が小さいので、最初に出てくる数値をすべて試すことができる。具体的には

* 最初に $v ( = 1, 2, \cdots ,N)$ が出る確率は $\dfrac{1}{N}$ になる
* さらにそこから勝つ確率は、$v$ からスタートして $K$ 以上になるまで表が出続ければよくて、表が出る必要のある回数を $n$ とすると、$(\frac{1}{2})^n$ になる
ということで、合計して、

* $\dfrac{1}{N} \times (\dfrac{1}{2})^n$

となる。これを $v = 1, 2, \cdots ,N$ について合計すれば OK。

最後に気になるのは $n$ (各 $v$ からスタートして $K$ 以上になるまでに出し続ける必要のある表の回数) の求め方だが、これは愚直に -->

### Second Explanation

Since the constraints are small, we can try all possible initial values. Specifically,

- The probability of getting $v ( = 1, 2, \cdots ,N)$ initially is $\dfrac{1}{N}$.
- Furthermore, the probability of winning from there is simply $(\frac{1}{2})^n$, where $n$ is the number of times heads must appear in a row starting from $v$ until reaching a score of $K$ or more.

Thus, the total probability for each initial value $v$ is:

- $\dfrac{1}{N} \times \Big(\dfrac{1}{2}\Big)^n$

Summing this expression for $v = 1, 2, \cdots ,N$ gives the desired result.

The only remaining concern is determining $n$, the number of consecutive heads required starting from each $v$ to reach a score of $K$ or more. This can be done straightforwardly.

```cpp
int n = 0;
while (v < K) v *= 2, ++n;
```

<!-- とかで大丈夫。このとき $v$ は指数的に大きくなるので、計算回数は $O(\log K)$ で抑えられる。以下の実装ではさらに、

* (\dfrac{1}{2})^n$

の計算も while 文の中でまとめて行うこととした。全体として計算量は $O(N \log K)$ になった。 -->

Something like that is fine. At this point, since $v$ grows exponentially, the number of calculations can be kept at $O(\log K)$. In the following implementation, we further consolidate the calculation of $(\frac{1}{2})^n$ within the while loop. Overall, the computational complexity has become $O(N \log K)$.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    
    double res = 0.0;
    for (long long n = 1; n <= N; ++n) {
        double tmp = 1.0;
        long long nn = n;
        while (nn < K) nn *= 2, tmp /= 2.0;
        res += tmp;
    }
    res /= N;
    cout << fixed << setprecision(10) << res << endl;
}
```