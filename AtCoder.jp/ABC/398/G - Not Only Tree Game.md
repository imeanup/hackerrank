## [G - Not Only Tree Game](https://atcoder.jp/contests/abc398/tasks/abc398_g)

The given graph does not contain any odd cycles, so each connected component is bipartite. We therefore consider the following five features of the graph:

* **$x$:** The number of edges that can be added while preserving bipartiteness without changing the connectivity.
* **$ee$:** The number of connected components whose two bipartition sets both contain an even number of vertices.
* **$oo$:** The number of connected components whose two bipartition sets both contain an odd number of vertices.
* **$eo$:** The number of connected components (with at least 2 vertices) in which one bipartition set has an even number of vertices and the other has an odd number.
* **$iso$:** The number of connected components that consist of a single vertex (isolated vertices).

The win/loss outcome is determined as follows:

* **When $N$ is odd:**
  * If $oo + x$ is odd, the first player wins; if it is even, the second player wins.
* **When $N$ is even and $eo = 0$:**
  * If $\frac{iso}{2} + x$ is odd, the first player wins; if even, the second player wins.
* **When $N$ is even and $1 \le eo \le 2$:**
  * The first player wins.
* **When $N$ is even and $eo \ge 3$:**
  * If $oo + x$ is odd, the first player wins; if even, the second player wins.

---

### Idea of the Proof

In this game, every move increases the number of edges in the graph by one, so the parity (even or odd) of the total number of edges in the final graph is crucial.

* **For odd $N$:**  
  At the end of the game, the sizes of the two bipartition sets in the bipartite graph will be one odd and one even. Hence, the total number of edges in the graph is always even. Thus, the win/loss outcome is determined solely by the current number of edges.

* **For even $N$:**  
  The parity of the total number of edges depends on whether the sizes of both bipartition sets are both even or both odd. The only factors that can change the parity of the sizes of the bipartition sets in the final graph are the ways in which connected components that contribute to $eo$ and $iso$ merge. Hence, properly managing these components is essential.

---

### Proof

#### When $N$ is odd

Since the number of edges in the final graph is always even regardless of the moves, the win/loss is determined solely by the current number of edges. The count of connected components in the current graph can be expressed as:

$$(\text{even} \times \text{even}) \times ee + (\text{odd} \times \text{odd}) \times oo + (\text{even} \times \text{odd}) \times eo - x.$$

The parity of this expression is equal to the parity of $oo + x$. Therefore, if $oo + x$ is odd, the first player wins; if it is even, the second player wins.

#### When $N$ is even and $eo = 0$

Note that in this case, $iso$ is even.  
- If $\frac{iso}{2} + x$ is odd, then at least one of $\frac{iso}{2}$ or $x$ is positive, which means one can add an edge either connecting two isolated vertices or an edge that does not change connectivity. This move can change the state to one where “$eo = 0$ and $\frac{iso}{2} + x$ is even.”
- If $\frac{iso}{2} + x$ is even, the possible moves are:
  1. Adding an edge that does not change connectivity.
  2. Adding an edge connecting two isolated vertices.
  3. Adding an edge connecting two non-isolated connected components.
  4. Adding an edge connecting an isolated vertex and another connected component.

After moves 1, 2, or 3, the state becomes “$eo = 0$ and $\frac{iso}{2} + x$ is odd.” With move 4 (noting that there still remain isolated vertices), if the opponent later adds an edge connecting an isolated vertex to the same connected component appropriately, the state reverts to “$eo = 0$ and $\frac{iso}{2} + x$ is even” on your turn.

Since the game ends when $eo = iso = x = 0$, by induction on the number of edges, in this case the condition that “$\frac{iso}{2} + x$ is odd” is both necessary and sufficient for the first player to win.

#### When $N$ is even and $eo = 1$

Due to the parity of the vertices, there must be at least one isolated vertex. By appropriately adding an edge between the connected component contributing to $eo$ and an isolated vertex, one can achieve a state where “$eo = 0$ and $\frac{iso}{2} + x$ is even” after the move.

#### When $N$ is even and $eo = 2$

By suitably adding an edge between the two connected components that contribute to $eo$, one can similarly reach a state where “$eo = 0$ and $\frac{iso}{2} + x$ is even” after the move.

#### When $N$ is even and $eo \ge 3$

Since in one move the change in $eo$ can be at most 2, if after a move $eo < 3$, then as already shown, that results in a losing position. Therefore, if one can always maintain three connected components contributing to $eo$ while playing, the outcome will match the case already analyzed for even $N$.

This completes the reduction of the even $N$ case to the previously handled scenarios.

