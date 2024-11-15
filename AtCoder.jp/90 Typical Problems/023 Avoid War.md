### [023 - Avoid War](https://atcoder.jp/contests/typical90/tasks/typical90_w)

<details><summary>Japanese</summary><br>

### 問題文

縦 $H$ マス、横 $W$ マスからなるグリッドがあり、上から $i$ 行目・左から $j$ 列目のマスを $(i,j)$ で表します。 各マスには色が塗られており、マス $(i,j)$ の色は $C_{i,j}$ が `#` のとき黒、$C_{i,j}$ が `.` のとき白です。

あなたはいくつかの白マスを選び（$1$ つも選ばなくても良い）、**キング**の駒を置きます。 **キング**同士が互いに攻撃し合わない（後述）ような置き方の数を、$10^9+7$ で割った余りを求めてください。

ただし、ある $2$ つの置き方が異なるとは、 「ある白マスが存在して、片方ではキングが置かれており、もう片方では置かれていない」 ことを言います。

「キング同士が互いに攻撃し合わない」とは

キングが置かれている任意の異なる $2$ マス $(i,j)$ および $(k,l)$ において、 $|i−k|>1$ または $|j−l| > 1$ が成り立つことを言います。


### 制約

* $1\le H, W\le 24$
* $H,W$ は整数
* $C_{i,j}$ は `#` または `.`
* 少なくとも $1$ つの白マスが存在する

### 小課題

1. ($1$ 点) $1 \le H,W \le 4$
2. ($1$ 点) $1 \le H,W \le 9$
3. ($2$ 点) $1 \le H, W \le 17$
4. ($3$ 点) 追加の制約はない。

---

### 入力

入力は以下の形式で標準入力から与えられます。


$H \quad W \\$
$C_{1,1} \ \dots \ C_{1,W} \\$
$\vdots \\$
$C_{H,1} \ \dots \ C_{H,W} \\$



### 出力

条件を満たす置き方の数を、$10^9+7$ で割った余りを出力してください。

---

### 入力例 1

```
1 3
...
```

### 出力例 1

```
5
```

以下の $5$ 通りがあります。( `o` はキングを置いたマスを表します。)

```
...     o..     .o.     ..o     o.o
```

これは小課題 $1,2,3,4$ の制約を満たします。

---

### 入力例 2

```
3 3
.#.
#..
.##
```

### 出力例 2

```
13
```

以下の $13$ 通りがあります。( `o` はキングを置いたマスを表します。)

```
.#.     o#.     .#o     .#.     .#.     .#.     o#o
#..     #..     #..     #o.     #.o     #..     #..
.##     .##     .##     .##     .##     o##     .##

o#.     o#.     .#o     .#.     o#o     o#.
#.o     #..     #..     #.o     #..     #.o
.##     o##     o##     o##     o##     o##
```

これは小課題 $1,2,3,4$ の制約を満たします。

---

### 入力例 3

```
8 9
######.##
####..##.
..#...#..
###...###
#....##.#
.##......
#.####..#
#.#######
```

### 出力例 3

```
273768
```

これは小課題 $2,3,4$ の制約を満たします。

---

### 入力例 4

```
17 17
.####...#.....#.#
.#....#.#####...#
#...##.##...#..##
..#..####..#...##
.#..#..#.#.##...#
.#.#.#...#.##..#.
#...#..#..##..###
###.#..###..###..
...#.##.##.#....#
..####....#.#...#
.##...##.#.#...#.
..########...###.
#..##....#.......
##.##..###.#.##..
.##....#........#
....#####..##.#..
.###...##..##.#..
```

### 出力例 4

```
314465173
```

$10^9+7$ で割った余りを出力してください。

これは小課題 $3,4$ の制約を満たします。

---

### 入力例 5

