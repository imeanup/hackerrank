## [E - Vitamin Balance](https://atcoder.jp/contests/abc390/tasks/abc390_e) 

この問題は、各ビタミン $i (1 \le i \le 3)$ について、「摂取カロリーの合計が $j (0\le j \le X)$ 以下となるように食べ物を選んで食べた時のビタミン $i$ の摂取量の最大値（他のビタミンについては考慮しない）」を動的計画法によって、あらかじめ求めておくことによって解くことができます。

最初に、「摂取カロリーの合計が **ちょうど** $j$ となるように食べ物を選んで食べた時のビタミン $i$ の摂取量の最大値」の計算を行います。\

$dp_i[k][j] (1\le i \le 3, 0\le j \le X, 0 \le k \le N)$ で、「$1$ 個目から $k$ 個目までの食べ物の中から摂取カロリーの合計が **ちょうど** $j$ となるように食べ物を選んで食べた時のビタミン $i$ の摂取量の最大値（できない場合は$−\infty$）」を表すとします。

まず、$dp_i[0][0] = 0, dp_i[0][j] = −1 (1 \le j \le X)$ です。

次に、食べ物 $k (1 \le k \le N)$ がビタミン $i$ を含まないならば $dp_i[k][j] = dp_i[k−1][j]$ です。含むならば、食べるか食べないかの選択によって、$dp_i[k][j] = \max⁡(dp_i[k−1][j], dp_i[k−1][j−C_k] + A_k) (C_k \ge j)$ となります。$j\ge c_k$ については $dp_i[k][j] = dp_i[k−1][j]$ となります。

このように更新を繰り返した時の、$dp_i[N][j]$ が求めたいものです。

次に、「摂取カロリーの合計が $j (0 \le j \le X)$ 以下となるように食べ物を選んで食べた時のビタミン $i$ の摂取量の最大値」$M_{i,j}$ は、$M_{i,j} = \displaystyle\max⁡_{0\le j' \le j} dp_i[N][j']$ と書くことができます。 これは、$M_{i,0} = dp_i[N][0], M_{i,j} = \max⁡(M_{i, j−1}, dp_i[N][j])$ として逐次的に計算することができます。

最後に、ビタミン $i (1\le i \le 3)$ の摂取のために食べる食べ物のカロリーの合計が $si$ 以下である時の 「ビタミン $1,2,3$ のうちもっとも摂取量が少ないものの摂取量」は $\min⁡(M_{1,s_1}, M_{2,s_2}, M_{3,s_3})$ で与えられるため、求めたい値は

$$
\max_{⁡s_1 + s_2 + s_3 = X} \min⁡(M_{1,s_1},M_{2,s_2}, M_{3,s_3})
$$

です。$\min⁡(M_{1,s_1}, M_{2,s_2}, M_{3,s_3})$ を最大化する組み合わせ $(s_1, s_2, s_3) = (S_1, S_2, S_3)$ は貪欲法によって、求めることができます。
具体的には、$S_1 = S_2 = S_3 = 0$ から始めて次の操作をちょうど $X$ 回繰り返します。

> $M_{1,S_1}, M_{2,S_2}, M_{3,S_3}$ を比較する。
> その中で一番小さいものが $M_{i, S_i}$ であったとき、$S_i$ を $1$ 増加させる。
> 最も小さいものが複数ある場合はその中からどれを選んでも良い。

求まった $(S_1, S_2, S_3)$ に対する値 $\min⁡(M_{1,S_1}, M_{2,S_2}, M_{3,S_3})$ が最終的な答えとなります。
時間計算量は全体で $O(NX)$ であり、十分高速です。
よって、この問題を解くことができました。

c++ による実装例:

---

```cpp
#include <bits/stdc++.h>
using namespace std;

#define M 5000
#define INF (int)2e+9

int main(void){
	int n,x,v,a,c;
	int dp[3][M+1]={};
	for(int i=0;i<3;i++){
		for(int j=0;j<M;j++){
			dp[i][j+1]=-INF;
		}
	}

	cin>>n>>x;
	for(int i=0;i<n;i++){
		cin>>v>>a>>c;
		for(int j=x;j>=c;j--){
			dp[v-1][j]=max(dp[v-1][j],dp[v-1][j-c]+a);
		}
	}
	for(int i=0;i<3;i++){
		for(int j=0;j<x;j++){
			dp[i][j+1]=max(dp[i][j],dp[i][j+1]);
		}
	}

	int idx[3]={0,0,0};
	for(int i=0;i<x;i++){
		if((dp[0][idx[0]]<=dp[1][idx[1]])&&(dp[0][idx[0]]<=dp[2][idx[2]]))idx[0]++;
		else if((dp[1][idx[1]]<=dp[0][idx[0]])&&(dp[1][idx[1]]<=dp[2][idx[2]]))idx[1]++;
		else idx[2]++;
	}
	cout<<min(dp[0][idx[0]],min(dp[1][idx[1]],dp[2][idx[2]]))<<endl;
	return 0;
}
```

