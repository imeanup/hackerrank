## [G - AtCoder Express 4](https://atcoder.jp/contests/abc414/tasks/abc414_g)


この問題はいわゆる **区間に辺を張るテク** を用いて解くことができます．このテクニックを用いる典型的な問題として以下の問題があります．

> $N$ 頂点 $0$ 辺のグラフがある．$i = 1, 2, \dots, M$ 回に対して以下を行う．
>
> * 整数 $l_i, r_i, L_i, R_i$ が与えられる．頂点 $a(l_i \le a\le r_i)$ から頂点 $b (L_i\le b \le R_i)$ へ重み $w_i$ の辺を追加する．
>
> 得られたグラフに対し，頂点 $s$ から各頂点への最短距離を求めよ．

この問題を問題文通りに解こうとすると，辺の本数が $O(N^2M)$ 本となってしまいます．ここで，うまくグラフを構成することで辺の本数を減らすというのが区間に辺を張るテクです．

グラフの頂点を拡張して segment tree の区間に対応する頂点を追加することで，辺の本数を減らすことができます．以下の図がわかりやすいので引用します．

（英語解説向け：下図では $[1, 4]$ から $[3, 7]$ にコスト $C$ の辺を張る様子を表しています）

![](https://img.atcoder.jp/abc414/375d89e653b0db2af887a6258897c349.png)

（出典：[https://x.com/noshi91/status/1193177214453338113](https://x.com/noshi91/status/1193177214453338113) ）

このグラフの頂点数は $O(N+M)$ 個，辺の本数は $O(N + M\log N)$ 個になるため，最短距離は dijkstra 法で 計算量 $O(N\log N+M\log^2N)$ で解くことができます．

<details style="border: 1px solid black; padding: 10px;"><summary><b>区間に辺を張るテクを用いて解ける問題（ネタバレを含みます）</b></summary><br>

* [(第二回全国統一プログラミング王決定戦予選 D) Shortest Path on a Line](https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d)
* [(CF406 div.1 D) Legacy](https://codeforces.com/contest/786/problem/B)
* [(JOI  ^2022^ ⁄~2023~ 春季トレーニング C) Passport](https://atcoder.jp/contests/joisp2023/tasks/joisp2023_c)

</details><br>

本問題も，同様のグラフを作ることで辺の本数を減らすことができます．

グラフの構築の仕方について考えます．頂点 $1$ 側を西，頂点 $N$ 側を東としたとき，まずは東行きの列車の処理を考えます． segment tree の各頂点に対して，乗車する側では「その頂点に対応する区間の **東端** の駅に到達するまでにかかる最小コスト」，降車する側では「その頂点に対応する区間の **西端** の駅に到達するまでにかかる最小コスト」を考えることにします．

グラフの辺は次のようになります．

* 乗車する側

![](https://img.atcoder.jp/abc414/3a05a2ec27594e4d3896251a050e7de2.png)

* 降車する側

![](https://img.atcoder.jp/abc414/9d3d6e70efe646017cac2bb26e34d972.png)

このとき，例えば $(l, r, L, R) = (1, 2, 4,6)$ であるような列車は以下のようにして表現できます．

![](https://img.atcoder.jp/abc414/031d24b5ac131a310cb8f7af4f9405d2.png)

具体的には

* 乗車する側の頂点を集約する頂点 $A$，降車する側の頂点を集約する頂点 $B$ を作る．
* 乗車する区間に対応する各頂点に対し，そこから頂点 $A$ に辺を張る．辺の重みはその頂点が対応する segment tree の区間を $[a,b]$ としたとき，$x_r−x_b$ である．
* 頂点 $A$ から頂点 $B$ に辺を張る．辺の重みは $x_L−x_r+c$ である．
* 降車する区間に対応する各頂点に対し，頂点 $B$ からその頂点に辺を張る．辺の重みはその頂点が対応する segment tree の区間を $[a,b]$ としたとき，$x_a− x_L$ である．

頂点 $u(1 \le u \le 2)$ から頂点 $v (4 \le v \le 6)$ に重み $x_v-x_u+c$ のパスが追加されていることが実際に上の図をたどることで確認できます．

同様にして西行きの列車を管理するグラフを作ることができます．

東行きの列車を管理するグラフと西行きの列車を管理するグラフを連結させることで，頂点 $0$ からの距離を dijkstra 法で求めることができます．グラフの頂点数は $O(N+M)$ 個，辺の本数は $O(N + M\log N)$ 個になるため，計算量は $O(N\log N + M \log^2 N)$ です．

自明なグラフの縮約をすることで，頂点の個数は $5N' + M$ にすることができます（$N'$ は $N$ 以上の最小の $2$ べき）．

---
---

This problem can be solved using the so‑called **technique of adding edges over intervals**. A typical problem that uses this technique is the following:

> You have a graph with $N$ vertices and initially 0 edges. For $i = 1, 2, \dots, M$, you are given integers $l_i, r_i, L_i, R_i$. You add a directed edge of weight $w_i$ from every vertex $a$ with $l_i \le a \le r_i$ to every vertex $b$ with $L_i \le b \le R_i$.
> Compute the shortest distance from a specified start vertex $s$ to every other vertex in the resulting graph.

If you try to implement this exactly as stated, you may end up with $O(N^2 M)$ edges. The interval‑edge technique reduces the number of edges by constructing the graph cleverly.

By extending the graph’s vertices to include one node for each segment‑tree interval, you can cut down the edge count. The figure below illustrates the idea:

*(For an English explanation: this diagram shows adding cost‑$C$ edges from interval $[1,4]$ to interval $[3,7]$.)*

![](https://img.atcoder.jp/abc414/375d89e653b0db2af887a6258897c349.png)

*(Source: [https://x.com/noshi91/status/1193177214453338113](https://x.com/noshi91/status/1193177214453338113))*

With this construction, the total number of vertices becomes $O(N + M)$ and the total number of edges $O(N + M\log N)$. Hence Dijkstra’s algorithm runs in $O\bigl(N\log N + M\log^2 N\bigr)$.

<details style="border: 1px solid black; padding: 10px;"><summary><b>Problems solvable by the interval‑edge technique (spoilers ahead)</b></summary><br>

* [(Nikkei 2nd Programming Contest D) Shortest Path on a Line](https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d)
* [(CF406 div.1 D) Legacy](https://codeforces.com/contest/786/problem/B)
* [(JOI 2022/2023 Spring Training C) Passport](https://atcoder.jp/contests/joisp2023/tasks/joisp2023_c)

</details><br>

In this problem, we similarly build such a graph to reduce the edge count.

Let’s consider how to construct the graph. Label vertex 1 as “west” and vertex $N$ as “east.” First, handle the east‑bound trains. For each segment‑tree node, we create two sets of vertices:

* **Embark vertices:** represent “the minimum cost to reach the east end of that node’s interval.”
* **Disembark vertices:** represent “the minimum cost to reach the west end of that node’s interval.”

The edges are then added as follows:

* **Embarking side:**
  ![](https://img.atcoder.jp/abc414/3a05a2ec27594e4d3896251a050e7de2.png)

* **Disembarking side:**
  ![](https://img.atcoder.jp/abc414/9d3d6e70efe646017cac2bb26e34d972.png)

For example, a train defined by $(l, r, L, R) = (1,2,4,6)$ is represented like this:

![](https://img.atcoder.jp/abc414/031d24b5ac131a310cb8f7af4f9405d2.png)

Concretely:

1. Create an aggregation vertex $A$ for the embarking side and an aggregation vertex $B$ for the disembarking side.
2. For each segment‑tree node covering $[a,b]$ within the embark interval, add an edge from that node’s embark vertex to $A$ with weight $\,x_r - x_b$.
3. Add an edge from $A$ to $B$ with weight $\,x_L - x_r + c$.
4. For each segment‑tree node covering $[a,b]$ within the disembark interval, add an edge from $B$ to that node’s disembark vertex with weight $\,x_a - x_L$.

By following the path through these edges, you verify that every path from a vertex $u$ ($l \le u \le r$) to a vertex $v$ ($L \le v \le R$) has cost $x_v - x_u + c$.

You repeat the same construction for west‑bound trains. Finally, you connect the east‑ and west‑bound subgraphs and run Dijkstra’s algorithm from a super‑source (vertex 0). Since there are $O(N+M)$ vertices and $O(N + M\log N)$ edges, the total complexity remains $O(N\log N + M\log^2 N)$.

With a bit of segment‑tree compression, you can reduce the vertex count to $5N' + M$, where $N'$ is the smallest power of two at least $N$.
