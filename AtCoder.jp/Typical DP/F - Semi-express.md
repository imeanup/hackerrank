## [F - Semi-express](https://atcoder.jp/contests/tdpc/tasks/tdpc_semiexp)

> Time Limit: 2 sec / Memory Limit: 256 MB

### Problem Statement

<!-- ある路線には駅 1 から駅 $N$ までの $N$ 個の駅がある。すぬけ君は、この路線に準急を走らせることにした。

* 準急は、駅 1 に止まり、{駅 2, ..., 駅 $N-1$} の部分集合に止まり、駅 $N$ に止まる。
* 連続する $K$ 個以上の駅に止まると、客が飽きてしまうので、そのようなことはしない。

準急の停車駅の組み合わせとして何通り考えられるか、mod 1,000,000,007 で求めよ。 -->

---

In a certain railway line, there are $N$ stations numbered from station $1$ to station $N$. Snuke has decided to run a semi-express train on this line.

- The semi-express train stops at station 1, a subset of stations from {station 2, ..., station $N-1$}, and station $N$.
- The train does not stop at $K$ or more consecutive stations, as it would bore the passengers.

Determine the number of possible combinations of stopping stations for the semi-express train, modulo $1,000,000,007$.

### Constraints

* $2 \le K \le N \le 1000000$

### Input Format

<!-- 入力は以下の形式で標準入力から与えられる。 -->
Input is given from standard input in the following format:

$N \quad K$

### Output Format

<!-- 答えを一行に出力せよ。 -->
Print the answer on one line.

---

### Sample Input 1

```
10 2
```

### Sample Output 1

```
21
```

---

### Sample Input 2

```
10 10
```

### Sample Output 2

```
255
```


---

We can “reduce” the problem to one about forbidden patterns in binary strings. (It turns out that with a little thought the answer can be expressed in “nice” closed‐form terms.) Let’s explain.

Suppose the train “stops” at some of the $N$ stations. (By definition the train always stops at station $1$ and station $N$.) For the intermediate stations (stations $2,3,\dots,N-1$) we “choose” whether or not to stop. (There are $2^{\,N-2}$ possible ways if no further rule applied.) Now, the condition “it is not allowed that the train stops at $K$ or more consecutive stations.” (In other words, if you list the stations at which the train stops, you are not allowed to have a block of $K$ (or more) consecutive stations. Equivalently, if you “mark” a $1$ at every station where the train stops and a $0$ where it does not, then—with the convention that stations $1$ and $N$ are always $1$—the resulting binary string of length $N$ is not allowed to have $K$ consecutive $1$’s.)

Thus the counting problem is:

> **Count the number of binary strings $a_1a_2\cdots a_N$ with**
>
> - $a_1 = a_N = 1$ (because the train always stops at station $1$ and $N$)
> - For $2\le i\le N-1,$ $a_i$ is $0$ (“don’t stop”) or $1$ (“stop”)
> - The string does not contain $K$ consecutive $1$’s.
>
> (The answer is taken modulo $10^9+7$.)

It is known (and you can prove by a short induction) that if we denote by

$$f(n)=\text{(Number of binary strings of length $n$ with no $K$ consecutive $1$’s)}$$

then

- For $n<K$ we have no possibility of “$K$ in a row” so
  $$f(n)=2^n.$$
  * Since the strings are too short to have $k$ consecutive ones.
- For $n\ge K,$ the recurrence
  $$f(n)= f(n-1)+f(n-2)+\cdots+f(n-K)$$

  holds (this is “well–known” for these “$K$–bonacci”–type recurrences).

But notice: our strings have the extra condition that the first and last digits are $1$. (They are “forced”.) How can we count those? (One nice idea is to “remove” the conditions by inclusion–exclusion.) In fact, one may show that the number of valid strings (of length $N$ with no $K$ consecutive $1$’s) that also satisfy $$a_1 = a_N = 1$$ is $$\text{Answer} = f(N) - 2f(N-1) + f(N-2).$$

Why? (A brief explanation follows.)

- $f(N)$ is the total number of valid strings (with no restriction on the endpoints).
- The number of valid strings with $a_1=0$ is exactly $f(N-1)$ (since if $a_1=0$ then the remaining $N-1$ digits can be any valid string of length $N-1$). (Likewise for $a_N=0$.)
- But then the strings with both $a_1=0$ and $a_N=0$ have been subtracted twice; they number $f(N-2)$. <details><summary>More on f(n-2)</summary> number of such strings $|A \cap B| = f(N-2)$, we fix $a_1 = 0$ and $a_N = 0$, leaving $N-2$ positions to fill. </details>

