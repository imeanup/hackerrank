## [B - Game](http://atcoder.jp/contests/tdpc/tasks/tdpc_game)


> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

Snuke and Sumeke are playing a game. At first, there are two piles. The left pile has $A$ objects, and the $i$-th object from the top has a value of $a_i$. The left pile has $B$ objects, and the $i$-th object from the top has a value of $b_i$. Snuke and Sumeke alternate between the following operations, starting with Snuke. 
* If both piles are empty, the game ends.
* If one pile is empty, take the top item from the other pile that is not empty.
* If both piles are not empty, choose whichever pile you like and take the top item.

When both players have done their best, find the total value of the items Snuke takes.

### Constraints

* $1 \le A,B \le 1000$
* $1 \le a_i, b_i \le 1000$

---

### Input Format

Input is given from standard input in the following format:

$A \quad B$ <br>
$a_1 \dots a_A$ <br>
$b_1\dots b_B$

### Output Format

Print the answer on one line.

---

### Sample Input 1

```
1 2
1
2 10
```

### Sample Output 1

```
11
```

Snuke should first choose the 1 from the left pile. Next Sumeke should choose the 2 from the right pile, and Snuke should choose the 10 from the right pile. The sum of Snuke's choices is 1 + 10 = 11.

---

### Sample Input 2

```
5 5
2 4 5 4 2
2 8 3 4 5
```

### Sample Output 2

```
21
```


---

