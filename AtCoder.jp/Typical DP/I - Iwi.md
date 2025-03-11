## [I - Iwi](https://atcoder.jp/contests/tdpc/tasks/tdpc_iwi)


> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

<!-- $s$ は i と w からなる文字列である。すぬけ君は、この中から連続する三文字が "iwi" となっている部分を取り除く操作を繰り返すことができる。(iwi を取り除くと、その左側と右側にあった文字列が連結され、長さが三文字短い新しい文字列ができる。) 操作を行うことのできる回数の最大値を求めよ。 -->

The string $s$ consists of the characters `i` and `w`. Snuke can repeatedly perform an operation where any consecutive three-character substring that forms `"iwi"` is removed. (When `"iwi"` is removed, the string to its left and the string to its right are concatenated to form a new string that is three characters shorter.) Determine the maximum number of times this operation can be performed.

### Constraints

* $1 \le |s| \le 300$
* Each character in $s$ will be either `i` or `w`.

---

### Input Format

<!-- 入力は以下の形式で標準入力から与えられる。 -->
Input is given from standard input in the following format:

$s$

### Output Format

<!-- 答えを一行に出力せよ。 -->
Print the answer on one line.

---

### Sample Input 1

```
iwiwii
```

### Sample Output 1

```
2
```

<!-- 先に 3 文字目から 5 文字目の iwi を取り除くのが最適である。 -->
It is best to remove the iwi characters 3 through 5 first.

---

### Sample Input 2

```
iwiwwwiiiwiwiwiiwii
```

### Sample Output 2

```
5
```

---

We can solve this problem by “interval DP.” Intuitively, we want to “simulate” the removal operations (which remove exactly three characters: “iwi”) on a substring. (The removals can be performed in any order, and—by “removing” a substring—the remaining parts become adjacent so that later removals may “bridge” between characters that were originally separated.) Because the string’s length is at most 300, we can use an algorithm that works in roughly $O(n^3)$ time.

A key idea is to “decompose” the string into (contiguous) intervals and decide in which intervals we can remove characters completely (i.e. reduce the interval to “nothing”) by repeatedly removing “iwi” blocks. (In such a process the total “score” is the number of removals performed.) However, when our removals are performed on one part of the string, they are “independent” of removals done on a disjoint part. (For example, if we can completely remove two adjacent segments, then removing them both is valid.) Also, we might perform removals on an interval without completely deleting it. (For example, one may remove some disjoint “iwi” blocks and leave some “leftover” letters.)  
 
To organize our DP we define two functions on an interval $[i,j]$ (using 0–based indices):

1. **$dp[i][j]$**: the maximum number of removals that can be performed on the substring $s[i\ldots j]$ (the removals may be performed “inside” the interval; we do not require that the whole interval is removed).

2. **$rem[i][j]$**: the maximum number of removals obtainable **if** we can completely remove (i.e. “fully eliminate”) the substring $s[i\ldots j]$ by a sequence of removals. (If it is impossible to completely remove the substring, we set $rem[i][j] = -\infty$. Since all valid removal counts are nonnegative we can represent “impossible” by $-1$ in our code.)

Then the final answer will be $dp[0][n-1]$ (where $n = |s|$).

### How Do We Compute the DP?

There are two kinds of transitions:

1. **Splitting the interval:**  
   Any interval $[i,j]$ can be “split” at some index $k$ (with $i \le k < j$); then we can work on the left and right pieces separately. In other words, we have
   $$dp[i][j] = \max_{i\le k<j} \{dp[i][k] + dp[k+1][j]\}\,.$$
   (Likewise, if both pieces can be completely removed, then the entire interval can be completely removed:
   $$rem[i][j] = \max_{i\le k<j} \{ rem[i][k] + rem[k+1][j] \}\,.$$
   Of course, when either piece is not completely removable (i.e. its $rem$ value is “impossible”) then that splitting does not yield a “complete removal”.)

2. **Removing a block “iwi” that spans an interval:**  
   Notice that the only removal operation is to remove three consecutive characters that (in the current string) read “iwi.” (After some removals the remaining characters become adjacent even if they were not consecutive in the original string.)  
   
   Thus, one way to completely remove an interval is if its first and last characters are both `'i'` and for some position $m$ between them we have a `'w'` so that, after **completely** removing the “inside” parts, the three letters become adjacent and form the pattern “iwi.” More precisely, if
   - $s[i] = \mathtt{'i'}$ and $s[j] = \mathtt{'i'}$,
   - and for some $m$ with $i+1 \le m \le j-1$ we have $s[m] = \mathtt{'w'}$,
   - and if the “middle parts” $s[i+1\,..\,m-1]$ and $s[m+1\,..\,j-1]$ can be completely removed (or are empty),
   
   then by first completely removing the two inner parts and then removing the resulting “iwi” (which adds one removal operation) we completely remove the whole interval. In formula we get a candidate removal count
   $$1 + (\text{removals to remove } s[i+1\,..\,m-1]) + (\text{removals to remove } s[m+1\,..\,j-1])\,.$$
   We maximize over all such choices of $m$. (If the interval length is exactly 3 and $s[i..j] = \mathtt{"iwi"}$, then we set $rem[i][j] = 1$.)
   
Once we have computed $rem[i][j]$ (the best count when we can completely remove $s[i\ldots j]$), we update
$$dp[i][j] = \max\{dp[i][j],\, rem[i][j]\}\,.$$

### Base Cases

- For an interval of length 0 (empty string) we can say that “completely removed” has a value of 0.
- For intervals of length 1 or 2, no removal is possible so we set $dp[i][j] = 0$ and $rem[i][j] = -1$ (impossible).
- For an interval of length 3, if it is exactly “iwi” then we set $dp[i][j] = rem[i][j] = 1$; otherwise, they are 0 and “impossible” (i.e. $-1$) respectively.

