 ### E: 1 or 2

<!--
各条件は
* $Z_i \equiv 0 (\mod 2)$ のとき $$A_{X_i} = A_{Y_i}$$
* $Z_i \equiv 1 (\mod 2)$ のとき $$A_{X_i} \ne A_{Y_i} \ (A_{X_i} = 3 − A_{Y_i})$$

です。すなわち、$A_{X_i}$ または $A_{Y_i}$ の一方が分かればもう一方を知ることができます。

したがって、$(X_1, Y_1), \cdots ,(X_M, Y_M)$ 間にのみ辺が存在する $N$ 頂点のグラフ $G$ を考えると、$i$ 番目のカー

ドをめくると $G$ 上で頂点 $i$ と同じ連結成分の頂点に対応するカードの数字が分かります。よって、$G$ の連結
成分数が答えになります。

これは、塗りつぶしの要領で深さ優先探索を行うことや、Union-Find を用いることで $O(N + M)$ または
$O((N + M)\alpha(M))$ の計算時間で求めることができます。ここで、$\alpha$ はアッカーマン関数の逆関数ですが、非
常に小さいため、ほとんど定数と同じと考えて構いません。

#### おまけ (Hard バージョン)

**問題** 入力に矛盾がある場合は $-1$ を出力せよ。

**解説**

各条件は
$$A_{X_i} + A_{Y_i} \equiv Zi (\mod 2)$$

と表すことができます。

さらに、$i = 1, 2, \cdots , N$ , $j = 1, 2$ に対して、$p_{i,j} \in \{\textit{true, false}\}$ を
$p_{i,j} = \textit{true} \iff i$ 番目のカードに $j$ が書かれている

と定義します。すると、各条件は
* $Z_i \equiv 0 (\mod 2)$ のとき
$$p_{X_i,0} = p_{Y_i,0} \\
p_{X_i,1} = p_{Y_i,1}$$
* $Z_i \equiv 1 (\mod 2)$ のとき
$$p_{X_i,0} = p_{Y_i,1} \\
p_{X_i,1} = p_{Y_i,0}$$

です。このとき、$i = 1, 2, \cdots, N$ について

$$p_{i,0}  \ne p_{i,1}$$

であることを確認すれば良いです。各 $p_{i,j}$ に対応する頂点を作った Union-Find を考えます。各 $p_{i_1,j_1} = p_{i_2,j_2}$ に対してこれらに対応する頂点同士を unite します。最後に、$p_{i,0}  \ne p_{i,1}$ に対して、こ れらに対応する頂点同士が unite されていない (同じグループに属していない) かを調べることで矛盾 があるか確認することができます。 -->

Each condition states that:
* When $Z_i \equiv 0 (\mod 2)$, $$A_{X_i} = A_{Y_i}$$
* When $Z_i \equiv 1 (\mod 2)$, $$A_{X_i} \ne A_{Y_i} \ (A_{X_i} = 3 - A_{Y_i})$$

In other words, knowing one of $A_{X_i}$ or $A_{Y_i}$ allows us to determine the other.

Therefore, considering a graph $G$ with $N$ vertices, where edges exist only between $(X_1, Y_1), \cdots ,(X_M, Y_M)$, flipping the $i$-th card reveals the number on the card corresponding to the vertex in the same connected component as vertex $i$ in $G$. Thus, the number of connected components in $G$ is the answer.

This can be found in $O(N + M)$ or $O((N + M)\alpha(M))$ time using depth-first search or Union-Find, respectively. Here, $\alpha$ is the inverse function of Ackermann's function, but it is extremely small and can be treated almost like a constant.

#### Bonus (Hard Version)

**Problem:** Output $-1$ if there is a contradiction in the input.

**Explanation:**

Each condition can be expressed as:
$$A_{X_i} + A_{Y_i} \equiv Z_i (\mod 2)$$

Furthermore, for $i = 1, 2, \cdots , N$ and $j = 1, 2$, define $p_{i,j} \in \{\textit{true, false}\}$ as
$p_{i,j} = \textit{true} \iff$ card $i$ has $j$ written on it.

Then, each condition becomes:
* When $Z_i \equiv 0 (\mod 2)$,
$$p_{X_i,0} = p_{Y_i,0} \\
p_{X_i,1} = p_{Y_i,1}$$
* When $Z_i \equiv 1 (\mod 2)$,
$$p_{X_i,0} = p_{Y_i,1} \\
p_{X_i,1} = p_{Y_i,0}$$

In this case, for $i = 1, 2, \cdots, N$,

$$p_{i,0}  \ne p_{i,1}$$

must be confirmed. 

Consider a Union-Find structure for each $p_{i,j}$. Unite the vertices corresponding to each $p_{i_1,j_1} = p_{i_2,j_2}$. Finally, check if $p_{i,0}  \ne p_{i,1}$ for each vertex, which corresponds to checking if they are not united (not in the same group). This allows us to confirm if there is a contradiction.

---

### Approach 2
<!-- 
#### 考えたこと
要するに

* 各カードの値が偶数なのか奇数なのかだけを知りたい 

ということが言える。こういう問題では、$\mod 2$ ですべてを考えるとよい。われわれにあたえられた条件は

$$
A_x+A_y \equiv 0 or 1(\mod 2)
$$

という形をしたものが $M$ 個与えられるということになる。この条件は一体何を意味しているのだろうか？？

#### 条件式の意味

例えば

$$
A_2+A_5 \equiv 0 or 1
$$ 
 
という条件があったとき、

