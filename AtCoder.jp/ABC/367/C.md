## [C - Enumerate Sequences](https://atcoder.jp/contests/abc367/tasks/abc367_c)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese editorial</b></summary><br>

「 $1$ 以上 $5$ 以下の整数からなる長さ $8$ の数列」は $5^8=390625$ 個です。 出力すべき数列の個数はこの数以下なので、出力が大きすぎる心配をする必要はありません。

#### 方針1. 再帰を使って列挙する

* 最初に $1$ つ目の要素を小さい順に固定する
* $1$ つ目の要素を固定した下に再帰を呼び、 $2$ つ目の要素を小さい順に固定する
* $\dots$
* 要素が出そろったら、総和が $K$ の倍数であるかを判定した後出力する

というような再帰を実装するとこの問題に正解できます。

実装例 (C++):

```cpp
#include<bits/stdc++.h>

using namespace std;

int n,k;
int r[8];
int seq[8];

void solve(int lv){
  if(lv==n){
    int s=0;
    for(int i=0;i<n;i++){ s+=seq[i]; }
    if(s%k==0){
      for(int i=0;i<n;i++){
        if(i){cout << " ";}
        cout << seq[i];
      }cout << "\n";
    }
    return;
  }
  for(int i=1;i<=r[lv];i++){
    seq[lv]=i;
    solve(lv+1);
  }
}

int main(){
  cin >> n >> k;
  for(int i=0;i<n;i++){
    cin >> r[i];
  }
  solve(0);
  return 0;
}
```



#### 方針2. 数列に対応する整数をデコードする

「 $K$ の倍数 」という条件を無視すれば、数列として考えられるものは  $P = R_1 \times R_2 \times \cdots \times R_N$ 通りです。
実は、 $0$ から $P−1$ までの整数から以下の通りに数列を復元すれば、その数列は辞書順に並びます。

* 整数 $t$ から復元される数列を $S$ とする。また、変数 $x \gets t$ を用意する。
* $i = N$ から $1$ まで、次を繰り返す。
  * $S_i \gets (x\%R_i)+1$ とする。 ( $p\%q \dots p$ を $q$ で割った余り)
  * その後、 $x$ を $\dfrac{x}{R_i}$ (小数点以下切り捨て) に置き換える。

直感的には、数列は特殊な N 進法表記に対応します。
$R = (6,3,2,5)$ とすると、後ろの要素(下の位)から順に $1$ の位、 $5$ の位、 $5 \times 2$ の位、 $5 \times 2 \times 3$ の位 と並んでいると捉えることができます。ここで、 $A = (1,3,1,2)$ は $0\times 30 + 2 \times 10 + 0 \times 5 + 1$ に対応します (この際、 $1$ から $R_i$ までの各要素を $0$ から $R_i−1$ までに修正する必要があることに注意してください)。

他にも、この方針の亜種として別のデコード方法を採用し最後に全ての数列をソートするという方法もあります。 ( 例えば C++ では、 `vector<vector<int>>` をソートすると中身の `vector<int>` を辞書順に並べることができます)

実装例 (C++):


```cpp
#include<bits/stdc++.h>

using namespace std;

int n,k;
int r[8];
int seq[8];

int main(){
  cin >> n >> k;
  int tot=1;
  for(int i=0;i<n;i++){
    cin >> r[i];
    tot*=r[i];
  }
  for(int t=0;t<tot;t++){
    int x=t;
    int s=0;
    for(int i=n-1;i>=0;i--){
      seq[i]=(x%r[i])+1;
      s+=seq[i];
      x/=r[i];
    }
    if(s%k==0){
      for(int i=0;i<n;i++){
        if(i){cout << " ";}
        cout << seq[i];
      }cout << "\n";
    }
  }
  return 0;
}
```


</details><br>

"A sequence of length 8 consisting of integers from 1 to 5" has $5^8 = 390625$ possible sequences. Since the number of sequences to be output is less than or equal to this number, there is no need to worry about the output being too large.

#### Approach 1: Enumerate Using Recursion

* First, fix the first element in ascending order.
* Call the recursion under the fixed first element and fix the second element in ascending order.
* $\dots$
* Once all elements are fixed, check if the sum is a multiple of $K$, and then output it.

Implementing such a recursive approach can solve this problem.

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include<bits/stdc++.h>

using namespace std;

int n,k;
int r[8];
int seq[8];

void solve(int lv){
  if(lv==n){
    int s=0;
    for(int i=0;i<n;i++){ s+=seq[i]; }
    if(s%k==0){
      for(int i=0;i<n;i++){
        if(i){cout << " ";}
        cout << seq[i];
      }cout << "\n";
    }
    return;
  }
  for(int i=1;i<=r[lv];i++){
    seq[lv]=i;
    solve(lv+1);
  }
}

int main(){
  cin >> n >> k;
  for(int i=0;i<n;i++){
    cin >> r[i];
  }
  solve(0);
  return 0;
}
```

</details><br>

#### Approach 2: Decode the Integer Corresponding to the Sequence

Ignoring the "multiple of $K$" condition, the possible sequences are $P = R_1 \times R_2 \times \cdots \times R_N$. 
In fact, if you restore the sequence from an integer between 0 and $P-1$ as follows, the sequences will be in lexicographical order.

* Let $S$ be the sequence restored from integer $t$. Prepare a variable $x \gets t$.
* Repeat the following from $i = N$ to 1:
  * Set $S_i \gets (x \% R_i) + 1$. ($p \% q$ means the remainder of $p$ divided by $q$)
  * Then replace $x$ with $\left\lfloor \frac{x}{R_i} \right\rfloor$ (integer division).

Intuitively, the sequence corresponds to a special base-$N$ representation.
For example, with $R = (6,3,2,5)$, the elements are aligned from the back (lower digits) as the unit’s place, 5’s place, 5×2’s place, 5×2×3’s place. Here, $A = (1,3,1,2)$ corresponds to $0 \times 30 + 2 \times 10 + 0 \times 5 + 1$ (Note that each element from 1 to $R_i$ needs to be adjusted to 0 to $R_i−1$).

Additionally, as a variant of this approach, you can adopt another decoding method and then sort all the sequences at the end. (For example, in C++, sorting `vector<vector<int>>` will arrange the inner `vector<int>` in lexicographical order.)

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include<bits/stdc++.h>

using namespace std;

int n,k;
int r[8];
int seq[8];

int main(){
  cin >> n >> k;
  int tot=1;
  for(int i=0;i<n;i++){
    cin >> r[i];
    tot*=r[i];
  }
  for(int t=0;t<tot;t++){
    int x=t;
    int s=0;
    for(int i=n-1;i>=0;i--){
      seq[i]=(x%r[i])+1;
      s+=seq[i];
      x/=r[i];
    }
    if(s%k==0){
      for(int i=0;i<n;i++){
        if(i){cout << " ";}
        cout << seq[i];
      }cout << "\n";
    }
  }
  return 0;
}
```

</details><br>
