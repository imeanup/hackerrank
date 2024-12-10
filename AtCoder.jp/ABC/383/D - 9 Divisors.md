## [D - 9 Divisors](https://atcoder.jp/contests/abc383/tasks/abc383_d)

> nok0

整数 $M$ が素数 $p_1, \dots, p_k$ を用いて $p_1^{r_1} \times p_2^{r_2} \times \dots  \times p_k{r_k}$ と素因数分解されるとき、$M$ の約数の個数は $(r_1 + 1)(r_2 + 1) \dots (r_k + 1)$ となることが知られています。

この事実を用いると、素数 $p$ を用いて $p^8$ と表される正整数のうち $N$ 以下のものの個数と、異なる素数 $p,q$ を用いて $p^2q^2$ と表される正整数のうち $N$ 以下のものの個数が分かればよいです。

まず、前者は簡単です。素数を小さい順に見ていき、$8$ 乗が $N$ を超えたところで打ち切ればよいです。

後者について考えます。まず、$p,q$ については $O(N)$ 以下の素数のみ考えればよいです。

$p$ を昇順に全探索していきます。このとき、$p^2q^2 \le N$ なる $q$ の最大値は単調に減少していくので、尺取り法を用いることで、$O(N)$ 以下の素数の個数に対して線形時間でこの問題を解くことが出来ます。

---

When an integer $M$ is expressed as a prime factorization $p_1^{r_1} \times p_2^{r_2} \times \dots \times p_k^{r_k}$, the number of divisors of $M$ is known to be $(r_1 + 1)(r_2 + 1)\dots(r_k + 1)$.

Using this fact, the task is to determine two counts for integers less than or equal to $N$:
1. The count of integers expressed as $p^8$ (where $p$ is a prime).
2. The count of integers expressed as $p^2q^2$ (where $p$ and $q$ are distinct primes).

### Approach:

1. **Count of Integers in the Form $p^8$:**
   - This is straightforward. Iterate through primes in ascending order and compute $p^8$ until $p^8 > N$.

2. **Count of Integers in the Form $p^2q^2$:**
   - Only consider primes $p, q$ that are less than or equal to $\sqrt{N}$.
   - Explore all $p$ in ascending order. For each $p$, find the largest $q$ such that $p^2q^2 \leq N$.
   - Since the value of $q$ decreases monotonically as $p$ increases, a two-pointer (sliding window) technique can efficiently solve this problem in linear time relative to the number of primes less than $\sqrt{N}$.

---

> potato167

公式解説にもあるように、相異なる素数 $p,q$ を用いて $p^8$ もしくは $p^2q^2$ と表せるものが答えです。

これらはどちらも平方数です。(一般に、正の約数の数が奇数であることと平方数であることは同値です。)

よって、$N$ 以下の整数全てに対して素因数分解をして、それらが $p^4$ もしくは $pq$ という形で表せるかを判断したら良いです。

$p^4$ であることは約数の数が $5$ 個であることと同値です。

$pq$ であることは約数の数が $4$ 個かつ、$1$ でも $pq$ でもない二つの素数が互いに素であることと同値です。

これを実装すれば良いです。

