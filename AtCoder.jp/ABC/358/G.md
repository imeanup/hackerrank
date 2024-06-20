## [G - AtCoder Tour](https://atcoder.jp/contests/abc358/tasks/abc358_g)


<details><summary><b>Japanese Editorial</b></summary><br>

最適解において、高橋君は通ったマスの中で $A_{i, j}$ が最大であるマスでのみ現在いるマスに留まる行動を取るとしてよいです（そうでないマスで留まった場合、そのマスに留まらないかわりに通ったマスのうち $A_{i, j}$ が最大であるマスに留まると解が改善します）。また、このことから一度現在いるマスに留まった場合は、それ以降ずっとそのマスに留まるとしてよいことがわかります。

高橋君がすべての行動を終えた後にいるマスを $G_{i}, G_j$ とおきます。上の事実から、高橋君は $S_i, S_j$ から $G_{i}, G_j$ に移動し、$G_{i}, G_j$ に留まることを $0$ 度以上繰り返すとしてよいです。

$S_i, S_j$ から $G_{i}, G_j$ までの移動について考えます。上で示したことから高橋君はこの過程で留まることはありませんが、さらに $2$ 度以上同じマスにいることがないとしてよいこともわかります。これは $(p, q)$ を $2$ 度通るとすると、一度 $(p, q)$ を出て $(p, q)$ に戻る過程を取り除き、そのかわりに $G_{i}, G_j$ で留まるとしても解は悪化しないことから従います。

したがって、$S_i, S_j$ から $G_{i}, G_j$ への経路は長さが $HW$ 以下であるもののみ考えればよいです。

これにより素朴な dp で答えが求められることがわかります。

具体的には、$dp_{i, j, k}$ を $i$ 回の行動で $(j, k)$ にいるときの楽しさの合計の最大値とすればよいです。答えは $\max ((K-i) A_{j, k} + dp_{i, j, k})$ となります。

$i \le HW$ の範囲のみ計算すればよいため、上の dp は時間計算量 $O((HW)^2)$ で計算可能です。$K < HW$ のケースなどに注意してください。


</details><br>

## [G - AtCoder Tour](https://atcoder.jp/contests/abc358/tasks/abc358_g)

In the optimal solution, Takahashi should only stay on the cell with the maximum $A_{i,j}$ among the cells he has visited. If he stays on a different cell, the solution can be improved by instead staying on the cell with the maximum $A_{i,j}$. Additionally, once Takahashi decides to stay on a cell, he should continue to stay there for the rest of his actions.

Let $G_i, G_j$ be the cell where Takahashi ends up after all his actions. From the above fact, Takahashi can move from $S_i, S_j$ to $G_i, G_j$ and then repeatedly stay on $G_i, G_j$ zero or more times.

Consider the movement from $S_i, S_j$ to $G_i, G_j$. Based on the above, Takahashi will not stay during this movement. Moreover, he will not visit any cell more than once, meaning he won't pass through the same cell twice. If he were to pass through cell \((p, q)\) twice, removing the process of leaving \((p, q)\) and then returning to it, and instead staying on $G_i, G_j$, would not worsen the solution.

Therefore, we only need to consider paths from $S_i, S_j$ to $G_i, G_j$ that have a length of $HW$ or less.

This allows us to solve the problem using a straightforward dynamic programming (dp) approach.

Specifically, let $dp_{i,j,k}$ be the maximum sum of fun obtained after $i$ actions and being at cell \((j, k)\). The answer will be $\max ((K-i) A_{j,k} + dp_{i,j,k})$.

Since we only need to compute this for $i \le HW$, the dp calculation can be done in $O((HW)^2)$ time. Be mindful of cases where $K < HW$.
