## [F - Tree Degree Optimization](https://atcoder.jp/contests/abc359/tasks/abc359_f)

<details><summary>Japanese Editorial</summary><br>

木の次数列 $d = (d_1, \dots, d_N)$ としてあり得る整数列は以下を満たすものです。

* $d_i \ge 1$
* $\sum_{i=1}^N d_i = 2N-2$

（補足：この事実は、プリューファーコードを考えることで直ちに従います。または、総和の条件から $d_i = 1$ を満たす頂点が必ず存在することから、そのような頂点 $i$ とそれ以外の頂点の辺を取り除くことを考えて、帰納法を回すことでも示せます。）

この条件を満たす任意の列は木の次数列としてあり得るので、上の条件を満たす列にたいするコストの最小値を考えればよいです。

これは、今回のコストの増加分が $d_i$ の値に対して単調増加なことから、貪欲法を行うことで解くことが出来ます。

（補足：貪欲法の正当性は凸関数同士の畳み込みを考えれば示せます。）

具体的には、はじめ全ての $i$ について $d_i = 1$ で初期化し、$d_i$ を $1$ 増やしたときのコストの増加分が最小となるような $i$ について $d_i$ を $1$ 増やすことを $N-2$ 回繰り返せばよいです。

更にこの貪欲法は priority_queue などを使うことで高速化できて、$O(N\log N)$ で動作します。

</details><br>


The sequence of degrees $d = (d_1, \dots, d_N)$ that can represent a tree must satisfy the following conditions:

* $d_i \ge 1$
* $\sum_{i=1}^N d_i = 2N-2$

(Note: This fact can be immediately derived by considering the Prüfer code. Alternatively, it can be shown by induction based on the total sum condition, where a vertex $i$ that satisfies $d_i = 1$ must exist, and considering the removal of such a vertex $i$ and its edges to other vertices.)

Any sequence that satisfies these conditions can be the degree sequence of a tree. Therefore, we need to consider the minimum cost for a sequence that meets the above conditions.

Since the increase in cost for the current problem is monotonically increasing with respect to the value of $d_i$, it can be solved greedily.

(Note: The validity of the greedy approach can be shown by considering the convolution of convex functions.)

Specifically, initially set $d_i = 1$ for all $i$. Then, increase $d_i$ by 1 for the $i$ that results in the smallest cost increase. Repeat this process $N-2$ times.

Furthermore, this greedy approach can be optimized using a priority queue, allowing it to run in $O(N\log N)$ time.