* $A_2$ が偶数か奇数かがわかったら、$A_5$ についてもわかるし、
* $A_5$ が偶数か奇数かがわかったら、$A_2$ についてもわかる、

という関係にあることがわかる。では

$$
A_x+A_y \equiv 0 \ \textit{or} \ 1 \\
Ay+Az \equiv 0 \ \textit{or} \ 1
$$

という $2$ つの関係式があったらどうなるであろう...これは、「$A_x,A_y,A_z$ のうちどれか 1 つでも偶奇かがわかれば、3 つすべての偶奇がわかる」ということになる。よってわれわれはノードが $1,2, \cdots ,N$ のグラフを用意して、 $M$ 個の $A_x,A_y$ に関する条件に対して

* ノード $x$ とノード $y$ との間に辺を張ったグラフを用意したとき、
* 各連結成分については、どれか 1 個でも偶奇がわかれば、連結成分内のすべてのノードの偶奇がわかる

ということになる。注意点として例えば

$$
A_1+A_2 \equiv 0 \\
A_2+A_3 \equiv 0 \\
A_1+A_3 \equiv 1
$$

のような関係式があったら、これらは矛盾し合っていて、これを満たす解は存在しない。でもそのようなことは起こらないことが問題文から保証されている。ただし

$$
A_1+A_2 \equiv 0 \\
A_2+A_3 \equiv 0 \\
A_1+A_3 \equiv 1
$$ 

のような関係式の組はありうる。つまり 3 本目の式は 1 本目と 2 本目から導かれるので冗長なのだ。この 3 本のうちの 2 本だけでよい。でもこういうのは問題ない。

問題の答え
以上の考察から「上のように作ったグラフの連結成分の個数」が答えであることがわかった。これは例えば Union-Find でパッと求めることができる。

#### Union-Find 使って連結成分数出す方法

意外とここが詰まる方も多い気がする。実際はとても簡単で Union-Find というのは

* 同じ連結成分にあるノード間では root の値が等しい
* 異なる連結成分にあるノード間では root の値が異なる

という性質を満たすものであったことを思い出す。そうすると、ノード $v = 1, 2, \cdots ,N$ に対して $root(v)$ を求めてあげて、その種類が何通りあるかを見れば OK。 -->


### Considerations

In essence,

* We only need to know whether each card's value is even or odd.

For such problems, considering everything $\mod 2$ is beneficial. The conditions given to us are of the form:

$$
A_x + A_y \equiv 0 \ \text{or} \ 1 (\mod 2)
$$

What does this condition imply?

#### Meaning of the Conditions

For example, when we have:

$$
A_2 + A_5 \equiv 0 \ \text{or} \ 1
$$

* If we know whether $A_2$ is even or odd, we can deduce the parity of $A_5$, and
* If we know whether $A_5$ is even or odd, we can deduce the parity of $A_2$.

Similarly, if we have two such relations:

$$
A_x + A_y \equiv 0 \ \text{or} \ 1 \\
A_y + A_z \equiv 0 \ \text{or} \ 1
$$

Then, knowing the parity of any one of $A_x, A_y, A_z$ allows us to determine the parities of all three. Hence, we prepare a graph with nodes numbered $1,2, \cdots ,N$ and, for each pair of $A_x,A_y$ among the $M$ given conditions:

* If we prepare a graph by connecting nodes $x$ and $y$ with an edge,
* Then, for each connected component, if we know the parity of any one node, we know the parities of all nodes within that component.

It's worth noting that, for example:

$$
A_1 + A_2 \equiv 0 \\
A_2 + A_3 \equiv 0 \\
A_1 + A_3 \equiv 1
$$

Such relations contradict each other, and no solution exists. However, this scenario is guaranteed not to occur according to the problem statement. Nonetheless:

$$
A_1 + A_2 \equiv 0 \\
A_2 + A_3 \equiv 0 \\
A_1 + A_3 \equiv 1
$$

Such sets of relations are possible. Hence, only two of the three equations are necessary, as the third one is redundant. But this situation is acceptable.

#### Answer to the Problem

From the above analysis, we deduce that the number of connected components in the graph we constructed is the answer. This can be quickly obtained, for example, using Union-Find.

#### Using Union-Find to Determine the Number of Connected Components

This step might be a stumbling block for some. In fact, using Union-Find is straightforward:

* Nodes within the same connected component have the same root value.
* Nodes in different connected components have different root values.

Thus, we calculate $root(v)$ for each node $v = 1, 2, \cdots ,N$ and count how many different root values exist. That's it!

```cpp
#include <bits/stdc++.h>
using namespace std;

struct union_find {
    vector<int> parent;
    vector<int> size;
    int components = 0;

    union_find(int n = -1) {
        if (n >= 0)
            init(n);
    }

    void init(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        size.assign(n, 1);
        components = n;
    }

    int find(int x) {
        return x == parent[x] ? x : parent[x] = find(parent[x]);
    }

    bool unite(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y)
            return false;

        if (size[x] < size[y])
            swap(x, y);

        size[x] += size[y];
        parent[y] = x;
        components--;
        return true;
    }
};

int main(){
    int n, m; cin >> n >> m;
    union_find uf(n);

    for (int i = 0; i < m; i++){
        int x, y, z; cin >> x >> y >> z;
        x--, y--;
        uf.unite(x, y);
    }
    set<int> connected;
    for (int i = 0; i < n; i++){
        connected.insert(uf.find(i));
    }
    cout << connected.size() << "\n";
    return 0;
}
```