<!-- # C 問題 - [Vacation](https://atcoder.jp/contests/dp/tasks/dp_c)

**【問題概要】**

$N$ 日間の夏休みです。$i$ 日目には、

$A$: 海で泳ぐ。幸福度 $a_i$ を加算
$B$: 山で虫取りする。幸福度 $b_i$ を加算
$C$: 家で宿題をする。幸福度 $c_i$ を加算

の三択の中から好きなものを選ぶことができます。ただし、$2$ 日連続で $A, B, C$ のうちの同一種類の活動を選択をすることはできません。この制約下で最終的に得られる幸福度の総和を最大にせよ。

**【制約】**

* $1 \le N \le 10^5$

## キーポイント

* $DP$ テーブルに添字を付け加えて拡張する

## 解法

もし「$2$ 日連続で同一種類の選択をできない」という制約がなければ、単純に各日程ごとに $\max(a_i, b_i, c_i)$ を合計するだけですね。実際は制約があるのでそれに応じた解法を考えてあげる必要があります。

これも今までと同じように自然な $DP$ で解くことができます (やはり $0$-indexed にして考えます...添字が少しややこしいです)。

* $dp[i]$ := 最初の $i$ 日間で得られる幸福度の最大値 ($= i-1$ 日目までで得られる幸福度の最大値)

とすることを考えてみましょう。初期条件は活動開始前には幸福度は $0$ なので、

* $dp[0] = 0$

とあります。このような形式の $DP$ を考えたくなる理由として、

* 全探索で解こうとすると、各日程につき $3$ 通りの選択がある (本当は初日以外は $2$ 通りだがざっくり) ので $3^n$ 通りを調べることになってしまう
* よく考えると、$i$ 日目の選択をする上で、ずっと昔にどういう選択をしていたかの情報は不要で、**前日のことだけわかっていればいい**

といったあたりがポイントになるかと思います。このような $i$ 日目にとりうる選択肢が何通りかあって、愚直に全探索すると $O(2^n)$ とか $O(3^n)$ とか $O(K^n)$ とかになるな...という場面では「$dp[i]$ := 最初の $i$ 日間での最適解」の形の $DP$ を検討してみるのはアリだと思います。

