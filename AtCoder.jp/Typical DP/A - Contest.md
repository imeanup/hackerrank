## [A - Contest](https://atcoder.jp/contests/tdpc/tasks/tdpc_contest)

> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

<!-- $N$ 問の問題があるコンテストがあり、$i$ 問目の問題の配点は $p_i$ 点である。コンテスタントは、この問題の中から何問か解き、解いた問題の配点の合計が得点となる。このコンテストの得点は何通り考えられるか。 -->

There is a contest with $N$ problems, and the score for the $i$-th problem is $p_i$ points. Contestants solve some of these problems, and the total score for the solved problems is their score. How many possible scores are there in this contest?

### Constraints

* $1 \le N \le 100$
* $1 \le p_i \le 100$

### Input Format

<!-- 入力は以下の形式で標準入力から与えられる。 -->
Input is given from standard input in the following format:

$N$ <br>
$p_1p_2\dots p_N$

### Output Format

<!-- 答えを一行に出力せよ。 -->
Print the answer on one line.

### Sample Input 1

```
3
2 3 5
```

### Sample Output 1

```
7
```

<!-- 0, 2, 3, 5, 7, 8, 10 の 7 通りの得点が考えられる。 -->
There are seven possible scores: 0, 2, 3, 5, 7, 8, and 10.

---

### Sample Input 2

```
10
1 1 1 1 1 1 1 1 1 1
```

### Sample Output 2

```
11
```

<!-- 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 の 11 通りの得点が考えられる。 -->
There are 11 possible scores: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

---

We can solve this problem using a simple dynamic programming (DP) technique that is very similar to the “subset sum” problem. In this problem, we want to determine which total scores (i.e. sums) are achievable by picking some subset of the $N$ problems. (Note that choosing no problems gives a score of $0$.)

Given that $N$ can be up to $100$ and each $p_i \le 100$, the maximum score possible is $100 \times 100 = 10\,000$. Thus, we only need to consider sums from $0$ up to $10\,000$.

A very convenient way to implement this is by using C++’s `bitset`. The idea is as follows:

1. **DP Definition:**

   We define a bitset `dp` where `dp[s]` is `true` if it is possible to achieve a total score of $s$ by solving some subset of the problems.

2. **Initialization:**

   Initially, `dp[0]` is set to `true` since a score of $0$ is always achievable (by not solving any problem).

3. **DP Transition:**

   For each problem with score $p$, we update our DP as follows:
   
   - If a sum $s$ was already achievable, then by solving this problem we can also achieve the sum $s + p$.
   - In terms of bitset, we can “shift” the current bitset to the left by $p$ positions (i.e. `dp << p`) and then combine it with the current `dp` using the bitwise OR operator.
   - This is written concisely as:  
     ```cpp
     dp |= (dp << p);
     ```

4. **Counting the Possible Scores:**

   At the end, the number of distinct achievable scores is just the count of `true` bits in the `dp` bitset. We then print this count.

---

### C++ Code

```cpp
#include <iostream>
#include <bitset>
using namespace std;

int main(){
    int N; 
    cin >> N;
    // Maximum possible total score: 100 problems * 100 points each = 10000
    const int MAX_SUM = 10000;  
    // dp[s] will be true if sum s is achievable
    bitset<10001> dp; 
    dp[0] = 1;  // score 0 is always possible
    
    for (int i = 0; i < N; i++){
        int p; 
        cin >> p;
        // Update dp: if dp[s] is true, then dp[s+p] becomes true.
        dp |= (dp << p);
    }
    
    // The answer is the count of true bits in dp.
    cout << dp.count() << "\n";
    return 0;
}
```

---

### Detailed Explanation

1. **Input Reading:**
   
   - We first read the number of problems $N$.
   - Then, for each problem, we read its score $p_i$.

2. **Dynamic Programming Setup:**

   - We create a `bitset<10001>` named `dp` to cover all possible scores from $0$ to $10\,000$.
   - We initialize `dp[0]` as `true` since a score of $0$ is achievable without solving any problems.

3. **DP Transition with Bitset:**

   - For every problem with score $p$, we shift the entire bitset left by $p$ positions. The bitset shift `dp << p` represents every score increased by $p$.
   - We then merge these new possible scores with the existing ones using the OR operator (`|=`), ensuring that all previously achievable scores remain marked as achievable.

4. **Output:**

   - After processing all problems, `dp.count()` gives the total number of positions in the bitset that are `true`, i.e., the number of distinct scores that can be obtained.
   - We print this count.

---

### Example Walk‐through

For **Sample Input 1**:
```
3
2 3 5
```

- **Initialization:**  
  `dp[0] = true`.

- **After first problem (2 points):**  
  Shifting `dp` by 2: score $0$ leads to score $2$ being achievable.  
  Now achievable scores: $0, 2$.

- **After second problem (3 points):**  
  From $0$, we get $3$; from $2$, we get $5$.  
  Now achievable scores: $0, 2, 3, 5$.

- **After third problem (5 points):**  
  From $0$, we get $5$; from $2$, we get $7$; from $3$, we get $8$; from $5$, we get $10$.  
  Now achievable scores: $0, 2, 3, 5, 7, 8, 10$.

- **Result:**  
  There are 7 distinct scores.

This matches the sample output.

---

This solution efficiently computes the number of possible scores using bit-level operations in $O(N \times \text{MAX\_SUM})$ time, which is very efficient for the given constraints.
