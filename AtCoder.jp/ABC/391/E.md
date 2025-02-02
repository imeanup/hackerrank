## [E - Hierarchical Majority Vote](https://atcoder.jp/contests/abc391/tasks/abc391_e)

> sotanishy

この問題は **動的計画法 (DP)** により解くことができます．

$A$ に対して $k$ 回操作を繰り返した列を $A^{(k)} = (A_1^{(k)}, \dots , A_{3N−k}^{(k)})$ とします．$A(k)$ は問題文の操作を愚直に実行することで求めることができます． $A_i^{(k)}(i = 1, \dots , 3^{N−k})$ の値を反転させるために $A$ で変更する必要のある要素の個数の最小値を $f(k,i)$ とします．$f(N,1)$ が求める答えです．

まず，$k = 0$ については明らかに $f(0,i) = 1 (i = 1, \dots, 3^N)$ です．

$k \ge 1$ のときを考えます．$Ai(k)$ は $A_{3i−2}^{(k−1)},A_{3i−1}^{(k−1)},A_{3i}^{(k−1)}$ の過半数を占める値です．$A_{3i−2}^{(k−1)},A_{3i−1}^{(k−1)},A_{3i}^{(k−1)}$ の中に $Ai(k)$ と同じ値のものは $2$ 個か $3$ 個あります．この個数に関して場合分けをします．

* 同じ値のものが $3$ 個あるとき： $A_i^{(k)}$ の値を反転させるためには， $A_{3i−2}^{(k−1)}, A_{3i−1}^{(k−1)}, A_{3i}^{(k−1)}$ のうち $2$ つを反転させる必要があります．よって，$f(k,i)$ は $f(k−1, 3i−2), f(k−1, 3i−1), f(k−1, 3i)$ で小さい方から $2$ つの和です．

* 同じ値のものが $2$ 個あるとき：一般性を失わず $A_i^{(k)} = A_{3i−2}^{(k−1)} = A_{3i−1}^{(k−1)}$ とします．このとき，$A_{3i}^{(k−1)}$ を反転させる必要はなく，$A^{(k-1)}_{3i−2}, A_{3i−1}^{(k−1)}$ の一方を反転させればよいです．$f(k−1, 3i−2), f(k−1, 3i−1)$ の小さい方を反転させればよいので，$f(k,i) = \min⁡\{f(k−1, 3i−2), f(k−1,3i−1)\}$ です．

以上より，$k$ が小さい方から順番に求めていくことで，すべての $f(k,i)$ を求めることができます．時間計算量は $O(3^N)$ です．

実装は，再帰関数を用いるのが簡便です．

