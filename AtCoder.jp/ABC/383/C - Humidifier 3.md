## [C - Humidifier 3](https://atcoder.jp/contests/abc383/tasks/abc383_c) 


この問題は多始点BFSの練習問題です。

グリッドのマスを頂点だと思い、壁でない隣接する二マスを表す頂点間に辺を貼ると、加湿器が置いてあるマスを表す頂点から D**D** 回以下の移動で到達できる頂点の個数を求める問題となります。

まず、加湿器が置いてあるマスが一つの場合、普通の幅優先探索で解けます。queue に加湿器が置いてあるマスをまず入れます。

次に、queue が非空である限り、queue の先頭の頂点を取り出し、その頂点に隣接していて未訪問のマス全てについて距離を求めて queue に入れることを繰り返せば良いです。

始点が複数ある場合は多始点 bfs と呼ばれますがこの場合もほぼ同様です。はじめに queue に始点の頂点を全て追加しておけば、他は完全に通常の bfs と同じ処理で問題ないです。

計算量は $O(HW)$ です。

---

This problem is a practice problem for multi-source BFS (Breadth-First Search).

Think of the grid cells as vertices. By connecting edges between adjacent vertices that are not walls, the task becomes finding the number of vertices that can be reached within **D** moves or fewer from the vertices representing the cells where humidifiers are placed.

### Solution Approach:

1. **Single Humidifier Case**:
   - If there is only one cell where a humidifier is placed, the problem can be solved using a standard BFS.
   - Start by adding the cell with the humidifier to the queue.
   - While the queue is not empty:
     - Remove the front vertex from the queue.
     - For each unvisited neighboring cell of that vertex, calculate its distance and add it to the queue.

2. **Multiple Humidifiers Case**:
   - When there are multiple starting points, this becomes a multi-source BFS problem. 
   - Begin by adding all the cells with humidifiers to the queue.
   - After that, proceed with the same steps as the standard BFS.

### Computational Complexity:

The complexity is $O(HW)$, where $H$ and $W$ are the grid's height and width, respectively.
