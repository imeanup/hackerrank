<!-- # D 問題 - [Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d)

**【問題概要】**

$N$ 個の品物があって、$i$ 番目の品物の重さは $w_i$、価値は $v_i$ で与えられている。
この $N$ 個の品物から「重さの総和が $W$ を超えないように」いくつか選びます。このとき選んだ品物の価値の総和の最大値を求めよ。

**【制約】**

* $1 \le N \le 100$
* $1 \le W \le 10^5$
* $1 \le w_i \le W$
* $1 \le v_i \le 10^9$
* 入力はすべて整数

## キーポイント

* ナップサック DP
* 「部分和」を DP テーブルの添字に付け加える

## 解法

ついに DP というと必ずといっていいほど紹介される[ナップサック問題](https://qiita.com/drken/items/a5e6fe22863b7992efdb)に到達しました！！！

一応注意点として、条件反射で「ナップサックだから DP」とはならないようにすることが重要です。ナップサック問題も様々な制約の入れ方によって多様な問題を作り出すことができます。

さて、ここまで DP のイメージを固めて来た我々にとって、ナップサック DP もほとんどやることは変わらないです。今回の問題も各品物に対して「選ぶ」「選ばない」という 2 通りの選択肢があります。よって全探索すると $2^n$ 通りの選択肢を試すことになります。いかにも DP が効きそうな局面です。

まずは試しに

* $dp[i] := i-1$ 番目までの品物から重さが $W$ を超えないように選んだときの、価値の総和の最大値

としてみます。しかしこのままでは、詰まってしまいます。$dp[i]$ から $dp[i+1]$ への遷移を考えるときに $dp[i]$ に対して品物 $(w[i], v[i])$ を加えるか否かを考えるわけですが、加えたときに重さが $W$ を超えてしまうのかどうかがわからないという問題が起こります。そこで以下のように修正します:

* $dp[i][sum_w] := i-1$ 番目までの品物から重さが $sum_w$ を超えないように選んだときの、価値の総和の最大値

そして、$dp[i][sum_w]　(sum_w = 0, 1, \cdots, W)$ の値が求まっている状態で、$dp[i + 1][sum_w]　(sum_w = 0, 1, \cdots, W)$ を更新していくことを考えます。場合分けして考えてみましょう。

### 品物 $(w[i], v[i])$ を選ぶとき

選んだことによって、価値 $v[i]$ が加算されます。

$\max(dp[i + 1][sum_w], dp[i][sum_w - w[i] ] + v[i]);$

と更新します (ここでは「貰う DP」で考えています)。ただし、$sum_w - w[i] \ge 0$ である必要があるので、その場合のみこの更新を行います。

### 品物 $(w[ i ], v[ i ])$ を選ばないとき

$dp[i][sum_w]$ に対して特に何も価値を加算しないので

$\max(dp[i + 1][sum_w], dp[i][sum_w])$

と更新します。

[![DP遷移図・改.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F09416ec7-fa46-132e-cd00-d2197a1d0444.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d5955ba71e6477affaaf36d5da9297f8)](https://camo.qiitausercontent.com/8a10e9bd1eb18da42109865422e8dd128e1d2a6b/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f30393431366563372d666134362d313332652d636430302d6432313937613164303434342e6a706567)

具体例として、品物が $6$ 個で $(w, v) = (2,3), (1,2), (3,6), (2,1), (1,3), (5,85)$ の場合の遷移の様子を図示してみました。

* 赤マスについては「選ぶ」選択をした方が価値が高い (+ 85 になるのでそれはそう)
* 黄マスについては「選ばない」選択をした方が価値が高い

といった様子が見て取れます。なお、計算量は $O(NW)$ になります。

```cpp
#include <iostream>
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
const long long INF = 1LL<<60;

// 入力
int N;
long long W, weight[110], value[110]; // 品物の個数は 100 個なので少し余裕持たせてサイズ 110 に

// DPテーブル
long long dp[110][100100] = {0};


int main() {
    cin >> N >> W;
    for (int i = 0; i < N; ++i) cin >> weight[i] >> value[i];

    // DPループ
    for (int i = 0; i < N; ++i) {
        for (int sum_w = 0; sum_w <= W; ++sum_w) {

            // i 番目の品物を選ぶ場合
            if (sum_w - weight[i] >= 0) {
                chmax(dp[i+1][sum_w], dp[i][sum_w - weight[i]] + value[i]);
            }

            // i 番目の品物を選ばない場合
            chmax(dp[i+1][sum_w], dp[i][sum_w]);
        }
    }

    // 最適値の出力
    cout << dp[N][W] << endl;
}
```


## DP 定義の仕方の微妙な違いについて

ナップサック問題に対する DP を

* $dp[i][sum_w] := i-1$ 番目までの品物から **重さが sum_w 以下となる** ように選んだときの、価値の総和の最大値

と定義して解きましたが、よく似た定義として

* $dp[i][sum_w] := i-1$ 番目までの品物から **重さがちょうどピッタリ sum_w となる** ように選んだときの、価値の総和の最大値

としたくなる方もいるでしょう。どちらでやっても解けますし、実はループを回すときの緩和式はまるっきり一緒になります。違いが出て来るのは **初期条件** だけです。

* 前者の初期条件： $dp[0][w] = 0$　($w$ は任意)
* 後者の初期条件： $dp[0][0] = 0$　($0$ 以外の $w$ に対しては $dp[0][w] = -INF$)

## 類題

添字を付け加える系の DP を集めてみました。

* [TDPC A - コンテスト](https://atcoder.jp/contests/tdpc/tasks/tdpc_contest)
* [TDPC D - サイコロ](https://atcoder.jp/contests/tdpc/tasks/tdpc_dice)
* [ABC 015 D - 高橋くんの苦悩](https://atcoder.jp/contests/abc015/tasks/abc015_4)
* [1年生 (JOI 2010 予選 D)](https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d)
* [パスタ (JOI 2011 予選 D)](https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d)
* [暑い日々 (JOI 2012 予選 D)](https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d)
* [古本屋 (JOI 2010 本選 B)](https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho2)
* [AOJ 2566 Restore Calculation](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2566) -->


# D Problem - [Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d)

> [GFG: 0-1 KnapSack](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)

**[Problem Summary]**

There are N items, where the i-th item has a weight of w_i and a value of v_i. From these N items, choose some so that the total weight does not exceed W. Find the maximum possible total value of the selected items.

**[Constraints]**

* $1 \le N \le 100$
* $1 \le W \le 10^5$
* $1 \le w_i \le W$
* $1 \le v_i \le 10^9$
* All inputs are integers.

## Key Points

- Knapsack DP
- Adding "subset sum" as an index in the DP table

## Approach

We have finally arrived at the famous [knapsack problem](https://qiita.com/drken/items/a5e6fe22863b7992efdb) when it comes to DP!!!

As a precautionary note, it's important not to reflexively associate "knapsack" with "DP". The knapsack problem can also be varied by imposing different constraints.

Now, for us who have solidified our understanding of DP up to this point, knapsack DP is not much different. In this problem, as well, each item has two choices: "choose" or "not choose". Therefore, exhaustive search would involve trying out $2^n$ possibilities. It seems like a perfect fit for DP.

Let's try defining:

- $dp[i]$: Maximum total value of items chosen up to the $i$-th item ($dp[i]$ represents the maximum total value obtained by selecting items until the $(i-1)$-th item).

However, this approach will lead us to a dead end. When considering the transition from $dp[i]$ to $dp[i+1]$, we face the problem of not knowing whether adding the item $(w[i], v[i])$ will exceed the weight limit $W$. So, we need to make a modification:

- $dp[i][sum_w]$: Maximum total value of items chosen up to the $i$-th item with a total weight not exceeding $sum_w$ ($dp[i][sum_w]$ represents the maximum total value obtained by selecting items until the $(i-1)$-th item, with a total weight not exceeding $sum_w$).

Now, given the values of $dp[i][sum_w]$ for $sum_w = 0, 1, \cdots, W$, we want to update $dp[i+1][sum_w]$ for the same range of $sum_w$. Let's consider the following cases:

### Choosing item $(w[i], v[i])$

When we choose the item, its value $v[i]$ is added to the total value. We update as follows:

- $dp[i+1][sum_w] = \max(dp[i+1][sum_w], dp[i][sum_w - w[i]] + v[i])$

Note: We perform this update only if $sum_w - w[i] \ge 0$.

### Not choosing item $(w[i], v[i])$

When we don't choose the item, there is no change in the total value. We update as follows:

- $dp[i+1][sum_w] = \max(dp[i+1][sum_w], dp[i][sum_w])$

![DP Transition Diagram](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F09416ec7-fa46-132e-cd00-d2197a1d0444.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d5955ba71e6477affaaf36d5da9297f8)

For example, the transition behavior for $6$ items with weights and values $(w, v) = (2,3), (1,2), (3,6), (2,1), (1,3), (5,85)$ is illustrated. 

- In the red cells, it's more beneficial to "choose" (adds 85 to the total value).
- In the yellow cells, it's more beneficial to "not choose".

The time complexity is $O(NW)$.

```cpp
#include <iostream>
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
const long long INF = 1LL<<60;

// 入力
int N;
long long W, weight[110], value[110]; // 品物の個数は 100 個なので少し余裕持たせてサイズ 110 に

// DPテーブル
long long dp[110][100100] = {0};


int main() {
    cin >> N >> W;
    for (int i = 0; i < N; ++i) cin >> weight[i] >> value[i];

    // DPループ
    for (int i = 0; i < N; ++i) {
        for (int sum_w = 0; sum_w <= W; ++sum_w) {

            // i 番目の品物を選ぶ場合
            if (sum_w - weight[i] >= 0) {
                chmax(dp[i+1][sum_w], dp[i][sum_w - weight[i]] + value[i]);
            }

            // i 番目の品物を選ばない場合
            chmax(dp[i+1][sum_w], dp[i][sum_w]);
        }
    }

    // 最適値の出力
    cout << dp[N][W] << endl;
}
```

## About the Subtle Difference in DP Definitions

When solving the knapsack problem with DP, I defined it as:

* $dp[i][sum_w]$: Maximum total value obtained by selecting items up to the $(i-1)$-th item, ensuring that the **total weight is at most sum_w**.

Some might prefer a similar definition:

* $dp[i][sum_w]$: Maximum total value obtained by selecting items up to the $(i-1)$-th item, ensuring that the **total weight is exactly sum_w**.

Both approaches can solve the problem, and in fact, the relaxation formula used during iteration is exactly the same. The difference lies only in the **initial conditions**:

* Initial condition for the former: $dp[0][w] = 0$ (for any $w$).
* Initial condition for the latter: $dp[0][0] = 0$ (and $dp[0][w] = -\infty$ for $w \neq 0$).

## Related Problems

Here are some DP problems that involve adding indices:

* [TDPC A - Contest](https://atcoder.jp/contests/tdpc/tasks/tdpc_contest)
* [TDPC D - Dice](https://atcoder.jp/contests/tdpc/tasks/tdpc_dice)
* [ABC 015 D - Takahashi's Trouble](https://atcoder.jp/contests/abc015/tasks/abc015_4)
* [First Grader (JOI 2010 Qualification D)](https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d)
* [Pasta (JOI 2011 Qualification D)](https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d)
* [Hot Days (JOI 2012 Qualification D)](https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d)
* [Secondhand Bookstore (JOI 2010 Final B)](https://atcoder.jp/contests/joi2011ho/tasks/joi2011ho2)
* [AOJ 2566 Restore Calculation](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2566)