## [E - Weighted Tic-Tac-Toe](https://atcoder.jp/contests/abc349/tasks/abc349_e)

> [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)

<details><summary>Japanese Editorial <b>Click here</b></summary><br>

### 勝敗の判定方法

ゲームの各時点における盤面は，各要素が $\{$ 白，赤，青 $\}$ のいずれかの値を取るような $3 \times 3$ の2次元配列 $C$ で表すことができます．すなわち，$C_{i,j}$ はマス $(i, j)$ の色に対応します．盤面の色が $C$ である状態からゲームを続けたとき，最終的に勝つプレイヤーを $f(C)$ とします．

$I$ を，すべての要素が白である $3 \times 3$ の2次元配列とします（初期状態に対応）．求める答えは $f(I)$ ですから，任意に与えられた $C$ に対して $f(C)$ を高速に求めることができれば，問題を解くことができます．

$f(C)$ の計算方法を考えましょう．以下，現在の手番のプレイヤーを $x$，もう一方のプレイヤーを $y$ とします．

もし， $C$ がすでに終了状態（赤または青の同じ色で塗られたマスが $3$ マス連続するか，白のマスが存在しない）であれば，勝敗は容易に判定できます．

$C$ が終了状態でない場合， $x$ が白で塗られたマスを一つ選んで自分の色で塗ることにより，別の盤面に遷移します．このとき，次が成り立ちます．

* $C$ から $1$ 回の操作で遷移できる盤面 $C'$ のうち， $f(C') = x$ となるようなものがあれば， $C$ から $C'$ に遷移することで $x$ が勝つことができる
* 逆に，$C$ から $1$ 回の操作で遷移できるすべての盤面 $C'$ について， $f(C') = y$ ならば，$x$ はどのように操作しても勝つことができない

この性質より， $C$ から遷移できるすべての盤面 $C'$ について $f(C')$ が求まっていれば，それらの値から $f(C)$ を求めることができます．このような処理は，**再帰関数**による実装が簡便です．

### 再帰関数による実装

再帰関数による実装では，盤面 $C$ に対して関数 $f$ が呼び出されたときに，次のような処理を行います．

