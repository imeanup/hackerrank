

## [D - Pedometer](https://atcoder.jp/contests/abc367/tasks/abc367_d)


<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese editorial</b></summary><br>

便宜上、休憩所 $k$ の番号を $k-1$ に取り換えて、 $0$ から $N-1$ までの番号で取り扱います。

以下のような配列を考えてみましょう。

$R_i = $ ( 休憩所 $0$ から出発して、 $i$ 番目の休憩所として休憩所 $i\%N$ に到着するまでにかかる歩数を $M$ で割った余り ) とします。 これを $i$ が $0$ から $2N-1$ まで計算しておきます。
例えば、 $A=(1,2,3,4),M=6$ とすると $R=(0,1,3,0,4,5,1,4)$ となります。

$s$ から $t$ まで歩く ( $s \ne t$ ) のにかかる最小の歩数が $M$ の倍数であるのはどのような場合でしょうか?

* $s < t$ のとき、 $R_s=R_t$ であることが求める条件です。
  * これは、 $R_{N+s} = R_{N+t}$ と同値です。
* $s > t$ のとき、 $R_s = R_{N+t}$ であることが求める条件です。

これらを踏まえて、以下の問題が解ければよいことになります。

> $i = N, N+1, \dots, 2N-1$ について、以下の答えを足し合わせよ。
>
> * $R_{i−N+1},R_{i−N+2}, \dots ,R_{i−1}$ の中に、 $R_i$ と等しい要素は何個ありますか?

直感的には、休憩所 $i\%N$ へと時計回りに歩いた時、歩数が $M$ の倍数となるものを $i = N, N+1, \dots,2N−1$ について足し合わせています。

この問題は、次のようにして解くことができます。

* まず、 $R_0$ から $R_{N−1}$ において $0$ から $M−1$ までの $k$ の出現頻度を 記録した配列を $B = (B[0],B[1], \cdots ,B[M−1])$ とする。
* $i = N, N+1, \dots, 2N−1$ について以下を繰り返す。
  * $B[R_{i-N}]$ から $1$ 減算する。
    * これにより、現在の $B$ は $i−N+1$ から $i−1$ までの頻度を管理する配列となる。
  * 答えに $B[R_i]$ を加算する。
  * $B[R_i]$ に $1$ 加算する。
    * これにより、現在の $B$ は $i−N+1$ から $i$ までの頻度を管理する配列となる。


</details><br>

For convenience, let's replace the index of rest area $k$ with $k-1$, so that we handle the indices from 0 to $N-1$.

Let's consider the following array:

Define $R_i =$ (the remainder when the number of steps required to reach the $i$th rest area $i \% N$ after starting from rest area 0 is divided by $M$). Calculate this for $i$ from 0 to $2N-1$.
For example, if $A = (1, 2, 3, 4)$ and $M = 6$, then $R = (0, 1, 3, 0, 4, 5, 1, 4)$.

Under what conditions is the minimum number of steps required to walk from $s$ to $t$ (where $s \neq t$) a multiple of $M$?

* When $s < t$, the condition is $R_s = R_t$.
  * This is equivalent to $R_{N+s} = R_{N+t}$.
* When $s > t$, the condition is $R_s = R_{N+t}$.

Given this, we can solve the following problem:

> For $i = N, N+1, \dots, 2N-1$, sum the following:
>
> * How many elements in $R_{i-N+1}, R_{i-N+2}, \dots, R_{i-1}$ are equal to $R_i$?

Intuitively, this sums up the number of times the number of steps to walk clockwise to rest area $i \% N$ results in a multiple of $M$ for $i = N, N+1, \dots, 2N-1$.

This problem can be solved as follows:

* First, create an array $B = (B[0], B[1], \dots, B[M-1])$ that records the frequency of each $k$ from 0 to $M-1$ in $R_0$ to $R_{N-1}$.
* For $i = N, N+1, \dots, 2N-1$, repeat the following:
  * Subtract 1 from $B[R_{i-N}]$.
    * This adjusts $B$ to manage the frequency of values from $i-N+1$ to $i-1$.
  * Add $B[R_i]$ to the answer.
  * Add 1 to $B[R_i]$.
    * This adjusts $B$ to manage the frequency of values from $i-N+1$ to $i$.

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include<bits/stdc++.h>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int n,m;
  cin >> n >> m;
  vector<int> a(n);
  for(auto &nx : a){cin >> nx;}
  vector<int> r={0};
  for(int i=0;i<2*n;i++){
    r.push_back((r.back()+a[i%n])%m);
  }
  vector<int> b(m,0);
  for(int i=0;i<n;i++){b[r[i]]++;}
  long long res=0;
  for(int i=n;i<2*n;i++){
    b[r[i-n]]--;
    res+=b[r[i]];
    b[r[i]]++;
  }
  cout << res << "\n";
  return 0;
}
```


</details><br>
