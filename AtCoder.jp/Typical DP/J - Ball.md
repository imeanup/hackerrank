# [J - Ball](https://atcoder.jp/contests/tdpc/tasks/tdpc_ball)

> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

There are $N$ objects. The $i^{th}$ object is placed at coordinate $x_i$. When Snuke throws a ball towards a point at coordinate $x$, the ball will land at one of the points $x-1$, $x$, or $x+1$ with a probability of $\frac{1}{3}$. If an object is placed at the point where the ball lands, it will fall over.

Find the expected number of throws needed to knock down all objects when throwing the ball with an optimal strategy.

Note: **The location where the ball is thrown can be decided after observing where the previous ball landed.**

### Constraints

* $1 < N \le 16$
* $0 \le x_i \le 15$
* $x_i$ are pairwise distinct.

### Input Format

Input is given from standard input in the following format:

$N$ <br>
$x_1\dots x_N$

### Output Format

Print your answer on one line. It is considered valid if the absolute error is $10^{−6}$ or less.

### Sample Input 1
```
2
0 2
```
### Sample Output 1
```
4.500000000
```

It is best to keep throwing the ball towards coordinate $1$.

### Sample Input 2
```
5
1 3 4 2 5
```
### Sample Output 2
```
8.986111111
```

Below is a refined explanation that incorporates the suggested clarifications:

---

### Detailed Explanation

We solve the problem using state dynamic programming by “simulating” the process of throwing the ball until all objects are knocked down. Since there are at most 16 objects, we can represent the state by a bitmask of length $N$, where a 1 in the bitmask means that the corresponding object is still standing. The initial state is represented by the bitmask
$$(1 \ll N) - 1,$$
which means all objects (indices $0,1,\dots,N-1$) are present.

#### DP Definition

Let
$$dp[S] = \text{the expected number of additional throws required to knock down all objects, given that the set } S \text{ of objects is still up.}$$
The base case is when $S = \varnothing$ (i.e. all bits are 0), in which case
$$dp[\varnothing] = 0.$$

#### Transition Dynamics

When we throw a ball, we choose an aiming coordinate $a$ (an integer). The ball will then land at one of the three positions: $a-1$, $a$, or $a+1$; each outcome occurs with probability $\tfrac{1}{3}$.

- **If an object is present** at the landing coordinate and that object is still up (i.e. its bit is set in the state $S$), then that object is knocked down. We update the state by “removing” that object:
  - **Check:** `mask & (1 << objIndex)` checks if the object with index `objIndex` is still standing.
  - **Update:** `newMask = mask & ~(1 << objIndex)` clears the corresponding bit (sets it to 0), indicating that the object has fallen.

- **If no object is present** at the landing coordinate or if the object there is already knocked down, then the state remains unchanged.

Since the same throw produces three outcomes (landing at $a-1$, $a$, and $a+1$), let us denote the resulting states by:
- $S_{a-1}$ for landing at $a-1$,
- $S_{a}$ for landing at $a$,
- $S_{a+1}$ for landing at $a+1$.

A naïve recurrence would be:
$$dp[S] = 1 + \frac{1}{3}\Bigl( dp[S_{a-1}] + dp[S_a] + dp[S_{a+1}] \Bigr).$$
However, if one or more outcomes leave the state unchanged (i.e. $S_i = S$ for some $i$), we obtain a self–loop in the recurrence.

#### Handling Self–Loops

Suppose that, for a chosen aim $a$ from state $S$, the three outcomes yield:
- Outcome 1: new state $S_1$,
- Outcome 2: new state $S_2$,
- Outcome 3: new state $S_3$.

Let
$$p_{\text{same}} = \sum_{i:\; S_i=S} \frac{1}{3}$$
be the total probability that the state does not change, and let
$$q = \sum_{i:\; S_i \neq S} \frac{1}{3}\, dp[S_i]$$
be the contribution from outcomes that change the state.

Then one throw yields:
$$dp[S] = 1 + p_{\text{same}}\,dp[S] + q.$$
Solving for $dp[S]$ gives:
$$dp[S] = \frac{1 + q}{1 - p_{\text{same}}}.$$
*Note:* If $p_{\text{same}} = 1$ (i.e. all outcomes leave the state unchanged), then that aiming coordinate does not help; we simply skip that option.

#### Choosing the Best Aiming Position