We can solve this problem using a standard “minimax” (or [zero‐sum game](https://en.wikipedia.org/wiki/Zero-sum_game)) dynamic programming (DP) approach. In this game both players try to maximize their own final score and—because the total of all item values is fixed—their objective is equivalent to *maximizing the difference* between their score and the opponent’s score.

The key idea is to define a DP state that represents the best possible “difference” (current player’s score minus opponent’s score) obtainable from the current configuration of the two piles.

Let the left pile have $A$ items with values $a_1, a_2, \dots, a_A$ (from top to bottom) and the right pile have $B$ items with values $b_1, b_2, \dots, b_B$. We define a state $(i,j)$ where:
- $i$ is the index of the next item in the left pile (if $i \le A$) and 
- $j$ is the index of the next item in the right pile (if $j \le B$).

If $i > A$ then the left pile is empty, and similarly if $j > B$ then the right pile is empty.

Define $\text{dp}[i][j]$ as the maximum difference (current player’s score minus opponent’s score) that the current player can guarantee from the state $(i,j)$.

### How to Set Up the Recurrence

1. **Both piles empty:**  
   If both piles are empty then the game is over:
   $$\text{dp}[A+1][B+1] = 0.$$

2. **One pile is empty:**  
   - **Left empty ($i > A$, $j \le B$):**  
     The current player is forced to take the top item from the right pile. Taking the value $b_j$ gives:
     $$\text{dp}[A+1][j] = b_j - \text{dp}[A+1][j+1].$$
   - **Right empty ($j > B$, $i \le A$):**  
     The current player must take the top item from the left pile:
     $$\text{dp}[i][B+1] = a_i - \text{dp}[i+1][B+1].$$

3. **Both piles are non‐empty ($i \le A$ and $j \le B$):**  
   The current player may choose either pile. If the player:
   - **Takes from the left pile:** They gain $a_i$ and the game state becomes $(i+1, j)$ (with roles reversed). The net effect is:
     $$a_i - \text{dp}[i+1][j].$$
   - **Takes from the right pile:** They gain $b_j$ and the state becomes $(i, j+1)$, so the net effect is:
     $$b_j - \text{dp}[i][j+1].$$
   Thus, we have:
   $$\text{dp}[i][j] = \max \Big( a_i - \text{dp}[i+1][j],\; b_j - \text{dp}[i][j+1] \Big).$$

The game starts at state $(1,1)$ with Snuke’s turn. At the end, we have computed
$$\text{dp}[1][1] = \text{(Snuke's score)} - \text{(Sumeke's score)}.$$
Let the total sum of all items be
$$\text{total} = \sum_{i=1}^{A} a_i + \sum_{j=1}^{B} b_j.$$
Since
$$\text{Snuke's score} - \text{Sumeke's score} = \text{dp}[1][1]$$
and
$$\text{Snuke's score} + \text{Sumeke's score} = \text{total},$$
we can solve for Snuke’s score:
$$\text{Snuke's score} = \frac{\text{total} + \text{dp}[1][1]}{2}.$$

---

### C++ Code

Below is the complete C++ code implementing the above idea:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int A, B;
    cin >> A >> B;
    
    // Use 1-indexing for convenience.
    vector<int> a(A+1), b(B+1);
    int total = 0;
    
    // Read left pile values.
    for (int i = 1; i <= A; i++){
        cin >> a[i];
        total += a[i];
    }
    // Read right pile values.
    for (int j = 1; j <= B; j++){
        cin >> b[j];
        total += b[j];
    }
    
    // dp[i][j] = maximum difference (current player's score - opponent's score)
    // from state (i, j), where i is the index of the next item in the left pile
    // and j is the index of the next item in the right pile.
    // We create a table with dimensions (A+2) x (B+2) to handle the empty pile cases.
    vector<vector<int>> dp(A+2, vector<int>(B+2, 0));
    
    // Base case: when both piles are empty.
    dp[A+1][B+1] = 0;
    
    // If left pile is empty (i > A) but right is not, forced move.
    for (int j = B; j >= 1; j--){
        dp[A+1][j] = b[j] - dp[A+1][j+1];
    }
    
    // If right pile is empty (j > B) but left is not, forced move.
    for (int i = A; i >= 1; i--){
        dp[i][B+1] = a[i] - dp[i+1][B+1];
    }
    
    // Now fill in dp for states where both piles have items.
    for (int i = A; i >= 1; i--){
        for (int j = B; j >= 1; j--){
            int takeLeft = a[i] - dp[i+1][j];   // Current player takes from left.
            int takeRight = b[j] - dp[i][j+1];    // Or takes from right.
            dp[i][j] = max(takeLeft, takeRight);
        }
    }
    
    // dp[1][1] is (Snuke's score - Sumeke's score).
    int diff = dp[1][1];
    // Total score is: Snuke's score + Sumeke's score = total.
    // Let S = Snuke's score, then S - (total - S) = diff -> 2S = total + diff.
    int snukeScore = (total + diff) / 2;
    
    cout << snukeScore << "\n";
    return 0;
}
```

---

### Explanation of the Code

1. **Input and Initialization:**
   - The numbers $A$ and $B$ are read.
   - Two vectors `a` and `b` (of size $A+1$ and $B+1$ respectively) store the values of the objects in each pile.
   - We also compute the total sum of all items, which will be used later to compute Snuke’s final score.

2. **DP Table Setup:**
   - We define a 2D vector `dp` with dimensions $(A+2) \times (B+2)$. The extra row and column simplify handling cases where one pile is empty.
   - Base case: When both piles are empty, we set `dp[A+1][B+1] = 0`.

3. **Handling Forced Moves:**
   - If the left pile is empty (i.e. $i > A$), the player must take from the right pile. For each such state, we set:
     $$\text{dp}[A+1][j] = b_j - \text{dp}[A+1][j+1].$$
   - Similarly, if the right pile is empty (i.e. $j > B$), the player must take from the left pile:
     $$\text{dp}[i][B+1] = a[i] - \text{dp}[i+1][B+1].$$

4. **Filling the DP Table for General States:**
   - For states $(i,j)$ where both piles have items, the current player chooses the best option between taking the left item or the right item:
     $$\text{dp}[i][j] = \max\big( a_i - \text{dp}[i+1][j], \; b_j - \text{dp}[i][j+1] \big).$$

5. **Computing Snuke’s Score:**
   - The game starts at $(1,1)$ with Snuke’s turn. Thus, `dp[1][1]` equals (Snuke's score – Sumeke's score).
   - Since the sum of both scores is `total`, if we let $S$ be Snuke’s score then:
     $$S - (total - S) = \text{dp}[1][1] \quad \Longrightarrow \quad 2S = total + \text{dp}[1][1].$$
   - Finally, we compute:
     $$\text{snukeScore} = \frac{total + \text{dp}[1][1]}{2}.$$

6. **Output:**
   - The final answer (Snuke’s total score) is printed.

---

### Sample Walk‐through

Consider **Sample Input 1**:

```
1 2
1
2 10
```

- **Initial State:**  
  Left pile: [1]  
  Right pile: [2, 10]  
  Total sum = $1+2+10 = 13$.

- **Forced Moves:**  
  When the left pile is empty, the moves are forced (and similarly for when the right pile is empty).

- **DP Computation:**  
  After filling the table using the recurrence, we get:
  $$\text{dp}[1][1] = 9,$$
  which is the difference (Snuke’s score – Sumeke’s score).

- **Final Calculation:**  
  Snuke’s score $= \frac{13 + 9}{2} = 11$, which matches the sample output.

---

This DP solution runs in $O(A \times B)$ time, which is perfectly efficient for $A, B \le 1000$.
