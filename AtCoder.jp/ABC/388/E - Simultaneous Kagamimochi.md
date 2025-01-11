
## [E - Simultaneous Kagamimochi](https://atcoder.jp/contests/abc388/tasks/abc388_e)

**より高速な解法**

---

最悪時間計算量を $O(N)$ 時間とする $2$ つの方針について解説します。

---

餅の列を先頭 $\left\lfloor \dfrac{N}{2}\right\rfloor$ 個とそれ以外に分けます。

後ろの列を先頭から順に見て、それぞれの餅ごとに先頭の列のうち残っている中で最小の餅（存在すれば）と組み合わせて鏡餅を作れるなら作るアルゴリズムを考えます。

このアルゴリズムで作られる鏡餅の個数が求める最大値です。 このことは、$K$ 個の鏡餅を作ることができるなら先頭 $K$ 個を上側として使い、後半 $\left\lceil \dfrac{N}{2}\right\rceil$ 個のうち $K$ 個を下側として使う鏡餅の作り方が存在することと、そのような作り方で先頭 $K$ 個に対応する鏡餅を作り終えた時点での後半の鏡餅の残り方として最良のものをこのアルゴリズムが与えることから確認できます。

実装例は以下のようになります。

```cpp
#include <iostream>
#include <deque>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    // 餅列の先頭側 floor(N / 2) 個
    deque<unsigned> A(N / 2);
    for (auto&& a : A)
        cin >> a;

    unsigned ans{};

    for (unsigned i{N / 2}; i < N; ++i) {
        unsigned a;
        cin >> a;
        // もし残っているうち最小の餅と鏡餅を作れるなら作る
        if (A.front() * 2 <= a) {
            ++ans;
            A.pop_front();
        }
    }

    cout << ans << endl;

    return 0;
}
```

**Faster Solution**

---

I will explain two approaches that achieve a worst-case time complexity of $O(N)$.

---

The sequence of mochi is divided into the first $\left\lfloor \dfrac{N}{2}\right\rfloor$ mochi and the remaining ones.

The algorithm examines the back half of the sequence and, for each mochi, attempts to form a kagami mochi (a paired mochi stack) by pairing it with the smallest remaining mochi in the front half (if one exists).

The number of kagami mochi created by this algorithm is the maximum number that can be formed. This is verified by the fact that if it is possible to create $K$ kagami mochi, the first $K$ can be used as the top side, and $K$ mochi from the second half (the remaining $\left\lceil \dfrac{N}{2}\right\rceil$ mochi) can be used as the bottom side. This approach guarantees the best way to form kagami mochi for the first $K$ mochi while keeping the remaining mochi in the back half in the best configuration.

An example implementation is as follows:

```cpp
#include <iostream>
#include <deque>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    // First half of the mochi sequence, floor(N / 2)
    deque<unsigned> A(N / 2);
    for (auto&& a : A)
        cin >> a;

    unsigned ans{};

    for (unsigned i{N / 2}; i < N; ++i) {
        unsigned a;
        cin >> a;
        // If we can form a kagami mochi with the smallest remaining mochi
        if (A.front() * 2 <= a) {
            ++ans;
            A.pop_front();
        }
    }

    cout << ans << endl;

    return 0;
}
```

---

便宜上、列の後ろに無限の大きさの餅が無限に並んでいることとします。 ここで、先頭 $K$ 項を上段の餅としてすべて使って $K$ 個鏡餅を作る作り方における、下段に使われる鏡餅のインデックスの最大値の最小値について考えます（つまり、$K$ 個鏡餅を作るのに少なくとも何番目までの餅を使う必要があるかについて考えます）。

$B_i \mathrel{:=} i$ 番目の餅を上段の餅として使うときの、下段の餅としてありえる最小のインデックス $(1\le i \le N)$ を求めることは $O(N)$ 時間でできます（C 問題と同様の尺取り法を用いればよいです）。 すると、$B_i$ を用いて上の値は $K + \displaystyle\max\left\{\max_{1\le i \le K}\{B_i − i\}, K\right\}$ と表せます。

あとは、これが $N$ 以下であるような最大の $K$ を求めればよいです。 これは $B_i$ を求めながら $K$ を小さいほうから調べていけばよいです。

実装例は以下のようになります（ここまでの説明は 1-indexed で行われていましたが、実装例では 0-indexed になっていることに注意してください）。

```cpp
#include <iostream>
#include <vector>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    vector<unsigned> A(N);
    for (auto&& a : A)
        cin >> a;

    for (unsigned i = 0, j = 0, d = 0; i < N; ++i) {
        // j := i 番目の餅を乗せられる最小の餅の番号
        while (j < N && A[i] * 2 > A[j]) ++j;
        // d := 上下の餅の番号の差の最大値
        d = max(d, j - i);
    
        // 後ろがはみ出したら
        if (i + max(d, i + 1) >= N) {
            // 直前の値が答え
            cout << i << endl;
            return 0;
        }
    }
    return 0;
}
```


$K$ 個 $(0 \le K \le \dfrac{N}{2})$ の鏡餅を作るとき、先頭 $K$ 個と末尾 $K$ 個の餅を使うとしてかまいません（上に乗せられている餅が先頭 $K$ 個と異なる場合、先頭 $K$ 個の餅が上になるように入れ替えることができます。末尾 $K$ 個も同様です）。

