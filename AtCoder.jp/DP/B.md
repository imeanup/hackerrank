<!-- # B 問題 - [Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b)

**【問題概要】**
$N$ 個の足場があって、$i$ 番目の足場の高さは $h_i$ です。
最初、足場 $1$ にカエルがいて、ぴょんぴょん跳ねながら足場 $N$ へと向かいます。カエルは足場 $i$ にいるときに

* 足場 $i$ から足場 $i+1$ へと移動する (そのコストは $|h_i−h_{i+1}|$)
* 足場 $i$ から足場 $i+2$ へと移動する (そのコストは $|h_i−h_{i+2}|$)
* ...
* 足場 $i$ から足場 $i+K$ へと移動する (そのコストは $|h_i−h_{i+K}|$)

のいずれかの行動を選べます。カエルが足場 1 から足場 𝑁 へと移動するのに必要な最小コストを求めよ。

**【制約】**

* $2 \le N \le 10^5$
* $1 \le K \le 100$

## 解法

[A 問題](https://qiita.com/drken/items/dc53c683d6de8aeacf5a#a-%E5%95%8F%E9%A1%8C---frog-1)とほとんど同じですが、毎ターンの選択肢が「$2$ 通り」から「$K$ 通り」に増えました。それでも実装はほとんど一緒で、今まで

```cpp
chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
```

としていたところを (今回は「配る DP」でやってみます)

```cpp
chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
...
chmin(dp[i + K], dp[i] + abs(h[i] - h[i + K]));
```

とするだけですね。ただし $K$ 個書き並べることはできないので for 文で回すことにします。そうすると全体の実装は以下のようになるでしょう。計算量は各ノードにつき高々 $K$ 通りの遷移があるので、$O(NK)$ になります。

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

const long long INF = 1LL << 60;

// 入力
int N;
long long h[110000];

// DP テーブル
long long dp[110000];

int main() {
    int N, K; cin >> N >> K;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 110000; ++i) dp[i] = INF;

    // 初期条件
    dp[0] = 0;

    // ループ
    for (int i = 0; i < N; ++i) {
        for (int j = 1; j <= K; ++j) {
            chmin(dp[i + j], dp[i] + abs(h[i] - h[i + j]));
        }
    }

    // 答え
    cout << dp[N-1] << endl;
}
```

## 類題

* [ABC 099 C - Strange Bank](https://atcoder.jp/contests/abc099/tasks/abc099_c) -->


# Problem B - [Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b)

**[Problem Summary]**

There are $N$ stepping stones, and the height of the $i$-th stone is $h_i$.
Initially, a frog is on stone $1$ and jumps from stone to stone until it reaches stone $N$. When the frog is on stone $i$, it can:

* Move from stone $i$ to stone $i+1$ (cost: $|h_i−h_{i+1}|$)
* Move from stone $i$ to stone $i+2$ (cost: $|h_i−h_{i+2}|$)
* ...
* Move from stone $i$ to stone $i+K$ (cost: $|h_i−h_{i+K}|$)

The task is to find the minimum cost required for the frog to move from stone 1 to stone $N$.

**[Constraints]**

* $2 \le N \le 10^5$
* $1 \le K \le 100$

## Approach

It's almost the same as the [A problem](/DP/A.md), but now the choices per turn have increased from $2$ to $K$. Nevertheless, the implementation is almost the same. Instead of what we had before:

```cpp
chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
```

this time (using "distributive DP"):

```cpp
chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
...
chmin(dp[i + K], dp[i] + abs(h[i] - h[i + K]));
```

We just need to iterate with a for loop since we can't write $K$ items individually. Then the overall implementation will look like this. The time complexity is at most $O(NK)$ since each node has at most $K$ possible transitions.

<details><summary><b> Forward DP</b> </summary><br>

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

const long long INF = 1LL << 60;

// 入力
int N;
long long h[110000];

// DP テーブル
long long dp[110000];

int main() {
    int N, K; cin >> N >> K;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 110000; ++i) dp[i] = INF;

    // 初期条件
    dp[0] = 0;

    // ループ
    for (int i = 0; i < N; ++i) {
        for (int j = 1; j <= K; ++j) {
            chmin(dp[i + j], dp[i] + abs(h[i] - h[i + j]));
        }
    }

    // 答え
    cout << dp[N-1] << endl;
}

```

</details>

<details><summary><b>Reversed DP </b></summary>

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
template<class T> inline bool chmin(T&a, T b){
    if (a > b) {
        a = b;
        return 1;
    }
    return 0;
}
const ll INF = INT_MAX;
const int MAX = 100005;
int H[MAX], dp[MAX];

int main(){
    int N, K; cin >> N >> K;
    for (int i = 0; i < N; i++) cin >> H[i];
    for (int i = 0; i < N; i++) dp[i] = INF;
    dp[0] = 0;
    for (int i = 0; i < N; i++){
        for (int j = 1; j <= K; j++){
            if (i - j >= 0) chmin(dp[i], dp[i-j] + abs(H[i] - H[i-j]));
        }
    }
    cout << dp[N-1] << "\n";
    return 0;
}
```

</details>

## Similar Problems

* [ABC 099 C - Strange Bank](https://atcoder.jp/contests/abc099/tasks/abc099_c)