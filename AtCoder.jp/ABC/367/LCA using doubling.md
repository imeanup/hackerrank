## Algorithm for Finding the Lowest Common Ancestor (LCA) in a Tree Using Doubling

In a tree, the **ancestor** of a vertex refers to "*a vertex that can be reached by tracing back through the parent nodes.*" The **common ancestor** of two vertices refers to "*an ancestor that both vertices share.*"

The Lowest Common Ancestor (LCA) of vertices $u$ and $v$ is defined as "the closest vertex to both $u$ and $v$ among their common ancestors."

![Tree with root at vertex 0. The LCA of vertex 4 and vertex 6 is vertex 1](https://algo-logic.info/wp-content/uploads/2020/03/tree-2.png)

Tree with root at vertex $0$. The LCA of vertex $4$ and vertex $6$ is vertex $1$.

## Algorithm

### Algorithm to find the LCA using doubling

#### Preprocessing
1. Perform a DFS (or a similar traversal) to determine the distance from the root and the parent for each vertex.
2. Use doubling to calculate the ancestor at a distance of $2^k$ for each vertex.

#### Query (Finding the LCA of $u$ and $v$)
1. Adjust the deeper vertex (either $u$ or $v$) to bring it to the same level as the other vertex, resulting in new vertices $u_1$ and $v_1$ such that the distance to the LCA is the same for both.
2. Using binary search, gradually move $u_1$ and $v_1$ closer to their LCA, stopping just before they become equal.
3. The vertex just before $u_1$ and $v_1$ become equal is the LCA.


**Note:** Since all vertices beyond the LCA are "common ancestors," binary search can be used. However, a straightforward binary search where you "determine a distance $d$ and try to find the vertex at $d$ distance back" would take $O(\log N)$ time per query, leading to a total time complexity of $O((\log N)^2)$. This would occur if you used binary search to find the smallest $d$ that satisfies the condition "the vertex at $d$ distance back from both $u_1$ and $v_1$ is a common ancestor."

However, by using doubling with values $k = 2^k, 2^{k-1}, 2^{k-2}, \dots, 2^0$ to check if moving $u_1$ and $v_1$ forward by $k$ steps results in a common ancestor, you can move $u_1$ and $v_1$ step by step until they are just before the LCA, achieving a total time complexity of $O(\log N)$.

It might be quicker to understand this concept by looking at an implementation example.

**Note:** One of $u_1$ or $v_1$ will be the same as the original $u$ or $v$.

![Vertex `u` is deeper than `v`](https://algo-logic.info/wp-content/uploads/2020/03/tree-6.png)

$u$ is deeper than $v$

![Adjusting `u` to be at the same level as `v`](https://algo-logic.info/wp-content/uploads/2020/03/tree-5.png)

Since $u$ is deeper, adjust it to the same level as $v$.

For more details on doubling, refer to [The Basic Concept of Doubling and Its Applications](https://algo-logic.info/doubling/).

### Time Complexity

* Preprocessing: $O(N \log N)$ time, $O(N \log N)$ space
* Query: $O(\log N)$

When there are $N$ vertices, it is necessary to store approximately $\log N$ values for each vertex. Therefore, both the time complexity and the space complexity are $O(N \log N)$.

### Implementation Example in C++ and Summary

This implementation performs preprocessing on the graph $G$ with the given root, and then finds the LCA using binary search.

```cpp
struct Edge {
    long long to;
};
using Graph = vector<vector<Edge>>;

/* 
LCA(G, root): A structure to find the Lowest Common Ancestor in a tree G with root as the root.
    query(u,v): Finds the LCA of u and v. Time complexity: O(logn)
    Preprocessing: O(nlogn) time, O(nlogn) space
*/
struct LCA {
    vector<vector<int>> parent;  // parent[k][u]:= The 2^k-th ancestor of u
    vector<int> dist;            // Distance from the root
    LCA(const Graph &G, int root = 0) { init(G, root); }

    // Initialization
    void init(const Graph &G, int root = 0) {
        int V = G.size();
        int K = 1;
        while ((1 << K) < V) K++;
        parent.assign(K, vector<int>(V, -1));
        dist.assign(V, -1);
        dfs(G, root, -1, 0);
        for (int k = 0; k + 1 < K; k++) {
            for (int v = 0; v < V; v++) {
                if (parent[k][v] < 0) {
                    parent[k + 1][v] = -1;
                } else {
                    parent[k + 1][v] = parent[k][parent[k][v]];
                }
            }
        }
    }

    // Calculate the distance from the root and the next vertex
    void dfs(const Graph &G, int v, int p, int d) {
        parent[0][v] = p;
        dist[v] = d;
        for (auto e : G[v]) {
            if (e.to != p) dfs(G, e.to, v, d + 1);
        }
    }

    int query(int u, int v) {
        if (dist[u] < dist[v]) swap(u, v);  // Ensure u is deeper
        int K = parent.size();
        // Adjust the distance to the LCA
        for (int k = 0; k < K; k++) {
            if ((dist[u] - dist[v]) >> k & 1) {
                u = parent[k][u];
            }
        }
        // Use binary search to find the LCA
        if (u == v) return u;
        for (int k = K - 1; k >= 0; k--) {
            if (parent[k][u] != parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        }
        return parent[0][u];
    }
};
```

## Explanation of the Algorithm

### What is Doubling?

[Doubling](https://algo-logic.info/doubling/) is an algorithm that allows you to find "the element `K` steps ahead" in $O(K)$ time when the total number of elements is $N$.

* Preprocessing: $O(N \log K)$ time, $O(N \log K)$ space
* Query: $O(\log K)$

The implementation works as follows:

* Preprocessing
  1. For each element, record the element that is 1 step ahead.
  2. Use the previous results to record the element that is 2 steps ahead for each element.
  3. Use the previous results to record the element that is 4 steps ahead for each element.
  4. Use the previous results to record the element that is 8 steps ahead for each element.
  5. Use the previous results to record the element that is 16 steps ahead for each element.
  6. …
* Query: Search for the element $K$ steps ahead using a method similar to binary search or repeated squaring.

If you know the element $2^k$ steps ahead, you can easily find "the element $2^k$ steps ahead of $2^k$ steps ahead," allowing you to quickly determine "the element $2^{k + 1}$ steps ahead."

### Idea to Find LCA Using Doubling

![](https://algo-logic.info/wp-content/uploads/2020/03/tree-6.png)

Let the distance from the root to vertex $v$ be denoted as $\rm dist(v)$. When the LCA (Lowest Common Ancestor) of vertices $u$ and $v$ is $x$, the following conditions should hold:

* The point reached by tracing back $\rm dist(u) - dist(x)$ steps from $u$ is $x$.
* The point reached by tracing back $\rm dist(v) - dist(x)$ steps from $v$ is $x$.

As it stands, this approach cannot utilize doubling. To address this, consider creating points $u_1$ and $v_1$ where the distance to $x$ is the same. Let's assume that $u$ is the deeper point for simplicity, meaning $\rm dist(u) > dist(v)$.

* Let $u_1$ be the point reached by tracing back $\rm |dist(u) - dist(v)|$ steps from $u$.
  * The point reached by tracing back $\rm dist(v) – dist(x)$ steps from $u_1$ is $x$.
* Set $v$ as $v_1$.
  * The point reached by tracing back $\rm dist(v) – dist(x)$ steps from $v_1$ is $x$.

![](https://algo-logic.info/wp-content/uploads/2020/03/tree-5.png)

The distance to $x$ is the same.

In this way, you can say that if you trace back from $u_1$ and $v_1$ a distance $d$ that is at least $\rm dist(v) – dist(x)$, they will meet at the same vertex (since all ancestors beyond the closest common ancestor are common ancestors).

With this setup, you can use binary search. By using binary search, you can gradually move $u_1$ and $v_1$ to the point just before the LCA $x$ (moving them as close as possible without them becoming the same).

## Applications

### Finding the Distance Between Any Two Vertices with LCA

During the LCA calculation process, the distance from the root to all vertices has already been computed.

If the LCA of vertices $u$ and $v$ is $x$, then the distance between $u$ and $v$ can be determined as:

$$
\rm dist(u) + dist(v) - 2 \times dist(x)
$$

```cpp
int get_dist(int u, int v) { 
    return dist[u] + dist[v] - 2 * dist[query(u, v)]; 
}
```

### Checking if a Vertex is on a Path

You can easily determine if a vertex `a` lies on the path connecting vertices $u$ and $v$.

If vertex $a$ is on the path, then:

* The distance from $u$ to $a$ plus the distance from $a$ to $v$
* The distance from $u$ to $v$

will be equal. If they are not equal, $a$ is not on the path.

```cpp
bool is_on_path(int u, int v, int a) { 
    return get_dist(u, a) + get_dist(a, v) == get_dist(u, v); 
}
```

## Practice Problems

* [AOJ GRL_5_C Lowest Common Ancestor](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C&lang=ja): For verification
* [[AtCoder] ABC 014 D – Tree](https://atcoder.jp/contests/abc014/tasks/abc014_4)

<details><summary><b>Japanese</b></summary><br>

# ダブリングによる木の最近共通祖先（LCA：Lowest Common Ancestor）を求めるアルゴリズム

最近木においてある頂点の祖先は「親をたどってたどり着ける頂点」を指し、2頂点の共通祖先は「2頂点が共通して持つ祖先」のことを言います。

頂点 u と v の最近共通祖先(LCA: Lowest Common Ancestor) とは、「共通祖先の中でも、最も u, v に近い頂点」のことです。

![](https://algo-logic.info/wp-content/uploads/2020/03/tree-2.png)
頂点0 を根とする木。頂点 4 と頂点 6 の LCA は頂点 1

## アルゴリズム

**ダブリングによりLCAを求めるアルゴリズム：**

* 前処理
  1. DFSなどによって、全ての頂点について、根からの距離と親を求める
  2. ダブリングによって $2^k$ 先の祖先を求める
* クエリ（u と v の最近共通祖先 x を求める。）
  1. u と v の深い方の頂点を変更して「x までの距離が同じ点 u1, v1」にする
  2. 二分探索を用いて u1, v1 を最近共通祖先 x の一つ手前まで段階的に移動させる（u1, v1 が同じにならないギリギリまで移動させる）
  3. 最終的な u1, v1 の一つ先が LCA

※ x から先の頂点は全て「共通祖先」となるため二分探索が使用できますが、普通の二分探索のように、「dを決め打ちして、d先の頂点を実際に得ようとする」のは一回あたり $O(\log N)$ かかり、全体で $O((\log N)^2)$ の計算量になります。（つまり「条件 C(d)：u1 と v1 から d さかのぼった点は共通祖先か」を満たす最小の d を二分探索で見つけるような場合です。）

ですが $k = 2^k, 2^{k-1}, 2^{k-2}, \dots, 2^0$ について 「k個先を確認して共通祖先でないなら u1,v1 をk個先に移動」ということを繰り返すと、最終的に u1,v1 が LCA の直前になるまで移動させることができ、全体で $O(\log N)$ で求めることが可能です。

以上の話は実装例を見たほうが早いかもしれません。

※ u1, v1 の片方は、もともとの u, v と同じ頂点です。

![](https://algo-logic.info/wp-content/uploads/2020/03/tree-6.png)
u の方が v よりも深い

![](https://algo-logic.info/wp-content/uploads/2020/03/tree-5.png)
u の方が深いので、同じ高さになるように変更する

※ダブリングについては、[ダブリングの基本概念とその応用](https://algo-logic.info/doubling/) を参照してください

### 計算量

* 前処理：$O(N \log N)$ 時間, $O(N \log N)$ 空間
* クエリ：$O(\log N)$

N 頂点あった時、一つの頂点あたり約 $\log N$ 個の値を保持する必要があります。よって、時間計算量・区間計算量ともに $O(N \log N)$ です。

### C++ による実装例とまとめ

グラフ G と根 root を受け取って前処理を行い、LCA を二分探索で求めます。

```cpp
struct Edge {
    long long to;
};
using Graph = vector<vector<Edge>>;

/* LCA(G, root): 木 G に対する根を root として Lowest Common Ancestor を求める構造体
    query(u,v): u と v の LCA を求める。計算量 O(logn)
    前処理: O(nlogn)時間, O(nlogn)空間
*/
struct LCA {
    vector<vector<int>> parent;  // parent[k][u]:= u の 2^k 先の親
    vector<int> dist;            // root からの距離
    LCA(const Graph &G, int root = 0) { init(G, root); }

    // 初期化
    void init(const Graph &G, int root = 0) {
        int V = G.size();
        int K = 1;
        while ((1 << K) < V) K++;
        parent.assign(K, vector<int>(V, -1));
        dist.assign(V, -1);
        dfs(G, root, -1, 0);
        for (int k = 0; k + 1 < K; k++) {
            for (int v = 0; v < V; v++) {
                if (parent[k][v] < 0) {
                    parent[k + 1][v] = -1;
                } else {
                    parent[k + 1][v] = parent[k][parent[k][v]];
                }
            }
        }
    }

    // 根からの距離と1つ先の頂点を求める
    void dfs(const Graph &G, int v, int p, int d) {
        parent[0][v] = p;
        dist[v] = d;
        for (auto e : G[v]) {
            if (e.to != p) dfs(G, e.to, v, d + 1);
        }
    }

    int query(int u, int v) {
        if (dist[u] < dist[v]) swap(u, v);  // u の方が深いとする
        int K = parent.size();
        // LCA までの距離を同じにする
        for (int k = 0; k < K; k++) {
            if ((dist[u] - dist[v]) >> k & 1) {
                u = parent[k][u];
            }
        }
        // 二分探索で LCA を求める
        if (u == v) return u;
        for (int k = K - 1; k >= 0; k--) {
            if (parent[k][u] != parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        }
        return parent[0][u];
    }
};
```


## アルゴリズムの説明

### ダブリングとは

[ダブリング](https://algo-logic.info/doubling/)は全体の要素数がN個のとき「K個先の要素を求めるのに $O(K)$ かかる」ような状況を

* 前処理：$O(N \log K)$ 時間, $O(N \log K)$ 空間
* クエリ：$O(\log K)$

で行うことができるようにするアルゴリズムです。

実現のためには以下のようにします。

* 前処理
  1. それぞれの要素について 1 個先の要素が何か記録
  2. 前の結果を利用して、それぞれの要素について 2 個先の要素が何か記録
  3. 前の結果を利用して、それぞれの要素について 4 個先の要素が何か記録
  4. 前の結果を利用して、それぞれの要素について 8 個先の要素が何か記録
  5. 前の結果を利用して、それぞれの要素について 16 個先の要素が何か記録
  6. …
* クエリ：二分探索や繰り返し二乗法と同様の方法で K 個先の要素が何か探索

$2^k$ 先の要素が分かっていれば「 “ $2^k$ 先の要素" の $2^k$ 先」を簡単に求めることができるので、$2^{k+1}$ 先の要素が何か」を高速に求めることができます。

### LCAをダブリング求めるアイディア

![](https://algo-logic.info/wp-content/uploads/2020/03/tree-6.png)

根から頂点 v への距離を dist(v) と書くことにします。頂点 u, v の LCA が x だった場合、以下が成り立つはずです。

* **u** から dist(u)-dist(x) 回 だけ根へさかのぼった時の点が x
* **v** から dist(v)-dist(x) 回 だけ根へさかのぼった時の点が x

このままではダブリングが使えません。そこで以下のように「x までの距離が同じ点 u1, v1」を用意します。簡単のために u の方がより深い点としましょう。つまり dist(u)>dist(v) です。

* **u** から |dist(u)-dist(v)| 回 さかのぼった点を u1 とする
  * u1 から「 dist(v) – dist(x) 」回さかのぼった点が x
* **v** を v1 とする
  * v1 から 「dist(v) – dist(x)」 回さかのぼった点が x

![](https://algo-logic.info/wp-content/uploads/2020/03/tree-5.png)
x までの距離は同じ

こうすると、「u1 と v1 からある距離（dist(v) – dist(x)）以上の距離 d だけさかのぼると同じ頂点になる」と言えます（最近共通祖先から先の祖先は全て共通祖先です）。

このようにすると、二分探索を利用することができて、二分探索を用いて u1, v1 を最近共通祖先 x の一つ手前まで段階的に移動させる（u1, v1 が同じにならないギリギリまで移動させる）ようにすれば良いです。


## 応用

### LCA で 任意の2頂点間の距離が分かる

LCA の計算過程で、根からの距離を全ての頂点について計算済みです。

頂点 u, v の LCA が x だった場合、

* dist(u) + dist(v) – 2 × dist(x)

で u, v 間の距離を求めることができます。

```cpp
int get_dist(int u, int v) { return dist[u] + dist[v] - 2 * dist[query(u, v)]; }
```

### パス上にある頂点があるか分かる

頂点 u, v を結ぶパス上に、ある頂点 a が存在するかも簡単に判定ができます。

頂点 a がパス上にあれば

* u と a の距離 + a と v の距離
* u と v の距離

が等しくなります。逆に等しくなければパス上にはありません。

```cpp
bool is_on_path(int u, int v, int a) { return get_dist(u, a) + get_dist(a, v) == get_dist(u, v); }
```

## 練習問題

* [AOJ GRL_5_C Lowest Common Ancestor](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C&lang=ja)：チェック用
* [[AtCoder] ABC 014 D – 閉路](https://atcoder.jp/contests/abc014/tasks/abc014_4)

</details><br>

> [Source](https://algo-logic.info/lca/)
