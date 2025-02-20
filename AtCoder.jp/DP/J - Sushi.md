# [J - Sushi](https://atcoder.jp/contests/dp/tasks/dp_j)

## Explanation

### Problem Recap

You are given $N$ dishes. For each dish $i$ there are $a_i$ pieces of sushi (with $a_i \in \{1,2,3\}$). In each operation, you randomly choose one dish (each with probability $\frac{1}{N}$); if that dish still has sushi, you eat one piece. The process repeats until all sushi pieces are eaten. We wish to compute the expected number of operations performed.

### DP State

We define a state by the triple:
- $i$: the number of dishes with exactly $1$ piece,
- $j$: the number of dishes with exactly $2$ pieces,
- $k$: the number of dishes with exactly $3$ pieces.

Let $\text{dp}[i][j][k]$ denote the expected number of operations needed to finish all sushi from that state.

The initial state is determined by counting the dishes with 1, 2, and 3 sushi pieces:
- Let $cnt_1, cnt_2, cnt_3$ be those counts, respectively.

### **DP Recurrence (Transition)**

At a state $(i,j,k)$ the total number of dishes that still have sushi is $s = i + j + k$. In one operation:
- With probability $\frac{N-s}{N}$ you pick a dish with no sushi ($0$), so the state remains $(i,j,k)$.
- With probability $\frac{i}{N}$ you pick one of the $i$ dishes having $1$ sushi. Eating one makes that dish empty. The new state becomes $(i-1, j+1, k)$ because that dish “loses” its last piece and effectively moves from the 1-sushi group to the “empty” group.
- With probability $\frac{j}{N}$ you pick one of the $j$ dishes having $2$ sushi. After eating one, it will have 1 sushi, so the state becomes $(i+1, j-1, k)$.
- With probability $\frac{k}{N}$ you pick one of the $k$ dishes having $3$ sushi. After eating one, it will have 2 sushi, so the state becomes $(i, j+1, k-1)$.

Because we always perform one operation regardless, the recurrence is derived as follows. Let $E(i,j,k)$ be the expected additional operations:
$$E(i,j,k) = 1 + \frac{N-s}{N}E(i,j,k) + \frac{i}{N}E(i-1,j+1,k) + \frac{j}{N}E(i+1,j-1,k) + \frac{k}{N}E(i,j+1,k-1).$$
Rearranging by multiplying both sides by $N$ and isolating $E(i,j,k)$:
$$s\, E(i,j,k) = N + i\, E(i-1,j+1,k) + j\, E(i+1,j-1,k) + k\, E(i,j+1,k-1),$$
so that
$$E(i,j,k) = \frac{N + i\, E(i-1,j+1,k) + j\, E(i+1,j-1,k) + k\, E(i,j+1,k-1)}{s}.$$

The base state is $E(0,0,0) = 0$ because if no dish has any sushi, no operations are needed.

### **Computing the Answer**

After precomputing $cnt_1, cnt_2, cnt_3$ from the input, the final answer is $\text{dp}[cnt_1][cnt_2][cnt_3]$.

---

## **C++ Code**

Below is the complete C++ solution using the provided template:

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = unsigned long long;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){ if(a < b){ a = b; return true; } return false; }
template<class T> inline bool chmin(T &a, T b){ if(a > b){ a = b; return true; } return false; }

// We'll use double for expected value calculations.
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    // Count the number of dishes with 1, 2, and 3 pieces of sushi.
    int cnt1 = 0, cnt2 = 0, cnt3 = 0;
    rep(i, n) {
        int a;
        cin >> a;
        if(a == 1) cnt1++;
        else if(a == 2) cnt2++;
        else if(a == 3) cnt3++;
    }
    
    // dp[i][j][k] will be the expected number of operations 
    // needed when there are i dishes with 1 sushi, j dishes with 2 sushi,
    // and k dishes with 3 sushi.
    vector<vector<vector<double>>> dp(n+1, 
        vector<vector<double>>(n+1, vector<double>(n+1, 0.0)));
    
    // Base case: when there is no sushi, no operations are needed.
    dp[0][0][0] = 0.0;
    
    // Iterate over all possible states.
    // Total sushi-bearing dishes s = i + j + k ranges from 1 to n.
    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= n; j++){
            for (int k = 0; k <= n; k++){
                if(i == 0 && j == 0 && k == 0) continue;
                double s = i + j + k;
                // The expected operations from the current state:
                // We always perform 1 operation,
                // plus the expected number from the next state.
                double expect = n; // "n" comes from moving the term with probability of picking an empty dish.
                if(i > 0)
                    expect += i * dp[i-1][j+1][k];
                if(j > 0)
                    expect += j * dp[i+1][j-1][k];
                if(k > 0)
                    expect += k * dp[i][j+1][k-1];
                dp[i][j][k] = expect / s;
            }
        }
    }
    
    cout << fixed << setprecision(10) << dp[cnt1][cnt2][cnt3] << "\n";
    return 0;
}
```

---

## **Summary**

- **DP State:**  
  $\text{dp}[i][j][k]$ – expected operations from state with $i$ dishes having 1 sushi, $j$ having 2, and $k$ having 3.

- **DP Transition:**  
  $$dp[i][j][k] = \frac{n + i\,dp[i-1][j+1][k] + j\,dp[i+1][j-1][k] + k\,dp[i][j+1][k-1]}{i+j+k},$$
  derived by accounting for the probabilities of selecting a dish with sushi versus an empty dish.

- **Approach:**  
  Use a three-dimensional DP to cover all states (which is efficient since $n \le 300$) and compute the expected number of operations from the initial state $(cnt_1, cnt_2, cnt_3)$.

This solution efficiently computes the expected number of operations needed to finish all sushi using dynamic programming. 

This approach uses a triple-nested loop to calculate the expected number of operations. Due to the large input sizes, floating-point precision is necessary. The time complexity is around $O(n^3)$.
