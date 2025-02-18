# [X - Tower](https://atcoder.jp/contests/dp/tasks/dp_x)


### **Problem Recap**

You have $N$ blocks, each with:
- **Weight $w_i$**
- **Solidness $s_i$**
- **Value $v_i$**

You need to build a tower (by selecting and stacking some of the blocks) such that for every block in the tower, the sum of the weights of the blocks above it is no more than its solidness. The goal is to maximize the total value of the blocks in the tower.

---

We can solve this problem by “building-up” the tower from the top. The key observation is that when you add a block to the bottom of an already‐built tower, the only “new” check you have to perform is that the total weight of the tower above the new block does not exceed its solidness.

Let’s denote by $T$ the current total weight of the blocks already in the tower (which are “above” the new block you’re about to place). Then if you want to add a block $i$ (with weight $w_i$, solidness $s_i$, and value $v_i$) to the bottom, you must have: $$T \le s_i.$$
Once you add block $i$ below, the new tower weight becomes $T + w_i$ and the value increases by $v_i$.

One important trick is to sort the blocks in increasing order of $w_i + s_i$. Intuitively, a block’s “capacity” to support weight is given by its solidness, and if you add its own weight you get the “limit” that the entire tower must respect when that block is used. Sorting by $w_i+s_i$ ensures that you consider “weaker” blocks first and that when you try to add a new block, the blocks already chosen do not violate the constraint.

---

### Dynamic Programming Approach

**DP State:**

- Let $dp[t]$ be the maximum total value that can be achieved for a tower whose total weight is exactly $t$.

**Base Case:**

- $dp[0] = 0$, meaning that a tower of weight 0 (an empty tower) has value $0$.

**Transition:**

- When processing a block $i$ (after sorting the blocks), we try to “place” it at the bottom of an existing tower. Suppose the current tower has weight $t$ (and value $dp[t]$). We can add block $i$ below the tower only if:
  $$t \le s_i.$$
  If the condition is met, the new tower will have weight $t + w_i$ and value $dp[t] + v_i$. Thus, we update:
  $$dp[t + w_i] = \max(dp[t + w_i],\ dp[t] + v_i).$$
  
- **Important:** We iterate over $t$ in **decreasing** order when processing each block to avoid reusing the same block more than once.

**Final Answer:**

- The answer is the maximum value over all possible weights:
  $$\text{ans} = \max_{t} dp[t].$$

---

### Complete C++ Code (TLE)

Below is one complete C++ solution with comments explaining the details:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

struct Block {
    ll w, s, v;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    vector<Block> blocks(n);
    for (int i = 0; i < n; i++){
        cin >> blocks[i].w >> blocks[i].s >> blocks[i].v;
    }
    
    // Sort blocks by (weight + solidness) in increasing order.
    sort(blocks.begin(), blocks.end(), [](const Block &a, const Block &b){
        return a.w + a.s < b.w + b.s;
    });
    
    // Calculate the maximum possible total weight (sum of all block weights)
    ll maxW = 0;
    for (auto &b: blocks)
        maxW += b.w;
    
    // dp[t] = maximum value achievable with a tower of total weight t.
    // Initialize with a very small number (acting as -∞)
    const ll NEG_INF = -1e18;
    vector<ll> dp(maxW + 1, NEG_INF);
    dp[0] = 0; // base case: empty tower
    
    ll ans = 0; // to store the answer
    
