## G - Mediator

<!-- グラフ全体が常に森であるため、質問クエリに対して以下の事柄が言えます。

* もし $u$ と $v$ が異なる連結成分に属する場合、題意を満たす頂点は存在しない。
* $u$ と $v$ が同じ連結成分に属する場合は、以下が成立する。
  * その連結成分中の適当な頂点を根とした木を考える。
  * このとき、題意を満たす頂点 $w$ が存在すれば、「 $w$ は $u$ の親ノード」「 $w$ は $v$ の親ノード」の少なくとも一方が満たされる。

もしオフラインで解くことが許されるなら、クエリを先読みした上で最終的な全ての連結成分について適当に根を取って、各ノードについて親ノードを求めた上で、解の候補である高々 $2$ つのノードが正当であるか ( 辺 $u-w$, 辺 $v-w$ が質問クエリの時点で存在するか ) を調べることでこの問題に正解できます。

しかし、クエリが暗号化されているためクエリを先読みして解くことは難しいです。よって、オンラインでこの問題を解くことを考えましょう。

そこで、以下の **クエリ平方分割** と呼ばれる技法を活用します。

* クエリをサイズ $B$ ずつのブロックに分割する。
* 各ブロックを処理し始める際に、これまでのクエリ全体に関して時間計算量 $O(N)$ 程度の処理をかける。
* 各ブロックの範疇で、そのブロック内で生じた変更をクエリごとの時間計算量 $O(B)$ 程度で反映させる。
* その結果、全体の時間計算量は $O(\frac{NQ}{B} + BQ)$ となる。 $B = \sqrt{N}$ と選択することにより、 $O(Q \sqrt{N})$ を達成することができる。

#### 各ブロックの処理開始時の処理

それまでに追加された辺に関して森を構成します。そのもとで全ての連結成分について先ほどと同様に適当に根を取って親を求めておきます。
さらに、この時点でのグラフ $G_i$ について、どの頂点がどの連結成分にあるかも調べておきます。

#### 各ブロック内でのクエリの処理

辺の追加は、単に「この辺を追加した」と記憶しておきます。

質問クエリは、ブロック開始時の $G_i$ を見て、以下の場合分けを行います。

* $G_i$ 上で $u$ と $v$ とが同一の連結成分にある場合
  * 先ほど同様、題意を満たす頂点は $u$ の親ノードか $v$ の親ノードのどちらかです。
* $G_i$ 上で $u$ と $v$ とが異なる連結成分にある場合
  * もし題意を満たす頂点 $w$ が存在するなら、そのブロック内で $u-w$ 辺または $v-w$ 辺が追加されている必要があります。ブロック内の辺は高々 $B$ 本です。

以上を実装することでこの問題に時間計算量 $O(QN)$ で正解できます (が、自然な実装だと $\log$ が入るので、実装時間に気を遣わなかった場合は $B$ を調整して高速化する必要があるかもしれません。)

実装例 (C++): -->

The entire graph being always a forest, we can say the following regarding the query:

- If $u$ and $v$ belong to different connected components, there are no vertices satisfying the condition.
- If $u$ and $v$ belong to the same connected component, the following holds:
  - Consider a tree rooted at an arbitrary vertex in that connected component.
  - In this case, if there exists a vertex $w$ satisfying the condition, at least one of the following is true: "$w$ is the parent node of $u$" or "$w$ is the parent node of $v$".

If solving offline is allowed, you can preprocess the queries, choose appropriate roots for all final connected components after reading the queries in advance, determine parent nodes for each node, and check whether at most two nodes, which are candidates for the solution, are valid (whether the edges $u-w$ and $v-w$ exist at the time of the query). However, solving by preemptively reading the queries is difficult due to query encryption. Therefore, let's consider solving this problem online.

Here, we'll utilize a technique called query square root decomposition:

* Split the queries into blocks of size $B$.
* Start processing each block by applying processing of approximately $O(N)$ for all previous queries.
* Within the scope of each block, reflect the changes that occurred within that block with a time complexity of approximately $O(B)$ per query.
* As a result, the overall time complexity becomes $O(\frac{NQ}{B} + BQ)$. By choosing $B = \sqrt{N}$, we achieve $O(Q \sqrt{N})$.

