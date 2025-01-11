## [D - Coming of Age Celebration](https://atcoder.jp/contests/abc388/tasks/abc388_d)

$i$ 人目の宇宙人を単に人 $i$ と書きます。

石を受け取る操作ではなく渡す操作に注目することで、以下のように言い換えても問題の答えは変わらないことがわかります。

> 人 $i$ は $A_i$ 個の石を持っており、$i$ 年後に成人する。
>
> 人 $i$ は成人したときに人 $i+1,i+2, \dots,N$ の順に（石を持っていれば）石を $1$ 個渡す。
>
> 最終的に各宇宙人が持っている石の個数はいくつか？

以下では言い換え後の問題を考えます。

長さ $N$ の数列 $C$ と長さ $N+1$ の数列 $D$ を用意し、各要素を $0$ で初期化します。$C_i$ が人 $i$ が受け取る石の数の合計になるように計算をすることを目指します。

人 $i$ が成人後に石を渡す人を人 $i+1,i+2,\dots ,R_i$ とします。ここで、$j=i+1,i+2, \dots ,R_i$ に対して $C_j$ に $1$ を加算したいですが、これを愚直に行ってしまうと全体で時間計算量は $O(N^2)$ になってしまいます。そこで、以下のように imos 法の要領による高速化を行います。$D$ が $C$ の差分を取った数列の役割を果たします。

* $i = 1,2, \dots, N$ の順に以下の操作を行う。
  * （$i > 1$ のとき） $C_i$ に $C_{i−1} + D_i$ の値を代入する。これにより人 $i$ が成人したときに持っている石の個数がわかり、$R_i$ の値が定まる。
  * $D_{i+1}$ に $1$、$D_{R_i}+1$ に $−1$ を加算する。

これらの操作は全体として $O(N)$ 時間で行えます。

実装例 (0-indexed)

---

We refer to the $i$-th alien simply as "person $i$."

By focusing on the operation of passing stones, rather than receiving them, we can rephrase the problem in the following way without changing the answer:

> Person $i$ has $A_i$ stones and will become an adult in $i$ years.
>
> When person $i$ becomes an adult, they will pass one stone to each person from $i+1$ to $N$ (if they have any stones left).
>
> What is the final number of stones each person will have?

In the following, we will consider the rephrased version of the problem.

We prepare two sequences: an array $C$ of length $N$ and an array $D$ of length $N+1$, both initialized to 0. Our goal is to calculate the total number of stones received by person $i$ as stored in $C_i$.

After person $i$ becomes an adult, the people who will receive stones from them are persons $i+1, i+2, \dots, R_i$. For each $j = i+1, i+2, \dots, R_i$, we want to increment $C_j$ by 1. However, directly performing this operation would result in a time complexity of $O(N^2)$. Therefore, we optimize this using the "Imos method," where $D$ represents the difference array of $C$.

### Steps:
* For $i = 1, 2, \dots, N$, perform the following operations:
  * (When $i > 1$) Set $C_i$ to $C_{i-1} + D_i$. This will give the number of stones person $i$ has when they become an adult and determine the value of $R_i$.
  * Add $1$ to $D_{i+1}$ and subtract $1$ from $D_{R_i+1}$.

These operations can be performed in $O(N)$ time overall.

Example implementation (0-indexed):

---

```cpp
#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> a(n);
	rep(i, n) cin >> a[i];
	vector<int> c(n), d(n + 1);
	rep(i, n) {
		if (i != 0) {
			c[i] = c[i - 1] + d[i];
			a[i] += c[i];
		}
		int cnt = min(n - i - 1, a[i]);
		a[i] -= cnt;
		d[i + 1]++;
		d[min(n, i + cnt + 1)]--;
	}
	rep(i, n) cout << a[i] << " \n"[i == n - 1];
}
```
