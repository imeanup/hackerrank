
## [D - Laser Marking](https://atcoder.jp/contests/abc374/tasks/abc374_d)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese</b></summary><br>

$N \le 6$ という非常に小さな制約に着目しましょう。
この制約であれば、ありうるレーザ照射の方法を全探索できそうです。

全探索をするのであれば、それに伴って調べ尽くす必要のあるパラメータを全て見つけて固定してしまいましょう。

* 線分を描く順序 $N!$ 通り
* 線分を描く向き(どちらの点からどちらの点へと描くか) $2^N$ 通り

$N=6$ に対して、全体で $6! \times 26 = 46080$ 通りしかなく、これはコンピュータを用いれば容易に全探索できる数です。

線分を描く順序は、長さ $N$ の順列を全列挙することで尽くせます。
再帰関数を用いて順列を全列挙したり、 C++ においては `next_permutation` を利用すると便利です。

線分を描く向きは、 $0$ から $2^N−1$ までの整数について下から $i$ bit目が $0$ の時は $(A_i, B_i) \to (C_i,D_i)$ 、 $1$ の時はこの逆と取り決めることで尽くせます。

線分を描く順序と、線分を描く向きとを固定すれば、それを最短の時間で実現する方法は定まります(始点または線分の終わりから次の線分の始まりまでを一直線に移動するのが最善です)。

よって、この2つを二重ループの構造でループさせると、 $N! \times 2^N$ 通りの全探索が実現します。

実装例 (C++):

</details><br>


Let's focus on the very small constraint of $N \le 6$. With this constraint, it seems possible to perform a brute-force search of all possible laser irradiation methods.

Since we are doing a brute-force search, let's find and fix all the parameters that need to be thoroughly examined:

- The order in which to draw the line segments: $N!$ ways
- The direction in which to draw the line segments (from which point to which point): $2^N$ ways

For $N = 6$, there are only $6! \times 2^6 = 46080$ ways in total, which is a number small enough to explore exhaustively using a computer.

The order of drawing the line segments can be exhausted by enumerating all permutations of length $N$. You can use a recursive function to enumerate permutations, or in C++, the `next_permutation` function is convenient.

The direction of drawing the line segments can be exhausted by iterating over integers from $0$ to $2^N - 1$, and determining that when the $i$-th bit is $0$, the segment is drawn from $(A_i, B_i)$ to $(C_i, D_i)$, and when it is $1$, it is drawn in the reverse direction.

Once both the order of drawing the line segments and the direction of drawing are fixed, the method to achieve it in the shortest time is determined (moving in a straight line from the end of one segment to the start of the next is optimal).

Therefore, by looping over these two parameters in a double loop structure, a brute-force search of all $N! \times 2^N$ possibilities can be achieved.
