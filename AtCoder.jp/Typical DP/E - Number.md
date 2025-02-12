## [E - Number](https://atcoder.jp/contests/tdpc/tasks/tdpc_number)


> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

<!-- $N$ 以下の正整数であって、十進法表記したときの各桁の数の和が $D$ の倍数であるものの個数を $\mod 10^9 + 7$ で求めよ。 -->

Find the number of positive integers less than or equal to $N$ such that the sum of the digits in their decimal representation is a multiple of $D$, and compute this number modulo $10^9 + 7$.

### Constraints

* $1 \le N \le 10^{10000}$
* $1 \le D \le 100$

---

### Input Format

<!-- 入力は以下の形式で標準入力から与えられる。 -->

Input is given from standard input in the following format:

$D \\ N$

### Output Format

<!-- 答えを一行に出力せよ。 -->
Print the answer on one line.

---

### Sample Input 1

```
3
100
```

### Sample Output 1

```
33
```

<!-- 1 以上 100 以下の 3 の倍数 33 個が条件を満たす。 -->
The 33 multiples of 3 between 1 and 100 satisfy the condition.

---

### Sample Input 2

```
7
123456789012345678901234567890
```

### Sample Output 2

```
468357804
```

---

We can solve this problem with a digit dynamic programming (DP) approach. The goal is to count the positive integers in the range $[1, N]$ whose sum of decimal digits is a multiple of $D$. (In other words, the sum of digits modulo $D$ is $0$.) Because $N$ can have up to 10,000 digits, we cannot iterate over all numbers. Instead we “simulate” the process of constructing the number digit‐by‐digit while keeping track of:

1. **The remainder $r$ modulo $D$ of the sum of digits chosen so far.**

2. **Whether we have already “started” the number (i.e. have seen a nonzero digit) or are still placing leading zeroes.**

3. **Whether the number we are building is still “tight” with respect to $N$ (i.e. we haven’t already chosen a digit smaller than the corresponding digit in $N$ so far) or not.**

We define a DP state as:
- **pos**: the current digit position (from 0 to $n-1$, where $n$ is the length of $N$).
- **tight**: a flag that is 1 if the digits chosen so far match the prefix of $N$, and 0 if the number already became smaller.
- **started**: a flag that is 0 if we have not yet chosen a nonzero digit (so the number is still “empty” or only consists of leading zeros) and 1 if we have.
- **r**: the current remainder modulo $D$ of the sum of digits (if we haven’t started, we always have $r=0$).

Let

$$\text{dp}[pos][tight][started][r]$$

be the number of ways (modulo $10^9+7$) to build a prefix (from the most‐significant digit to position $pos-1$) that meets the conditions. (We can “compress” the DP to only store the current position’s states.) 

### DP Transition

At a given position we decide which digit $d$ (from 0 up to a maximum that depends on the “tight” flag) to place:
- If **tight** is 1 then the digit $d$ can go from 0 up to the digit $L$ (the digit in $N$ at this position). (If $d = L$ the next state remains tight; otherwise it becomes loose.)
- If **tight** is 0 then we can choose any digit $0 \le d \le 9$.

When choosing $d$:
- The **started** flag becomes 1 if it was already 1 or if $d>0$ (i.e. the first nonzero digit appears).
- The new remainder is updated as follows:
  - If we have not started (i.e. we still have all zeros) then the remainder stays 0.
  - Otherwise, the new remainder is $(r + d) \mod D$.

### Final Answer

After processing all digits we sum over all states (regardless of the tight flag) that yield remainder 0. **But** the number “0” (i.e. when we never started) is included in these states. Since the problem asks for positive integers, we subtract 1 from the final count.

### Implementation Details

We use a DP state of dimensions:  
- **tight**: 2 states (0 or 1)  
- **started**: 2 states (0 or 1)  
- **r**: from 0 to $D-1$ (so $D$ states)

Because $N$ may have up to 10,000 digits, we process the digits one by one. The overall number of operations is roughly  

$$\text{(number of digits)} \times 2 \times 2 \times D \times 10,$$

