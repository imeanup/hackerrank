## [C - Various Kagamimochi](https://atcoder.jp/contests/abc388/tasks/abc388_c) 

鏡餅を構成する $2$ つの餅のうち大きいほうを固定して、つまり「ある餅をひとつ取ってきて、その餅が下になる鏡餅についてのみ」考えます。

大きさ $a$ の餅が下になる鏡餅の種類数は、大きさが $\dfrac{a}{2}$ 以下である餅の個数と等しいです。 よって、すべての餅について、大きさが自身の半分以下である餅の個数を求め、それを合計することでこの問題を解くことができます。

しかし、$i$ 番目の餅に対して大きさが自身の半分以下である餅の個数は $O(i)$ 個程度まで多くなることがあり、一つ一つ数えていては実行時間制限に間に合いません（$A_i = i$ とすることで個数を $\dfarc{i}{2}$ 個とできます。適切なケースを作ることでより多くすることもできます）。

ここで、尺取り法や二分探索を用いるとこの問題を十分高速に解くことができます。 より具体的には、餅が小さいほうから並んでいることから「どこまでの餅が大きさが $x$ 以下でどこからが $x$ より大きいか」がわかれば $x$ 以下の餅の個数を求めることができます。

尺取り法を用いることで全体の時間計算量を $O(N)$ に、二分探索を用いた場合は時間計算量を $O(N\log⁡ N)$ とすることができます。

答えが 32 bit⁡ 整数に収まらない大きさになる場合があることに注意してください。

実装例は以下のようになります。

(C++, 二分探索)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (auto&& a : A)
        cin >> a;

    long ans = 0;
    for (const auto a : A)
        // a / 2 以下の餅の個数 = a / 2 を超える餅と先頭との距離
        ans += ranges::upper_bound(A, a / 2) - begin(A);

    // 合計が答え
    cout << ans << endl;

    return 0;
}

```

(C++, 尺取り法)

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (auto&& a : A)
        cin >> a;

    long ans = 0;
    // a / 2 より大きい最初の要素（なければ最後の次）を表す値 j
    for (int j = 0; const auto a : A) {
        // 越えるまで進める
        while (j < N && A[j] * 2 <= a) j++;
        ans += j;
    }

    cout << ans << endl;

    return 0;
}

```

---


To solve the problem, we focus on each possible kagamimochi by fixing the larger rice cake of the two. In other words, we consider only kagamimochi where a given rice cake is at the bottom.

The number of different kagamimochi that can be formed with a rice cake of size $a$ at the bottom is equal to the number of rice cakes with size less than or equal to $\frac{a}{2}$. Therefore, the problem can be solved by counting, for each rice cake, the number of rice cakes with size less than or equal to half of its size, and summing these counts for all rice cakes.

However, counting the number of such rice cakes individually for each $i$-th rice cake could take up to $O(i)$ operations. This approach would be too slow and exceed the time limit in the worst case, such as when $A_i = i$, where the number of smaller rice cakes can be as large as $\frac{i}{2}$ (or even more in specifically constructed cases).

To optimize, we can use either the **sliding window method** or **binary search** to solve this problem efficiently. Specifically, since the rice cakes are sorted by size, we can quickly determine the boundary between rice cakes with size $\leq x$ and those with size $> x$, enabling us to count the rice cakes of size $\leq x$.

- Using the **sliding window method**, we can achieve an overall time complexity of $O(N)$.
- Using **binary search**, we can achieve a time complexity of $O(N \log N)$.

Note: Be careful, as the answer may exceed the size of a 32-bit integer.

### Implementation Examples

#### **(C++, Binary Search)**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (auto&& a : A)
        cin >> a;

    long ans = 0;
    for (const auto a : A)
        // Number of rice cakes ≤ a / 2 = distance between upper_bound for a / 2 and the beginning
        ans += ranges::upper_bound(A, a / 2) - begin(A);

    // Output the total sum
    cout << ans << endl;

    return 0;
}
```

#### **(C++, Sliding Window Method)**

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (auto&& a : A)
        cin >> a;

    long ans = 0;
    // j represents the first element larger than a / 2 (or next to last if none exists)
    for (int j = 0; const auto a : A) {
        // Move j forward until it exceeds a / 2
        while (j < N && A[j] * 2 <= a) j++;
        ans += j;
    }

    cout << ans << endl;

    return 0;
}
```

