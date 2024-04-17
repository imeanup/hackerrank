### F: XOR Matching
<!-- 
$K \ge 2M$ のとき、明らかに解は存在しません。なぜなら $2^M$ 未満の整数同士の排他的論理和をとっても $2^M$ 以上になることはないからです。以下、そうでないときを考えます。
* $M = 0$ のとき、$a$ は一意であり $K = 0$ の解です。
* $M = 1$ のとき、$K = 0$ では解が存在し $K = 1$ では存在しないことが全列挙などで分かります。
* $M \ge 2$ のとき、$0$ 以上 2M 未満の任意の $K$ について解が存在します。このことを具体的に $a$ を構成する ことで示します。

$K$ 以外の $0$ 以上 $2^M$ 未満の整数を昇順に並べた数列を $b$ とします。また $b$ の逆順を $c$ とします。このと き $b K c K$ と並べてできる数列を $a$ とすればよいです。

というのも、まず任意の $i (0 \le i < 2^M, i  \ne K)$ について、この数列中の $2$ つの $i$ の間には、$K$ が $1$ 回、 それ以外の数が $2$ 回現れます。よって $K$ 以外の数は打ち消し合って、題意の排他的論理和は $K$ になります。

次に、この数列中の $2$ つの $K$ の間には、$K$ 以外の $0$ 以上 $2^M$ 未満の整数が $1$ 回ずつ現れます。これらの 排他的論理和は、演算の性質を考えると $(0 \oplus 1 \oplus \cdots \oplus (2^M − 1)) \oplus K$ と書けます（$\oplus$ は排他的論理和演算を 表します）。この式の括弧で囲った部分については、排他的論理和が $2^M − 1$ になるペアを偶数個作れるので $0$ になります。つまり式の値は $K$ になります。
よって $K$ に関しても題意の排他的論理和は $K$ であり、この数列は与えられた条件を満たすことが分かり
ます。 -->

When $K \ge 2^M$, it's obvious that a solution doesn't exist because the exclusive OR of integers less than $2^M$ can never exceed $2^M$. Let's consider the case when this condition doesn't hold:
* When $M = 0$, $a$ is unique and it's a solution for $K = 0$.
* When $M = 1$, we can enumerate and see that a solution exists for $K = 0$ but not for $K = 1$.
* When $M \ge 2$, a solution exists for any $K$ between $0$ and $2^M$. We'll demonstrate this by explicitly constructing $a$.

Let's denote the sequence of integers from $0$ to $2^M$ (excluding $K$) in ascending order as $b$. Also, let's denote the reverse of $b$ as $c$. Then, we can form a sequence $a$ by concatenating $b$, $K$, and $c$ in this order.

This is because, for any $i$ in the range $0 \le i < 2^M$, $i \ne K$, there's exactly one occurrence of $K$ and two occurrences of other numbers between any two instances of $i$ in this sequence. Therefore, the non-$K$ numbers cancel out, resulting in the exclusive OR being equal to $K$.

Furthermore, between any two occurrences of $K$, each integer from $0$ to $2^M - 1$, excluding $K$, appears exactly once. Considering the properties of the XOR operation, the exclusive OR of these integers can be expressed as $(0 \oplus 1 \oplus \cdots \oplus (2^M − 1)) \oplus K$. The part within the parentheses yields $0$ since an even number of pairs that XOR to $2^M - 1$ can be formed, making the overall result equal to $K$.

Hence, the sequence satisfies the given conditions for the exclusive OR, concluding that it indeed provides a solution for the given problem.

---

<!-- ### 考えたこと

こういうのはまずは小さい $M$ で作ってみる。

$M = 0$ のとき、 $0$ が $2$ 個しかなくて、作れる数列も “0 0” しかない。$K = 0$ ならこれを出力して、$K > 0$ なら $-1$。

$M = 1$ のとき、“0 0 1 1” とかだけど、どう並べても $K = 0$ にしかできない。