```
22 18
.##.##.#.#.#...##.
####.#..###.#.#..#
#####.##...##.###.
...#.#.#.##.##.###
..#.##.#.#....#...
#.###.##....###..#
....#####...#...#.
.#..##..#..###....
....#..##.#.#..#.#
###.#.....#..##.#.
#..#..#.#.##..###.
#...#....##..###..
..#...#..###..##..
.#....#.#.#..###.#
##.#.#..#..###..##
....###.##.##.##..
#...####.#.#..##..
..#.###.###.###.##
#...##.#.#.#...#.#
#..###..########..
#.##.#####.#..#.##
#..#........#...#.
```

### 出力例 5

```
47296634
```

これは小課題 $4$ の制約を満たします。

---

### Source Name

[「競プロ典型90問」23日目](https://twitter.com/e869120/status/1385725481920520193)

</details><br>

---


### Problem Statement

There is a grid with height $H$ and width $W$, represented by cells arranged in $H$ rows and $W$ columns. We represent the cell in the $i$-th row from the top and $j$-th column from the left as $(i, j)$. Each cell is painted a color: if the color of cell $(i, j)$, represented by $C_{i,j}$, is `#`, it is black; if $C_{i,j}$ is `.`, it is white.

You may select any number of white cells (including choosing none) and place **King** pieces on them. Calculate the number of ways to place these **King** pieces such that they do not "attack" each other (explained below), and return the result modulo $10^9+7$.

Two different arrangements are considered distinct if there exists a white cell where one arrangement has a King and the other does not.

Two Kings are considered to not attack each other if:

For any two distinct cells $(i, j)$ and $(k, l)$ with Kings, it holds that $|i - k| > 1$ or $|j - l| > 1$.

### Constraints

- $1 \leq H, W \leq 24$
- $H$ and $W$ are integers
- Each $C_{i,j}$ is either `#` or `.`
- There is at least one white cell.

### Subtasks

1. (1 point) $1 \leq H, W \leq 4$
2. (1 point) $1 \leq H, W \leq 9$
3. (2 points) $1 \leq H, W \leq 17$
4. (3 points) No additional constraints.

---

### Input

The input is provided in the following format:

$$
H \quad W \\C_{1,1} \ \dots \ C_{1,W} \\\vdots \\C_{H,1} \ \dots \ C_{H,W} \\
$$

### Output

Print the number of valid ways to arrange the Kings such that they do not attack each other, modulo $10^9+7$.

---

### Example Input 1

```
1 3
...
```

### Example Output 1

```
5
```

There are 5 possible placements (`o` represents a cell with a King):

```
...     o..     .o.     ..o     o.o
```

This satisfies the constraints of Subtasks 1, 2, 3, and 4.

---

### Example Input 2

```
3 3
.#.
#..
.##
```

### Example Output 2

```
13
```

There are 13 possible placements (`o` represents a cell with a King):

```
.#.     o#.     .#o     .#.     .#.     .#.     o#o
#..     #..     #..     #o.     #.o     #..     #..
.##     .##     .##     .##     .##     o##     .##

o#.     o#.     .#o     .#.     o#o     o#.
#.o     #..     #..     #.o     #..     #.o
.##     o##     o##     o##     o##     o##
```

This satisfies the constraints of Subtasks 1, 2, 3, and 4.

---

### Example Input 3

```
8 9
######.##
####..##.
..#...#..
###...###
#....##.#
.##......
#.####..#
#.#######
```

### Example Output 3

```
273768
```

This satisfies the constraints of Subtasks 2, 3, and 4.

---

### Example Input 4

```
17 17
.####...#.....#.#
.#....#.#####...#
#...##.##...#..##
..#..####..#...##
.#..#..#.#.##...#
.#.#.#...#.##..#.
#...#..#..##..###
###.#..###..###..
...#.##.##.#....#
..####....#.#...#
.##...##.#.#...#.
..########...###.
#..##....#.......
##.##..###.#.##..
.##....#........#
....#####..##.#..
.###...##..##.#..
```

### Example Output 4

```
314465173
```

Output the result modulo $10^9+7$.

This satisfies the constraints of Subtasks 3 and 4.

---

### Example Input 5

```
22 18
.##.##.#.#.#...##.
####.#..###.#.#..#
#####.##...##.###.
...#.#.#.##.##.###
..#.##.#.#....#...
#.###.##....###..#
....#####...#...#.
.#..##..#..###....
....#..##.#.#..#.#
###.#.....#..##.#.
#..#..#.#.##..###.
#...#....##..###..
..#...#..###..##..
.#....#.#.#..###.#
##.#.#..#..###..##
....###.##.##.##..
#...####.#.#..##..
..#.###.###.###.##
#...##.#.#.#...#.#
#..###..########..
#.##.#####.#..#.##
#..#........#...#.
```

### Example Output 5

```
47296634
```

This satisfies the constraints of Subtask 4.

---

### Source

[“90 Typical Problems for Competitive Programming” - Day 23](https://twitter.com/e869120/status/1385725481920520193)

---

![](https://pbs.twimg.com/media/EzyN_3jVoAAF3Gz?format=jpg&name=large)

<details><summary>Part 1</summary><br>

キーワード：小さい制約は bit 全探索

小課題1

小課題1の制約はHW≤4と非常に小さいです。こういう場合は、何通りの置き方を探索する必要があるかを考えてみましょう。

左図のようにマス目に番号を振ると、合計 HW 個のマスがあることが分かります。（H.W）=（4,4）でも 16 個です。各マスは「置くか置かないか」の2通りなので、2^{16}＝65536通りです。

そこで、計算回数 10^8～10^9程度であればTLE にならないので、全探索をすることを考えるのですが、どのように複雑な構造を全探索をすれば良いのでしょうか。

1つの手法として、bit 全探索が考えられます。

そこで、i＝0,1.2.....2^{HW-1} の順にfor 文ループを回すことを考えます。
各iでのマス目の状態は、次のように設定します。

① 下からj（0≤j≤HW-1）桁目が0のとき、番号」のマスに駒を置かない。そうでないときを置く。
具体例は次のようになります。左側が i=21＝10101（）右側がi＝1048＝ 10000011000_{(2)} の場合です。

このような方法を使うと全通り調べ上げられます。Valid な置き方かを判定するのに0（HW）かかるので、全体計算量は0（2^{HW}✕HW）です。

このように、bit 全素を使うことで全体計算量0（2HW✕HW）で解くことができました。
しかし、この解法ではH、W≤9の制約の場合、2^{81}x81＝1026回という恐ろしい数の計算を行う必要があります。どのように高速化すれば良いのでしょうか。
【類題】
• ABC190-C [Bowls and Dishes]
• ABC196-D THanjoJ

</details><br>

---

**Part 1:**

**Keyword**: Small constraints are suitable for bit exploration (bit search).

### Subtask 1  
The constraints for Subtask 1 are $HW \leq 4$, which is very small. In such cases, let's consider how many possible arrangements need to be explored.

<style>
  table {
    border-collapse: collapse;
  }
  table, th, td {
    border: 1px solid black;
  }
  td {
    background-color: yellow;
    text-align: center;
    width: 30px;
    height: 30px;
  }
</style>

<table>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
  </tr>
  <tr>
    <td>8</td>
    <td>9</td>
    <td>10</td>
    <td>11</td>
  </tr>
  <tr>
    <td>12</td>
    <td>13</td>
    <td>14</td>
    <td>15</td>
  </tr>
</table>


If we number the grid squares as shown in the left diagram, we see that there are a total of $HW$ squares. For example, when $(H, W) = (4, 4)$, there are 16 squares. Each square has two options: "place" or "not place." Therefore, there are $2^{16} = 65,536$ possible arrangements.

With a calculation count of around $10^8$ to $10^9$, it will not result in a TLE (Time Limit Exceeded). Therefore, we can consider performing a brute-force search. But how should we perform a brute-force search on a complex structure?

One possible approach is **bit exploration** (bit search).

Here, we consider using a `for` loop to iterate through $i = 0, 1, 2, \ldots, 2^{HW-1}$. The state of each cell for each $i$ is set as follows:

1. If the $j$-th (where $0 \leq j \leq HW-1$) bit from the bottom is 0, do not place a piece in the cell with that number. Otherwise, place a piece.

Here are some concrete examples:

- When $i = 21 = 10101_{(2)}$, the left diagram shows the placement.
- When $i = 1048 = 10000011000_{(2)}$, the right diagram shows the placement.

<style>
  table {
    border-collapse: collapse;
    margin: 10px;
  }
  table, th, td {
    border: 1px solid black;
  }
  td.red {
    background-color: red;
    text-align: center;
    width: 30px;
    height: 30px;
  }
  td.gray {
    background-color: gray;
    text-align: center;
    width: 30px;
    height: 30px;
  }
  td.yellow {
    background-color: yellow;
    text-align: center;
    width: 30px;
    height: 30px;
  }
  td.green {
    background-color: green;
    text-align: center;
    width: 30px;
    height: 30px;
  }
  td.white {
    background-color: white;
    text-align: center;
    width: 30px;
    height: 30px;
  }
  .container {
    display: flex;
    justify-content: space-around;
  }
</style>

<div class="container">
  <div>
    <strong>Matrix 1:</strong>
    <table>
      <tr>
        <td class="red">0</td>
        <td class="gray">1</td>
        <td class="red">2</td>
        <td class="gray">3</td>
      </tr>
      <tr>
        <td class="red">4</td>
        <td class="gray">5</td>
        <td class="gray">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="gray">8</td>
        <td class="gray">9</td>
        <td class="gray">10</td>
        <td class="gray">11</td>
      </tr>
      <tr>
        <td class="gray">12</td>
        <td class="gray">13</td>
        <td class="gray">14</td>
        <td class="gray">15</td>
      </tr>
    </table>
  </div>
  <div>
    <strong>Matrix 2:</strong>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="red">3</td>
      </tr>
      <tr>
        <td class="red">4</td>
        <td class="gray">5</td>
        <td class="gray">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="gray">8</td>
        <td class="gray">9</td>
        <td class="red">10</td>
        <td class="gray">11</td>
      </tr>
      <tr>
        <td class="gray">12</td>
        <td class="gray">13</td>
        <td class="gray">14</td>
        <td class="gray">15</td>
      </tr>
    </table>
  </div>
</div>



Using this method allows us to examine all possible arrangements. Checking whether a placement is valid takes $O(\text{HW})$, so the total computational complexity is $O(2^{\text{HW}} \times \text{HW})$.

In this way, by using bit exploration, we were able to solve it with a total computational complexity of $O(2^{HW} \times \text{HW})$. However, with constraints where $H, W \leq 9$, this method would require an enormous number of calculations: $2^{81} \times 81 = 10^{26}$. How can we optimize it to be faster?

**Related Problems**  
- [ABC190-C Bowls and Dishes](https://atcoder.jp/contests/abc190/tasks/abc190_c)
- [ABC196-D Hanjo](https://atcoder.jp/contests/abc196/tasks/abc196_d)

---

![](https://pbs.twimg.com/media/EzyOAtvVgAM2dWD?format=jpg&name=large)

<details><summary>Part 2</summary><br>

キーワード：ビットDP で高速化

小課題 2
盤面の状態を一行ごとに決めていくことを考えます。そこで、次のような性質があります。

①ある行の置き方が実現できるかは、直前 1 行で全部決まる実際、

下図のように、2 行前以前がどのようになっていても、1 行前の盤面だけで「そのような置き方ができるか」が決まるのです。

そこで、次のような「1 行前の状態を記録した DP」を考えます。

dp[今何行目][1 行前の状態] ＝ 通り数

DP 配列のサイズは $H\times 2^W$、移は行の置き方を全部調べれば良いので $2^W$ 通りです。したがって、全体計算量 $O(H\times 4^W)$ となり現実的です.

![alt text](image.png)

DP の週のイメー

なお、DP で扱う配列において、1 行前の状態は 2 進数を用いて記録す ると実装しやすいです。このような手法をビットDP といいます。具体例は次の通りです。

![alt text](image-1.png)
$2^1 = 2$ より 2として記録する

![alt text](image-2.png)
$2^1 + 2^2 + 2^3 = 14$ より 14 として記録する

![alt text](image-3.png)
何も置かれてないので 0として記録する

このように、ビットDPを使うことで全体計算量 $O(4^W\times H)$ で解くことができました。

しかし、この解法では $H,W \le 17$ の制約の場合、$4^{17} \times 17 = 10^{11}$ 回という恐ろしい数の計算を行う必要があります。

どのように高速化すれば良いのでしょうか。

【類題】
• s8pc #1 G Revenge of Traveling Salesman Problem
・JOl 2017予選4「ぬいぐるみの整理」

---

</details><br>

**Keyword:** Speeding Up with Bit DP

#### Subtask 2
Let’s think about determining the state of the board row by row. Here, the following property holds:

1. Whether a certain arrangement of a row is possible depends entirely on the arrangement of the **previous row**. In practice, as shown in the figure below, no matter how the board looked two or more rows before, it is determined solely by the arrangement of the **immediately preceding row** whether the arrangement of the current row is valid.

Thus, we consider a "DP that records the state of the previous row" as follows:

$$
dp[\text{current row number}][\text{state of the previous row}] = \text{number of ways}
$$

The size of the DP array is $H \times 2^W$, and there are $2^W$ possible ways to examine the placement for a single row. Therefore, the total computational complexity becomes $O(H \times 4^W)$, which is practical.

![Illustration of DP array](image.png)

#### Weekly Concept of DP

Additionally, in the DP array, it is easier to implement the state of the previous row by recording it in binary. This method is called **Bit DP**. A concrete example is as follows:

![Example 1](image-1.png)
If $2^1 = 2$, it is recorded as **2**.

![Example 2](image-2.png)
If $2^1 + 2^2 + 2^3 = 14$, it is recorded as **14**.

![Example 3](image-3.png)
If nothing is placed, it is recorded as **0**.

In this way, by using Bit DP, the problem can be solved with a total computational complexity of $O(4^W \times H)$.

However, with constraints such as $H, W \leq 17$, this method would require a terrifying $4^{17} \times 17 = 10^{11}$ calculations.

How can we speed this up?

#### Related Problems:
- **s8pc #1 G**: *Revenge of Traveling Salesman Problem*
- **JOI 2017 Preliminary #4**: *Organizing Stuffed Animals*

---

![](https://pbs.twimg.com/media/EzyOBqmVEAAGxOp?format=jpg&name=large)

<details><summary>Part 3</summary><br>

キーワード：DPの遷移を細かくする

小課題ろ

盤面の状態を1行に決めていく場合、計算量が大きくなってしまいます。そこで、左上のマスから順に、1マス毎に決めることを考えます。

あるマスに駒を置くか決めるとき、「置けるかどうか」に関係するマスは下図の通りです。左上から順に番号を振ったとき、該当するマスに駒を置けるかは直前の W＋1マスのみに依存することが分かります。

<div class="container">
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="red">3</td>
      </tr>
      <tr>
        <td class="green">4</td>
        <td class="green">5</td>
        <td class="green">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="green">8</td>
        <td class="yellow">9</td>
        <td class="gray"> </td>
        <td class="gray"> </td>
      </tr>
      <tr>
        <td class="gray"> </td>
        <td class="gray"> </td>
        <td class="gray"> </td>
        <td class="gray"> </td>
      </tr>
    </table>
    <div>
    9 マス目に置くか決める場合
    </div>
  </div>
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="gray">3</td>
      </tr>
      <tr>
        <td class="gray">4</td>
        <td class="gray">5</td>
        <td class="gray">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="gray">8</td>
        <td class="green">9</td>
        <td class="green">10</td>
        <td class="green">11</td>
      </tr>
      <tr>
        <td class="gray">12</td>
        <td class="green">13</td>
        <td class="yellow">14</td>
        <td class="gray"> </td>
      </tr>
    </table>
    <div>
    14 マス目に置くか決める場合
    </div>
  </div>
</div>

そこで、次のような DP を考えます。

dp[次見るマスの番号][直前 $W＋1$ マスの状態] ＝ 通り数

直前 $W＋1$ マスの状態は、2進数を用いたビットDPで記録すると実 1 装がしやすいです。具体例は次の通りです。（赤マスが駒を置いたマス)

次見るマスの番号は $10$、直前 $W＋1$ マスの状態は $5$ マス目から順に$（0,0,1,0,1）［0 - indexed$ で 2 個目と 4 個目が 1］である。$2^2＋2^4 = 20$ だから、この状態は $dp[10][20]$ として記録される。
$$
dp[pos][mask] = 
\begin{cases} 
dp[pos+1]\left[\left\lfloor\dfrac{mask}{2}\right\rfloor \right] & (前を置かない) \\ 
dp[pos+1]\left[\left\lfloor\dfrac{mask}{2} + 2^W \right\rfloor \right] & (（駒左造＜)
\end{cases}
$$

状態数 O(2^W \times HW)$ 移 $O(1)$ より、計算量は $O(2^W \times HW)$ です.

このように、DP の遷移を「1 行ごと」から「1 マスごと」まで細かくすることで、全体計算量 $O(2^W\times HW)$ で解くことができました。

しかし、この解法では $H,W \le 24$ の制約の場合、TLE どころか MLE してしまいます。さらに高速化する方法はあるのでしょうか。

【類題】
• Yukicoder #611 Day of the Mountain]
・ 蟻本p.177「ドミノ敷き詰め」


---

</details><br>

**Keyword:** Refining DP Transitions

#### Subtask 3

When deciding the state of the board one row at a time, the computational complexity becomes quite large. Therefore, let us consider determining the state one cell at a time, starting from the top-left cell.

When deciding whether to place a piece on a particular cell, the cells that affect "whether it can be placed" are as shown in the diagram below. By numbering the cells sequentially from the top left, it becomes clear that whether a piece can be placed on a particular cell depends only on the **W + 1** cells immediately preceding it.

<div class="container">
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="red">3</td>
      </tr>
      <tr>
        <td class="green">4</td>
        <td class="green">5</td>
        <td class="green">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="green">8</td>
        <td class="yellow">9</td>
        <td class="gray"> </td>
        <td class="gray"> </td>
      </tr>
      <tr>
        <td class="gray"> </td>
        <td class="gray"> </td>
        <td class="gray"> </td>
        <td class="gray"> </td>
      </tr>
    </table>
    <div>
    When deciding whether to place a piece on cell <b>9</b>.
    </div>
  </div>
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="gray">3</td>
      </tr>
      <tr>
        <td class="gray">4</td>
        <td class="gray">5</td>
        <td class="gray">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="gray">8</td>
        <td class="green">9</td>
        <td class="green">10</td>
        <td class="green">11</td>
      </tr>
      <tr>
        <td class="gray">12</td>
        <td class="green">13</td>
        <td class="yellow">14</td>
        <td class="gray"> </td>
      </tr>
    </table>
    <div>
    When deciding whether to place a piece on cell <b>14</b>.
    </div>
  </div>
</div>

Thus, we define the DP as follows:

$$
dp[\text{next cell number}][\text{state of the previous } W + 1 \text{ cells}] = \text{number of ways}
$$

The state of the previous **W + 1** cells is recorded using **Bit DP**, which makes implementation easier. A concrete example is as follows (the red cells indicate cells where a piece is placed):

- The next cell number is **10**, and the state of the previous **W + 1** cells, from cell **5** onward, is $(0, 0, 1, 0, 1)$ (0-indexed). Since the 2nd and 4th cells are **1**, this state is represented as:
  $$
  2^2 + 2^4 = 20
  $$
  Thus, this state is recorded as $dp[10][20]$.

The DP transitions are expressed as:

$$
dp[\text{pos}][\text{mask}] = 
\begin{cases} 
dp[\text{pos} + 1]\left[\left\lfloor \frac{\text{mask}}{2} \right\rfloor \right] & (\text{if no piece is placed}) \\ 
dp[\text{pos} + 1]\left[\left\lfloor \frac{\text{mask}}{2} + 2^W \right\rfloor \right] & (\text{if a piece is placed})
\end{cases}
$$

Since there are $O(2^W \times H \times W)$ states and each transition takes $O(1)$, the computational complexity is $O(2^W \times H \times W)$.

By refining the DP transitions from "one row at a time" to "one cell at a time," we were able to solve the problem with a total complexity of $O(2^W \times H \times W)$.

However, with constraints such as $H, W \leq 24$, this solution might not just run into **TLE (Time Limit Exceeded)** but also **MLE (Memory Limit Exceeded)**. Is there a way to make it even faster?

#### Related Problems:
- **Yukicoder #611**: *Day of the Mountain*
- *Page 177 of the Ant Book*: *Tiling with Dominoes*

---

![](https://pbs.twimg.com/media/EzyOClUUUAA3m9b?format=jpg&name=large)

<details><summary>Part 4</summary><br>

キーワード：不要な状態を削る

小課題 4

小課題3ではたくさんの不要な状態があります。例えば次のような状 態はあり得るのでしょうか。（赤マスが駒を置いたマス）

<div class="container">
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="gray">3</td>
      </tr>
      <tr>
        <td class="red">4</td>
        <td class="gray">5</td>
        <td class="red">6</td>
        <td class="red">7</td>
      </tr>
      <tr>
        <td class="white"></td>
        <td class="white"></td>
        <td class="white"> </td>
        <td class="white"> </td>
      </tr>
      <tr>
        <td class="white"> </td>
        <td class="white"> </td>
        <td class="white"> </td>
        <td class="white"> </td>
      </tr>
    </table>
    <div>
    dp[8][26] の場合の状態
    </div>
  </div>
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="gray">3</td>
      </tr>
      <tr>
        <td class="gray">4</td>
        <td class="gray">5</td>
        <td class="gray">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="gray">8</td>
        <td class="gray">9</td>
        <td class="red">10</td>
        <td class="red">11</td>
      </tr>
      <tr>
        <td class="red">12</td>
        <td class="gray">13</td>
        <td class="red">14</td>
        <td class="white"> </td>
      </tr>
    </table>
    <div>
    dp[15][23] の場合の状態
    </div>
  </div>
</div>

このような状態はvalidではなく、通りであることが分かります。 基本的に、2つの隣接マスに連続して駒を置く場合はあり得ません。

実際、「あり得る状態」の数はどの程度なのでしょうか。

結論から書くと、フィボナッチ数の第 $N$ 項を $fib(N)$ とするとき、「あり得る状態数」は $fib(W) ＝ O(1.62^W)$ 通り程度しかないのです.

なぜなら、長さ $W$ の $01$ 文字列の中で、$1$ が $2$ つ連続しないものの個数 は $fib(W)$ 個だからです。つまり、例えば $W ＝ 24$ の場合 $99\%$ 以上の 状態が不要だったことになります。

$$
\begin{array}{ccc}
2^W \text{ 通り} & \overset{\text{99\% カット！}}{\Longrightarrow} & \text{fib}(W) \text{ 通り} \\
\text{16,777,216 通り} & & \text{200,000 通り以下}
\end{array}
$$

そこで、あり得る状態に $0,1,2,\dots $ と番号を振り、次の DP を考えます。

dp[次見るマスの番号][態の番号] ＝ 通り数

次どの状態に移するかは単純な式で計算できませんが、移先を計算することで、全体計算量 $O(fib(W)\times HW)$ で解けます。

このように、「絶対あり得ない状態」を排除して実装すると、全体計算量 $O(fib(W) \times HW) = O (1.62^W \times HW)$ で解くことができます。

フィボナッチ数の計算量見積もりは難しいですが、「アルゴリズム・AtCoder のための数学」3-4.節に掲載されているので是非ご覧ください。

【類題】
・JOI 2011予選6「JOI 旗」

</details><br>

---

**Keyword:** Eliminating Unnecessary States

#### Subtask 4

In Subtask 3, there are many unnecessary states. For instance, consider the following configurations (red cells indicate positions where a piece is placed):

<div class="container">
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="gray">3</td>
      </tr>
      <tr>
        <td class="red">4</td>
        <td class="gray">5</td>
        <td class="red">6</td>
        <td class="red">7</td>
      </tr>
      <tr>
        <td class="white"></td>
        <td class="white"></td>
        <td class="white"></td>
        <td class="white"></td>
      </tr>
      <tr>
        <td class="white"></td>
        <td class="white"></td>
        <td class="white"></td>
        <td class="white"></td>
      </tr>
    </table>
    <div>
    State in $dp[8][26]$
    </div>
  </div>
  <div>
    <table>
      <tr>
        <td class="gray">0</td>
        <td class="gray">1</td>
        <td class="gray">2</td>
        <td class="gray">3</td>
      </tr>
      <tr>
        <td class="gray">4</td>
        <td class="gray">5</td>
        <td class="gray">6</td>
        <td class="gray">7</td>
      </tr>
      <tr>
        <td class="gray">8</td>
        <td class="gray">9</td>
        <td class="red">10</td>
        <td class="red">11</td>
      </tr>
      <tr>
        <td class="red">12</td>
        <td class="gray">13</td>
        <td class="red">14</td>
        <td class="white"></td>
      </tr>
    </table>
    <div>
    State in $dp[15][23]$
    </div>
  </div>
</div>

These states are **not valid** and can be excluded. Essentially, it is impossible to place pieces consecutively in two adjacent cells.

But how many "valid states" are there?

To summarize, if $\text{fib}(N)$ represents the $N$-th Fibonacci number, the number of "valid states" is approximately:

$$
\text{fib}(W) = O(1.62^W)
$$

This is because the number of \(01\)-strings of length $W$ where no two \(1\)'s are adjacent is equal to $\text{fib}(W)$. For example, when $W = 24$, over **99%** of the states turn out to be unnecessary.

$$
\begin{array}{ccc}
\text{Initial states: } 2^W & \overset{\text{99\% reduction}}{\Longrightarrow} & \text{fib}(W) \text{ states} \\
16,777,216 \text{ states} & & \text{Less than 200,000 states}
\end{array}
$$

Thus, by numbering the valid states as $0, 1, 2, \dots$, we can define the following DP:

$$
dp[\text{next cell number}][\text{state index}] = \text{number of ways}
$$

The transition to the next state cannot be calculated by a simple formula, but precomputing the transitions allows us to solve the problem with a total complexity of:

$$
O(\text{fib}(W) \times H \times W) = O(1.62^W \times H \times W)
$$

By eliminating "impossible states" from the implementation, we achieve this reduced complexity.

For more details on estimating the complexity of Fibonacci numbers, refer to Section 3-4 in *Mathematics for Competitive Programming*.

#### Related Problems:
- **JOI 2011 Preliminary #6**: *JOI Flags*
