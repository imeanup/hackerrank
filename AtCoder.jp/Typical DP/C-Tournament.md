## [C-Tournament](https://atcoder.jp/contests/tdpc/tasks/tdpc_tournament)

### Problem Statement

A tournament is held with $2^K$ participants. Matches in this tournament are conducted in the following manner:

- In the **1st round**, participants 1 and 2, 3 and 4, ... compete against each other.
- In the **2nd round**, the winners of (1 vs. 2) and (3 vs. 4), the winners of (5 vs. 6) and (7 vs. 8), ... compete against each other.
- In the **3rd round**, the winners of ((1 vs. 2) vs. (3 vs. 4)) and ((5 vs. 6) vs. (7 vs. 8)), the winners of ((9 vs. 10) vs. (11 vs. 12)) and ((13 vs. 14) vs. (15 vs. 16)), ... compete against each other.
- This continues similarly up to the **$K$-th round**.

After the $K$-th round, the overall winner of the tournament is determined. Given the [Elo Rating](https://en.wikipedia.org/wiki/Elo_rating_system) $R_i$ for participant $i$, calculate the probability of each participant becoming the winner.

The probability of participant $P$ (with Elo Rating $R_P$) defeating participant $Q$ (with Elo Rating $R_Q$) is given by:

$$\frac{1}{1 + 10^{(R_Q - R_P)/400}}$$

It is also assumed that the outcomes of different matches are independent.

<details><summary>Elo Rating </summary><br>

> The Elo rating system is a method for calculating the relative skill levels of players in zero-sum games, such as chess and esports. It's named after its creator, Hungarian-American physics professor Arpad Elo.

</details><br>

---

### Constraints

- $1 \leq K \leq 10$
- $0 \leq R_i \leq 4000$

---

### Input Format

The input is provided in the following format from standard input:

$
K \\
R_1 \\
\vdots \\
R_{2^K}
$

---

### Output Format

Output $2^K$ lines. The $i$-th line should contain the probability of participant $i$ becoming the winner. The result will be considered correct if the absolute error is less than or equal to $10^{-6}$.

### Sample Input 1

```
2200
2600
```

### Sample Output 1

<section><pre>0.090909091
0.909090909
</pre></section>

### Sample Input 2

<section><pre>3
2000
2500
2300
2700
2100
2400
2600
2200
</pre></section>

### Sample Output 2

<section><pre>0.000086893
0.122042976
0.005522752
0.493464665
0.000651695
0.053982389
0.321828438
0.002420190
</pre></section>


---

We can solve this problem by “simulating” the tournament round‐by‐round. In round 0 every participant is “alive” (with probability 1). Then in each round the tournament bracket is fixed: in a block of consecutive participants the left half of the block faces the right half. (For example, in round 1 the matches are (1 vs.2), (3 vs.4), …; in round 2 the winners of (1 vs.2) and (3 vs.4) face off, etc.)  

For a fixed round, consider one bracket (group) of size $2^r$. Let the left half be those participants with indices  
$$\texttt{groupStart} \quad \ldots \quad \texttt{groupStart}+2^{r-1}-1,$$  
and the right half be  
$$\texttt{groupStart}+2^{r-1} \quad \ldots \quad \texttt{groupStart}+2^r-1.$$

If we denote by $dp[r][i]$ the probability that participant $i$ reaches (and wins) round $r$, then (after the match in round $r$):

- For a participant $i$ in the left half, the new probability is  
  $$dp[r][i] = dp[r-1][i] \times \sum_{j \text{ in right half}} \Bigl( dp[r-1][j] \times P(i \text{ beats } j) \Bigr),$$
- And similarly for a participant $j$ in the right half,  
  $$dp[r][j] = dp[r-1][j] \times \sum_{i \text{ in left half}} \Bigl( dp[r-1][i] \times P(j \text{ beats } i) \Bigr).$$

Here, the winning probability is given by the Elo formula  
$$P(i \text{ beats } j) = \frac{1}{1 + 10^{\frac{R_j-R_i}{400}}}\,.$$

Since the tournament is structured so that in every sub-bracket exactly one wins, the probabilities in each bracket “normalize” as we move from one round to the next.

Finally, after $K$ rounds the overall winning probability for participant $i$ is $dp[K][i]$.

The complete C++ code is provided below.

---

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;
 
// Function to compute the probability that player i (rating R[i]) beats player j (rating R[j])
double winProbability(int R_i, int R_j) {
    return 1.0 / (1.0 + pow(10.0, (R_j - R_i) / 400.0));
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int K;
    cin >> K;
    int n = 1 << K; // number of participants = 2^K
    vector<int> R(n);
    for (int i = 0; i < n; i++){
        cin >> R[i];
    }
    
    // dp[r][i] is the probability that participant i reaches round r.
    // Round 0 means "before any match" so dp[0][i] = 1.
    vector<vector<double>> dp(K+1, vector<double>(n, 0.0));
    for (int i = 0; i < n; i++){
        dp[0][i] = 1.0;
    }
    
    // For rounds 1 through K, simulate the matches.
    // In round r, the block size is 2^r.
    for (int r = 1; r <= K; r++){
        int groupSize = 1 << r; // number of players in the group
        int halfSize = groupSize >> 1; // players in one half
        // Process each group (bracket) in this round.
        for (int groupStart = 0; groupStart < n; groupStart += groupSize){
            // For every participant in the left half, sum up the probability 
            // that they beat one of the opponents from the right half.
            for (int i = groupStart; i < groupStart + halfSize; i++){
                double sumProb = 0.0;
                // Sum over the opponents in the right half.
                for (int j = groupStart + halfSize; j < groupStart + groupSize; j++){
                    sumProb += dp[r-1][j] * winProbability(R[i], R[j]);
                }
                dp[r][i] = dp[r-1][i] * sumProb;
            }
            // Similarly, for every participant in the right half.
            for (int j = groupStart + halfSize; j < groupStart + groupSize; j++){
                double sumProb = 0.0;
                // Sum over the opponents in the left half.
                for (int i = groupStart; i < groupStart + halfSize; i++){
                    sumProb += dp[r-1][i] * winProbability(R[j], R[i]);
                }
                dp[r][j] = dp[r-1][j] * sumProb;
            }
        }
    }
    
    // After K rounds, dp[K][i] is the probability that participant i becomes the champion.
    cout << fixed << setprecision(6);
    for (int i = 0; i < n; i++){
        cout << dp[K][i] << "\n";
    }
    
    return 0;
}
```

---

### Explanation

1. **Input and Initialization:**
   - We read $K$ and then $2^K$ ratings into the vector `R`.
   - The dp table is initialized with $dp[0][i] = 1$ for all participants since everyone starts in the tournament.

2. **Simulating the Tournament Round-by-Round:**
   - For round $r$ (from 1 to $K$), the size of each group (bracket) is $2^r$ and each group is divided into two halves.
   - For each participant in the left half of a group, we calculate the total probability of winning in the round by summing over the probabilities of beating each opponent in the right half. (The opponent’s probability of reaching this round, $dp[r-1][j]$, is factored in.)
   - The same is done for participants in the right half, summing over opponents in the left half.
   - The new probability is the product of the probability of reaching the round (from the previous dp value) and the sum computed.

3. **Output:**
   - After simulating $K$ rounds, the final probabilities $dp[K][i]$ are printed, one per line, with 6 digits after the decimal point (which meets the error tolerance).

This solution efficiently computes the overall winning probability for each participant by carefully “merging” the probabilities in each bracket using the given Elo formula.