A quick check with the samples shows that this is exactly what we need. (Remember the “forbidden run” means that the maximum allowed consecutive stops is “one less than $K$”.) For example:

- **Sample 1:** $N=10,\; K=2$.

  With $K=2$ “$2$ consecutive stops are forbidden” (i.e. no two stops in a row are allowed). (Since station $1$ and station $N$ are forced stops, the rule forces station $2$ and station $N-1$ to be “don’t‐stop”. In fact one may show that in this case the number of possibilities is exactly the number of independent sets on a path of length $6$ – which is $21$.)

  Let’s compute using our recurrence. For $K=2,$ note that for $n<2$ we have

  $$f(0)=1,\quad f(1)=2.$$

  And for $n\ge 2,$

  $$f(n)=f(n-1)+f(n-2).$$

  So

  $$f(2)=2+1=3,\;f(3)=3+2=5,\;f(4)=5+3=8,\;f(5)=8+5=13,\;f(6)=13+8=21,\;f(7)=21+13=34,\;f(8)=34+21=55,\;f(9)=55+34=89,\;f(10)=89+55=144.$$

  Then the answer is

  $$144-2\cdot89+55 =144-178+55=21.$$
- **Sample 2:** $N=10,\; K=10$.

  Here (since $K$ is so large) no “run–restriction” is effective except that the string with all $1$’s (which would be $10$ consecutive $1$’s) is forbidden. (In other words, $f(n)=2^n$ for $n<10,$ and for $n=10,$

  $$f(10)=2^{10}-1=1023.)$$

  Then

  $$f(10)-2f(9)+f(8) = 1023-2\cdot512+256 =1023-1024+256=255.$$

Because $N$ can be as large as $10^6$ (and $K$ up to $N$), we can “pre–compute” all the values $f(0),f(1),\dots,f(N)$ in $O(N)$ time using a “sliding–window” sum for the recurrence. (The recurrence

$$f(n)=f(n-1)+f(n-2)+\cdots+f(n-K)$$

can be computed in $O(1)$ per step if we maintain the sum $f(n-1)+\cdots+f(n-K)$.)

The following C++ code implements the solution. (See the comments for details.)

```cpp
#include<bits/stdc++.h>
using namespace std;
#include <atcoder/modint>
using namespace atcoder;
using mint = modint1000000007;

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<mint>f(n+1, mint(0));
    f[0] = mint(1);
    int LIM = min(n, k-1);
    for (int i = 1; i <= LIM; i++){
        f[i] = 2*f[i-1];
    }
    mint window = 0;
    if (n >= k) {
        for (int i = 0; i < k; i++){
            window += f[i];
        }
        f[k] = window;
        for (int i = k+1; i <= n; i++){
            window += f[i-1];
            window -= f[i-1-k];
            f[i] = window;
        }
    }
    mint ans = f[n] - 2*f[n-1] + f[n-2];
    cout << ans.val() << "\n";
    return 0;
}
```

### Explanation of the Code

1. **Input and Setup:** We read $N$ (the number of stations) and $K$ (the “forbidden‐run” threshold). (Recall that stations $1$ and $N$ are forced stops.)
2. **DP Array “$f$” for Valid Strings:** We let $f(n)$ be the number of binary strings of length $n$ that do not contain $K$ consecutive $1$’s. For small $n$ (i.e. $n < K$) we have $f(n)=2^n$ because no run of $K$ ones can occur. For $n\ge K$ we use the recurrence

   $$f(n)= f(n-1)+f(n-2)+\cdots+f(n-K).$$

   We compute these values in a loop from $n=0$ to $n=N$ using a “sliding–window” sum so that each step takes $O(1)$ time. (Since $N\le 10^6,$ this is efficient.)
3. **Extracting the Answer:** Not every valid $n$–long string is “admissible” for our problem because we require the first and last digits to be $1$. (That is, the train must stop at station $1$ and station $N$.) By a short inclusion–exclusion argument the number of valid strings with $a_1 = a_N = 1$ is

   $$f(N) - 2 f(N-1) + f(N-2).$$

   (You can check that this formula works for small values.) We then output the answer modulo $10^9+7$.
