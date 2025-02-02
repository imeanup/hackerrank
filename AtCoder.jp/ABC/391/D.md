## [D - Gravity](https://atcoder.jp/contests/abc391/tasks/abc391_d)

> sotanishy

時刻 $T$ にブロック $A$ が存在するかどうか判定することを考えます．ブロック $A$ が $X_A$ 列目にあるブロックの中ではじめ下から $c_A$ 番目にあるとします．すると，ブロック $A$ が消える時刻は，一番下の行のブロックが $c_A$ 回目に消滅する時刻になります．よって，一番下の行のブロックが消滅する時刻 $d_1 < d_2 < \dots $ を列挙することができれば，$T$ と $d_{c_A}$ の大小関係を見ることで，質問に答えることができます（ブロックの消滅が $c_A$ 回以上起こらないときは，$d_{c_A}=\infty$ とします）．

ブロックが消滅する時刻 $d_1 < d_2 < \dots$ を求めます．$d_c$ は，各列で下から $c$ 番目のブロックが一番下の行に到達する時刻の最大値 $+1$ です．$c$ 個以上ブロックが存在しない列が $1$ つでもあれば $d_c = \infty$ です．

$d_1$ は，単に各列で一番下にあるブロックが一番下の行に到達する時刻の最大値 $+1$ を求めれば良いです．$x$ 列目で下から $c$ 番目のブロックがはじめマス $(x,y_{x,c})$ にあるとすると，$d_1 = \max \{y_{1,1}, \dots, y_{W,1} \}$ となります．

次に，$d_c(c \ge 2)$ を求めます．$x$ 列目で下から $c$ 番目にあるブロックが一番下の行に到達する時刻を考えます．もしそのブロックが，それより下にあるブロックに一度も遮られることなく一番下の行に到達するならば，そのブロックは時刻 $y_{x,c}−1$ に一番下の行に到達します．もし途中で下にあるブロックに遮られたとすると，それ以降は $c−1$ 番目のブロックが $1$ マス落ちるたびに $c$ 番目のブロックも一緒に $1$ マス落ちていき，$c−1$ 番目のブロックが消滅する時刻 $d_c − 1$ に $c$ 番目のブロックが一番下の行に到達します．よって，$d_c = \max \{y_{1,c}, \dots,y_{W,c}, d_{c−1} + 1\}$ となります．

以上より，次のようなアルゴリズムで $d$ を求めることができます．

* $d_1, d_2, \dots, d_{N+1}$ を $0$ で初期化する．
* $x = 1, \dots, W$ について以下を行う．
  * $x$ 列目にあるブロックの $y$ 座標をソートして，$y_{x,1} < y_{x,2} < \dots , y_{x,C}$ とする．
  * 各 $c = 1,\dots, C$ について，$d_c \gets \max \{d_c, y_x, c\}$ と更新する．
  * $d_{C+1} \gets \infty $ と更新する．
* $c = 2, \dots, N+1$ について，$d_c \gets \max \{d_c,d_{c−1} + 1\}$ と更新する．

このアルゴリズムの時間計算量は，ソートがボトルネックとなり $O(N \log ⁡N)$ です．$d$ が求まれば，各質問には $O(1)$ で答えることができるので，全体の時間計算量は $O(N \log ⁡N + Q)$ です．

[実装例 (Python)](https://atcoder.jp/contests/abc391/submissions/62237381)

---

We consider the problem of determining whether block $A$ exists at time $T$. Suppose that block $A$ is initially the $c_A$-th block from the bottom in column $X_A$. The time at which block $A$ disappears is the time when the bottom-most row’s block disappears for the $c_A$-th time.  

Thus, if we can list the disappearance times of the bottom-most row’s blocks as $d_1 < d_2 < \dots$, we can determine the answer by comparing $T$ with $d_{c_A}$. (If fewer than $c_A$ disappearances occur, we define $d_{c_A} = \infty$.)  

### Computing the disappearance times $d_1 < d_2 < \dots$:

Each $d_c$ represents the maximum time at which the $c$-th block from the bottom in any column reaches the bottom-most row, plus one. If there is even a single column with fewer than $c$ blocks, then $d_c = \infty$.  

For $d_1$, we simply find the maximum time at which the bottom-most block in each column reaches the bottom-most row, plus one. If the $c$-th block from the bottom in column $x$ is initially located at $(x, y_{x,c})$, then:  

$$
d_1 = \max \{ y_{1,1}, \dots, y_{W,1} \} + 1
$$

### Computing $d_c$ for $c \geq 2$:

Consider the time at which the $c$-th block from the bottom in column $x$ reaches the bottom-most row:

- If it reaches the bottom row without being blocked, it arrives at time $y_{x,c} - 1$.  
- If it is blocked by the block below it, it will descend along with the $(c-1)$-th block. In this case, it reaches the bottom row at time $d_{c-1} - 1$, so:  

$$
d_c = \max \{ y_{1,c}, \dots, y_{W,c}, d_{c-1} + 1 \}
$$

### Algorithm:

Using the above observations, we can compute $d$ as follows:

1. Initialize $d_1, d_2, \dots, d_{N+1}$ to 0.  
2. For each column $x = 1, \dots, W$:  
   - Sort the block heights in column $x$ such that $y_{x,1} < y_{x,2} < \dots < y_{x,C}$.  
   - For each $c = 1, \dots, C$, update $d_c$ as:  
     $$
     d_c \gets \max \{ d_c, y_{x,c} \}
     $$
   - Set $d_{C+1} = \infty$.  
3. For $c = 2, \dots, N+1$, update:  
   $$
   d_c \gets \max \{ d_c, d_{c-1} + 1 \}
   $$

### Complexity Analysis:

The bottleneck of this algorithm is sorting, resulting in a time complexity of $O(N \log N)$.  
Once $d$ is computed, each query can be answered in $O(1)$, so the total complexity is $O(N \log N + Q)$.  

[Example Implementation (Python)](https://atcoder.jp/contests/abc391/submissions/62237381)

