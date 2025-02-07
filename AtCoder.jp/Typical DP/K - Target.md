## [K - Target](https://atcoder.jp/contests/tdpc/tasks/tdpc_target)

> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

The sequence of circles $C_1, C_2, \dots, C_K$ is called a target of size $K$ if, for each $i$, $C_{i+1}$ is strictly inside $C_i$. Snuke draws $N$ circles. The $i$-th circle has its center at $(x_i, 0)$ and radius $r_i$. When selecting some circles from this set to form a target, determine the maximum size of the target that can be formed.

<!-- 円の列 $C_1, C_2, \dots,C_K$ は各 $i$ に対し $C_{i+1}$ が $C_i$ の strictly に内部にあるときサイズ $K$ のターゲットであるという。 すぬけ君は、円を $N$ 個描いた。$i$ 番目の円は中心が $(x_i, 0)$ であり、半径が $r_i$ である。この中から円をいくつか選んでターゲットを作るとき、ターゲットの最大サイズを求めよ。 -->

### Constraints

* $1 \le N \le 100000$
* $0 \le x_i \le 100,000,000$
* $1 \le r_i \le 100,000,000$

---

### Input Format

The input is provided in the following format via standard input.

<!-- 入力は以下の形式で標準入力から与えられる。 -->

$N$ `<br>`
$x_1r_1$ `<br>`
$\dots$ `<br>`
$x_Nr_N$

### Output Format

Output the answer in one line.

<!-- 答えを一行に出力せよ。 -->

### Sample Input 1

```
3
1 1
0 3
3 2
```

### Sample Output 1

```
2
```

It is sufficient to make $C_1$ the second circle and $C_2$ the first circle.

<!-- $C_1$ を二番目の円、$C_2$ を一番目の円とすればよい。 -->

### Sample Input 2

```
2
1 1
2 2
```

### Sample Output 2

```
1
```

The inclusion relationship of the circles is strict (if the boundaries overlap, it is not considered to be inside).

<!-- 円の包含関係は strict である (境界が重なっている場合は内部とはみなさない)。 -->
Below is an updated, polished explanation that corrects a few minor typos and clarifies why the sorting order must be adjusted. (The logic is essentially the same as your explanation, but with slight modifications for clarity.)

---

We can solve this problem by transforming it into a “Longest Decreasing Subsequence” (LDS) problem.

### Step 1: Reformulate the Problem

Each circle is given by its center $(x_i, 0)$ and radius $r_i$. Its “coverage” along the $x$-axis can be represented by an interval:
$$L_i = x_i - r_i \quad \text{and} \quad R_i = x_i + r_i.$$

A circle $C_j$ is strictly inside another circle $C_i$ if and only if:
$$L_i < L_j \quad \text{and} \quad R_j < R_i.$$

### Step 2: Sorting

We first sort the circles by their left endpoint $L$ in ascending order. **However, if two circles have the same $L$, they cannot be nested (since we require $L_i < L_j$).** To force the algorithm to treat circles with equal $L$ as mutually exclusive, we sort them by their right endpoint $R$ in **ascending** order (not descending). 

Why change the usual order?  
- In the standard “Russian Doll” envelope problem, when you want to compute a longest increasing subsequence (LIS) in the second coordinate, you sort by the first coordinate ascending and the second coordinate **descending** to prevent using two items with the same first coordinate.  
- Here the roles are reversed: we want $L$ to be strictly increasing and $R$ to be strictly *decreasing*. Sorting by $L$ ascending satisfies the $L$ condition (at least weakly), and for circles with equal $L$ the one with the smaller $R$ (i.e. the one that would lead to a larger value when we set $s = -R$) comes first. When processing a later circle with the same $L$, its $R$ will be larger (thus its corresponding $s$ will be smaller), and the dynamic programming update will replace the earlier candidate rather than extend the chain. This ensures that at most one circle per distinct $L$ appears in the chain.

### Step 3: Longest Decreasing Subsequence (LDS)

After sorting by $L$, the problem reduces to finding the longest sequence where $R$ values are strictly decreasing. To do this efficiently in $O(N \log N)$ time, we apply a standard trick:

1. **Transform the $R$ values:**  
   Define $s = -R$. Then, a strictly increasing sequence in $s$ corresponds exactly to a strictly decreasing sequence in $R$.

2. **Apply the standard LIS algorithm:**  
   Using binary search (via `lower_bound`), we can compute the longest increasing subsequence (LIS) in the $s$ values. The length of this sequence is the answer.

### C++ Code

Below is the complete C++ solution with comments:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i, x) for (int i = 0; i < int(x); i++)

// Structure to represent a circle using its left and right endpoints
struct Circle { 
    int L, R;  // L = x - r, R = x + r
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<Circle> circle(n);

    // Read each circle and compute its L and R values
    rep(i, n){
        int x, r;
        cin >> x >> r;
        circle[i].L = x - r;
        circle[i].R = x + r;
    }
    
    // Sort circles by L ascending.
    // For equal L, sort by R ascending to force mutual exclusion.
    sort(circle.begin(), circle.end(), [&](const Circle &a, const Circle &b){
        if (a.L == b.L) return a.R < b.R;
        return a.L < b.L;
    });
    
    // dp will hold the current longest increasing sequence of s = -R.
    vector<int> dp;
    
    rep(i, n){
        // Convert R to s = -R so that an increasing sequence in s corresponds
        // to a decreasing sequence in R.
        int s = -circle[i].R;
        
        // Find the first element in dp that is not less than s.
        auto it = lower_bound(dp.begin(), dp.end(), s);
        
        // If s is greater than all elements in dp, append it.
        if (it == dp.end()) 
            dp.push_back(s);
        else 
            // Otherwise, replace the found element with s.
            *it = s;
    }
    
    // The size of dp is the length of the longest increasing subsequence in s,
    // which corresponds to the longest decreasing subsequence in R.
    cout << dp.size() << "\n";
    return 0;
}
```

---

### Summary

1. **Reformulation:**  
   Each circle’s interval $[x_i - r_i, x_i + r_i]$ is used, and one circle can be nested inside another if $L_i < L_j$ and $R_j < R_i$.

2. **Sorting:**  
   - Sort by $L$ in ascending order.  
   - For circles with the same $L$, sort by $R$ in **ascending** order to ensure that only one circle per distinct $L$ can be part of the chain.

3. **Transform & Solve:**  
   Convert $R$ to $s = -R$ and find the longest increasing subsequence of $s$, which is equivalent to finding the longest decreasing subsequence of $R$.