また、上に乗せる $K$ 個の餅と下段として使われる $K$ 個の餅を決めたとき、それらをすべて使って $K$ 個の鏡餅が作れることは、それぞれ小さいほうから組にしたときに $K$ 個の鏡餅が作れることと同値です（$\Leftarrow$ は明らかです。$\Rightarrow$ は、出来上がった鏡餅を上の餅の大きさでソートしたときに下の餅がソートされていないなら、下の餅をソートしても $K$ 個の鏡餅を作れることから言えます）。

以上より、$K$ を定めたときに $K$ 個の鏡餅が作れるかを判定することは $O(K)$ 時間で可能です。

ある非負整数 $K$ について鏡餅を $K$ 個作れるなら、任意の非負整数 $l (l\le k)$ について鏡餅を $l$ 個作れるので、二分探索を行うことでこの問題を解くことができます。

時間計算量は $O(N\log ⁡N)$ となります。

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
#include <ranges>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    vector<unsigned> A(N);
    for (auto&& a : A)
        cin >> a;

    // 判定関数
    // K 個の鏡餅を作ることができるか？
    const auto check{
        [N, &A](unsigned K) {
            for (unsigned i = 0; i < K; ++i)
                // 先頭と末尾から K 個ずつ取ってきて
                if (A[i] * 2 > A[N - K + i])
                    // どれか 1 つでも半分より大きかったら false
                    return false;
            // そうでなければ true
            return true;
        }
    };

    // 0 から N / 2 の間で、判定関数が true になる最大の値（false になる最小の値 - 1）を二分探索で求める
    cout << *ranges::partition_point(views::iota(0U, N / 2 + 1), check) - 1 << endl;

    return 0;
}

```

For convenience, let us assume that an infinitely large number of mochi is placed at the back of the sequence, extending infinitely. We will now consider the minimum possible maximum index of the mochi in the bottom half when creating $K$ kagami mochi (stacked mochi), using the first $K$ mochi as the top part. This essentially asks, for creating $K$ kagami mochi, what is the highest index of mochi in the bottom half that must be used (i.e., which is the smallest index of mochi that needs to be used in the bottom half to make $K$ kagami mochi).

It is possible to compute the smallest possible index in the bottom half when using the $i$-th mochi as the top half mochi, denoted $B_i \mathrel{:=} i$, in $O(N)$ time (this can be done using a sliding window technique similar to problem C). Then, we can express the value as $K + \displaystyle\max\left\{\max_{1\le i \le K}\{B_i − i\}, K\right\}$.

Next, we need to find the largest $K$ such that this value is less than or equal to $N$. This can be done by checking for the largest $K$ starting from the smallest $K$ while computing $B_i$.

An example implementation is as follows (note that the explanation above was done using 1-indexing, but the implementation example below uses 0-indexing):

```cpp
#include <iostream>
#include <vector>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    vector<unsigned> A(N);
    for (auto&& a : A)
        cin >> a;

    for (unsigned i = 0, j = 0, d = 0; i < N; ++i) {
        // j := smallest mochi index where the i-th mochi can be placed
        while (j < N && A[i] * 2 > A[j]) ++j;
        // d := maximum difference between the indices of top and bottom mochi
        d = max(d, j - i);
    
        // If the back exceeds
        if (i + max(d, i + 1) >= N) {
            // The previous value is the answer
            cout << i << endl;
            return 0;
        }
    }
    return 0;
}
```

When creating $K$ kagami mochi $(0 \le K \le \dfrac{N}{2})$, it is acceptable to use the first $K$ mochi and the last $K$ mochi (if the mochi on top differ from the first $K$, they can be swapped so that the first $K$ mochi are placed on top. The same applies to the last $K$ mochi).

Additionally, when deciding which $K$ mochi to use for the top and bottom parts, it is equivalent to forming $K$ kagami mochi when pairing them starting from the smallest mochi (i.e., arranging the top mochi with the bottom mochi sorted in ascending order). This is true because if we can make $K$ kagami mochi after sorting the top mochi, the bottom mochi will be sorted as well.

Therefore, when $K$ is given, determining if we can form $K$ kagami mochi can be done in $O(K)$ time.

If we can form $K$ kagami mochi for some non-negative integer $K$, we can also form $l$ kagami mochi for any $l \leq K$, so we can solve this problem using binary search.

The time complexity will be $O(N \log N)$.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
#include <ranges>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;

    vector<unsigned> A(N);
    for (auto&& a : A)
        cin >> a;

    // Checking function
    // Can we make K kagami mochi?
    const auto check{
        [N, &A](unsigned K) {
            for (unsigned i = 0; i < K; ++i)
                // Take K mochi from the front and the back
                if (A[i] * 2 > A[N - K + i])
                    // If any of them is greater than half, return false
                    return false;
            // Otherwise, return true
            return true;
        }
    };

    // Using binary search to find the maximum value of K for which the check function returns true
    // This corresponds to the largest K such that check returns true
    cout << *ranges::partition_point(views::iota(0U, N / 2 + 1), check) - 1 << endl;

    return 0;
}
```
