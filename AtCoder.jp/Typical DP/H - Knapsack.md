## [H - Knapsack](https://atcoder.jp/contests/tdpc/tasks/tdpc_knapsack)


### Problem Statement

$N$ 個の物があり、$i$ 番目のものの重さ、価値、色はそれぞれ $w_i, v_i, c_i$ である。すぬけ君は、いくつかのものをナップザックに入れることにした。ただし、ナップザックに入れるものの重さの合計は $W$ 以下であり、色は $C$ 種類以下でなければならない。ナップザックに入れられるものの価値の合計の最大値を求めよ。

There are $N$ objects, and the weight, value, and color of the $i$-th object are $w_i, v_i$, and $c_i$, respectively. Snuke decides to put some objects into his knapsack. However, the total weight of the objects in the knapsack must be less than or equal to $W$, and the number of colors must be less than or equal to $C$. Find the maximum total value of the objects that can be put into the knapsack.

---


### Constraints

* $1 \le N \le 100$
* $1 \le W \le 10000$
* $1 \le C \le 50$
* $1 \le w_i, v_i \le 10000$
* $1 \le c_i \le 50$

---

### Input Format

入力は以下の形式で標準入力から与えられる。

Input is given from standard input in the following format:

<pre><var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathnormal" style="margin-right: 0.10903em;">N</span></span></span></span></span></var> <var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>W</mi></mrow><annotation encoding="application/x-tex">W</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathnormal" style="margin-right: 0.13889em;">W</span></span></span></span></span></var> <var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.68333em; vertical-align: 0em;"></span><span class="mord mathnormal" style="margin-right: 0.07153em;">C</span></span></span></span></span></var>
<var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>w</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">w_1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right: 0.02691em;">w</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.301108em;"><span class="" style="top: -2.55em; margin-left: -0.02691em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span></var> <var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>v</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">v_1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right: 0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.301108em;"><span class="" style="top: -2.55em; margin-left: -0.03588em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span></var> <var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>c</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">c_1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathnormal">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.301108em;"><span class="" style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span></var>
<var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>…</mo></mrow><annotation encoding="application/x-tex">…</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.12em; vertical-align: 0em;"></span><span class="minner">…</span></span></span></span></span></var>
<var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>w</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">w_N</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right: 0.02691em;">w</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.328331em;"><span class="" style="top: -2.55em; margin-left: -0.02691em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right: 0.10903em;">N</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span></var> <var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>v</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">v_N</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right: 0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.328331em;"><span class="" style="top: -2.55em; margin-left: -0.03588em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right: 0.10903em;">N</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span></var> <var><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>c</mi><mi>N</mi></msub></mrow><annotation encoding="application/x-tex">c_N</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.58056em; vertical-align: -0.15em;"></span><span class="mord"><span class="mord mathnormal">c</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.328331em;"><span class="" style="top: -2.55em; margin-left: 0em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right: 0.10903em;">N</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.15em;"><span class=""></span></span></span></span></span></span></span></span></span></span></var>
</pre>

### Output Format

答えを一行に出力せよ。

Print the answer on one line.


### Sample Input 1

```
4 5 2
1 10 1
1 20 2
1 30 3
10 100 4
```

### Sample Output 1

```
50
```

二番目と三番目のものを入れるとよい。

It's a good idea to include the second and third ones.

---

### Sample Input 2

```
10 20 2
4 5 6
3 3 9
5 2 9
4 1 6
6 8 3
3 7 6
2 4 9
4 7 3
6 5 6
3 2 9
```

### Sample Output 2

```
27
```

---

We can solve “H‐Knapsack” by noticing that the extra twist is that items have colors and we can use at most $C$ distinct colors. One effective approach is to “group by color” and then, for each color group, compute all the “efficient” ways to pick some items from that group (i.e. the (weight, value) pairs you can achieve by picking a non‐empty subset of items in that group). (Remember that if you pick nothing from a color group, you are not “using” that color and no “color count” is spent.) Then, you combine the groups with a second DP over (number of used colors, total weight) where you “add” one group’s contribution at a time.

The idea is as follows:

1. **Group items by color.**  
   For each color, we compute the best ways to pick a nonempty subset from that group. (We do a standard 0–1 knapsack restricted to the items in that group.) Then, we “compress” the resulting $(weight, value)$ pairs so that only “efficient” (non‐dominated) pairs remain.

2. **DP over groups.**  
   We set up a DP array $dp[j][w]$ = maximum total value achievable using exactly $j$ colors and total weight $w$, and update it group by group. When “adding” a group we consider all ways (from its efficient list) to use that color (which uses one color) and update accordingly.

3. **Answer:**  
   Finally, the answer is the maximum total value over all $j$ with $j\le C$ and total weight $\le W$.


---

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

const int NEG_INF = -1000000000; // a very small number to represent "impossible"

