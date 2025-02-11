## [D - Dice](https://atcoder.jp/contests/tdpc/tasks/tdpc_dice)

> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

When a dice is rolled $N$ times, find the probability that the product of the numbers that comes up is a multiple of $D$.

### Constraints

* $1 \le N \le 100$
* $1 \le D \le 10^{18}$

---

### Input Format

Input is given from standard input in the following format:

$N \quad D$

### Output Format

Print your answer on one line. Your answer is considered valid if the absolute error is less than or equal to $10^{−6}$.

---

### Sample Input 1

```
2 6
```

### Sample Output 1

```
0.416666667
```

When a dice is rolled twice, there are 36 possible combinations, of which 15 have a product that is a multiple of 6, so the desired probability is 15/36.

---

### Sample Input 2

```
3 2
```

### Sample Output 2

```
0.875000000
```

---


We can solve the problem by “tracking” how many factors of $2$, $3$, and $5$ are needed. (These are the only primes that ever appear in a dice outcome.) In fact, the dice outcomes (1 through 6) have the following prime‐factorizations:

- $1 = 1$    (no factors)
- $2 = 2$
- $3 = 3$
- $4 = 2^2$
- $5 = 5$
- $6 = 2\times3$

Thus, if $D$ has any prime factor other than $2$, $3$, or $5$ then no product of dice outcomes can be a multiple of $D$ (and the answer is $0$). Otherwise, write
$$D=2^{r_2}\times3^{r_3}\times5^{r_5}.$$
Our goal is then to find the probability that when a dice is rolled $N$ times the product of outcomes contains at least $r_2$ factors of $2$, $r_3$ factors of $3$, and $r_5$ factors of $5$.

Because $N$ is up to 100 and $D$ up to $10^{18}$, the required exponents may be moderately large (e.g. $r_2$ can be as high as about 60 in the worst case if $D$ is a power of 2). We will solve the problem using dynamic programming (DP) that “accumulates” the factors obtained after each dice roll.

---

### DP Idea

Define a DP state by the tuple $(i,j,k)$ representing that we have accumulated
- at least $i$ factors of $2$ (capped at $r_2$),
- at least $j$ factors of $3$ (capped at $r_3$), and
- at least $k$ factors of $5$ (capped at $r_5$).

Let $dp[i][j][k]$ be the probability of reaching that state after a certain number of rolls. Our initial state is
$$dp[0][0][0]=1.$$
When we roll the dice, for each outcome we “add” its contribution to the number of factors. (If we “exceed” the required number, we simply cap it at the required value.) For example, if we are in state $(i,j,k)$ and roll a $6$ (which contributes $(1,1,0)$), we move to the state:
$$\left(\min(r_2,i+1),\, \min(r_3,j+1),\, k\right).$$

Since each dice outcome is equally likely (with probability $1/6$), we update our DP accordingly.

After $N$ rolls the answer is the probability stored in the state
$$dp[r_2][r_3][r_5],$$
which represents that we have reached (or exceeded) the needed exponents.

---

### Implementation Details

1. **Factorize $D$:**
   - Count how many times $2$, $3$, and $5$ divide $D$.
   - If after removing these factors $D\neq1$, then output $0$.

2. **Dynamic Programming:**
   - Use a 3D DP array of dimensions $(r_2+1)\times(r_3+1)\times(r_5+1)$.
   - For each dice roll update the DP array using the 6 possible outcomes.
   - Each outcome’s contribution is precomputed.
   - After $N$ rolls, the probability that the product is a multiple of the original $D$ is $dp[r_2][r_3][r_5]$.

3. **Output the result:**
   - Print the probability with appropriate precision (e.g. fixed with 9 decimal places).

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    ll d;
    cin >> n >> d;
    int two = 0, three = 0, five = 0;
    // Factorize d by primes 2, 3, and 5 i.e 2^two * 3^three * 5^five
    while (d % 2LL == 0){
        two++;
        d /= 2LL;
    }
    while (d % 3LL == 0){
        three++;
        d /= 3LL;
    }
    while (d % 5LL == 0){
        five++;
        d /= 5LL;
    }
    // if d has no prime factors, no product of dice outcomes can be a multiple.
    if(d != 1){
        cout << fixed << setprecision(9) << 0.0 << endl;
        return 0;
    }
    // Let r2, r3, and r5 be the required exponents
    int r2 = two, r3 = three, r5 = five;
    // Precalculate dice outcome 
    vector<array<int, 3>> dice = {
        {0, 0, 0}, // Outcome 1
        {1, 0, 0}, // Outcome 2
        {0, 1, 0}, // Outcome 3
        {2, 0, 0}, // Outcome 4
        {0, 0, 1}, // Outcome 5
        {1, 1, 0} // Outcome 6
    };

    // dp[i][j][k] = probability of obtaining at least i 2's, j 3's and k 5's
    vector dp(r2 + 1, vector (r3 + 1, vector<double>(r5 + 1, 0.0)));
    // Initial case
    dp[0][0][0] = 1.0;
    // DP for n dice rolls.
    for (int roll = 0; roll < n; roll++){
        // new dp table after this roll.
        vector ndp(r2 + 1, vector (r3 + 1, vector<double>(r5 + 1, 0.0)));
        for (int i = 0; i <= r2; i++){
            for (int j = 0; j <= r3; j++){
                for (int k = 0; k <= r5; k++){
                    if (dp[i][j][k] == 0.0) continue;
                    double cur_prob = dp[i][j][k];
                    for (int d = 0; d < 6; d++){
                        // Each outomce we add its contributions to the number of factors.
                        int add2 = dice[d][0];
                        int add3 = dice[d][1];
                        int add5 = dice[d][2];
                        int ni = min(r2, i + add2);
                        int nj = min(r3, j + add3);
                        int nk = min(r5, k + add5);
                        ndp[ni][nj][nk] += cur_prob/6.0;
                    }
                }
            }
        }
        dp = ndp;
    }
    // Answer is the probability to have reached atleast (r2, r3, r5).
    cout << fixed << setprecision(9) << dp[r2][r3][r5] << endl;

    return 0;
}
```


### Detailed Explanation

1. **Factorizing $D$:**

   We remove factors of $2$, $3$, and $5$ from $D$ while counting them. If after that $D$ is not 1, then $D$ contains some other prime factor and the answer is 0.

2. **DP Array Initialization:**

   We initialize a 3D array `dp` of size $(R2+1) \times (R3+1) \times (R5+1)$ with all values set to $0$, except `dp[0][0][0]` which is $1.0$ because initially no factors have been collected.

3. **Dice Outcome Contributions:**

   We precompute for each dice outcome the number of additional factors of 2, 3, and 5 it contributes. For example, rolling a 4 gives two extra factors of 2.

4. **DP Transition:**

   For each dice roll, we iterate over all states $(i,j,k)$ and for each outcome update the state. The new state is:
   $$(\min(R2,\, i+\text{add2}),\, \min(R3,\, j+\text{add3}),\, \min(R5,\, k+\text{add5})).$$
   We add $\frac{1}{6}$ of the current state's probability to the new state because each outcome occurs with probability $1/6$.

5. **Result:**

   After $N$ rolls, the probability that the product is a multiple of $D$ is stored in `dp[R2][R3][R5]`.

6. **Output:**

   The result is printed with 9 decimal places, ensuring that the absolute error is within $10^{-6}$.