---

> Knapsack

This problem can be solved by using dynamic programming, for each vitamin $i (1 \le i \le 3)$, precalculatng the maximum intake of vitamin $i$ (ignoring the other vitamin) so that the total calorie intake does not exceed $j (0\le j \le X)$.

Initially, calculate the maximum intake of vitamin $i$ when foods are chosen and eaten so that the total calorie intake is **exactly** $j$.

Let $dp_i[k][j] (1\le i \le 3, 0\le j \le X, 0 \le k \le N)$ represent the maximum intake of vitamin $i$ when foods from $1$-th to $k$-th foods are chosen and eaten so that the total calorie intake is **exactly** $j$ (if this is not possible, use $−\infty$).

First, $dp_i[0][0] = 0, dp_i[0][j] = −1 (1 \le j \le X)$.

Next, if food $k (1 \le k \le N)$ does not contain vitamin $i$, then $dp_i[k][j] = dp_i[k−1][j]$. If it does contain vitamin $i$, then $dp_i[k][j] = \max⁡(dp_i[k−1][j], dp_i[k−1][j−C_k] + A_k) (C_k \ge j)$, depending on whether or not to eat it. For $j\ge c_k$, $dp_i[k][j] = dp_i[k−1][j]$.

What we want to find is $dp_i[N][j]$ after repeated updates like this.

Next, we consider $M_{i,j}$, the "maximum intake of vitamin $i$ when choosing and eating foods that result in a total calorie intake of less than or equal to $j (0 \le j \le X)$," can be written as $M_{i,j} = \displaystyle \max⁡_{0\le j' \le j} dp_i[N][j']$. This can be calculated sequentially as $M_{i,0} = dp_i[N][0], M_{i,j} = \max⁡(M_{i, j−1}, dp_i[N][j])$.

Finally, when the total calories of the foods eaten to obtain vitamin $i (1\le i \le 3)$ are less than or equal to $s_i$, the "lowest intake of vitamins $1, 2, 3$" is given by $\min⁡(M_{1,s_1}, M_{2,s_2}, M_{3,s_3})$, so the value we want to find is

$$
\max_{⁡s_1 + s_2 + s_3 = X} \min⁡(M_{1,s_1},M_{2,s_2}, M_{3,s_3})
$$

The combination $(s_1, s_2, s_3) = (S_1, S_2, S_3)$ that maximizes $\min⁡(M_{1,s_1}, M_{2,s_2}, M_{3,s_3})$ can be found using the greedy algorithm.

Specifically, starting from $S_1 = S_2 = S_3 = 0$, repeat the following operation exactly $X$ times.

> Compare $M_{1,S_1}, M_{2,S_2}, M_{3,S_3}$.
>
> If the smallest of these is $M_{i, S_i}$, increase $S_i$ by $1$.
>
> If there are multiple smallest combinations, any of them can be chosen.

The value $\min⁡(M_{1,S_1}, M_{2,S_2}, M_{3,S_3})$ found for $(S_1, S_2, S_3)$ is the final answer.
The total time complexity is $O(NX)$, which is sufficiently fast.
Hence, we have solved this problem.

Example implementation in c++:

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = unsigned long long;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}