struct Item {
    int w, v;
};

struct Pair {
    int w, v;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, W, C;
    cin >> N >> W >> C;
    
    // There are up to 50 colors. Use 1-indexed colors.
    const int maxColor = 50;
    vector<vector<Item>> groups(maxColor + 1);
    
    for (int i = 0; i < N; i++){
        int w, v, c;
        cin >> w >> v >> c;
        groups[c].push_back({w, v});
    }
    
    // For each color group, compute all (weight, value) pairs obtainable by picking a nonempty subset of items in that group.
    // We will compute a DP for each group: f[wt] = maximum value achievable using items from that group (with total weight exactly wt).
    // Then, we will collect pairs (wt, f[wt]) for wt>=1 and "compress" the list to keep only efficient pairs.
    // We'll store these lists in poss[color] (if the group is non-empty).
    vector<vector<Pair>> poss(maxColor + 1);
    
    for (int c = 1; c <= maxColor; c++){
        if (groups[c].empty()) continue;  // no items of this color
        
        // We'll do a knapsack for this group. Use capacity up to W (since we never need more than total W).
        vector<int> f(W+1, NEG_INF);
        f[0] = 0;
        for (auto &it : groups[c]){
            // iterate in reverse so that each item is used at most once
            for (int wt = W; wt >= it.w; wt--){
                if(f[wt - it.w] != NEG_INF)
                    f[wt] = max(f[wt], f[wt - it.w] + it.v);
            }
        }
        // Now collect all pairs (wt, f[wt]) for wt >= 1 (nonempty subset) and where f[wt] != NEG_INF.
        vector<Pair> cur;
        for (int wt = 1; wt <= W; wt++){
            if (f[wt] != NEG_INF)
                cur.push_back({wt, f[wt]});
        }
        // Sort by weight (increasing)
        sort(cur.begin(), cur.end(), [](const Pair &a, const Pair &b){
            return a.w < b.w;
        });
        // Compress: remove dominated pairs.
        // A pair (w1, v1) dominates (w2, v2) if w1 <= w2 and v1 >= v2.
        vector<Pair> comp;
        int best = -1;
        for (auto &p : cur) {
            if (p.v > best) {
                comp.push_back(p);
                best = p.v;
            }
        }
        poss[c] = comp;
    }
    
    // Now do DP over the groups.
    // dp[j][wt] = maximum total value achievable using exactly j colors and total weight wt.
    // We have j from 0 to C and wt from 0 to W.
    vector<vector<int>> dp(C+1, vector<int>(W+1, NEG_INF));
    dp[0][0] = 0;
    
    // For each color from 1 to maxColor, we try to update dp.
    // There are two options for a group: skip it or use it (if there is at least one possibility).
    for (int c = 1; c <= maxColor; c++){
        // We update dp using group c only if poss[c] is non-empty.
        if (poss[c].empty()) continue;
        // We'll update from higher color count downwards to avoid double counting.
        // Create a temporary copy of dp.
        vector<vector<int>> new_dp = dp;
        // For each color count j (we can add one more color) and for each weight w,
        // try adding one possibility from group c.
        for (int j = C - 1; j >= 0; j--){
            for (int wt = 0; wt <= W; wt++){
                if (dp[j][wt] == NEG_INF) continue;
                // Try each possibility from group c.
                for (auto &p : poss[c]){
                    int newWt = wt + p.w;
                    if (newWt <= W) {
                        new_dp[j+1][newWt] = max(new_dp[j+1][newWt], dp[j][wt] + p.v);
                    }
                }
            }
        }
        dp = move(new_dp);
    }
    