### Recurrence Summary

For an interval $[i,j]$ (with $j-i+1\ge4$):

1. **Splitting:**  
   $$dp[i][j] = \max_{i \le k < j} \{ dp[i][k] + dp[k+1][j] \}\,,$$
   and similarly try
   $$rem[i][j] = \max_{i \le k < j,\; rem[i][k] \neq -1,\; rem[k+1][j] \neq -1} \{ rem[i][k] + rem[k+1][j] \}\,.$$

2. **Pattern “iwi” removal:**  
   If $s[i]=='i'$ and $s[j]=='i'$ then for every $m$ with $i+1 \le m \le j-1$ such that $s[m]=='w'$ do:
   - Let $L =$ (if $i+1 \le m-1$ then $rem[i+1][m-1]$ else 0)
   - Let $R =$ (if $m+1 \le j-1$ then $rem[m+1][j-1]$ else 0)
   - If both the left and right parts are completely removable (i.e. if they are either empty or $rem$ is not $-1$), then candidate $= 1 + L + R$.  
     
   Then set
   $$rem[i][j] = \max\{ rem[i][j], \text{candidate} \}\,.$$
   
3. Finally, set  
   $$dp[i][j] = \max\{dp[i][j], rem[i][j]\}\,.$$

### Example

Let’s check the sample input  
```
iwiwii
```
(indexed as 0 1 2 3 4 5: i, w, i, w, i, i).  
- The substring $s[0\ldots2] = \mathtt{"iwi"}$ is removable (base case) with count 1.  
- Then one optimal strategy is to first remove the block “iwi” covering indices 2–4; then the remaining characters (from positions 0,1,5) form “iwi” and can be removed to get a second removal.  
Thus the answer is 2.

### Implementation

Below is the complete C++ code with comments.

---

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = unsigned long long;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    int n = s.size();

    // dp[i][j] = maximum number of removal operations possible on s[i...j]
    // rem[i][j] = maximum removals possible if s[i...j] can be completely removed,
    //             or -1 if it is not completely removable.
    vector dp(n, vector<int>(n, 0));
    vector rem(n, vector<int>(n, -1));
    // Base cases: intervals of length 1 and 2 cannot be removed.
    for (int i = 0; i < n; i++){
        dp[i][i] = 0;
        rem[i][i] = -1;
    }

    for (int i = 0; i + 1 < n; i++){
        dp[i][i+1] = 0;
        rem[i][i+1] = -1;
    }
    // Base case: intervals of length 3.
    for (int i = 0; i + 2 < n; i++){
        int j = i+2;
        if (s[i] == 'i' && s[i+1] == 'w' && s[j] == 'i'){
            dp[i][j] = 1;
            rem[i][j] = 1;
        }
        else {
            dp[i][j] = 0;
            rem[i][j] = -1;
        }
    }
    // Process intervals of length L from 4 to n.
    for (int l = 4; l <= n; l++){
        for (int i = 0; i+l <= n; i++){
            int j = i+l-1;
            int best = 0;
            // Option 1: split the interval into two parts.
            for (int k = i; k < j; k++){
                chmax(best, dp[i][k] + dp[k+1][j]);
            }

            dp[i][j] = best;

            int rem_val = -1;
            // Option A: if s[i]=='i' and s[j]=='i', then try to pick a middle letter 'w'
            if (s[i] == 'i' && s[j] == 'i'){
                for (int m = i+1; m <= j-1; m++){
                    if (s[m] == 'w'){
                        int left_val = 0, right_val = 0;
                        if (m-1 >= i+1){
                            if (rem[i+1][m-1] == -1) continue;
                            left_val = rem[i+1][m-1];
                        }
                        if (m+1 <= j-1){
                            if (rem[m+1][j-1] == -1) continue;
                            right_val = rem[m+1][j-1];
                        }
                        chmax(rem_val, 1 + left_val + right_val);
                    }
                }
            }
            // Option B: try splitting the entire interval into two completely removable parts.
            for (int k = i; k < j; k++){
                if (rem[i][k] != -1 && rem[k+1][j] != -1){
                    chmax(rem_val, rem[i][k] + rem[k+1][j]);
                }
            }

            rem[i][j] = rem_val;
            chmax(dp[i][j], rem[i][j]);
        }
    }
    cout << dp[0][n-1] << "\n";

    return 0;
}
```

---

### Explanation Recap

1. **Base Cases:**  
   Intervals of length 1 or 2 cannot be removed (so $dp=0$ and $rem=-1$); for an interval of length 3, if it is exactly “iwi” we set $dp=rem=1$.

2. **Splitting:**  
   For any interval $[i,j]$ we first try all ways of splitting it into two parts and combine the best scores.

3. **Complete Removal (“rem”) Option:**  
   We then check if the entire interval can be completely removed by “contracting” it into a single “iwi” removal. For this, if $s[i]=='i'$ and $s[j]=='i'$, we try every index $m$ (from $i+1$ to $j-1$) where $s[m]=='w'$ and require that the intervals immediately inside (i.e. $s[i+1\,..\,m-1]$ and $s[m+1\,..\,j-1]$) are completely removable. This yields one removal plus the removals from the inner parts. We also try splitting the interval completely (if two adjacent pieces are each completely removable).

4. **Combining:**  
   Finally, $dp[i][j]$ is the maximum of the value we get by splitting and the value from complete removal. Our answer is $dp[0][n-1]$.

In the sample, “iwiwii” the optimal answer is 2.

---

This solution runs in $O(n^3)$ time which is acceptable for $n\le300$.