    // Process each block one by one
    for (int i = 0; i < n; i++){
        // Iterate in reverse order so that each block is used at most once.
        for (ll t = maxW - blocks[i].w; t >= 0; t--){
            // Only consider valid states.
            if(dp[t] == NEG_INF)
                continue;
            // Check if the current tower (of weight t) can be supported by block i.
            if(t <= blocks[i].s){
                dp[t + blocks[i].w] = max(dp[t + blocks[i].w], dp[t] + blocks[i].v);
                ans = max(ans, dp[t + blocks[i].w]);
            }
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```

---

### **Explanation Recap**

1. **Sorting:** We sort the blocks by $w_i + s_i$ so that blocks with lower “support capacity” come first.

2. **DP State:**  
   - **dp[t]** stores the maximum value we can get with a tower weighing exactly $t$.

3. **Transition:**  
   - For each block $i$, for every possible current tower weight $t$ (iterated in reverse order), if $t \le s_i$ (i.e. block $i$ can support the current tower), then update the state for the new weight $t + w_i$ with the new value $dp[t] + v_i$.

4. **Answer:**  
   - The maximum value over all $dp[t]$ gives the answer.

This method correctly takes care of the constraint for each block and ensures that every block is used at most once. 

---

Below is one way to fix the TLE problem. In the original solution we used a full DP array of size roughly “sum of weights” (up to $10^7$) and iterated over every weight for every block. In the worst‐case that costs about
$$O(N\cdot \sum w_i) \approx 10^3 \times 10^7 = 10^{10}\text{ iterations,}$$
which is far too slow.

The trick is to notice that many weights are “never reached” in the DP and that we only care about “pareto‐optimal” states: states that are not dominated by another state with a lower weight and a higher value. We can then store only those reachable states in a vector of pairs. This “sparse DP” usually has far fewer than $10^7$ entries.

---

### **The Idea**

1. **Sort the Blocks:**  
   As before, sort the blocks by $w_i+s_i$ (increasing order). This guarantees that when you try to put a new block at the bottom, you only try it on “feasible” towers.

2. **DP State (Sparse):**  
   Maintain a vector `dp` of pairs $(W,V)$ meaning that there is a way to build a tower of total weight $W$ with total value $V$. Moreover, we only keep the **non‐dominated** states – if you can achieve the same or a higher value with a smaller weight, then the heavier state is not needed.

   Initially, you have the state $(0,0)$.

3. **Transition:**  
   For each block (with $(w,s,v)$ ), try to put it under every state $(W,V)$ in `dp` **if** $W\le s$. This yields a candidate new state:
    $$(W+w,\; V+v).$$
   Then merge all these new candidate states with the old states, and filter out any state that is “dominated” by another state (i.e. if for two states $(W_1,V_1)$ and $(W_2,V_2)$ with $W_1 \le W_2$ but $V_1 \ge V_2$, then $(W_2,V_2)$ is useless).

4. **Answer:**  
   The final answer is the maximum $V$ over all states in `dp`.

---

### **C++ Code**

Below is the complete C++ solution using this “sparse DP” method:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

struct Block {
    int w, s;
    ll v;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<Block> blocks(n);
    for (int i = 0; i < n; i++){
        cin >> blocks[i].w >> blocks[i].s >> blocks[i].v;
    }
    
    // Sort blocks by (w + s) in increasing order.
    sort(blocks.begin(), blocks.end(), [](const Block &a, const Block &b) {
        return a.w + a.s < b.w + b.s;
    });
    
    // dp stores pairs (total_weight, total_value)
    // and is maintained as a set of pareto-optimal states.
    vector<pair<int, ll>> dp;
    dp.push_back({0, 0});
    
    // Process each block.
    for (int i = 0; i < n; i++){
        // Collect candidates by trying to put block i under each tower.
        vector<pair<int, ll>> cand;
        for (auto &state : dp) {
            int curWeight = state.first;
            ll curValue = state.second;
            // Only if the block can support the current tower.
            if (curWeight <= blocks[i].s) {
                int newWeight = curWeight + blocks[i].w;
                ll newValue = curValue + blocks[i].v;
                cand.push_back({newWeight, newValue});
            }
        }
        // If no new candidate is generated, move on.
        if (cand.empty()) continue;
        
        // Sort candidates by weight.
        sort(cand.begin(), cand.end());
        
        // Merge dp and cand (both sorted by weight) into a new dp.
        vector<pair<int, ll>> merged;
        int p = 0, q = 0;
        while (p < dp.size() || q < cand.size()){
            pair<int, ll> cur;
            if (q == cand.size() || (p < dp.size() && dp[p].first < cand[q].first)) {
                cur = dp[p++];
            } else if (p == dp.size() || (q < cand.size() && cand[q].first < dp[p].first)) {
                cur = cand[q++];
            } else { // both have the same weight
                cur = {dp[p].first, max(dp[p].second, cand[q].second)};
                p++; q++;
            }
            // Only add if it is not dominated.
            if (!merged.empty() && merged.back().second >= cur.second) continue;
            merged.push_back(cur);
        }
        dp = move(merged);
    }
    
    // The answer is the maximum value among all states.
    ll ans = 0;
    for (auto &state : dp) {
        ans = max(ans, state.second);
    }
    cout << ans << "\n";
    
    return 0;
}
```

---

### **Explanation Recap**

1. **Sorting:**  
   Blocks are sorted by $w_i+s_i$ so that we “use up” the blocks with a lower support capacity first.

2. **DP State:**  
   Instead of maintaining an array of size up to $\sum w_i$ (which could be $10^7$), we maintain a sparse list `dp` of pairs $(W,V)$ that are “pareto‐optimal” – meaning that for any two states, if one has a lower weight and at least as high a value, the other is not needed.

3. **Transition:**  
   For each block, for every state in `dp` with weight $W$ that is not too heavy for the block (i.e. $W \le s$), we form a candidate new state $(W+w, V+v)$. Then we merge these candidates with the old states, keeping only the non‐dominated ones.

4. **Answer:**  
   Finally, the maximum value among all states is printed.

This sparse DP approach avoids iterating over all $10^7$ possible weights for each block and passes within the constraints.

---

---

### **Approach**

1. **Sorting the Blocks:**

   - **Key Idea:** Sort the blocks in increasing order of $w_i + s_i$.
   - **Why?**  
     $w_i + s_i$ represents the maximum total weight that block $i$ can bear (its own weight plus the weight it can support). Sorting by this sum ensures that we consider blocks with lower support capacity first, which makes it easier to maintain the validity of the tower as you add more blocks.

2. **Using Sparse Dynamic Programming:**

   - **Traditional DP Problem:**  
     A straightforward DP might use a table where `dp[t]` is the maximum value for a tower weighing exactly $t$. However, the total weight can go up to around $10^7$ (since $w_i \le 10^4$ and $N \le 10^3$ ), leading to a huge state space.
     
   - **Sparse DP Technique:**  
     Instead of a large DP array, we maintain a **list of "states"**—each state is a pair $(W, V)$ where:
     - $W$ is the total weight of a tower built so far.
     - $V$ is the maximum total value achievable with that weight.
     
     These states are kept **Pareto-optimal**. That is, if you can achieve the same or a higher value with a lower weight, any state with a higher weight and lower or equal value is not needed.

3. **State Transitions:**

   - For each block $i$ (after sorting), try to add it **below** every tower state $(W, V)$ in your DP list.
   - **Validity Check:**  
     You can add block $i$ to a state $(W, V)$ only if the current tower weight $W$ is at most the block's solidness $s_i$ (i.e., $W \le s_i$ ).
   - **Updating the State:**  
     If the block can support the current tower, then adding it creates a new state:
     $$(W + w_i,\, V + v_i)$$
   - **Merging States:**  
     After generating new candidate states from the current block, merge these candidates with your existing DP states. While merging, remove any states that are **dominated** (if one state has a lower weight and at least the same or a higher value, the other state is redundant).

4. **Final Answer:**

   - After processing all blocks, the answer is the maximum value $V $ among all stored DP states.

---

### **DP State Details**

- **Representation:**  
  The DP is a vector of pairs:  
  $$\text{dp} = \{ (W, V) \}$$
  where each pair signifies that there exists a way to build a tower with total weight $W$ and total value $V$.

- **Pareto-Optimality:**  
  The DP list is maintained so that if there exists a state $(W_1, V_1)$ and another state $(W_2, V_2)$ with $W_1 \le W_2$ and $V_1 \ge V_2$, then the state $(W_2, V_2)$ is redundant and can be removed.

- **Transition Mechanism:**  
  For each block:
  - **Iterate:** Over each state $(W, V)$ in DP.
  - **Condition:** If $W \le s_i$ for the current block $i$, then form a new state:
    $$(W + w_i,\, V + v_i)$$
  - **Merge:** Combine the new states with the old ones and filter out dominated states.