Since our strategy is adaptive, we try every possible aiming coordinate $a$ from $-1$ to $16$ (we extend slightly outside the range $[0,15]$ to cover edge cases). For each aiming coordinate $a$ we compute the resulting state for each outcome, then calculate the candidate expected throws using the above formula. Finally, we choose the minimal expected value over all aiming choices:
$$dp[S] = \min_{a \in \{-1,\dots,16\}} \frac{1 + q}{1 - p_{\text{same}}}.$$

#### Precomputation of Object Positions

Since each object is at a distinct coordinate $x_i$ (with $0 \le x_i \le 15$), we precompute an array `posAt` such that:
- If an object is at coordinate $x$, then `posAt[x]` is its index.
- If no object is at coordinate $x$, then `posAt[x] = -1`.

This lets us quickly determine whether a ball landing at a given coordinate will knock down an object.

---

### Complete C++ Code

Below is the complete code with detailed comments implementing the above logic:

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
#include <iomanip>
#include <algorithm>
using namespace std;

const double INF = 1e9; // A large constant

// Global variables:
// positions: stores the coordinates of the objects (size = N)
// posAt[x]: if an object is at coordinate x, posAt[x] is its index; otherwise, -1.
vector<int> positions;
vector<int> posAt(100, -1);

// dp[mask] stores the expected additional throws needed when the set of objects 
// (represented as a bitmask) are still standing.
vector<double> dp;

int N; // number of objects

// Recursive DP function.
// mask: bitmask representing which objects are still up.
double solve_dp(int mask) {
    if (mask == 0) return 0.0; // Base case: no object remains.
    if (dp[mask] >= 0.0) return dp[mask];
    
    double best = INF;
    // Try every possible aiming coordinate a from -1 to 16.
    for (int a = -1; a <= 16; a++) {
        double p_same = 0.0; // Total probability that the state remains S.
        double q = 0.0;      // Weighted sum of dp for outcomes that change the state.
        
        // Process the three outcomes: landing at a-1, a, a+1.
        for (int delta = -1; delta <= 1; delta++) {
            int landing = a + delta;
            int newMask = mask;
            // Check if landing coordinate is within the valid range.
            if (landing >= 0 && landing <= 15) {
                int objIndex = posAt[landing];
                // Only attempt to knock down if there is an object at this coordinate 
                // and it is still standing.
                if (objIndex != -1 && (mask & (1 << objIndex))) {
                    newMask = mask & ~(1 << objIndex);
                }
            }
            // If newMask is the same as mask, the state does not change.
            if (newMask == mask) {
                p_same += 1.0 / 3.0;
            } else {
                q += (1.0 / 3.0) * solve_dp(newMask);
            }
        }
        // If p_same is 1, this aiming coordinate is not useful (skip it).
        if (fabs(1 - p_same) < 1e-9) continue;
        
        double candidate = (1 + q) / (1 - p_same);
        best = min(best, candidate);
    }
    
    dp[mask] = best;
    return best;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N;
    positions.resize(N);
    // Initialize posAt for coordinates 0 to 99.
    for (int i = 0; i < 100; i++){
        posAt[i] = -1;
    }
    
    for (int i = 0; i < N; i++){
        cin >> positions[i];
        posAt[positions[i]] = i;
    }
    
    // There are 2^N states.
    int totalStates = 1 << N;
    dp.assign(totalStates, -1.0);
    
    double ans = solve_dp((1 << N) - 1);
    cout << fixed << setprecision(9) << ans << "\n";
    return 0;
}
```

---

### Summary

1. **State Representation:**  
   - Use a bitmask of length $N$ where a 1 bit indicates an object is still standing.
   - The initial state is $(1 \ll N) - 1$.

2. **Transition and Recurrence:**  
   - When throwing a ball aimed at $a$, it lands at $a-1$, $a$, or $a+1$, each with probability $\frac{1}{3}$.
   - If an object is present (and still standing), remove it from the state.
   - If an outcome does not change the state, handle the self–loop by letting
     $$
     dp[S] = \frac{1 + q}{1 - p_{\text{same}}}.
     $$

3. **Choosing the Best Strategy:**  
   - Try all aiming coordinates $a \in \{-1, \dots, 16\}$ and take the minimum expected throws.

4. **Precomputation:**  
   - Use the `posAt` array to quickly map coordinates to object indices.