$M \ge 2$ のとき この辺りから色んな $K$ で作れることがわかってくる。まず $K=0$ のときは、例えば $M=3$ だったら

* 0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 0

とかで OK。$K \ge 2^M$ のときは明らかにダメなので、$1 \le K < 2^M$ の場合を考える。実は必ず作れることがわかる。

例えば、$M = 3, K = 5$ のとき

$$
0 \oplus 5 = 5
1 \oplus 4 = 5
2 \oplus 7 = 5
3 \oplus 6 = 5
$$

となっていることを利用して、

* $0, 5, 1, 4, 5, 0, 4, 1, 2, 7, 3, 6, 7, 2, 6, 3$

とかで作ることができた。つまり「前半は 0 xor 5 と 1 xor 4 を使う」「後半は 2 xor 7 と 3 xor 6 を使う」という風にしている。なんかうまいことできてる。あとは各 K
 に対してこういうペアリングが求められればよくて

$$
0 \oplus K = K //
1 \oplus (1 \oplus K) = K //
2 \oplus (2 \oplus K) = K 
$$

を列挙すれば、(被りはあるが) ペアリングをすべて求めることができた。 -->

### Idea

Let's start by creating sequences for small values of $M$.

When $M = 0$, there are only two zeros, so the only possible sequence is "0 0". If $K = 0$, output this sequence; otherwise, output "-1".

When $M = 1$, we have sequences like "0 0 1 1", but no arrangement results in $K = 0$.

As $M \ge 2$, we realize that we can achieve various values of $K$. For example, when $K = 0$ and $M = 3$:

* $0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 0$

works fine. When $K \ge 2^M$, it's obviously not feasible, so let's consider the case $1 \le K < 2^M$. Interestingly, it's always possible to construct a sequence.

For instance, when $M = 3$ and $K = 5$:

$$
0 \oplus 5 = 5 \\
1 \oplus 4 = 5 \\
2 \oplus 7 = 5 \\
3 \oplus 6 = 5
$$

Using this property:

* We can construct: $0, 5, 1, 4, 5, 0, 4, 1, 2, 7, 3, 6, 7, 2, 6, 3$.

Essentially, we pair the first half using "0 xor 5" and "1 xor 4", and the second half using "2 xor 7" and "3 xor 6". It's quite clever. We just need to find such pairings for each $K$. By enumerating:

$$
0 \oplus K = K \\
1 \oplus (1 \oplus K) = K \\
2 \oplus (2 \oplus K) = K 
$$

(Although there might be duplicates), we can obtain all the pairings.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve(int M, int K) {
    if (M == 0) {
        if (K != 0) cout << -1 << endl;
        else cout << "0 0" << endl;
        return;
    }
    if (M == 1) {
        if (K != 0) cout << -1 << endl;
        else cout << "0 0 1 1" << endl;
        return;
    }

    if (K >= (1<<M)) {
        cout << -1 << endl;
        return;
    }
    if (K == 0) {
        for (int bit = 0; bit < (1<<M); ++bit) {
            cout << bit << " ";
        }
        for (int bit = (1<<M)-1; bit >= 0; --bit) {
            cout << bit << " ";
        }
        cout << endl;
        return;
    }
                

    using pint = pair<int,int>;
    vector<pint> v;
    for (int bit = 0; bit < (1<<M); ++bit) {
        v.push_back(pint(min(bit, bit^K), max(bit, bit^K)));
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());

    for (int i = 0; i < v.size(); i += 2) {
        cout << v[i].first <<  " " << v[i].second << " "
             << v[i+1].first << " " << v[i+1].second << " "
             << v[i].second << " " << v[i].first << " "
             << v[i+1].second << " " << v[i+1].first << " ";
    }
    cout << endl;
}

int main() {
    int M, K; cin >> M >> K;
    solve(M, K);
}
```