[実装例 (Python)](https://atcoder.jp/contests/abc391/submissions/62238726)

---

This problem can be solved using **Dynamic Programming (DP)**.  

Let $A^{(k)} = (A_1^{(k)}, \dots , A_{3N−k}^{(k)})$ be the sequence obtained by applying the given operation $k$ times to $A$. The sequence $A^{(k)}$ can be computed straightforwardly by following the operations described in the problem statement.  

Define $f(k, i)$ as the minimum number of elements in $A$ that need to be changed to flip the value of $A_i^{(k)}$. The final answer is $f(N,1)$.  

### Base Case:  
For $k = 0$, it is clear that:  
$$
f(0, i) = 1 \quad (i = 1, \dots, 3^N)
$$  

### Recursive Case ($k \geq 1$):  
Each element $A_i^{(k)}$ is determined by the **majority value** among $A_{3i−2}^{(k−1)}, A_{3i−1}^{(k−1)}, A_{3i}^{(k−1)}$.  
Within these three values, there are either **two or three** occurrences of the same value as $A_i^{(k)}$. We consider two cases:

1. **If all three values are the same**:  
   - To flip $A_i^{(k)}$, at least two of $A_{3i−2}^{(k−1)}, A_{3i−1}^{(k−1)}, A_{3i}^{(k−1)}$ must be flipped.  
   - Thus, $f(k, i)$ is the sum of the two smallest values among $f(k−1, 3i−2), f(k−1, 3i−1), f(k−1, 3i)$.

2. **If two values match $A_i^{(k)}$ and one is different**:  
   - Without loss of generality, assume $A_i^{(k)} = A_{3i−2}^{(k−1)} = A_{3i−1}^{(k−1)}$.  
   - In this case, flipping $A_{3i}^{(k−1)}$ is unnecessary. We only need to flip one of $A_{3i−2}^{(k−1)}$ or $A_{3i−1}^{(k−1)}$.  
   - Thus, $f(k, i) = \min \{ f(k−1, 3i−2), f(k−1, 3i−1) \}$.

By computing $f(k, i)$ iteratively from smaller values of $k$, we can determine all values of $f(k, i)$. The time complexity is **$O(3^N)$**.  

### Implementation:  
It is convenient to use a **recursive function** for implementation.  

[Example Implementation (Python)](https://atcoder.jp/contests/abc391/submissions/62238726)

---

> kyopro_friends

$SP[n][L][x] = A_L A_{L+1} \dots A_{L+3^n}$ に対して操作をした結果を $x$ にするために必要な変更箇所の最小値

とすると、

$$
DP[n][L][x] = \begin{cases}
0 & n = 0 かつ x = A_L \\

1 & n = 0 かつ x \ne A_L\\ 

DP[n-1][L][x], DP[n-1][L+3^{n-1}][x], DP[n-1][L+2\times 3^{n-1}][x] & のうち小さい2つの和 otherwise
\end{cases}
$$

となり、メモ化再帰などにより解くことができます。

```py
N=int(input())
S=input()

def dfs(n,l):
  if n==0:
    return (0,1) if S[l]=="0" else (1,0)
  zero,one=zip(*[dfs(n-1,l+k*3**(n-1)) for k in range(3)])
  return (sum(zero)-max(zero),sum(one)-max(one))

print(max(dfs(N,0)))

```

なお、各 $n,L$ について、$DP[n][L][0],DP[n][L][1]$ は一方が 0 で他方が非0 になります。このため、DP[n][L] の表し方として、ここで述べた (0にする最小値, 1にする最小値) 以外にも、(値が0なのは0と1のどちらか, 他方の値) という持ち方も考えられ、[公式解説](https://atcoder.jp/contests/abc391/editorial/12103) はこちらによるものです。


---

### Translation:

Define $SP[n][L][x]$ as the minimum number of changes needed to transform the result of applying the operation to the sequence $A_L A_{L+1} \dots A_{L+3^n}$ into $x$.  

Then, the recursive formula for $DP[n][L][x]$ is:

$$
DP[n][L][x] =
\begin{cases}
0 & if n = 0 and x = A_L \\  
1 & if n = 0 and x \neq A_L \\  
\text{The sum of the two smallest values among} DP[n-1][L][x], DP[n-1][L+3^{n-1}][x], DP[n-1][L+2\times 3^{n-1}][x] & \text{otherwise  }
\end{cases}
$$

This can be solved using **memoized recursion**.

---

### Python Implementation:

```py
N = int(input())
S = input()

def dfs(n, l):
    if n == 0:
        return (0, 1) if S[l] == "0" else (1, 0)
    zero, one = zip(*[dfs(n - 1, l + k * 3**(n - 1)) for k in range(3)])
    return (sum(zero) - max(zero), sum(one) - max(one))

print(max(dfs(N, 0)))
```

---

For each $n, L$, one of $DP[n][L][0]$ or $DP[n][L][1]$ is always 0, while the other is nonzero.  
Thus, an alternative way to represent $DP[n][L]$ is **(which value is 0, and the minimum number of changes for the other value)** instead of explicitly storing both values.  

The **[official editorial](https://atcoder.jp/contests/abc391/editorial/12103)** follows this alternative representation.
