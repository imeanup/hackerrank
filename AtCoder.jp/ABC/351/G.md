# G - Hash on Tree

<!-- この問題はいくつかの解法がありますが、この解説では **Static top tree** と呼ばれるデータ構造を利用した $O((N+Q)\log N)$ 解法を説明します。

## 目標 : 木 DP をセグ木に載せる !?

はじめに、この問題を解くためにはどのような操作が必要となるかを考えてみます。

まず、この問題をクエリあたり $O(N)$ の計算量で解くことを考えてみましょう。これは簡単で、典型的な木 DP を行えばよいです。すなわち、次のような $f(n)$ をボトムアップに計算するコードを書いて、$A$ を更新するたびに毎回 (頂点 $0$ を根として) `calc_dp(0)` を呼び出せばよいです。しかしながらこの方法では $O(NQ)$ の計算量がかかり TLE してしまいます。


さて、この問題は次の 2 種類のクエリを処理する問題とみなすことが出来ます。

> #### 問題をクエリ形式で言い換えたもの
>
> * $N$ 頂点の根付き木と数列 $(A_1, A_2, \cdots, A_N)$ が与えられる。次の $2$ 種類のクエリを処理
>   * $A_v$ の値を $x$ に更新
>   * 上記の木 DP を計算して、$f(1)$ を出力

つまり、この問題は木 DP に関して「頂点の値を更新」「全体の値を取得」という 2 種類のクエリを要求しています。
このような形式の問題は木においては珍しいですが、列に関する問題では頻出なのは皆さんもご存じの通りかと思います。 -->

This problem has several solutions, but in this explanation, I will describe an $O((N+Q)\log N)$ solution using a data structure called **Static top tree**.

## Goal: Embedding Tree DP into Segment Tree!?

First, let's think about what operations are needed to solve this problem.

First, let's consider solving this problem with a computational complexity of $O(N)$ per query. This is simple, as you can perform the typical tree DP. That is, you can write code to calculate $f(n)$ (bottom-up) as follows, and call `calc_dp(0)` each time $A$ is updated (with vertex $0$ as the root). However, this approach takes $O(NQ)$ computation time and results in TLE (Time Limit Exceeded).

```cpp
using mint = atcoder::modint998244353;

vector<vector<int>> g; // Adjacency list of the rooted tree
mint A[n_max];
mint calc_dp(int v) {
  if(g[v].empty()) return A[v];
  mint prod = 1;
  for(auto& child : g[v]) prod *= calc_dp(child);
  return A[v] + prod;
}
```

Now, this problem can be viewed as a problem of handling the following two types of queries.

> #### Problem rephrased in query format
>
> * Given a rooted tree with $N$ vertices and a sequence $(A_1, A_2, \cdots, A_N)$. Process the following $2$ types of queries:
>   * Update the value of $A_v$ to $x$.
>   * Compute the above tree DP and output $f(1)$.

In other words, this problem demands two types of queries regarding tree DP: "update the value of a vertex" and "retrieve the overall value." While such problems are rare in trees, they are common in problems involving sequences.

<!-- > #### 典型的な列の問題
>
> * 列 $A_1, A_2, \cdot, A_N$ が与えられる。次の 2 種類のクエリを処理
>   * $A_i$ の値を $x$ に更新
>   * $A_1 \oplus A_2 \oplus \cdot \oplus A_N$ を計算 ($\oplus$ は何らかのモノイド和)

列の問題は、セグメント木を利用することでクエリあたり $O(\log N)$ で高速に処理することができるようになります。また、木の場合でもクエリが列に関するクエリに帰着できる場合は (例 : パス上の頂点に載っているモノイドの和) 、重軽分解とセグメント木を組み合わせて処理することが出来ます。

一方、元の問題は、木 DP を計算する過程をデータ構造とみなした時に、木 DP の 1 点更新・全体取得に相当する操作が要求されています。この問題はいわば、「木 DP をセグメント木に載せる」ような処理が求められているとも言えるでしょう。(当然ですが通常のセグメント木には載りません)

では、木 DP をどのようにしてセグメント木状のデータ構造に載せればよいかを考えてみることにします。

## 考察 1 : 完全二分木の場合の解法

簡単なコーナーケースとして、根付き木が完全二分木の場合に問題を解く方法を考えてみましょう。

上述した木 DP を付け焼き刃的に高速化する方法として次のようなコードが考えられます。


コードの概要を説明します。 まず、あらかじめ前計算で $f(1), f(2), \cdots , f(n)$ の値をメモしておきます。そして、`A[v]` の値を更新したときに $f(n)$ の値が変わるのは $v$ および $v$ の祖先の頂点だけなので、それ以外の頂点に関する情報は前計算したものを使用しながら、$v$ の祖先の情報をボトムアップに再計算するというものです。

この解法は特定のケースに対しては非常に高速に動作するようになります。それが根付き木が完全二分木である場合です。完全二分木は深さが $O(\log N)$ であり、各頂点の子が高々 $2$ 個しかなく各頂点の再計算も $O(1)$ で済むため、クエリあたり $O(\log N)$ で DP の結果を再計算することが出来ます。

もちろん、一般の木ではこの解法は最悪計算量が $O(NQ)$ のままで改善できていません。具体的には、

* 深さが最悪 $O(N)$ である
* $1$ つの頂点が持つ子の個数が最悪 $O(N)$ である