1. $C$ が終了状態ならば，勝敗を判定して答えを返す
2. $C$ が終了状態でなければ， $C$ から $1$ 回の操作で遷移できる盤面 $C'$ をすべて列挙する
3. 各 $C'$ について $f(C')$ を計算する
4. 計算した $f(C')$ の結果から，前節の議論に基づいて $f(C)$ の値を定める

関数 $f$ の処理の中で関数 $f$ 自身を呼び出している（ステップ 3）ので，このような処理は再帰と呼ばれます．ここで， $f(C)$ から呼び出される $f(C')$ の $C'$ は $C$ よりも終了状態に近づいているので，このような再帰的な呼び出しが無限に続くことはありません（形式的には，盤面の遷移関係からなるグラフは **有向非巡回グラフ (DAG)** になっています）．

$f$ が呼び出される回数を大雑把に見積もってみましょう．1回目の手番で可能な操作は $9$ 通り，2回目の手番で可能な操作は $8$ 通り，…となるので，初期状態から終了状態へ到達するまでの操作の組み合わせは $9! \approx 3.6 \times 10^5$ 通り程度であり，十分高速です（実際には，同じ色で塗られたマスが $3$ つ連続した時点でゲームが終了し，再帰的呼び出しがそこで打ち切られるため，より少ない呼び出し回数になります）．

[実装例 (Python)]
[Implementation Python](https://atcoder.jp/contests/abc349/submissions/52204714)

### 発展：メモ化再帰による実装

本問題ではナイーブな再帰関数でも十分高速に動作しますが，**メモ化**と呼ばれる工夫をすることで，再帰的呼び出しの回数を減らすことができます．

再帰関数による実装では，初期状態 $I$ から盤面 $C$ に到達するまでの操作の組み合わせが複数個ある場合，その回数だけ $f(C)$ が呼び出されます．しかし，同じ $C$ に対しては $f(C)$ は常に同じ値を返すため，毎回再帰的呼び出しにより $f(C)$ を計算するのは無駄です．そこで， $f(C)$ を最初に計算したときの結果を覚えておいて，2回目以降に $f(C)$ が呼び出されたときにはその覚えておいた値を返すようにします．

メモ化を行ったときの $f(C)$ の呼び出し回数を見積もりましょう． $C$ としてありえるものは大雑把に見積もっても $3^{3\times 3} = 19683$ 程度であり，各盤面から遷移できる盤面はたかだか $9$ 通りですので， $f$ の呼び出し回数はたかだか $19683 \times 9 \approx 1.7 \times 10^5$. 回です．メモ化を行わないときの見積もり $3.6 \times 10^5$ に比べて小さくなっていることがわかります．

本問題ではメモ化は要求されていませんが，より盤面の数や可能な遷移の数が多いような問題では，メモ化を行うことで計算量が大幅に改善されることがあります.

[実装例 (Python)]
[Implementation Python](https://atcoder.jp/contests/abc349/submissions/52166908)

</details><br>

### Determining Victory or Defeat

The state of the board at each point in the game can be represented by a $3 \times 3$ 2D array $C$, where each element takes one of the values $\{$ white, red, blue $\}$. In other words, $C_{i,j}$ corresponds to the color of square $(i, j)$. Let $f(C)$ denote the player who ultimately wins when the game continues from the state with colors $C$.

Let $I$ be a $3 \times 3$ 2D array where all elements are white (corresponding to the initial state). The answer we seek is $f(I)$, so if we can efficiently determine $f(C)$ for any given $C$, we can solve the problem.

Let's consider how to calculate $f(C)$. Here, let $x$ be the current player's turn, and $y$ be the other player.

If $C$ is already in a terminal state (i.e., three consecutive squares are colored red or blue, or there are no white squares), we can easily determine the winner.

If $C$ is not in a terminal state, then by selecting one white square from $C$ and coloring it with their own color, player $x$ transitions to a different board state. In this case, the following holds:

- If among the board states $C'$ that can be reached from $C$ in one move, there exists a $C'$ where $f(C') = x$, then player $x$ can win by transitioning from $C$ to $C'$.
- Conversely, if for all board states $C'$ that can be reached from $C$ in one move, $f(C') = y$, then player $x$ cannot win regardless of their move.

From this property, if we have determined $f(C')$ for all board states $C'$ reachable from $C$, we can determine $f(C)$ from those values. Implementing this with a recursive function is straightforward.

### Implementation with Recursive Function

In the implementation using a recursive function, when the function $f$ is called for the board state $C$, the following process is performed:

1. If $C$ is in a terminal state, determine the outcome and return the answer.
2. If $C$ is not in a terminal state, enumerate all the board states $C'$ that can be reached from $C$ in one move.
3. Calculate $f(C')$ for each $C'$.
4. Determine the value of $f(C)$ based on the calculated results of $f(C')$ as discussed in the previous section.

Since the function $f$ calls itself within its own execution (Step 3), this type of processing is called recursion. Here, the $C'$ for which $f(C')$ is called from $f(C)$ is closer to a terminal state than $C$, so such recursive calls do not continue indefinitely (formally, the graph composed of the board state transitions forms a Directed Acyclic Graph (DAG)).

Let's roughly estimate the number of times $f$ is called. There are $9$ possible moves for the first turn, $8$ possible moves for the second turn, and so on. Therefore, the combinations of moves from the initial state to a terminal state are on the order of $9! \approx 3.6 \times 10^5$, which is sufficiently fast (in reality, the game ends when three consecutive squares are colored with the same color, and recursive calls are terminated at that point, resulting in fewer calls).

[Implementation Python](https://atcoder.jp/contests/abc349/submissions/52204714)

### Advanced: Implementation with Memoization

In this problem, a naive recursive function operates sufficiently quickly. However, by employing a technique called **memoization**, the number of recursive calls can be reduced.

In the implementation with a recursive function, if there are multiple combinations of moves to reach the board state $C$ from the initial state $I$, the function $f(C)$ is called as many times as the number of combinations. However, since $f(C)$ always returns the same value for the same $C$, it is wasteful to calculate $f(C)$ recursively every time. Therefore, we remember the result of $f(C)$ when it is calculated for the first time, and return this memorized value when $f(C)$ is called again.

Let's estimate the number of calls to $f(C)$ when memoization is applied. There are roughly $3^{3 \times 3} = 19683$ possible $C$ values, and each board state can transition to at most $9$ other states. Therefore, the number of calls to $f$ is at most $19683 \times 9 \approx 1.7 \times 10^5$. This is smaller than the estimate of $3.6 \times 10^5$ without memoization.

While memoization is not required for this problem, in problems where there are more board states and possible transitions, memoization can significantly improve computational efficiency.

[Implementation Python](https://atcoder.jp/contests/abc349/submissions/52166908)