const int INF = 1001001001;

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, x;
    cin >> n >> x;
    vector<vector<pair<int, int>>> foods(3);
    rep(i, n){
        int v, a, c;
        cin >> v >> a >> c;
        v--;
        foods[v].emplace_back(a, c);
    }
    vector d(3, vector<int>(x+1));
    rep(v, 3){
        vector<int> dp(x+1);
        for (auto [a, c] : foods[v]){
            for (int i = x; i >= c; i--){
                chmax(dp[i], dp[i-c] + a);
            }
        }
        d[v] = dp;
    }

    auto judge = [&](int r) {
        int tot = 0;
        rep(v, 3){
            if (d[v][x] < r) return false;
            tot += lower_bound(d[v].begin(), d[v].end(), r) - d[v].begin();
        }

        return tot <= x;
    };

    int ac = 0, wa = INF;
    while (ac + 1 < wa){
        int wj = (ac + wa)/2;
        if (judge(wj)) ac = wj;
        else wa = wj;
    }
    cout << ac << "\n";
    return 0;
}
```

---


We can solve this problem by “splitting” the foods by vitamin type. Notice that since each food gives only one vitamin, if we want to achieve at least $t$ units for each vitamin then we must “pay” separately for vitamin 1, vitamin 2, and vitamin 3. In other words, if we can compute, for each vitamin type, the minimum number of calories required to “buy” at least $t$ units then the answer is feasible if the sum of the three calorie costs is at most $X$.

A standard “0/1 knapSack” style dynamic programming (DP) works well here since the calorie constraint $X$ is small (up to 5000). For each vitamin type $v$ (i.e. $v\in\{1,2,3\}$) we can process only the foods that give vitamin $v$ and compute an array $dp_v[c]$ which is the maximum vitamin units achievable with exactly cost $c$. Then, we “relax” it to get 
$$
f_v[c] = \max_{0 \le i \le c} dp_v[i]
$$
so that $f_v[c]$ is the maximum vitamin units achievable with cost at most $c$.

Then for a given candidate value $t$ (which is a candidate for the “minimum vitamin intake”), we simply need to check for each vitamin $v$ what is the smallest calorie cost $c_v$ such that $f_v[c_v] \ge t$ (if one exists). If
$$
c_1 + c_2 + c_3 \le X,
$$
then it is possible to achieve at least $t$ units for each vitamin. We can binary search on $t$ (the answer is at most $\min(\text{total vitamin }1,\text{ total vitamin }2,\text{ total vitamin }3)$).

Below is the complete C++ solution.

---

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int N, X;
    cin >> N >> X;
    
    // We will use indices 1..3 for vitamin types.
    // Each food is stored as a pair: (cost, amount)
    vector<vector<pair<int,int>>> foods(4);
    // We'll also record the total vitamin amount available for each vitamin.
    vector<long long> total(4, 0);
    
    // Note: The input is in the order: vitamin, amount, calories.
    for (int i = 0; i < N; i++){
        int V, A, C;
        cin >> V >> A >> C;
        foods[V].push_back({C, A});
        total[V] += A;
    }
    
    // For each vitamin type, we want to compute:
    // dp[c] = maximum vitamin units achievable with EXACT cost c.
    // Then, we build best[v][c] = maximum vitamin units with cost at most c.
    // We use NEG_INF for unreachable states.
    const int NEG_INF = -1000000000;
    vector<vector<int>> best(4, vector<int>(X+1, 0));
    
    for (int v = 1; v <= 3; v++){
        vector<int> dp(X+1, NEG_INF);
        dp[0] = 0;
        // Process each food for vitamin type v.
        for (auto &item : foods[v]){
            int cost = item.first;
            int amt  = item.second;
            // 0/1 Knapsack: process in reverse order so we do not reuse an item.
            for (int cal = X; cal >= cost; cal--){
                if (dp[cal - cost] != NEG_INF)
                    dp[cal] = max(dp[cal], dp[cal - cost] + amt);
            }
        }
        best[v][0] = dp[0];
        for (int cal = 1; cal <= X; cal++){
            best[v][cal] = max(best[v][cal - 1], dp[cal]);
        }
    }
 
    // The answer cannot exceed the minimum total available vitamin.
    long long hi = min({ total[1], total[2], total[3] });
    long long lo = 0;
    
    // Check if we can achieve at least t units for each vitamin within the calorie limit.
    auto canAchieve = [&](long long t) -> bool {
        int sumCost = 0;
        for (int v = 1; v <= 3; v++){
            int neededCost = X + 1;
            for (int cal = 0; cal <= X; cal++){
                if (best[v][cal] >= t) {
                    neededCost = cal;
                    break;
                }
            }
            if (neededCost == X + 1) return false;
            sumCost += neededCost;
            if (sumCost > X) return false;
        }
        return sumCost <= X;
    };
 
    // Binary search for the maximum t that can be achieved.
    while (lo < hi) {
        long long mid = (lo + hi + 1) / 2;
        if (canAchieve(mid))
            lo = mid;
        else
            hi = mid - 1;
    }
 
    cout << lo << "\n";
    return 0;
}
```


---

### Explanation

1. **Input and Data Preparation:**  
   We read $N$ and $X$, then store each food in `foods[V]` where each food is a pair $(C, A)$. We also track the total vitamin amount available per type.

2. **DP for Each Vitamin Type:**  
   For each vitamin type $v$, we initialize a DP array `dp` of length $X+1$ where `dp[c]` is the maximum vitamin units obtainable with exactly $c$ calories. We update `dp` in reverse order (to avoid reusing an item) for every food. Then, we compute the prefix maximum array `best[v]` so that `best[v][c]` is the maximum vitamin units achievable with calorie cost up to $c$.

3. **Binary Search:**  
   We binary search for the maximum $t$ (the minimum vitamin among the three types) such that for each vitamin type we can pick foods with total calories at most $X$ (when summed over the three vitamins). The helper lambda `canAchieve(t)` computes, for each vitamin type, the minimal cost needed to achieve at least $t$ units and then checks if the total is within $X$.

4. **Output:**  
   Finally, we output the maximum $t$ found.

This solution meets the constraints and should run efficiently for $N \le 5000$ and $X \le 5000$.