という 2 つの要因により最悪計算量がクエリあたり $O(N)$ のままです。この解法を応用するためには、一般の木の持つ上記の 2 つの性質をクリアするような、何らかの深さが $O(\log N)$ の二分木に変換する必要がありそうです。 -->

> #### Typical Sequence Problem
>
> * Given a sequence $A_1, A_2, \cdots, A_N$. Process the following 2 types of queries:
>   * Update the value of $A_i$ to $x$.
>   * Compute $A_1 \oplus A_2 \oplus \cdots \oplus A_N$ ($\oplus$ denotes some monoid operation).

Sequence problems can be efficiently handled per query in $O(\log N)$ time using segment trees. Additionally, in the case of trees, if queries can be reduced to queries regarding sequences (e.g., the sum of monoids on vertices along a path), you can combine heavy-light decomposition (HLD) with segment trees to process them.

On the other hand, in the original problem, when considering the process of computing tree DP as a data structure, operations equivalent to updating a single point and retrieving the entire tree DP are required. One could say this problem essentially demands "embedding Tree DP into a segment tree" (although, naturally, it wouldn't fit onto a standard segment tree).

So, let's think about how to embed tree DP into a data structure resembling a segment tree.

## Consideration 1: Solution for the Case of Complete Binary Trees

As a simple corner case, let's consider how to solve the problem when the rooted tree is a complete binary tree.

As a method to hastily speed up the previously mentioned tree DP, the following code can be considered:

[Code]

```cpp
using mint = atcoder::modint998244353;

vector<vector<int>> g; // Adjacency list of the rooted tree
vector<int> P;         // Parent vertex (with P[0] = -1)
mint A[n_max], f[n_max];
mint precalc(int v) {
  if(g[v].empty()) return f[v] = A[v];
  mint prod = 1;
  for(auto& child : g[v]) prod *= precalc(child);
  return f[v] = A[v] + prod;
}

void update(int v, mint x) {
  A[v] = x;
  for(; v != -1; v = P[v]) {
    if(g[v].empty()) f[v] = A[v];
    mint prod = 1;
    for(auto& child : g[v]) prod *= f[child];
    f[v] = A[v] + prod;
  }
}
```

Let me explain the outline of the code. First, precompute and memoize the values of $f(1), f(2), \cdots , f(n)$. Then, when the value of `A[v]` is updated, the only vertices whose $f(n)$ value changes are $v$ and its ancestors. Therefore, for vertices other than these, use the precomputed information, and recalculate the information of ancestors of $v$ bottom-up.

This solution works very fast for specific cases, namely when the rooted tree is a complete binary tree. Complete binary trees have a depth of $O(\log N)$, each vertex has at most $2$ children, and the recalculation of each vertex is $O(1)$, so you can recalculate the DP result per query in $O(\log N)$.

Of course, for a general tree, this solution does not improve the worst-case time complexity, which remains $O(NQ)$ due to two factors:

* The depth could be as bad as $O(N)$.
* Each vertex could have as many as $O(N)$ children.

So, to apply this solution, it seems necessary to convert the general tree into some binary tree with depth $O(\log N)$, satisfying the above two properties.

<!-- ## 考察 2 : 木の分解と木 DP の関係性

考察を発展させるために、木 DP を別の角度から解釈してみます。実は、木 DP は実は「部分木をマージして根付き木を生成する過程に情報を載せたもの」と捉えることが出来ます。今からこのことを説明します。

マージにより木を生成する過程を考えるには、その逆、木を分解する過程を考えるのが有用です。そこではじめに木を分解する過程を説明します。
次の (1) ～ (3) を木から辺が無くなるまで再帰的に繰り返すことで、根付き木を頂点と辺に分解することができます。(下図も参照してください)

* (1) 根の頂点を取り除く。ただし根に隣接する辺は取り除かず、そのような辺は「情報を持たない頂点」を端点の一方に持つものとみなす。 (このような頂点を以降では **virtual な頂点** と呼ぶ。)
* (2) virtual な頂点で集約されている部分木たちを、virtual な頂点を分裂させることで分割する。
* (3) 各部分木の virtual な頂点および virtual な頂点に隣接する辺を取り除く。部分木は再び通常の根付き木になる。

![image1](https://img.atcoder.jp/abc351/1d95833aa7c30d78e72209d7a205a8f1.jpg)

この操作手順を逆順に行っていくことで、部分木がだんだんとマージされていき最終的に 1 つの根付き木を得ることが出来ます。
マージする過程を関数として表してみましょう。次の 4 種類の関数を定義します。以降では、頂点は情報を持ち区別できるが、辺同士は情報を持たず区別できないものとします。

* `vertex(v)` : 頂点 $v$ を生成する関数。
* `add_vertex(t, v)` : (1) の逆手順を行う関数。つまり、根が virtual な木 $t$ の根に $v$ を代入する関数。
* `merge(x, y)` : (2) の逆手順を行う関数。つまり、virtual な根を持つ 2 つの木 $x, y$ を 1 つにする関数。
* `add_edge(t)` : (3) の逆手順を行う関数。つまり、根付き木 $t$ に virtual な根を生やす関数。

そして、関数 `generate_tree(v)` を、隣接リスト $g$ が表す根付き木の頂点 $v$ を根とする部分木を生成する関数とします。すると、`generate_tree(v)` は次のようになります。

この部分木をマージして新たな部分木を生成する手順は木 DP の手順と一致しています。例えば先に上げた木 DP は、抽象化することで次のように書き換えられます。


`generate_tree(v)` 関数と `calc_dp(v)` 関数の 2 つが全く同じ形をしていることが注視すれば確認できると思います。

このような視点から考察すると、木 DP は部分木のマージ過程に情報を載せたものとして解釈できます。詳しく説明すると次のようになります。

* 葉の頂点からスタートして「頂点の追加」「辺の追加」「根が virtual な根付き木同士のマージ」という 3 種類の操作を繰り返して部分木をマージしていくことを考える。
* マージする過程で生成される部分木全てに対して、部分木に関連する何らかの情報を定義する。
* そして、情報同士をマージする関数を適切に定義することで、部分木のマージによって新たに生成される部分木に対応する情報を計算することができる。

さて、今までの話をまとめると次のようになります。

* 木が深さ $O(\log N)$ の二分木であれば$O(\log N)$ で木 DP を再計算できる
* 一般の木は次の 2 つの特徴を持ち、これが効率的な再計算を阻害する
  * 深さが最悪 $O(N)$ である
  * $1$ つの頂点が持つ子の個数が最悪 $O(N)$ である
* ところで木 DP は部分木をマージする過程に情報を載せたものである
  * 部分木をマージする過程は、木を分解する過程の逆を辿ることで生成できる

この 2 つの事実から次の帰結を得ることが出来ます。

* 深さが $O(\log N)$ で二分木状である部分木のマージ過程を生成できれば、それを辿ることで効率よく木 DP を再計算できる？

このような木のマージ手順を実現したものが **Static top tree** になります。 -->

## Consideration 2: Relationship Between Tree Decomposition and Tree DP

To further develop our analysis, let's interpret tree DP from another perspective. In fact, tree DP can be understood as a process of "embedding information into the process of merging subtrees to generate a rooted tree." Let me explain this.

To understand the process of generating a tree through merging, it's useful to consider the reverse process: decomposing a tree. Here's how you can decompose a rooted tree into vertices and edges until there are no edges left, recursively repeating steps (1) to (3) (refer to the diagram below as well):

* (1) Remove the root vertex. However, do not remove edges adjacent to the root, and consider such edges as having a "vertex with no information" as one of their endpoints. (I'll refer to such vertices as **virtual vertices** from now on.)
* (2) Divide the subtrees aggregated at virtual vertices by splitting the virtual vertex.
* (3) Remove each virtual vertex and the edges adjacent to it. The subtrees become regular rooted trees again.

![image1](https://img.atcoder.jp/abc351/1d95833aa7c30d78e72209d7a205a8f1.jpg)

By performing these operations in reverse order, subtrees gradually merge, eventually obtaining a single rooted tree. Let's represent the merging process as functions. We define the following four types of functions. From now on, vertices can have distinguishable information, but edges cannot.

* `vertex(v)`: A function to generate vertex $v$.
* `add_vertex(t, v)`: A function to perform the reverse of step (1), i.e., assigning $v$ to the root of the virtual tree $t$.
* `merge(x, y)`: A function to perform the reverse of step (2), i.e., merging two trees $x$ and $y$ with virtual roots into one.
* `add_edge(t)`: A function to perform the reverse of step (3), i.e., adding a virtual root to the rooted tree $t$.

Then, let's define the function `generate_tree(v)` as a function to generate a subtree with vertex $v$ as the root, representing the rooted tree represented by the adjacency list $g$. So, `generate_tree(v)` becomes as follows:

[Function]

```cpp
vector<vector<int>> g; // Adjacency list of the rooted tree

Tree generate_tree(int v) {
  if(g[v].empty()) return vertex(v);
  vector<Tree> children;
  for(auto& child : g[v]) {
    Tree t = generate_tree(child);
    children.push_back(add_edge(t));
  }
  Tree t = children[0];
  for(int i = 1; i < (int)children.size(); i++) {
    t = merge(t, children[i]);
  }
  return add_vertex(t, v);
}
```

The process of generating a new subtree by merging these subtrees aligns with the steps of tree DP. For example, the previously mentioned tree DP can be abstracted and rewritten as follows:

[Code]

```cpp
using mint = atcoder::modint998244353;

using T = mint;
T vertex(int v) { return A[v]; }
T add_vertex(T x, int v) { return x + A[v]; }
T merge(T x, T y) { return x * y; }
T add_edge(T x) { return x; } 

vector<vector<int>> g; // Adjacency list of the rooted tree

T calc_dp(int v) {
  if(g[v].empty()) return vertex(v);
  vector<T> children;
  for(auto& child : g[v]) {
    T t = calc_dp(child);
    children.push_back(add_edge(t));
  }
  T t = children[0];
  for(int i = 1; i < (int)children.size(); i++) {
    t = merge(t, children[i]);
  }
  return add_vertex(t, v);
}
```

By observing that the functions `generate_tree(v)` and `calc_dp(v)` have exactly the same structure, we can confirm this similarity.

From this perspective, tree DP can be interpreted as embedding information into the process of merging subtrees. In detail:

* Start from leaf vertices and consider "adding vertices," "adding edges," and "merging trees with virtual roots" as three types of operations, repeating them to merge subtrees.
* Define some information related to each subtree generated during the merging process.
* Then, by appropriately defining a function to merge information, you can calculate the information corresponding to the subtree newly generated by merging subtrees.

Now, summarizing what we've discussed:

* If the tree has depth $O(\log N)$ like a binary tree, we can recalculate tree DP in $O(\log N)$.
* For general trees, two characteristics hinder efficient recalculation:
  * The depth could be as bad as $O(N)$.
  * Each vertex could have as many as $O(N)$ children.
* However, tree DP is essentially embedding information into the process of merging subtrees.
  * The process of merging subtrees can be generated by tracing the reverse of the process of decomposing the tree.

From these two facts, we can draw the following conclusion:

* If we can generate the merging process of subtrees that has depth $O(\log N)$ and resembles a binary tree, can we efficiently recalculate tree DP by following it?

The realization of such a merging procedure for trees is the **Static top tree**.

<!--
## Static top tree

#### 注意 : Static top tree は Top tree の名を冠していますが、(狭義の) Top tree とは全く構造が異なるデータ構造です。Top tree を勉強したい方は混同しないようご注意ください。

* より正確には、Static top tree は「Link/Cut tree の normal edge が持つ情報を Splay tree でまとめ上げることで出来る、Top tree の機能のほとんどを代替できるデータ構造」(広義の Top tree) を static にしたものです。
  * なお、(狭義の) Top tree を static にすることで Static top tree を構成することも可能で、そのようなデータ構造を Static top tree と呼ぶ人もいます。ここでは説明を割愛しますが、興味がある方は [tatyam さんの実装およびコメント](https://atcoder.jp/contests/joisp2024/submissions/51887735) を参考にしてください。

Static top tree とは、「部分木をマージする過程を表した深さ $O(\log N)$ の二分木」です。(正確には「部分木」ではない。後述)

Static top tree を構成する方法を説明するために、まずはマージする過程の逆、木を分解する手順を説明します。
はじめに木を重軽分解して各辺に heavy edge, light edge を割り当てます。(重軽分解を知らない方は [ABC269 Ex の解説](https://atcoder.jp/contests/abc269/editorial/4838) を参考にしてください。)
そして、次の (1) ～ (4) を木から辺が無くなるまで再帰的に繰り返します。(先に挙げた分解の手順と異なる部分を **太字** で表しています。図も参照してください)

* (1) **根につながる heavy path を選び、そこから heavy edge を取り除く。**
* (2) 根の頂点を取り除く。ただし根に隣接する辺は取り除かず、そのような辺は virtual な頂点を端点の一方に持つものとみなす。
* (3) virtual な頂点で集約されている部分木たちを、virtual な頂点を分裂させることで分割する。
* (4) 各部分木の virtual な頂点および virtual な頂点に隣接する **light edge** を取り除く。部分木は再び通常の根付き木になる。

![image2](https://img.atcoder.jp/abc351/95bc2ae83181f951e9075e0a87619777.jpg)

ここで注記しておく点として、分解の過程で登場するグラフは根付き木の部分木に限らないという点が挙げられます。というのも、(1) の手順で辺を取り除く時に、辺を取り除く順番によっては途中で 「根付き木と呼べないもの」が発生するからです。そのため、以降では Top tree の用語を借りて、分解の過程で得られるグラフを **cluster** と呼ぶことにします。

図を見ると分かる通り、木を分解する過程において次の 2 種類の cluster が生成されます。

* virtual でない頂点を根とする部分木が $0$ 本以上の heavy edge でパス状につながってできる cluster
* virtual な頂点を根とする部分木の形をした cluster

こちらも Top tree の用語を借りて、前者を **path cluster** 、後者を **point cluster** と呼ぶことにします。(根につながる heavy edge が存在しない path cluster は path とは少し呼びづらいですが、ここでは気にしないことにします)

![image3](https://img.atcoder.jp/abc351/09f981f7cf3fcbb45f0be32b2fd1f0e0.png)

次に、分解する手順を逆順に辿ることで cluster を二分木状にマージしていくことを考えます。 分解する過程において、cluster 同士の merge は「path cluster 同士の merge」「point cluster 同士の merge 」の 2 種類が発生します。これもまた Top tree の用語を借りて、path cluster 同士の merge を **compress** 、point cluster 同士の merge を **rake** と呼ぶことにします。

さて、cluster を二分木状にマージする際に一工夫を入れることで深さを $O(\log N)$ に抑えるのが Static top tree のポイントです。とはいえ一工夫入れると言っても (2), (4) の逆手順は工夫の入れようがないので、工夫を入れる余地があるのは

* (1) 根につながる heavy path を選び、そこから heavy edge を取り除く。
* (3) virtual な頂点で集約されている部分木たちを、virtual な頂点を分裂させることで分割する。

の逆手順です。これらは直感的には次の戦略に従って cluster をマージしていくのが良さそうです。

* (1) の逆手順 : path cluster を compress でマージしていく時に、マージ過程が完全二分木状になるようにマージする
* (3) の逆手順 : point cluster を rake でマージしていく時に、マージ過程が完全二分木状になるようにマージする

これは非常に合理的な戦略です。なぜならば、一般の木が持つ効率的な再計算を阻害する 2 つの性質は

* 深さが最悪 $O(N)$ である
* $1$ つの頂点が持つ子の個数が最悪 $O(N)$ である 

という 2 つでしたが、前者を compress によるマージが、後者を rake によるマージが解消することになるからです。
しかしながら、この戦略は最悪ケースで木の深さが $O(\log^2 N)$ になってしまいます。(詳細は略します。重軽分解 + セグメント木でパスクエリを処理する際に自然な実装だと worst $O(\log^2 N)$ かかるのと同じ理屈です。)

-->

## Static Top Tree

#### Note: Static top tree bears the name "Top tree," but it is a completely different data structure from (narrowly defined) Top tree. Please be careful not to confuse them if you're interested in learning about Top trees.

More precisely, the Static top tree is a static version of the "Top tree," which is created by aggregating the information carried by the normal edges of a Link/Cut tree with a Splay tree and can substitute for most functionalities of the Top tree. (This is broadly defined as a Top tree).

- Additionally, by making (narrowly defined) Top tree static, it's also possible to construct the Static top tree, and some refer to such a data structure as the Static top tree. I'll skip explaining this here, but if you're interested, you can refer to [tatyam&#39;s implementation and comments](https://atcoder.jp/contests/joisp2024/submissions/51887735).

The Static top tree is a "binary tree of depth $O(\log N)$" representing the process of merging subtrees. (It's not precisely a "subtree." More on this later.)

To explain how to construct a Static top tree, let's first describe the reverse process of merging, which is the process of decomposing a tree.

- Start by Heavy-Light Decomposition to assign heavy and light edges to each edge in the tree. (For those unfamiliar with Heavy-Light Decomposition, please refer to the explanation in [ABC269 Ex](https://atcoder.jp/contests/abc269/editorial/4838).)
- Then, recursively repeat steps (1) to (4) until there are no edges left in the tree. (The steps are different from those mentioned earlier and are highlighted in **bold**. Please also refer to the diagram.)

* (1) **Select a heavy path connected to the root and remove heavy edges from there.**
* (2) Remove the root vertex. However, do not remove edges adjacent to the root, and consider such edges as having a virtual vertex as one of their endpoints.
* (3) Divide the subtrees aggregated at virtual vertices by splitting the virtual vertex.
* (4) Remove each virtual vertex and the **light edges** adjacent to it. The subtrees become regular rooted trees again.

![image2](https://img.atcoder.jp/abc351/95bc2ae83181f951e9075e0a87619777.jpg)

It's important to note that the graphs appearing in the decomposition process are not limited to subtrees of the rooted tree. This is because, when removing edges in step (1), you can end up with something that's not a "rooted tree" depending on the order of edge removals. Therefore, borrowing the terminology from the Top tree, we'll refer to the graphs obtained in the decomposition process as **clusters**.

As you can see in the diagram, two types of clusters are generated during the process of decomposing the tree:

* clusters consisting of heavy paths connected to non-virtual vertices, which are formed by one or more heavy edges
* clusters shaped like subtrees with a virtual vertex as the root

Also borrowing from the terminology of the Top tree, we'll call the former **path clusters** and the latter **point clusters**. (It might be a bit awkward to call a path cluster without heavy edges a path, but we'll overlook this here.)

![image3](https://img.atcoder.jp/abc351/09f981f7cf3fcbb45f0be32b2fd1f0e0.png)

Next, let's consider merging clusters into a binary tree by retracing the decomposition process in reverse. In the decomposition process, merging clusters results in two types of merges: merging path clusters and merging point clusters. Again borrowing from the Top tree terminology, we'll call merging path clusters **compress** and merging point clusters **rake**.

Now, the key to the Static top tree is to keep the depth to $O(\log N)$ by adding a little trick while merging clusters. Although there's not much room for improvement in steps (2) and (4) of the reverse process, we can make improvements in

* (1) Selecting a heavy path connected to the root and removing heavy edges from there.
* (3) Dividing the subtrees aggregated at virtual vertices by splitting the virtual vertex.

Intuitively, the strategy for merging clusters following these steps seems to be:

* Reversing step (1): When merging path clusters with compress, ensure that the merging process forms a complete binary tree.
* Reversing step (3): When merging point clusters with rake, ensure that the merging process forms a complete binary tree.

This strategy is quite reasonable because it resolves the two properties that hinder efficient recalculation of general trees:

* The depth could be as bad as $O(N)$.
* Each vertex could have as many as $O(N)$ children.

However, this strategy might result in a depth of $O(\log^2 N)$ in the worst-case scenario. (Details are omitted here. It's similar to implementing path queries with Heavy-Light Decomposition + Segment Tree, which takes worst $O(\log^2 N)$ time. )

<!-- そこで、さらにもう一工夫します。cluster を完全二分木状になるようにマージするとは、言い換えると「左右の子の含む cluster の個数ができるだけ等しくなるようにマージする」という操作になります。これを少し変更して、「cluster が含む頂点数ができるだけ左の子と右の子で等しくなるようにマージする」ということにします。実は、そのようにすることでマージ過程全体を表す木の深さを $O(\log N)$ に抑えられることが証明できます。(こちらも詳細は略します。重軽分解 + セグメント木でパスクエリを処理する際に少し工夫すると worst $O(\log N)$ になるのと同じ理屈です。参考 : [Nachia さんの記事](https://www.mathenachia.blog/mergetech-and-logn/), [errorgorn さんの記事の “Balanced HLD” の項](https://codeforces.com/blog/entry/104997))

以上の方法により、cluster をマージする過程を深さ $O(\log N)$ の二分木で表すことが出来ました。

[実装例(5 行目～ 74 行目)](https://atcoder.jp/contests/abc351/submissions/52777033) : 実装の際は maspy さんと tatyam さんの実装を参考にしました。

## 元の問題の解法

さて、Static top tree を使用して元の問題を解く方法を説明します。
cluster をマージする過程で必要なのは次の 5 種類の関数です。

* `vertex(v)` : 頂点 $v$ のみからなる path cluster を生成する関数。
* `compress(p, c)` : (1) の逆手順を行う関数。つまり、path cluster $p, c$ ($p$ が根に近い側にある) をマージする関数。
* `add_vertex(t, v)` : (2) の逆手順を行う関数。つまり、point cluster $t$ の根に頂点 $v$ を代入して path cluster にする関数。
* `rake(x, y)` : (3) の逆手順を行う関数。つまり、point cluster $x, y$ をマージする関数。
* `add_edge(t)` : (4) の逆手順を行う関数。つまり、path cluster $t$ に virtual な根を生やして point cluster にする関数。

木 DP を行う時と同様に、木に載せる情報を定義して、これら 5 種類の関数に対応する DP の遷移を構成することでこの問題を解くことが出来ます。

この中で一番難しいのは path cluster 同士のマージである compress です。なぜならば、point cluster は木 DP における部分木と対応しているため、木 DP 同様の情報を載せて rake でも同様の遷移を実装すれば基本的にどうにかなる一方、path cluster 同士のマージは「変な形をした何か」同士のマージになるからです。

ここで、cluster の外部との接点を、Top tree の用語を借りて **boundary vertex** と呼ぶことにします。path cluster は基本的に「根に近い方の boundary vertex」「根から遠い方の boundary vertex」という 2 つの boundary vertex を持ちます。(path cluster が根付き木の場合は例外で、2 つの boundary vertex が同一の頂点になります。) 問題によっては、この 2 つの boundary vertex に注目することで DP の遷移を構成しやすくなります。

適切な観察により、path cluster は「根から遠い方の boundary vertex にハッシュ値が $x$ である根付き木が結合した時に、根に近い方の boundary vertex を根とする根付き木のハッシュ値は $ax+b$ になる」となる値 $(a, b)$ を持てば良いことがわかります。このように path cluster に載せる情報を定義すると compress はアフィン関数の合成として定義することが出来ます。その他の関数も適切な考察により次のような関数を実装すればよいことがわかります。


Static top tree を適切に抽象化すれば、基本的に上の 5 種類の関数を実装するだけで問題を解くことが出来るようになります。これはセグメント木が 2 種類の関数を実装すれば使えるのに似ていますね。

* 余談ですが、セグメント木は当初は完全二分木に限らず平衡な二分木全般に対するアルゴリズムとして定義されていたようです。([参考](https://kmyk.github.io/blog/blog/2020/03/04/segment-tree-is-not-complete-binary-tree/))このような解釈に則ると、Static top tree を用いた木 DP の更新はセグメント木の類似と捉えることができそうです。

後はクエリを処理する関数を実装すればよく、これは DP を計算・更新する過程を適切に実装すればよいです。

[実装例(76 行目～ 134 行目)](https://atcoder.jp/contests/abc351/submissions/52777033) -->

So, let's take it a step further. Merging clusters into a complete binary tree can be rephrased as an operation where "the number of clusters contained in the left and right children is made as equal as possible." Let's tweak this a bit to ensure that "the number of vertices contained in the clusters is made as equal as possible between the left and right children." In fact, by doing so, we can prove that the depth of the tree representing the entire merging process can be kept to $O(\log N)$. (I'll omit the details here, but it's similar reasoning to how tweaking Heavy-Light Decomposition + Segment Tree can lead to worst-case $O(\log N)$. For reference: [Nachia&#39;s article](https://www.mathenachia.blog/mergetech-and-logn/), [the &#34;Balanced HLD&#34; section of errorgorn&#39;s article](https://codeforces.com/blog/entry/104997))

With the above methods, we have managed to represent the merging process of clusters with a binary tree of depth $O(\log N)$.

[Implementation example (lines 5 to 74)](https://atcoder.jp/contests/abc351/submissions/52777033): When implementing, I referred to implementations by maspy and tatyam.

## Solution to the Original Problem

Now, let's explain how to solve the original problem using Static top tree.

During the merging process of clusters, we need the following 5 types of functions:

- `vertex(v)`: A function that generates a path cluster consisting only of vertex $v$.
- `compress(p, c)`: A function that performs the reverse of step (1). That is, it merges path clusters $p$ and $c$ (with $p$ closer to the root).
- `add_vertex(t, v)`: A function that performs the reverse of step (2). That is, it assigns vertex $v$ to the root of point cluster $t$ to create a path cluster.
- `rake(x, y)`: A function that performs the reverse of step (3). That is, it merges point clusters $x$ and $y$.
- `add_edge(t)`: A function that performs the reverse of step (4). That is, it adds a virtual root to path cluster $t$ to create a point cluster.

Similar to when performing tree DP, define the information carried by the tree, and by constructing DP transitions corresponding to these 5 functions, we can solve the problem.

Among these, the most challenging one is compress, which merges path clusters. The reason is that while point clusters correspond to subtrees in tree DP, allowing for straightforward implementations of DP transitions even with rake, merging path clusters involves merging "something in a strange shape."

Here, let's call the points of contact between a cluster and the outside as **boundary vertices**, borrowing the terminology from the Top tree. Essentially, a path cluster has two boundary vertices: "the boundary vertex closer to the root" and "the boundary vertex farther from the root." (There's an exception when the path cluster is a rooted tree, in which case the two boundary vertices coincide.) Depending on the problem, focusing on these two boundary vertices can make it easier to construct DP transitions.

Through appropriate observations, we realize that a path cluster only needs to possess a value $(a, b)$ such that, when a rooted tree with a hash value $x$ at the boundary vertex farther from the root is joined, the hash value of the rooted tree with the boundary vertex closer to the root as the root becomes $ax + b$. Defining information on the path cluster in this way allows compress to be defined as a composition of affine functions. By similar considerations, we can implement the other functions as well.

```cpp
using mint = atcoder::modint998244353;

vector<int> A;
struct Path {
  mint a, b;
};
using Point = mint;
Path vertex(int i) { return {1, A[i]}; }
Path compress(Path p, Path c) { return {p.a * c.a, p.a * c.b + p.b}; };
Point rake(Point l, Point r) { return l * r; };
Point add_edge(Path d) { return d.b; };
Path add_vertex(Point d, int i) { return {d, A[i]}; };
```

By abstracting Static top tree appropriately, we essentially need to implement the above 5 functions to solve the problem. This is akin to how a segment tree can be used with just 2 functions.

* As a side note, segment trees were initially defined as algorithms not just for complete binary trees but for balanced binary trees in general ([reference](https://kmyk.github.io/blog/blog/2020/03/04/segment-tree-is-not-complete-binary-tree/)). Following this interpretation, updates in tree DP using Static top tree could be seen as similar to segment trees.

The remaining task is to implement the functions for handling queries. This can be done by appropriately implementing the process of computing and updating DP.

[Implementation example (lines 76 to 134)](https://atcoder.jp/contests/abc351/submissions/52777033)

<!-- ## Static top tree の応用

Static top tree の応用例を簡単にまとめます。

この問題では初等的な DP を Static top tree に載せただけでしたが、木 DP は非常に様々な種類があります。どのような木 DP であっても、compress をうまく定義することができれば木 DP を Static top tree に載せることが出来ます。
例えば以下の 2 つの問題は元の問題とは毛色の異なる問題ですが、 どちらも Static top tree を利用すればクエリあたり $O(\log N)$ で処理することが出来ます。(練習問題として考えてみましょう)

> (木における最大独立集合) : $N$ 頂点の木がある。各頂点には `B`, `R`, `?` の 3 状態のいずれかが割り当てられている。次の 2 種類のクエリを処理
>
> * 頂点を 1 つ選んで状態を変更
> * 次の条件を全て満たす頂点の集合の最大サイズを出力
>   * 状態が `B` の頂点は集合に含まれる
>   * 状態が `R` の頂点は集合に含まれない
>   * 集合に含まれるどの 2 個の頂点も木上で隣り合っていてはならない

> (木の直径) : $N$ 頂点の辺重み付き木がある。次の 2 種類のクエリを処理
>
> * 辺を 1 本選んで重みを変更
> * 木の直径の長さ、および直径のうちどれか 1 つの両端点を取得
>   * ヒント : 辺重み付き木を Static top tree に載せる場合は「Static top tree を辺の情報も扱えるように改造する」「辺を頂点とみなした $2N-1$ 頂点のグラフを考える」という方法が考えられます(後者の方が追加実装が少なく済むため楽です)

高難度コンテストにおける Static top tree を適用可能な問題の出題例もいくつか載せておきます。


また、Static top tree をうまく利用すると、木 DP だけでなく全方位木 DP の 1 点更新が可能になります。具体的には次のような問題も解くことが出来ます。(詳細は略します)

> [SPOJ QTREE6](https://www.spoj.com/problems/QTREE6/) ：$N$ 頂点の木がある。各頂点は黒か白で塗られている。次の 2 種類のクエリを処理
>
> * 頂点を 1 個選んで色を反転
> * 頂点を 1 個選んで、その頂点と連結な頂点の個数を出力。ここで頂点 $u$ と頂点 $v$ が連結であるとは、頂点 $u$ から頂点 $v$ までのパス上の頂点 (両端点も含む) の色が全て一致していることを言う

Static top tree の用途は木 DP の更新の高速化だけではありません。
列に対する操作と木に対する操作の対比を考えてみましょう。Static top tree は列で言うところの「列をセグメント木状に分割する操作」に相当します。これらは深さが $O(\log N)$ の二分木状に全体をマージしていく木構造のデータ構造である点が共通しています。このような対比を考えると、列をセグメント木状に分割する操作を経て出来るアルゴリズムは、木でも同じことが出来ると予想されます。例えば今までに扱った「木 DP の 1 点更新」は「セグメント木の 1 点更新・全体取得」の木 version と言えます。
列をセグメント木状に分割する操作はセグメント木以外でも有用です。例えば、列の分割統治では列をセグメント木状に分割します。逆に言うと、Static top tree 上で分割統治をすることで木上の分割統治を行うことが出来る、ということになります。具体的には、Static top tree を利用すれば次の問題を $O(N \log^2 N)$ で解くことが出来ます。

> * [ABC269Ex Antichain](https://atcoder.jp/contests/abc269/tasks/abc269_h) : $N$ 頂点の根付き木がある。(頂点 $a$ が頂点 $b$ の子孫) $\iff (a \le b)$ となるように二項関係を定義する。$k = 1, 2, \cdots, N$ について、サイズ $k$ の Antichain の個数 $\mod 998244353$ を計算

> * [yukicoder No.2595 Parsing Challenge](https://yukicoder.me/problems/no/2595) : `1` ~ `9`, `+`, `-`, `*`, `(`, `)` からなる長さ $N$ の数式を計算 (ヒント : 構文木を考える)

このような観点から考えると、 Static top tree には「木 DP を 1 点更新」だけでなく幅広い用途があると考えられます。

さて、現代の競技プログラミングでは「平衡二分木」や「Link/Cut tree」はコンテストに出題されることはほとんどありませんが、これらの機能を制限して static にしたデータ構造である「セグメント木」や「重軽分解 + セグメント木」は主要なアルゴリズムの 1 つに数えられるほどにコンテストで出題されています。
Static top tree は短時間コンテストで tier 1 のアルゴリズムになることは無いと予想していますが、セグメント木と同様に抽象化すれば軽実装になるのは魅力的で、さらに載せる演算が少し非自明なのはいくらか面白味があるので、今後何かの拍子で Static top tree が Top tree 状のデータ構造の static 版として局所的にメジャーになることもあるかもしれませんね。 -->

## Applications of Static Top Trees

Let's briefly summarize some applications of Static top trees.

In this problem, we simply placed elementary DP on Static top trees, but tree DP comes in various types. Regardless of the type of tree DP, if we can define compress appropriately, we can place tree DP on Static top trees. For example, the following two problems have a different flavor from the original problem, but both can be processed in $O(\log N)$ per query using Static top trees. (Let's think of them as practice problems)

> (Maximum Independent Set in a Tree): Given a tree with $N$ vertices. Each vertex is assigned one of three states: `B`, `R`, or `?`. Process the following two types of queries:
>
> * Change the state of one vertex.
> * Output the maximum size of a set satisfying the following conditions:
>   * Vertices with state `B` are included in the set.
>   * Vertices with state `R` are not included in the set.
>   * No two vertices in the set are adjacent on the tree.

> (Diameter of a Tree): Given an edge-weighted tree with $N$ vertices. Process the following two types of queries:
>
> * Change the weight of one edge.
> * Obtain the length of the tree's diameter and one of its endpoints.
>   * Hint: If you want to place an edge-weighted tree on a Static top tree, you can consider "modifying Static top tree to handle edge information" or "considering a graph with $2N-1$ vertices, treating edges as vertices" (the latter requires fewer additional implementations and is easier).

Here are some examples of problems that can be tackled with Static top trees in high-difficulty contests.

<details><summary><b> Examples (UCup, JOI, CodeForces Div 1 Spolier)</b> </summary>

* [The 2nd Universal Cup. Stage 19 F: When Anton Saw This Task He Reacted With 😩](https://contest.ucup.ac/contest/1487/problem/8133)
* [JOI 2023/2024 Spring Camp: JOI Tour](https://atcoder.jp/contests/joisp2024/tasks/joisp2024_h)
* [CodeTON Round 8 H: Farmer John&#39;s Favorite Intern](https://codeforces.com/contest/1942/problem/H)

</details><br>

Moreover, using Static top trees efficiently enables one-point updates in all-dimensional tree DP. Specifically, you can solve problems like the following (details omitted):

> [SPOJ QTREE6](https://www.spoj.com/problems/QTREE6/): Given a tree with $N$ vertices. Each vertex is colored black or white. Process the following two types of queries:
>
> * Invert the color of one vertex.
> * Select one vertex and output the number of vertices connected to it. Two vertices $u$ and $v$ are connected if all vertices (including endpoints) on the path from vertex $u$ to vertex $v$ have the same color.

The utility of Static top trees isn't limited to speeding up tree DP updates. Let's consider the contrast between operations on sequences and operations on trees. In terms of sequences, Static top trees correspond to "splitting the sequence into segments like a segment tree." They share the common feature of merging the entire structure into a binary tree with depth $O(\log N)$. Considering this analogy, algorithms that can be achieved by splitting sequences into segment-tree-like structures should also be achievable on trees. For example, the "one-point update of tree DP" we've discussed so far can be viewed as the tree version of "one-point update and whole retrieval" of a segment tree.

Splitting sequences into segment-tree-like structures is useful not only with segment trees but also in other contexts. For instance, segmenting sequences is a common strategy in divide and conquer. Conversely, by performing divide and conquer on Static top trees, you can conduct divide and conquer on trees. Specifically, using Static top trees, you can solve the following problems in $O(N \log^2 N)$:

> * [ABC269Ex Antichain](https://atcoder.jp/contests/abc269/tasks/abc269_h): Given a rooted tree with $N$ vertices. Define a binary relation such that $a$ is an ancestor of $b$ if and only if $a \leq b$. For $k = 1, 2, \ldots, N$, compute the number of antichains of size $k$ modulo $998244353$.
> * [yukicoder No.2595 Parsing Challenge](https://yukicoder.me/problems/no/2595): Compute the result of a length $N$ expression consisting of `1` to `9`, `+`, `-`, `*`, `(`, `)` (Hint: Consider a syntax tree).

From this perspective, Static top trees have a wide range of applications beyond just one-point updates in tree DP.

In modern competitive programming, "balanced binary trees" or "Link/Cut trees" are rarely used in contests. However, static versions of these structures, such as "segment trees" or "Heavy-Light Decomposition + Segment trees," are frequently featured as key algorithms in contests. While I don't expect Static top trees to become tier 1 algorithms in short contests, their abstraction similar to segment trees is attractive, and the slightly non-trivial operations they support add some interesting flavor. Perhaps someday Static top trees will become locally popular as static versions of Top tree-like data structures.