    // Answer is the maximum value among all dp[j][wt] for 0 <= j <= C and wt <= W.
    int ans = 0;
    for (int j = 0; j <= C; j++){
        for (int wt = 0; wt <= W; wt++){
            ans = max(ans, dp[j][wt]);
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```

---

### Explanation

1. **Grouping by Color:**  
   We store items in `groups[c]` (for colors $1 \le c \le 50$).  
   
2. **Processing Each Group:**  
   For each group we run a 0–1 knapsack (using a simple DP array `f[]` of size $W+1$) to compute all ways to pick a nonempty subset from that group. Then we collect and "compress" the pairs so that we keep only the efficient (non‐dominated) pairs.

   Initialization:

   We set an array `f` of size $W+1$ where `f[wt]` will eventually represent the maximum value obtainable **using items of the current group only** with exactly total weight `wt`. We initialize `f[0] = 0` (zero weight gives zero value) and the rest to a vary small number (`-INF`) to denote “impossible” states.

   Processing items:

   For each item in the cureent group (with weigth `it.w` and value `it.v`), we update the DP array in **reverse order**.
    
    * We loop over `wt` from $W$ down to `it.w`.
    * If `f[wt - it.w]` is not `-INF` (meaning it's not possible to achieve a total weight of `wt - it.w`), then we try to take this item and update:
        
        $f[wt] = \max(f[wt], f[wt - it.w] + it.v)$

    This ensures that each item is used atmost once(a standard trick in 0-1 knapsack).

    Collecting pairs:

    After processing all items in the group, we want to know all achievable pairs $(\text{weight}, \text{value})$ for a **nonempty subset**. That is, for every weight $wt$ from $1$ to $W$, if `f[wt]` is not `-INF`, we record the pair $(wt, f[wt])$.

    Sorting and compression:

    The vector `cur` is sorted by weight. Then, we "compress" the list by keeping only the **non-dominated** pairs. A pair $(w_1, v_1)$ dominated another pair $(w_2, v_2)$ if $w_1 < w_2$ and $v_1 \ge v_2$; 

3. **Main DP Over Colors:**  
   We use a 2D DP `dp[j][wt]` which represents the best total value using exactly $j$ colors and weight exactly $wt$. (Items from a group contribute only if we use at least one item; otherwise we “skip” that color.)  
   Then, for each color group that is nonempty, we update the DP by “adding” one possibility from that group. Note that we update the DP for increasing number of used colors.

4. **Result:**  
   Finally, we take the maximum total value over all states with at most $C$ colors and weight at most $W$.

### 2. Time Complexity Analysis

**For the per-group knapsack part:**

- **DP for each group:**  
  For each item in the group (say there are $k$ items) and for each weight from $W$ down to the weight of the item, we do a constant-time update. This gives a per-group complexity of roughly $O(k \times W)$.

  In the worst-case (if all $N = 100$ items are in one group), this is $O(100 \times W)$, and with $W \le 10^4$, that’s about $10^6$ operations.

- **Collecting pairs:**  
  
  We loop over weights from 1 to $W$, which is $O(W)$ per group (i.e. $O(10^4)$ in the worst-case per group).

- **Sorting:**  
  
  Sorting the collected pairs in the worst-case takes $O(P \log P)$ where $P$ is the number of pairs. Since $P$ is at most $W$ (in a pathological scenario), this is $O(W \log W)$.

- **Compression:**  
  
  A single pass over the sorted list costs $O(P)$, which is $O(W)$ in the worst-case.

Since there are at most 50 colors, the total worst-case cost for processing all groups is roughly: $O\left( \sum_{c=1}^{50} \left(k_c \times W + W + W \log W \right) \right)$

Since $\sum k_c = N \le 100$, this part is quite efficient in practice.

**For the Main DP Over Groups:**

- We maintain a DP table `dp[j][wt]` where $j$ runs from 0 to $C$ (at most 50) and $wt$ runs from 0 to $W$ (at most 10,000).
- For each color that has at least one candidate pair (from the above processing), we update the DP. The update iterates over color counts $j$ (up to 50), over weights $wt$ (up to $W$), and over the number of candidate pairs for that color.
- In the worst-case, if a group produced $P$ candidate pairs (the compressed list), the update is $O(C \times W \times P)$ per group.
  
Given that:
  - $C \le 50$,
  - $W \le 10^4$,
  - and $P$ is typically very small (since compression reduces many pairs, and note that $N=100$ limits how many items can be in any group),
  
the overall DP over groups is also efficient in practice. In a worst-case theoretical bound, if $P$ were $O(W)$ for some reason, you could get a factor of $O(50 \times 10^4 \times 10^4)$ per group, but that worst-case does not occur with $N = 100$ because the candidate list is bounded by the number of items in that group. Practically, $P$ might be on the order of tens rather than thousands.

---

### 3. Summary of Overall Complexity

- **Per-group processing:**  
  Roughly $O(N \times W)$ in total (across all groups, with $N \le 100$) plus some additional $O(W \log W)$ factors per group but with at most 50 groups.

- **DP over groups:**  
  Roughly $O(C \times W \times P_{\text{avg}})$ per group, where $P_{\text{avg}}$ is the average number of candidate pairs per group. With small $N$ and after compression, $P_{\text{avg}}$ is expected to be small.

Thus, the approach is efficient given the constraints ($N \le 100$, $W \le 10^4$, $C \le 50$).

---

### Final Notes

- **The inner knapsack loop (for each group)** works by trying every possible total weight from $W$ down to the weight of the current item, ensuring that each item is used at most once.
- **The reverse iteration** is a standard technique in 0–1 knapsack problems to avoid reusing items.
- **The compression step** is crucial when later combining groups because it ensures that for each color, you only consider “efficient” ways (weight, value pairs) to use that color, thereby keeping the DP state space small.

This combination of techniques (0–1 knapsack per group and a subsequent DP merging groups with a constraint on the number of colors) is a common pattern in problems where you have multiple constraints or “dimensions” (here, weight and number of colors).
