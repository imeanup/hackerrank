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