[実装例 c++ 1420ms](https://atcoder.jp/contests/abc383/submissions/60551428)

とても遅いです。なぜなら、時間/空間計算量ともに $O(N\log ⁡N)$ であるからです。実際にはそれぞれの数について、以下の値があれば判定ができます。

* 最小の素因数
* 約数の数

よって、空間計算量が $Θ(N)$ に抑えられます。

[実装例 c++ 96ms](https://atcoder.jp/contests/abc383/submissions/60551568)

---

As explained in the official commentary, the answer consists of numbers that can be expressed as $p^8$ or $p^2q^2$, where $p$ and $q$ are distinct primes.

### Key Observations:

- Both $p^8$ and $p^2q^2$ are perfect squares. (In general, a number having an odd number of positive divisors is equivalent to being a perfect square.)
- Therefore, we can check all integers less than or equal to $N$, factorize them, and determine whether they can be expressed in the form $p^4$ or $pq$.

### Conditions for Each Case:
1. A number is in the form $p^4$ if and only if it has exactly 5 divisors.
2. A number is in the form $pq$ if and only if:
   - It has exactly 4 divisors.
   - The two prime factors $p$ and $q$ are distinct and coprime (mutually prime).

### Implementation:
- This process can be implemented directly. 
- **Example (C++ Implementation 1420ms)**: [Link to Solution](https://atcoder.jp/contests/abc383/submissions/60551428)
  - This implementation is slow because the time and space complexity are both $O(N \log N)$.

### Optimization:
- Instead of factorizing every number, we can use precomputed data:
  - **Smallest prime factor** for each number.
  - **Number of divisors** for each number.
- Using this approach, the space complexity can be reduced to $\Theta(N)$.

- **Optimized Example (C++ Implementation 96ms)**: [Link to Solution](https://atcoder.jp/contests/abc383/submissions/60551568)

---

> blueberry1001

**実装面での補足と素数列挙の方法について（初心者向け**

---

公式解説にもあるように、相異なる素数 $p,q$ を用いて $p^8$ もしくは $p^2q^2$ と表せるものが答えです。

入力例2を見ると、答えは最大でも $407073$ であることがわかります。よって、全列挙が可能です。

$p,q$ を全探索します。ただし、$p,q$ は素数です。 $p^2q^2 \le N$ より、$p,q \le N$ なので、$N$ 以下の素数を列挙できれば、 $p,q$ を全探索することで答えを求めることができます。

素数の列挙はエラトステネスの篩と呼ばれるアルゴリズムを用いて行うことができます。（「素数列挙　競プロ」などで検索することですぐに見つけることができるため、コンテスト中に知らなかったとしてもこの情報にたどり着くことは可能です）

解法をまとめます。

* エラトステネスの篩を用いて、 $N$ 以下の素数を列挙する。（ただし実際には実装の簡略化のため、$N$ を計算せずに $10^6$ 以下の素数を列挙する）
* $2$ 重ループを用いて $p,q$ を全探索する。
* $p^2q^2$ が $N$ 以下であるとき答えに $1$ を加算する。
* $p^8$ が $N$ 以下であるときにも答えに$1$を加算する。ただし、オーバーフローに注意。

実装は以下のようになります。 なお、エラトステネスの篩は定期的に使用機会のあるアルゴリズムなので、ライブラリ化しておくとよいでしょう。（以下をコピペしても大丈夫です）

```cpp
#include<bits/stdc++.h>
using namespace std;
//この問題で扱う整数は最大4×10^12であり、int型の上限を超えるため、long longを用いる。
//実装の簡略化のためlong longをllとして使えるようにする。（以下、llという型はlong long型と同じ）
using ll = long long;

//コピペする場合はここから～
//Era(n)を呼んだ後、isprime[i]=iが素数かどうか　となっている。
vector < bool > isprime;
//返り値は素数のリスト。
vector < ll > Era(int n) {
	isprime.resize(n, true);
	vector < ll > res;
	isprime[0] = false;
	isprime[1] = false;
	for(ll i = 2; i < n; ++i) isprime[i] = true;
	for(ll i = 2; i < n; ++i) {
		if(isprime[i]) {
			res.push_back(i);
			for(ll j = i * 2; j < n; j += i) isprime[j] = false;
		}
	}
	return res;
}
//コピペする場合は～ここまで

int main(){
	ll n;
	cin >> n;
	vector<ll> v = Era(1000005);
	ll ans{};
	for(ll p:v){
		if(p*p*p*p>n)break;
		//オーバーフロー対策
		if(p<100){
			//pow関数は誤差が出ることに注意。8乗程度ならこうやって書いた方が安全（ただし数え間違いの危険はある）
			if(p*p*p*p*p*p*p*p<=n)ans++;
		}
		for(ll q:v){
			if(q<=p)continue;
			if(p*p*q*q<=n){
				ans++;
			}
			else{
				break;
			}
		}
	}
	cout << ans << endl;
	return 0;
}
```

---

### Additional Implementation Notes and Prime Enumeration Method (Beginner-Friendly)

---

As explained in the official commentary, the goal is to find numbers that can be expressed as $p^8$ or $p^2q^2$, where $p$ and $q$ are distinct primes.

From **Input Example 2**, we can observe that the maximum result is $407073$. Therefore, brute force enumeration is feasible.

### Steps to Solve the Problem:

1. **Enumerate $p, q$:**
   - Both $p$ and $q$ must be prime numbers.
   - Given $p^2q^2 \leq N$, it follows that $p, q \leq \sqrt{N}$.
   - If we can enumerate all primes less than $N$, we can explore $p, q$ to calculate the result.

2. **Prime Enumeration:**
   - Use the **Sieve of Eratosthenes**, an efficient algorithm for finding all prime numbers up to a given limit.
   - This algorithm is well-documented and can be quickly learned (e.g., by searching "prime enumeration competitive programming").
   - Even if unfamiliar during a contest, this information can be easily accessed.

### Summary of the Solution:

1. Use the Sieve of Eratosthenes to generate all primes less than $10^6$ (to simplify implementation, even if $N$ is smaller).
2. Perform a double loop to explore $p, q$:
   - Increment the answer when $p^2q^2 \leq N$.
3. Also increment the answer when $p^8 \leq N$, taking care to avoid overflow.

### Example Implementation (C++):

The following implementation demonstrates this approach. Note that Sieve of Eratosthenes is included as a reusable utility.

```cpp
#include<bits/stdc++.h>
using namespace std;

// Define long long for handling large numbers
using ll = long long;

// Sieve of Eratosthenes: Generates a list of primes up to n
vector<bool> isprime;
vector<ll> Era(int n) {
    isprime.resize(n, true);
    vector<ll> res;
    isprime[0] = false;
    isprime[1] = false;
    for (ll i = 2; i < n; ++i) isprime[i] = true;
    for (ll i = 2; i < n; ++i) {
        if (isprime[i]) {
            res.push_back(i);
            for (ll j = i * 2; j < n; j += i) isprime[j] = false;
        }
    }
    return res;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> primes = Era(1000005); // Generate primes up to 10^6
    ll ans = 0;

    // Check for numbers of the form p^8
    for (ll p : primes) {
        if (p * p * p * p > n) break; // Stop if p^4 > n
        // Prevent overflow by limiting p
        if (p < 100) {
            if (p * p * p * p * p * p * p * p <= n) ans++;
        }
    }

    // Check for numbers of the form p^2q^2
    for (ll p : primes) {
        for (ll q : primes) {
            if (q <= p) continue; // Ensure p < q
            if (p * p * q * q <= n) {
                ans++;
            } else {
                break; // Stop if p^2q^2 > n
            }
        }
    }

    cout << ans << endl;
    return 0;
}
```

---

### Key Notes:

1. **Prime Enumeration:**
   - The Sieve of Eratosthenes is an efficient $O(n \log \log n)$ algorithm.
   - This method is common in competitive programming and worth keeping as a library function.

2. **Overflow Handling:**
   - For $p^8$, manually multiply instead of using `pow()` to avoid precision errors.
   - Keep checks for overflow to ensure correctness.

3. **Performance:**
   - Time complexity is approximately $O(n \log \log n + k^2)$, where $k$ is the number of primes up to $\sqrt{N}$.
   - Space complexity is $O(N)$.

---


**$O(N^{1/3})$ 時間解法**

---

⚠️ 発展的な内容を含みます。

$n$ 以下の素数の個数を $\pi(n)$ と書きます。また、$S(n)$ を下記で定義します。

$$S(n) = \{1, 2, \dots, \left\lfloor n \right\rfloor \} \cup \{\left\lfloor \frac{n}{1} \right\rfloor, \left\lfloor \frac{n}{2} \right\rfloor, \dots, \left\lfloor \frac{n}{\lfloor n \rfloor}\right\rfloor$$

前提として、与えられた $n$ に対して、各 $i \in S(n)$ における $\pi(i)$ を求めるのは（全体で）$O(n^{2/3})$ 時間や $O(n^{2/3}/ \log⁡(n)^{1/3})$ 時間で可能です。

 **see also** : [関連スライド](https://rsk0315.github.io/slides/prime-counting.pdf)

---

$p^8 \le N$ なる素数の個数は愚直に求めても $O(N^{1/8})$ 時間なので、無視できます。

$p^2 q^2 \le N$ なる素数のペアに関して考えます。$p$ を固定したとき、$p < q \le \frac{N}{p}$ であるので、$p$ 以下の素数と $\frac{N}{p}$ 以下の素数を数えられればよいです。$q$ の整数性などから、$\pi\left(\left\lfloor \dfrac{\lfloor N \rfloor}{p} \right\rfloor\right) − \pi(p)$ に等しいです。

 **note** : $i$ 番目の素数 $\pi$ に対して $\pi(pi) = i$ なので、$\pi(p)$ の項は簡単に求められます。

よって、各 $i \in S(\lfloor N \rfloor)$ における $\pi(i)$ を求めておけばよく、これは $O(\lfloor N\rfloor^{2/3})=O(N^{1/3})$ 時間で可能です。

$p < q$ なので $p < N^{1/4}$ の範囲で和を取ればよく、（上記の前処理により各項は $O(1)$ 時間で求められるので、前処理の計算量に応じて）全体で $O(N^{1/3})$ 時間や $O(N^{1/3}/ \log⁡(N)^{1/3})$ 時間などになります。

[提出 #60552451](https://atcoder.jp/contests/abc383/submissions/60552451), 1 ms

---

### **$O(N^{1/3})$ Time Solution**

---

⚠️ This contains advanced content.

Let the number of primes less than or equal to $n$ be denoted as $\pi(n)$. Also, define $S(n)$ as follows:

$$
S(n) = \{1, 2, \dots, \left\lfloor n \right\rfloor \} \cup \left\{\left\lfloor \frac{n}{1} \right\rfloor, \left\lfloor \frac{n}{2} \right\rfloor, \dots, \left\lfloor \frac{n}{\left\lfloor n \right\rfloor}\right\rfloor \right\}
$$

### Assumptions:
- For a given $n$, it is possible to calculate $\pi(i)$ for each $i \in S(n)$ in $O(n^{2/3})$ time or $O(n^{2/3} / \log(n)^{1/3})$ time.

**See also**: [Related Slides](https://rsk0315.github.io/slides/prime-counting.pdf)

---

1. **Counting Primes for $p^8 \leq N$:**
   - The number of primes $p$ such that $p^8 \leq N$ can be computed directly, and this takes $O(N^{1/8})$ time, which is negligible in this case.

2. **Counting Prime Pairs for $p^2 q^2 \leq N$:**
   - When $p$ is fixed, $q$ must satisfy $p < q \leq \frac{N}{p}$. Therefore, we need to count the primes less than or equal to $p$ and the primes less than or equal to $\frac{N}{p}$.
   - The number of such primes is given by $\pi\left(\left\lfloor \frac{N}{p} \right\rfloor\right) - \pi(p)$.

   **Note**: For the $i$-th prime $p_i$, we have $\pi(p_i) = i$, so $\pi(p)$ can be easily computed.

3. **Efficient Calculation:**
   - If we compute $\pi(i)$ for each $i \in S(\lfloor N \rfloor)$, this can be done in $O(\lfloor N \rfloor^{2/3}) = O(N^{1/3})$ time.
   - Since $p < q$, we only need to consider $p$ up to $N^{1/4}$. Using the precomputed $\pi(i)$ values, each term can be calculated in $O(1)$ time. Thus, the overall complexity is $O(N^{1/3})$ or $O(N^{1/3} / \log(N)^{1/3})$, depending on the pre-processing.

**[Submission #60552451](https://atcoder.jp/contests/abc383/submissions/60552451), 1 ms**