#### Processing at the beginning of each block

Construct a forest considering the edges added so far. Under this, select appropriate roots and find parents for all connected components just like before. Additionally, examine which vertices belong to which connected component in the graph $G_i$ at this point.

#### Processing queries within each block

For added edges, simply remember "this edge was added".

For query queries, check the following cases based on $G_i$ at the beginning of the block:

- If $u$ and $v$ are in the same connected component in $G_i$:
  - As before, a vertex satisfying the condition is either the parent node of $u$ or the parent node of $v$.
- If $u$ and $v$ are in different connected components in $G_i$:
  - If there exists a vertex $w$ satisfying the condition, either the $u-w$ edge or the $v-w$ edge must have been added within that block. The edges within a block are at most $B$.

By implementing the above, you can correctly solve this problem with a time complexity of $O(QN)$ (though in a natural implementation, there might be a $\log$ factor, so if you're not careful about implementation time, you might need to adjust $B$ for optimization).

Example implementation (C++):

<details><summary><b>C++</b></summary>

```cpp
#include<bits/stdc++.h>
#include <atcoder/dsu>
#define mod 998244353

using namespace std;
using namespace atcoder;

using Graph=vector<vector<int>>;

int n,q;
Graph g;
vector<int> genpar(){
  vector<int> vis(n,0);
  vector<int> res(n,-1);
  queue<int> q;
  for(int i=0;i<n;i++){
    if(vis[i]){continue;}
    vis[i]=1;
    q.push(i);
    while(!q.empty()){
      int od=q.front(); q.pop();
      for(auto &nx : g[od]){
        if(vis[nx]==0){
          vis[nx]=1;
          res[nx]=od;
          q.push(nx);
        }
      }
    }
  }
  return res;
}

int b=2000;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cin >> n >> q;
  g.resize(n);

  vector<int> his={0};
  vector<int> cpar;
  vector<unordered_set<int>> st(n);
  dsu uf(n);
  vector<pair<int,int>> emem;

  for(int tr=0;tr<q;tr++){
    if(tr%b==0){
      cpar=genpar();
      for(auto &nx : emem){
        uf.merge(nx.first,nx.second);
      }
      emem.clear();
    }

    int a,b,c;
    long long ma,mb,mc;
    cin >> ma >> mb >> mc;

    ma*=(his.back()+1); ma%=mod; a=1+(ma%2);
    mb*=(his.back()+1); mb%=mod; b=1+(mb%n);
    mc*=(his.back()+1); mc%=mod; c=1+(mc%n);

    b--;c--;

    if(a==1){
      st[b].insert(c);
      st[c].insert(b);
      g[b].push_back(c);
      g[c].push_back(b);
      emem.push_back({b,c});
    }
    else{
      vector<int> cand;
      if(uf.same(b,c)){
        cand={cpar[b],cpar[c]};
      }
      else{
        for(auto &nx : emem){
          if(nx.first==b || nx.first==c){
            cand.push_back(nx.second);
          }
          if(nx.second==b || nx.second==c){
            cand.push_back(nx.first);
          }
        }
      }

      int oup=-1;
      for(auto &nx : cand){
        if(st[b].find(nx)==st[b].end()){continue;}
        if(st[c].find(nx)==st[c].end()){continue;}
        oup=nx;
      }

      oup++;
      cout << oup << "\n";
      his.push_back(oup);
    }
  }
  return 0;
}
```

</details><br>

---

<!-- 森に対して

* $u, v$ 間に辺を張る（森を保つ操作のみ行える）
* $u, v$ が同じ連結成分にあるかを調べる．同じ成分にある場合，$u$ から $v$ 方向に辺 $k$ 個分進む

といった操作は **Link Cut Tree** というデータ構造を用いて行える基本的な操作です．（Link：辺を張る操作のほかに，Cut：辺の削除も行えます）

したがって本問は Link Cut Tree を使えばすぐに解ける問題です．

Link Cut Tree は比較的実装が大変なデータ構造だということもあって，AtCoder 公式コンテストの想定解法になったことは私が知る限りありません（海外コンテスト等ではしばしば見かけます）が，興味があれば学んでみてください．

日本語文献では， -->

Here's the translation:

Operations such as adding an edge between $u$ and $v$ (while maintaining the forest structure) and checking whether $u$ and $v$ are in the same connected component can be performed using a data structure called **Link Cut Tree**. This data structure allows for basic operations such as linking (adding edges) and cutting (deleting edges).

Therefore, this problem can be solved immediately using Link Cut Tree.

Link Cut Tree is a relatively challenging data structure to implement, and as far as I know, it has not been a standard solution in AtCoder official contests (although it is often seen in international contests). However, if you're interested, I encourage you to learn more about it.

In Japanese literature,

<!-- * [プログラミングコンテストでのデータ構造 2 ～動的木辺～](https://www.slideshare.net/iwiwi/2-12188845) , iwiwi さん
* [かつっぱの木マスター養成講座](https://www.youtube.com/watch?v=sAN6hdpzhBE&ab_channel=%E3%81%8B%E3%81%A4%E3%81%A3%E3%81%B1%E7%AB%B6%E3%83%97%E3%83%AD), catupper さん
* [ei1333の日記, Link-Cut 木](https://ei1333.hateblo.jp/entry/2018/05/29/011140), ei1333さん
* [ei1333の日記, QTREE LCT + Dynamic Distance Sum](https://ei1333.hateblo.jp/entry/2019/07/09/005011), ei1333さん, いろいろな応用例の紹介

などが有名だと思います．いろいろな実装例を見たい場合には，Library Checker の Dynamic Tree シリーズ（[例](https://judge.yosupo.jp/problem/dynamic_tree_vertex_set_path_composite)）の提出などから探してみてください． -->

Here's the translation:

* [Data Structures 2 for Programming Contests: Dynamic Tree Edges](https://www.slideshare.net/iwiwi/2-12188845), by iwiwi
* [Catupper&#39;s Tree Master Training Course](https://www.youtube.com/watch?v=sAN6hdpzhBE&ab_channel=%E3%81%8B%E3%81%A4%E3%81%A3%E3%81%B1%E7%AB%B6%E3%83%97%E3%83%AD), by catupper
* [ei1333&#39;s Diary: Link-Cut Tree](https://ei1333.hateblo.jp/entry/2018/05/29/011140), by ei1333
* [ei1333&#39;s Diary: QTREE LCT + Dynamic Distance Sum](https://ei1333.hateblo.jp/entry/2019/07/09/005011), by ei1333, showcasing various applications

These are some well-known resources. If you want to see various implementation examples, you can explore submissions of the Dynamic Tree series on Library Checker ([example](https://judge.yosupo.jp/problem/dynamic_tree_vertex_set_path_composite)).

---

@keisuke6

<!-- 以下の解法について考えます。

---

* 隣接頂点を unordered_set で持つ隣接リストと、各頂点の連結状態を持つための Union-find を用意する。…(1)
* タイプ 1 のときは、隣接リスト / Union-find のそれぞれに辺を追加する。…(2)
* タイプ 2 のときは、頂点 $a, b$ について、

  * 2 点が非連結なら $0$を返す。（Union-find を用いる）…(3)
  * そうでない場合、以前に同様の質問をしていた場合は（結果が変わっていることはないため）その時の答えを返す。…(4)
  * そうでもない場合、次数が小さい方の頂点に隣接する頂点すべてについてもう一方の頂点に隣接しているか判定し、隣接しているものがあればその頂点番号を、なければ 0 を返す。（隣接リストを用いる）…(5)

結論から言えば、この解法は $O(N + Q\sqrt{Q})$ 時間で動いています。具体的には、(1) で $O(N)$ 時間、(5) で $O(Q\sqrt{Q})$ 時間かかり、この 2 つの工程がボトルネックとなっています。

(1)~(4) の計算量の解析は容易にできるものとして、(5) の計算量解析を以下に書きます。

---

証明：
頂点 $i$ についての最終的な次数を $d_i$ とします。また、 $i$ 番目の (5) の工程で質問されるクエリの 2 頂点を $(a_i, b_i)$ とします。ここで、このクエリで探索される頂点数は高々 $\min ⁡(𝑑_{𝑎_𝑖},𝑑_{𝑏_𝑖})$ 個であることに注意してください。

探索する頂点数の全体を通じての合計 ($= S$) を最大化するように $d, a, b$ を決めることを考えます。この際に、

* $d$ は広義単調減少である。
* $a_i < b_i$ である。

という 2 つの条件を加えても一般性を失いません。すると、 $i$ 番目のクエリでは高々 $d_{b_i}$ 個の頂点を探索することがわかります。

条件を緩和し、ちょうど $d_{b_i}$ 個の頂点を各クエリで探索するものとすると、 $b_i$ の小さいクエリを多く入れた方が探索個数が増えます。

そうすると $(a_1,b_1),(a_2,b_2),(a_3,b_3),(a_4,b_4) \cdots = (1, 2), (1, 3), (2, 3), (1, 4) \cdots$ とするのが最適です。この場合に、 $b_i > \sqrt{2Q}$ となる $i$ は存在しないことに注意してください。

ここで主客転倒を用います。各頂点 $i$ について、 $b_j > i$ を満たすクエリ $j$ すべてに対しての探索個数の合計値 $s_i$ を考えます $(\sum s = S)$ 。

$d$ の総和が $2Q$ 以下であることと $d$ の単調性に留意すれば、 $d_i \le \frac{2Q}{i}$ です。また、 $b_j > i$ なる $j$ の個数は高々 $i$ 個であるため、 $s_i \le 2Q (= \frac{2Q}{i} \times i)$ です。

さらに、 $b_i > \sqrt{2Q}$ となる $i$ は存在しないことを用いれば、 $s_i$ が正となる $i$ の個数は $2Q$ 個以下であることもわかるため、 $\sum s \le 2Q \sqrt{2Q}$ です。これは求めるべき答えです。

---

よって、この問題を $O(N + Q\sqrt{Q})$ 時間で解くことができました。 -->

Let's consider the following solution:

---

* Prepare an adjacency list with unordered sets for adjacent vertices and a Union-Find structure to maintain the connectivity status of each vertex. ...(1)
* For Type 1 queries, add edges to both the adjacency list and the Union-Find structure. ...(2)
* For Type 2 queries, regarding vertices $a$ and $b$:

  * If the two points are not connected, return $0$. (Using Union-Find) ...(3)
  * Otherwise, if a similar query has been made before (since the result won't change), return the previous answer. ...(4)
  * If not, determine if each vertex adjacent to the vertex with the smaller degree is adjacent to the other vertex. If so, return the vertex number; otherwise, return $0$. (Using the adjacency list) ...(5)

In conclusion, this solution runs in $O(N + Q\sqrt{Q})$ time. Specifically, (1) takes $O(N)$ time, and (5) takes $O(Q\sqrt{Q})$ time, making these two steps the bottlenecks.

Analyzing the computational complexity of (1)-(4) is straightforward. Now, let's analyze the complexity of (5).

---

Proof:
Let $d_i$ denote the final degree of vertex $i$, and let $(a_i, b_i)$ denote the two vertices queried in the $i$th step of (5). Note that the number of vertices searched in this query is at most $\min ⁡(𝑑_{𝑎_𝑖},𝑑_{𝑏_𝑖})$.

Let's determine $d$, $a$, and $b$ to maximize the total number of vertices searched ($= S$) throughout the process.

Adding the conditions that $d$ is strictly decreasing and $a_i < b_i$ does not lose generality. Then, in the $i$th query, we know that at most $d_{b_i}$ vertices are searched.

Relaxing the conditions and assuming that exactly $d_{b_i}$ vertices are searched in each query, we observe that including more queries with smaller $b_i$ values increases the number of searched vertices.

Therefore, the optimal choice is $(a_1,b_1),(a_2,b_2),(a_3,b_3),(a_4,b_4) \cdots = (1, 2), (1, 3), (2, 3), (1, 4) \cdots$. Note that there is no $i$ such that $b_i > \sqrt{2Q}$.

Now, let's use inversion. For each vertex $i$, let's consider the sum of the number of searched vertices for all queries $j$ such that $b_j > i$ (denoted by $s_i$) $(\sum s = S)$.

Considering that the sum of $d$ is less than or equal to $2Q$ and the monotonicity of $d$, we have $d_i \le \frac{2Q}{i}$. Also, since the number of queries $j$ with $b_j > i$ is at most $i$, we have $s_i \le 2Q (= \frac{2Q}{i} \times i)$.

Furthermore, considering that there is no $i$ such that $b_i > \sqrt{2Q}$, we conclude that the number of $i$ where $s_i$ is positive is at most $2Q$, so $\sum s \le 2Q \sqrt{2Q}$. This is the desired answer.

---

Thus, we have solved this problem in $O(N + Q\sqrt{Q})$ time.

<!-- なお、この解説と同様の考え方を用いる問題として、JOIsp2024 4-1 ([Problem joisp2024/escape2.PDF](https://img.atcoder.jp/joisp2024/escape2.pdf)) が挙げられます。 -->

Furthermore, a problem that uses a similar approach to this explanation is JOIsp2024 4-1 ([Problem joisp2024/escape2.PDF](https://img.atcoder.jp/joisp2024/escape2.pdf)).

---

> by MMNMM
<!-- 
**別解**

---

次数の大小によって場合分けを行うことでも、この問題を解くことができます。

まず、次のような $2$ つの解法について考えます。

> #### 解法 1
>
> 整数の集合 $\text{neighbor}_i,  (1 \le i \le N)$ と整数の組の集合 $\text{joint}_i, (1 \le i \le N)$ を管理する。
>
> * 辺 $(u, v)$ の追加クエリでは、
>   1. すべての $w \in \text{neighbor}_u$ に対し、$\text{joint}_v$ に $(w, u)$ を、$\text{joint}_w$ に $(v, u)$ を追加する。
>   2. すべての $w \in \text{neighbor}_v$ に対し、$\text{joint}_u$ に $(w, v)$ を、$\text{joint}_w$ に $(u, v)$ を追加する。
>   3. $\text{neighbor}_u$ に $v$ を、$\text{neighbor}_v$ に $u$ を追加する。
> * 頂点対 $(u, v)$ に対する質問クエリでは、$\text{joint}_u$ に $(v, k)$ の形の要素が含まれているか確認し、含まれているならば $k$ を回答する。そうでなければ、$0$ を回答する。

適切な連想配列などを用いることで、質問クエリは $O(1)$ 時間や $O(\log N)$ 時間で答えることができます。

しかし、辺の追加クエリでは頂点 $u, v$ の次数 $d_u, d_v$ に対して $O(d_u + d_v)$ の時間計算量および空間計算量を使い、クエリ全体では最悪 $O(Q^2)$ となってしまいます。

> #### 解法 2
>
> 整数の集合 neighbor⁡𝑖 $(1 \le i \le N)$ を管理する。
>
> * 辺 $(u, v)$ の追加クエリでは、$\text{neighbor}_u$ に $v$ を、$\text{neighbor}_v$ に $u$ を追加する。
> * 頂点対 $(u, v)$ に対する質問クエリでは、すべての $1 \le w \le N$ を探索し、$u \in \text{neighbor}_w$ かつ $v \in \text{neighbor}_w$ であるような $w$ が存在すればこれを回答する。存在しなければ、$0$ を回答する。

この解法も適切な連想配列などを用いることで、辺の追加クエリを $O(1)$ 時間や $O(\log N)$ 時間で処理することができます。

しかし、質問クエリでは $O(N\log N)$ 時間や $O(N)$ 時間が必要となり、クエリ全体では最悪 $O(Q N \log N)$ 時間や $O(Q N)$ 時間となってしまいます。

ここで、解法 1 と解法 2 を組み合わせることを考えます。

> #### 解法1+2
>
> 整数の集合 neighbor⁡𝑖 $(1 \le i \le N)$ と整数の組の集合 ${joint⁡}_i , (1 \le i \le N)$ を管理する。 また、整数 $D$ をひとつ定める。
>
> * 辺 $(u, v)$ の追加クエリでは、
>   1. **$|\text{neighbor}_u | \le D$ ならば** 、すべての $w \in \text{neighbor}_u$ に対し、$\text{joint}_v$ に $(w, u)$ を、$\text{joint}_w$ に $(v, u)$ を追加する。
>   2. **$|\text{neighbor}_v| \le D$ ならば** 、すべての $w \in \text{neighbor}_v$ に対し、$\text{joint}_u$ に $(w, v)$ を、$\text{joint}_w$ に $(u, v)$ を追加する。
>   3. $\text{neighbor}_u$ に $v$ を、$\text{neighbor}_v$ に $u$ を追加する。
> * 頂点対 $(u, v)$ に対する質問クエリでは、$\text{joint}_u$ に $(v, k)$ の形の要素が含まれているか確認し、含まれているならば $k$ を回答する。そうでなければ、**$|\text{neighbor}_w| > D$ であるような** すべての $1 \le w \le N$ を探索し、$u \in \text{neighbor}_w$ かつ $v \in \text{neighbor}_w$ であるような $w$ が存在すればこれを回答する。存在しなければ、$0$ を回答する。

このように変形し、$|\text{neighbor}_w| > D$ となるような $w$ 全体も同様に管理することで、追加クエリの計算時間を $O(QD)$（やそれに $\log$ がつく形）に、質問クエリの計算時間を $\widetilde O(\frac{Q^2}{D})$（やそれに $\log$ がつく形）にすることができます。

よって、$D = O(\sqrt{Q})$ などととることによって全体の計算時間を $O(Q\sqrt{Q})$（やそれに $\log$ がつく形）とすることができます。

最悪空間計算量が $O(QD)$ となることなどから、$D$ の値は小さめに取ることで定数倍が良好になります。 -->


**Another Solution**

---

By performing a case analysis based on the degree of vertices, this problem can also be solved.

First, let's consider two solutions as follows:

> #### Solution 1
>
> Manage sets of integers $\text{neighbor⁡}_i$ $(1 \le i \le N)$ and sets of pairs of integers $\text{joint}_i$ $(1 \le i \le N)$.
>
> * For an edge $(u, v)$ addition query:
>   1. For each $w \in \text{neighbor}_u$, add $(w, u)$ to $joint_v$ and $(v, u)$ to $\text{joint}_w$.
>   2. For each $w \in \text{neighbor}_v$, add $(w, v)$ to $joint_u$ and $(u, v)$ to $joint_w$.
>   3. Add $v$ to $neighbor_u$ and $u$ to $neighbor_v$.
> * For a query regarding vertex pair $(u, v)$:
>   Check if $joint_u$ contains an element in the form $(v, k)$, and if so, return $k$. Otherwise, return $0$.

By using appropriate associative arrays, query queries can be answered in $O(1)$ time or $O(\log N)$ time.

However, for edge addition queries, it requires a time complexity and space complexity of $O(d_u + d_v)$ with respect to the degrees $d_u$ and $d_v$ of vertices $u$ and $v$, respectively, and in the worst case, the overall complexity becomes $O(Q^2)$.

> #### Solution 2
>
> Manage sets of integers $neighbor⁡_i$ $(1 \le i \le N)$.
>
> * For an edge $(u, v)$ addition query, add $v$ to $neighbor_u$ and $u$ to $neighbor_v$.
> * For a query regarding vertex pair $(u, v)$, search all $1 \le w \le N$, and if there exists $w$ such that $u \in \text{neighbor}_w$ and $v \in \text{neighbor}_w$, answer this. Otherwise, return $0$.

By using appropriate associative arrays, edge addition queries can be processed in $O(1)$ time or $O(\log N)$ time.

However, for query queries, it requires $O(N\log N)$ time or $O(N)$ time, and in the worst case, the overall complexity becomes $O(Q N \log N)$ time or $O(Q N)$ time.

Now, let's consider combining Solution 1 and Solution 2.

> #### Solution1+2
>
> Manage sets of integers $neighbor⁡_i$ $(1 \le i \le N)$ and sets of pairs of integers $joint_i$ $(1 \le i \le N)$. Also, choose an integer $D$.
>
> * For an edge $(u, v)$ addition query:
>   1. **If $|\text{neighbor}_u | \le D$**, for each $w \in \text{neighbor}_u$, add $(w, u)$ to $joint_v$ and $(v, u)$ to $joint_w$.
>   2. **If $|\text{neighbor}_v| \le D$**, for each $w \in \text{neighbor}_v$, add $(w, v)$ to $joint_u$ and $(u, v)$ to $joint_w$.
>   3. Add $v$ to $neighbor_u$ and $u$ to $neighbor_v$.
> * For a query regarding vertex pair $(u, v)$:
>   Check if $joint_u$ contains an element in the form $(v, k)$, and if so, return $k$. Otherwise, **search all $1 \le w \le N$ such that $|\text{neighbor}_w| > D$**, and if there exists $w$ such that $u \in \text{neighbor}_w$ and $v \in \text{neighbor}_w$, answer this. Otherwise, return $0$.

By transforming in this way and managing all $w$ such that $|\text{neighbor}_w| > D$ in the same way, the computation time for additional queries can be $O(QD)$ (or with a $\log$ term), and the computation time for query queries can be $\widetilde O(\frac{Q^2}{D})$ (or with a $\log$ term).

Therefore, by taking $D = O(\sqrt{Q})$, the overall computation time can be $O(Q\sqrt{Q})$ (or with a $\log$ term).

Considering that the worst-case space complexity becomes $O(QD)$, choosing a smaller value for $D$ will result in a better constant factor.

<details><summary><b>C++</b></summary>

```cpp
#include <iostream>
#include <set>
#include <vector>
#include <map>

int main() {
    using namespace std;
    static constexpr unsigned small_limit{32}, P{998244353};
    unsigned N, Q;
    cin >> N >> Q;
    // 隣接リスト
    vector<set<unsigned>> edges(N);
    // dist2[i][j] := i-v-j なる辺が存在するような v
    vector<map<unsigned, unsigned>> dist2(N);
    // 次数が small_limit より大きい頂点
    vector<unsigned> large_size;

    const auto add_edge{[&edges, &dist2, &large_size](const unsigned from, const unsigned to) {
        // 次数が small_limit を越えるときに large_size に追加
        if (size(edges[from]) == small_limit)
            large_size.emplace_back(from);
        // small_limit 以下なら、dist2 を更新
        if (size(edges[from]) < small_limit)
            for (const auto &e: edges[from])
                dist2[min(to, e)][max(to, e)] = from;
        edges[from].emplace(to);
    }};

    for (unsigned i{}, x{}, A, B, C; i < Q; ++i) {
        cin >> A >> B >> C;
        A = A * (x + 1UL) % P % N;
        B = B * (x + 1UL) % P % N;
        C = C * (x + 1UL) % P % N;
        if (!A) {
            add_edge(B, C); // 辺 B-C を追加：i-B-C なる辺がある i について更新
            add_edge(C, B); // 辺 C-B を追加：B-C-i なる辺がある i について更新
        } else
            cout << (x = [&]() -> unsigned {
                if (dist2[B].contains(C)) // dist2 に情報があればそれを使う
                    return dist2[B][C] + 1;
                // なければ、答えの候補は次数の大きい頂点のどれか
                for (const auto &v: large_size)
                    if (edges[v].contains(B) && edges[v].contains(C))
                        return v + 1;
                return 0;
            }()) << endl;
    }
    return 0;
}
```

</details><br>