[![C.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F18f2a9fb-aa61-d7e2-7e23-3328d9a1cb4d.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b328e72166b8d0fb773491ccd3d8397c)](https://camo.qiitausercontent.com/c220d72853cb37ffff09fe10e8f857ab992b9d2e/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f31386632613966622d616136312d643765322d376532332d3333323864396131636234642e6a706567)

さて、この問題は $A$ 問題や $B$ 問題よりは少し難しくなっています。今我々は、「$i - 1$ 日目までで得られる幸福度の最大値」を表す $dp[i]$ が求められていることを前提に、「$i$ 日目までで得られる幸福度の最大値」を表す $dp[i + 1]$ を求めたいです。

しかしこのままでは、前日の $i-1$ 日目にどの活動を選択していたのかがわからないため、$i$ 日目ではどの活動が選択可能なのかが判然としません。上手く式を立てることができません。そこで $DP$ テーブルを拡張して

* $dp[i + 1][j] := i$ 日目までの活動履歴のうち、最終日である $i$ 日目には活動 $j (0: A, 1: B, 2: C)$ を選んだ場合の、得られる幸福度の最大値

という風にしてあげます。そして今度は $(dp[ i ][ 0 ], dp[ i ][ 1 ], dp[ i ][ 2 ])$ の値が求められている状態で、 $(dp[ i + 1 ][ 0 ], dp[ i + 1 ][ 1 ], dp[ i + 1 ][ 2 ])$ の値を求めることを考えます。$2$ 日連続で同じ活動は選択できないので、

* $dp[ i ][ 0 ]$ から $dp[ i + 1 ][ 1 ]$ への遷移
* $dp[ i ][ 0 ]$ から $dp[ i + 1 ][ 2 ]$ への遷移
* $dp[ i ][ 1 ]$ から $dp[ i + 1 ][ 0 ]$ への遷移
* $dp[ i ][ 1 ]$ から $dp[ i + 1 ][ 2 ]$ への遷移
* $dp[ i ][ 2 ]$ から $dp[ i + 1 ][ 0 ]$ への遷移
* $dp[ i ][ 2 ]$ から $dp[ i + 1 ][ 1 ]$ への遷移

の $6$ 個の遷移があります。以下のようにすればいいでしょう:

---

**【DP 遷移式】**

各 $j (= 0, 1, 2)$ と各 $k (= 0, 1, 2)$ に対して、$j \ne k$ ならば
$\max(dp[ i + 1 ][ k ], dp[ i ][ j ] + a[ i ][ k ])$

---

全体をまとめて、以下のようになります。計算量は各日程間について $6$ 通りと高々定数の遷移しかないので、$O(N)$ ですね。 -->

## Problem C - Vacation

**[Problem Summary]**

It's a summer vacation for $N$ days. On the $i$-th day, you can choose one of the following activities:

- $A$: Swim in the sea, adding happiness value $a_i$.
- $B$: Catch bugs in the mountains, adding happiness value $b_i$.
- $C$: Do homework at home, adding happiness value $c_i$.

However, you cannot choose the same type of activity for two consecutive days. Determine the maximum total happiness value obtained under these constraints.

**[Constraints]**

- $1 \leq N \leq 10^5$

## Key Points

- Extend the DP table by adding indices.

## Approach

If there were no constraint on choosing the same type of activity for two consecutive days, you could simply sum $\max(a_i, b_i, c_i)$ for each day. However, since there is a constraint, you need to consider an approach that accommodates it.

You can solve this problem naturally with DP, similar to before (assuming a 0-indexed approach). Let's consider:

- $dp[i]$: Maximum happiness value obtained in the first $i$ days ($= \text{maximum happiness value obtained in the first } i-1 \text{ days}$)

The initial condition is that the happiness value is $0$ before starting any activity:

- $dp[0] = 0$

The reason for considering this type of $DP$ is that:

- If you try to solve it with exhaustive search, there are $3$ choices for each day ($A$, $B$, or $C$), resulting in examining $3^n$ combinations.
- Upon closer inspection, you realize that, when selecting an activity on the $i$-th day, you only need to know what happened on the previous day, and you don't need to remember choices made long ago.

When you encounter a situation where there are many options for each day ($2^n$, $3^n$, $K^n$, etc.), it's worth considering this type of $DP$.

[![C.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F18f2a9fb-aa61-d7e2-7e23-3328d9a1cb4d.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b328e72166b8d0fb773491ccd3d8397c)](https://camo.qiitausercontent.com/c220d72853cb37ffff09fe10e8f857ab992b9d2e/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f31386632613966622d616136312d643765322d376532332d3333323864396131636234642e6a706567)

Now, let's solve the problem. This problem is slightly more difficult than problem A or B. We are already assuming that $dp[i]$, representing the maximum happiness value obtained in the first $i$ days, is available, and we want to find $dp[i + 1]$ representing the maximum happiness value obtained in the first $i$ days.

However, as it is, we don't know what activity was chosen on the $i - 1$ day, so we don't know which activities are available on the $i$-th day. We need to expand the DP table to:

- $dp[i + 1][j]$: The maximum happiness value obtained on day $i$ among the activities chosen up to day $i - 1$, with activity $j (0: A, 1: B, 2: C)$ chosen on the $i$-th day.

Now, suppose we already have $(dp[i][0], dp[i][1], dp[i][2])$. To find $(dp[i + 1][0], dp[i + 1][1], dp[i + 1][2])$, we need to consider transitions from previous days to the current day. Since the same activity cannot be chosen for two consecutive days, there are $6$ possible transitions:

- Transition from $dp[i][0]$ to $dp[i + 1][1]$
- Transition from $dp[i][0]$ to $dp[i + 1][2]$
- Transition from $dp[i][1]$ to $dp[i + 1][0]$
- Transition from $dp[i][1]$ to $dp[i + 1][2]$
- Transition from $dp[i][2]$ to $dp[i + 1][0]$
- Transition from $dp[i][2]$ to $dp[i + 1][1]$

For each $j (= 0, 1, 2)$ and each $k (= 0, 1, 2)$, if $j \neq k$, we choose:

---

**[DP Transition Formula]**

$\max(dp[i + 1][k], dp[i][j] + a[i][k])$

---

Overall, the solution looks like this, with a time complexity of $O(N)$.

<details><summary>C++ </summary>

```cpp

```

</details>