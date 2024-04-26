<!-- # E 問題 - [Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e)

**【問題概要】**

𝑁 個の品物があって、𝑖 番目の品物の重さは 𝑤𝑖、価値は 𝑣𝑖 で与えられている。
この 𝑁 個の品物から「重さの総和が 𝑊 を超えないように」いくつか選びます。このとき選んだ品物の価値の総和の最大値を求めよ。

**【制約】**

* 1≤𝑁≤100
* 1≤𝑊≤109
* 1≤𝑤𝑖≤𝑊
* 1≤𝑣𝑖≤103
* 入力はすべて整数

## キーポイント

* ナップサック DP
* dp[W] := 重み W 以下での価値の最大値 -> dp[V] := 価値 V 以上を達成できる重さの最小値

## 解法

[D 問題](https://qiita.com/drken/items/dc53c683d6de8aeacf5a#d-%E5%95%8F%E9%A1%8C---knapsack-1)と問題文はまったく同一で、 **制約だけ変わりました** 。
今回はさっきと同じように

* dp[ i ][ sum_w ] := i-1 番目までの品物から重さが sum_w を超えないように選んだときの、価値の総和の最大値

としてしまうとテーブルサイズが 𝑂(𝑁𝑊) となり、今回は 𝑊≤109 なので大変なことになります。そこで発想を転換してあげて、

* dp[ i ][ sum_v ] := i-1 番目までの品物から価値が sum_v となるように選んだときの、重さの総和の最小値

としてあげます。この DP テーブルの更新自体は、今までと同じような発想で素朴にできると思います:

```
// i 番目の品物を選ぶ場合
chmin(dp[i+1][sum_v], dp[i][sum_v - v[i]] + w[i]);

// i 番目の品物を選ばない場合
chmin(dp[i+1][sum_v], dp[i][sum_v]);
```

問題となるのはこの DP テーブルから実際の答えを得る部分ですが、それも単純で

---

dp[ N ][ sum_v ] の値が、W 以下であるような、sum_v の値の最大値

---

を求めてあげればよいです。計算量は、

* 𝑁 個の品物がある
* sum_v のとりうる値の上限値は、𝑉=max𝑖(𝑣𝑖) として、𝑁𝑉

ということでノード数が 𝑂(𝑁2𝑉) であり、各ノードにつき遷移は高々 2 通りなので、全体の計算量も 𝑂(𝑁2𝑉) になります。 -->


<!-- 
## 類題

添字を入れ替える系の発想をする問題を集めてみました。忘れた頃に見かけるイメージです。

* [ARC 057 B - 高橋君ゲーム](https://atcoder.jp/contests/arc057/tasks/arc057_b)
* [AOJ 2263 ファーストアクセプタンス](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2263)
* [ABC 032 D ナップサック問題](https://atcoder.jp/contests/abc032/tasks/abc032_d)　(半分全列挙も含みます) -->

# Problem E - [Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e)

**[Problem Description]**

There are $N$ items, and the $i$-th item has a weight of $w_i$ and a value of $v_i$.

Choose some of these $N$ items so that the total weight does not exceed $W$. Find the maximum possible total value of the selected items.

**[Constraints]**

* $1 \le N \le 100$
* $1 \le W \le 10^9$
* $1 \le w_i \le W$
* $1 \le v_i \le 10^3$
* All inputs are integers

## Key Points

* Knapsack DP
* $dp[W]$ := Maximum value with weight at most $W \to dp[V]$ := Minimum weight to achieve value at least $V$

## Approach

The problem statement is exactly the same as [Problem D](https://qiita.com/drken/items/dc53c683d6de8aeacf5a#d-%E5%95%8F%E9%A1%8C---knapsack-1), except for the **constraints**. Now, let's tackle it similarly.

If we define:

* $dp[i][sum_w]$: Maximum total value obtained by selecting items up to the $(i-1)$-th item, ensuring that the total weight is at most $sum_w$

then the size of the DP table would be $O(NW)$, and since $W \le 10^9$, it would be very large. So, let's change our perspective:

* $dp[i][sum_v]$: Minimum total weight obtained by selecting items up to the $(i-1)$-th item, ensuring that the total value is $sum_v$

The updates to this DP table can be done with a similar approach as before:

```cpp
// When selecting the i-th item
chmin(dp[i+1][sum_v], dp[i][sum_v - v[i]] + w[i]);

// When not selecting the i-th item
chmin(dp[i+1][sum_v], dp[i][sum_v]);
```

The challenge now lies in obtaining the actual answer from this DP table, which is straightforward:

---

The maximum value of $sum_v$ for which $dp[N][sum_v]$ is less than or equal to $W$.

---

```cpp
#include <iostream>
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
const long long INF = 1LL<<60;

const int MAX_N = 110;
const int MAX_V = 100100;

// 入力
int N;
long long W, weight[MAX_N], value[MAX_N]; // 品物の個数は 100 個なので少し余裕持たせてサイズ 110 に

// DPテーブル
long long dp[MAX_N][MAX_V];

int main() {
    cin >> N >> W;
    for (int i = 0; i < N; ++i) cin >> weight[i] >> value[i];

    // 初期化
    for (int i = 0; i < MAX_N; ++i) for (int j = 0; j < MAX_V; ++j) dp[i][j] = INF;

    // 初期条件
    dp[0][0] = 0;

    // DPループ
    for (int i = 0; i < N; ++i) {
        for (int sum_v = 0; sum_v < MAX_V; ++sum_v) {

            // i 番目の品物を選ぶ場合
            if (sum_v - value[i] >= 0) chmin(dp[i+1][sum_v], dp[i][sum_v - value[i]] + weight[i]);

            // i 番目の品物を選ばない場合
            chmin(dp[i+1][sum_v], dp[i][sum_v]);
        }
    }

    // 最適値の出力
    long long res = 0;
    for (int sum_v = 0; sum_v < MAX_V; ++sum_v) {
        if (dp[N][sum_v] <= W) res = sum_v;
    }
    cout << res << endl;
}
```

The complexity is as follows:

* There are $N$ items.
* The maximum value of $sum_v$ is $V = \max(v_i)$, so the number of nodes is $O(N^2V)$.
Since each node has at most two transitions, the overall complexity is $O(N^2V)$.

### Similar Problems

Here are some problems that require a change in the indices. They tend to appear just when you've forgotten about them.

* [ARC 057 B - Takahashi's Game](https://atcoder.jp/contests/arc057/tasks/arc057_b)
* [AOJ 2263 - First Acceptance](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2263)
* [ABC 032 D - Knapsack Problem](https://atcoder.jp/contests/abc032/tasks/abc032_d) (including exhaustive search)