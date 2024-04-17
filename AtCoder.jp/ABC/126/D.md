### D: Even Relation

<!-- 以下、与えられたグラフを適当な頂点を根とみなした根付き木として考えます。また根から頂点 $i$ への距離 を $d_i$ とします。

任意の $2$ 頂点 $u$ と $v$ について、その最小共通祖先を $w$ とすると、$u と v$ の距離は $d_u + d_v − 2d_w$ と書く ことができます。この式の第 $3$ 項は偶数なので、$d_u$ と $d_w$ の偶奇が等しいときに限り、$u と w$ の距離は偶数 になります。よって例えば $d_i$ が偶数の頂点は白に、奇数の頂点は黒に塗ることで条件を満たす塗り分けが可 能です -->


Consider the given graph as a rooted tree with an arbitrary vertex as the root. Let the distance from the root to vertex $i$ be denoted as $d_i$.

For any two vertices $u$ and $v$, let $w$ be their lowest common ancestor. Then, the distance between $u$ and $v$ can be written as $d_u + d_v - 2d_w$. Since the third term in this expression is even, the distance between $u$ and $w$ is even only when the parities of $d_u$ and $d_w$ are equal. Therefore, by coloring vertices with even $d_i$ in white and those with odd $d_i$ in black, we can satisfy the condition of the problem by properly partitioning the vertices.

### Second Approach

<!-- ### 考えたこと

考え方としては

* 二部グラフ判定

に近い。今回は各辺に重みがあるが、この重さは偶数か奇数かだけが問題である。

* その重さが奇数だったら、長さが 1 の辺
* その重さが偶数だったら、長さが 0 の辺 (あるいは u-v だとすると、u-w-v と間に頂点 w が挿入された長さ 2 の状態)

という感じ。今回はツリーなので「ツリー上の DFS」というのと「二部グラフ判定」というのがいい感じに組み合わせるような実装になる。

### ツリーを探索するとは

ツリーというと根から伸びているものを思いがちだが、今回は特に根が指定されているわけではない。そこでツリーを探索するときの常套手段は、

* 根をなんでもいいから 1 個決めてしまう

というもの。根を決めてしまえば、そこから自動的に探索することができる。特に理由がなければ根はノード 0 で構わない。そして多くの場合、以下のような書き方をテンプレとして持つことができる。

実際のツリー上の探索はこれにいろんなものを付け加えていく感じだが、ほとんどのツリー探索は下のような実装にちょっと付け加えるだけで書くことができる。

下の実装で「if (nv == p) continue;」のところがツリー探索で一般的な枝刈りで、これを行うことで、根から葉に向かって逆流することなく探索を行うことができる。 -->

### Thoughts

The approach is similar to bipartite graph detection. In this case, each edge has a weight, but only whether this weight is even or odd matters.

* If the weight is odd, it represents an edge of length 1.
* If the weight is even, it represents an edge of length 0 (or, if we consider it as between $u$ and $v$, then it represents a length 2 with an inserted vertex $w$ between $u$ and $v$).

This is the general idea. Since the given structure is a tree, the implementation would involve combining "DFS on a tree" and "bipartite graph detection" in a suitable manner.

### Exploring the Tree

When we talk about exploring a tree, we often tend to think about traversing from the root. However, in this case, there is no specific root specified. So, a common approach to exploring a tree is to:

* Arbitrarily select a root node.

Once the root is chosen, the exploration can proceed automatically from there. If there is no specific reason, the root can be chosen as node 0. Below is a typical template for tree traversal, which can be extended as needed.

Actual tree traversal involves adding various functionalities to this basic structure, but most tree traversals can be written with just a few additions to the following implementation.

The "if (nv == p) continue;" part in the implementation below is a common pruning technique in tree traversal. This pruning helps to explore the tree without backtracking from leaves to the root during traversal.

```cpp
using Graph = vector<vector<int> >;
Graph G;

// v は現在見ている頂点, p は v の親
void dfs(int v, int p ) {
  for (auto nv : G[v]) {
    if (nv == p) continue;  // これがツリー探索で一般的な書き方
    dfs(nv, v);
  }
}

int main() {
  int root = 0;
  dfs(root, -1); // root の親はいないので -1
}
```

<!-- ### 今回のツリー探索関数
今回のツリー探索は「色を塗る」という目的があるので、それに沿った設計にする。

下のように、再帰関数の引数に色を表す変数 c を付け加えてあげて、「次のノードを再帰的に呼び出す」というのをするときに

* エッジの重みが偶数だったら、次のノードも同色 c で塗る
* エッジの重みが奇数だったら、次のノードは異色 1-c で塗る

という風にすれば OK。 -->

### Tree Traversal Function for this Task
Since the purpose of this tree traversal is to "color the nodes," the design should align with that objective.

To achieve this, we can add a variable `c` representing the color to the arguments of the recursive function. When recursively calling the next node, we can follow these rules:

* If the weight of the edge is even, color the next node with the same color `c`.
* If the weight of the edge is odd, color the next node with a different color `1-c`.

Following these rules should suffice.

```cpp
// 入力
Graph G;

// res は答え
vector<int> res;

// c: 0 か 1 か。v を c に塗る
void dfs(int v, int p, int c) {
    res[v] = c;
    for (auto e : G[v]) {
        if (e.first == p) continue;
        if (e.second & 1) dfs(e.first, v, 1-c);
        else dfs(e.first, v, c);
    }
}
```

<!-- ### コード

以上をまとめて O(N) の計算時間でできる。 -->

### Code

All of the above can be summarized and implemented in O(N) computational time.

```cpp
#include <iostream>
#include <vector>
using namespace std;

using Edge = pair<int,int>;
using Graph = vector<vector<Edge> >;

// 入力
int N;
Graph G;

// res は答え
vector<int> res;

// v を c に塗る。p は v の親
void dfs(int v, int p, int c) {
    res[v] = c;
    for (auto e : G[v]) {
        if (e.first == p) continue;
        if (e.second & 1) dfs(e.first, v, 1-c);
        else dfs(e.first, v, c);
    }
}

int main() {
    cin >> N;
    G.assign(N, vector<Edge>());
    for (int i = 0; i < N-1; ++i) {
        int u, v, w; cin >> u >> v >> w;
        --u, --v;
        G[u].push_back(Edge(v, w));
        G[v].push_back(Edge(u, w));
    }
    res.assign(N, 0);
    dfs(0, -1, 1);
    for (auto v : res) cout << v << endl;
}
```