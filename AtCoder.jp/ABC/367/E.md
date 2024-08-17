## [E - Permute K times](https://atcoder.jp/contests/abc367/tasks/abc367_e) 

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese editorial</b></summary><br>

この問題は、 **ダブリング** と呼ばれるテクニックで解くことができます。

ダブリングに関する参考資料をいくつか挙げます。

* [ダブリングの基本概念とその応用](https://algo-logic.info/doubling/)
* [[競プロ用]ダブリングまとめ](https://qiita.com/Kept1994/items/ea91c057b0e552323da3)
* [【競技プログラミング】ダブリングまとめ](https://zenn.dev/fjnkt98/articles/3c0c21778b6101)

まず、 $k = 0, 1, \dots, 59$ について、以下のような配列 $P_k$ を求めることを考えます。

* $P_k,i:=$ ( $2^k$ 回操作をしたとき、操作後の数列の $i$ 番目には操作前の $P_{k,i}$ 番目の要素が入っている)

まず、 $P_0=X$ とできます。
さらに、 $P_{k−1}$ から $P_k$ を以下のように求めることができます。

* $P_{k,i} = P_{k−1}[P_{k−1,i}]$

直感的には、「 $2^{k−1}$ 回の操作」に相当する操作を $2$ 回かければ 「 $2^k$ 回の操作」に相当する操作が得られます。

より一般には、操作 $l$ 回に相当する列 $L$ と操作 $r$ 回に相当する列 $R$ について、 $T_i=R[L_i]$ とすれば操作 $l+r$ 回に相当する列 $T$ が得られます。これを「操作の合成」と呼ぶことにします。

これらの列 $P_i$ から「 $K$ 回操作をしたとき、操作後の数列の $i$ 番目には操作前の $Q_i$ 番目の要素が入っている」という数列 $Q$ を求めることができればこの問題を解くことができます。どのようにすればよいでしょうか。

これは、繰り返し二乗法に似た要領で実現可能です。具体的には、以下の通りに求められます。

* $Q = (1,2, \dots ,N)$ とする (操作 $0$ 回に相当します)。
* $i=0,1, \dots ,59$ まで次を繰り返す。
  * もし $K$ を $2$ で割った余りが $1$ なら $Q$ と $P_i$ とを合成する。
  * その後、 $K$ を $2$ で割る(小数点以下切り捨て)。

</details><br>

This problem can be solved using a technique called **doubling**.

Here are some references for doubling:

* [Basic concepts of doubling and its applications](https://algo-logic.info/doubling/)
* [[For Competitive Programming] Summary of Doubling](https://qiita.com/Kept1994/items/ea91c057b0e552323da3)
* [Summary of Doubling for Competitive Programming](https://zenn.dev/fjnkt98/articles/3c0c21778b6101)

First, let's consider calculating an array $P_k$ for $k = 0, 1, \dots, 59$ as follows:

* $P_{k,i} :=$ (after performing the operation $2^k$ times, the element at position $i$ in the sequence will be the element that was originally at position $P_{k,i}$).

Initially, you can set $P_0 = X$.

Furthermore, $P_k$ can be derived from $P_{k-1}$ as follows:

* $P_{k,i} = P_{k-1}[P_{k-1,i}]$

Intuitively, if you apply the operation corresponding to $2^{k-1}$ twice, you obtain the operation corresponding to $2^k$.

More generally, for a sequence $L$ corresponding to $l$ operations and a sequence $R$ corresponding to $r$ operations, if you define $T_i = R[L_i]$, then the sequence $T$ corresponds to $l + r$ operations. Let's call this "operation composition."

If we can find the sequence $Q$ from these sequences $P_i$ such that after $K$ operations, the element at position $i$ in the sequence will be the element that was originally at position $Q_i$, then we can solve this problem. How can we achieve this?

This can be implemented similarly to the method of repeated squaring. Specifically, it can be done as follows:

* Initialize $Q = (1, 2, \dots, N)$ (this corresponds to 0 operations).
* Repeat the following for $i = 0, 1, \dots, 59$:
  * If the remainder of $K$ divided by 2 is 1, compose $Q$ with $P_i$.
  * Then, divide $K$ by 2 (discarding the fractional part).

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include<bits/stdc++.h>

using namespace std;

int main(){
  int n;
  long long k;
  cin >> n >> k;
  vector<vector<int>> p(60,vector<int>(n+1));
  for(int i=1;i<=n;i++){
    cin >> p[0][i];
  }
  vector<int> a(n+1);
  for(int i=1;i<=n;i++){
    cin >> a[i];
  }
  for(int lv=1;lv<60;lv++){
    for(int i=1;i<=n;i++){
      p[lv][i]=p[lv-1][p[lv-1][i]];
    }
  }
  vector<int> q(n+1);
  for(int i=1;i<=n;i++){q[i]=i;}
  for(int lv=0;lv<60;lv++){
    if(k%2){
      for(int i=1;i<=n;i++){
        q[i]=p[lv][q[i]];
      }
    }
    k/=2;
  }
  for(int i=1;i<=n;i++){
    if(i>=2){cout << " ";}
    cout << a[q[i]];
  }cout << "\n";
  return 0;
}
```

</details><br>
