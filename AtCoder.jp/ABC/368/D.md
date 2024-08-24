## [D - Minimum Steiner Tree](https://atcoder.jp/contests/abc368/tasks/abc368_d)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Slides</b></summary><br>

$K = 1$ のとき答えは明らかに $1$ です。そうでないときを考えます。

「もとのグラフからいくつかの($0$ 個でもよい)辺と頂点を削除してできる木のうち、頂点 $V_1, \dots ,V_K$ を全て含むようなもの」を**条件を満たす木**と呼ぶことにします。

「次数が $1$ であり、$V_1, \dots ,V_K$ のいずれでもない頂点」を**悪い頂点**と呼ぶことにします。

もとの木から始めて、悪い頂点とそれに接続する辺を削除することを可能な限り繰り返してできる木が求める木です。

<details style="border: 1px solid black; padding: 10px;"><summary><b>証明</b></summary><br>

もとの木は条件を満たす木であり、悪い頂点を取り除く操作を行っても条件を満たす木のままなので、得られる木は条件を満たす木です。

悪い頂点を取り除く操作の過程で悪い頂点がそうでなくなることはありません。よって、この操作を行えるだけ行った後の木は操作順序によらず一意です。

条件を満たす木に悪い頂点が存在した場合、その頂点を削除しても条件を満たす木であるままです。よって頂点数最小の条件を満たす木には悪い頂点は存在しません。

以上で示せました。

</details><br>

この操作は、各頂点について、直接辺でつながっている頂点をsetで管理することなどで高速に行うことができます。

</details><br>

When $K = 1$, the answer is obviously $1$. Let's consider the case when $K$ is greater than 1.

We will refer to "a tree formed by deleting some edges and vertices (including possibly 0) from the original graph, which still includes all vertices $V_1, \dots , V_K$" as a **valid tree**.

We will refer to "a vertex that has a degree of $1$ and is not among $V_1, \dots , V_K$" as a **bad vertex**.

Starting from the original tree, the tree we seek is obtained by repeatedly removing the bad vertices and the edges connected to them as much as possible.

<details style="border: 1px solid black; padding: 10px;"><summary><b>Proof</b></summary><br>

The original tree is a valid tree, and even after performing the operation of removing bad vertices, the resulting tree remains a valid tree. Therefore, the resulting tree is a valid tree.

During the process of removing bad vertices, a bad vertex does not stop being a bad vertex. Thus, the tree obtained after performing this operation as much as possible is unique, regardless of the order of operations.

If a valid tree contains a bad vertex, removing that vertex will still leave the tree valid. Therefore, the valid tree with the smallest number of vertices does not contain any bad vertices.

This completes the proof.

</details><br>

This operation can be performed efficiently by managing the directly connected vertices for each vertex using a set.


<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()

int main() {
    int n, k; 
    cin >> n >> k;
    vector<set<int>> edge(n);
    rep(i, n-1) {
        int u, v; 
        cin >> u >> v;
        u--, v--;
        edge[u].insert(v);
        edge[v].insert(u);
    }
    set<int> V;
    rep(i, k) {
        int x;
        cin >> x;
        V.insert(x - 1);
    }
    vector<int> degree(n);
    rep(i, n) {
        degree[i] = edge[i].size();
    }
    queue<int> q;
    rep(i, n) {
        if (degree[i] == 1) q.push(i);
    }
    int ans = n;
    while (!q.empty()) {
        int v = q.front(); q.pop();
        if (V.count(v)) continue;
        int vv = *edge[v].begin(); 
        edge[vv].erase(v);
        ans--;
        
        if (edge[vv].size() == 1) {
            q.push(vv);
        }
    }
    cout << ans << endl;
    
    return 0;
}

```

</details><br>