which (with $D\le 100$) is acceptable.

Below is the complete C++ solution with comments.

---

### C++ Code

```cpp
#include<bits/stdc++.h>
using namespace std;
#include <atcoder/modint>
using namespace atcoder;
using ll = unsigned long long;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}
using mint = modint1000000007;
signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int D;
    string s;
    cin >> D >> s;
    int N = s.size();

    // dp[tight][started][r]
    // tight: 1 if current prefix is eactly equal to the prefix of N, else 0.
    // started: 1 if we have already seen a non-zero digit
    // r: remainder of the sum of digits modulo D.
    vector dp(2, vector(2, vector<mint>(D, mint(0))));
    
    // Initial start no dgits are placed.
    dp[1][0][0] = 1;

    // Process each digit position(from 0 to n-1).
    for (int pos = 0; pos < N; pos++){
        int limit = s[pos] - '0'; // Current digit of s.

        // Compressing the DP.
        vector ndp(2, vector(2, vector<mint>(D, mint(0))));
        
        // Iterate over all current DO states.
        for (int tight = 0; tight < 2; tight++){
            for (int started = 0; started < 2; started++){
                for (int r = 0; r < D; r++){
                    mint ways = dp[tight][started][r];
                    if (ways == mint(0)) continue;

                    // Determine the max digit allowed in this position.
                    int max_digit = (tight == 1 ? limit : 9); 

                    for (int d = 0; d <= max_digit; d++){
                        // New tight flag: remains 1 only if we are tight and choose the limit digit.
                        int ntight = (tight && (d == max_digit) ? 1 : 0);
                        // Update started: if we haven't started and choose a nonzero digit, then we start.
                        int nstarted = started;
                        if (!nstarted && d != 0) nstarted = 1;
                        // Update remainder.
                        int nr;
                        if (!nstarted){
                            // Still not started so the sum is 0.
                            nr = 0;
                        }
                        else {
                            nr = (r + d)%D;
                        }
                        ndp[ntight][nstarted][nr] += ways;
                    }
                }
            }
        }
        dp = ndp;
    }
    // Sum over all states (regardless of the tight flag) that have remainder 0.
    mint ans = mint(0);
    for (int tight = 0; tight < 2; tight++){
        for (int started = 0; started < 2; started++){
            ans += dp[tight][started][0];
        }
    }
    // Subtract 1 to remove the count for the number 0 (which is not a positive integer).
    cout << ans.val()-1 << endl;
    return 0;
}
```

---

### Explanation

1. **Input Reading:**

   We read $D$ and the huge number $N$ (as a string) from standard input.

2. **DP Array Initialization:**

   We create a 3D DP array `dp[tight][started][r]` where:
   - `tight` is 1 if the number built so far exactly matches the prefix of $N$.
   - `started` is 1 if a nonzero digit has been placed.
   - `r` is the remainder modulo $D$ of the sum of digits.
   
   Initially, we set:
   
   ```cpp
   dp[1][0][0] = 1;
   ```
   
   This represents that before any digit is placed, we are “tight” and haven’t started the number (so the sum is 0).

3. **DP Transition:**

   For each digit position:
   - We determine the maximum digit that can be placed based on the current state of `tight` (if tight, the maximum is the corresponding digit of $N$; otherwise it’s 9).
   - For each possible digit $d$ we update:
     - **ntight:** It remains 1 only if we were tight and we chose exactly the allowed limit; otherwise, it becomes 0.
     - **nstarted:** It becomes 1 if we already had started or if $d>0$ (starting the number).
     - **nr:** If the number has started, update the remainder by adding $d$ modulo $D$; if not, it stays 0.
     
   We add the number of ways (dividing by possibilities implicitly) to the new DP state modulo $10^9+7$.

4. **Final Answer:**

   After processing all digits, we sum all states (over both tight and non‐tight and regardless of started) where the remainder is 0. This sum counts the number $0$ as well, so we subtract 1 to count only positive integers.

5. **Output:**

   The answer is printed with modulo $10^9+7$.
