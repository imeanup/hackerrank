## [E - Forbidden Prefix](https://atcoder.jp/contests/abc403/tasks/abc403_e)


### 前提：トライ木 (Trie)

本問題は，**トライ木** (Trie) の練習問題です．トライ木は，文字列のリストを根付き木として表現するデータ構造であり，木の各頂点に適切な情報を持たせることで，接頭辞に関する処理を効率的に行うことができます．

トライ木は，各頂点が文字を表し，根から他の頂点までのパスが文字列に対応するように構成されます．共通の接頭辞を持つ文字列は，トライ木の根に近い部分でパスを共有します．

トライ木の各頂点は，以下の情報を持ちます．　

* その頂点が表す文字
* その頂点の子のリスト
* その頂点で**受理**される文字列のリスト：根からその頂点へのパスが表す文字列と一致する文字列のリスト

例えば，$(S_1, S_2, S_3, S_4, S_5) = (\texttt{cat} , \texttt{car} , \texttt{car}, \texttt{do}, \texttt{dog})$ という文字列のリストを表すトライ木は以下のようになります．頂点の右上の数字が，その頂点が受理する文字列を表しています．

![](https://img.atcoder.jp/abc403/e380ef79eaafae5446a7d9082739f777.png)

### 本問題の解法

トライ木を用いて本問題を解く方法を述べます．与えられる文字列 $S_i$ を（$X,Y$ のどちらに属するかに関係なく）すべて $1$ つのトライ木 $T$ で管理します．また，「$Y$ に含まれる文字列 $S_i$ であって，ある $X$ の要素 $S_j$ を接頭辞として持つもの」の集合 $Z$ を管理します．求める答えは $|Y| − |Z|$ となります．$S_i$ が与えられるごとに，$Z$ を高速に更新できれば，問題を解くことができます．

$Z$ に要素が追加される状況は以下の $2$ 通りです．

1. クエリ $1$ において $S_i$ を $X$ に追加したことで，$S_j \in Y(j < i)$ が $S_i$ を接頭辞として含むようになり，$S_j$ が $Z$ に追加される
2. クエリ $2$ において $S_i$ を $Y$ に追加したことで，$S_j \in X(j < i)$ が $S_i$ に接頭辞として含まれるようになり，$S_i$ が $Z$ に追加される

以下，それぞれのクエリを処理する方法を述べます．

### クエリ 1 の処理

$S_i \in X$ を受理する頂点を根とする部分木に，$S_j \in Y$ を受理する頂点があれば，$S_j$ を $Z$ に追加することになります．

部分木の頂点をすべて調べていては，実行時間制限に間に合いません．そこで，あらかじめ $T$ の各頂点 $v$ について，「次に $v$ で受理されるような $S_i \in X$ が追加されたとき，新たに $Z$ に追加する $S_j \in Y$ の集合」$Z_v$ を管理しておきます．これはあらかじめ $S_j \in Y$ を $T$ に追加するときに，$S_j$ の接頭辞を受理する頂点 $v$ すべてについて，$S_j$ を $Z_v$ に追加しておけばよいです． そして，$S_i \in X$ を追加するとき，$S_i$ を受理する頂点を $v$ として，「$j \in Z_v$ をすべて $Z$ に追加し，その後 $Z_v$ を空にする」という操作を行います．$Z_v$ の要素数は $Q$ 個程度になりうるので，一見非効率的ですが，操作全体で $S_j$ がいずれかの $Z_v$ から取り出される回数はたかだか $|S_j|$ 回です．よって，すべての処理にかかる時間計算量は $O(\displaystyle\sum_{i=1}^Q |S_i| \log ⁡Q)$ です．

### クエリ 2 の処理

$S_i \in Y$ の接頭辞を受理する頂点 $v$ であって，ある $S_j \in X$ を受理するようなものがあるか判定すればよいです．これは，$T$ の各頂点 $v$ について，その頂点で受理される $X$ の文字列が存在するかどうかを表すフラグ $f_v$ を管理しておけばよいです．つまり，$X$ の文字列を $T$ に追加するとき，それを受理する頂点を $v$ として $f_v = \texttt{true}$ と設定し，$Y$ の文字列を追加したときには，その接頭辞を受理する頂点の先祖 $v$ であって $f_v = \texttt{true}$ なるものがあるかどうか判定すればよいです．

### まとめ

クエリ 1, 2 の処理をまとめて，各クエリについて以下のように処理をすればよいです．

* $S_i$ を $X$ に追加するとき
  * $S_i$ を $T$ に追加する
  * $S_i$ を受理する頂点を $v$ として，以下を行う
    * 各 $S_j \in Z_v$ を $Z$ に追加する．その後，$Z_v$ を空にする
    * $f_v = \texttt{true}$ とする
* $S_i$ を $Y$ に追加するとき
  * $S_i$ を $T$ に追加する
  * $S_i$ の接頭辞を受理する頂点 $v$ それぞれについて以下を行う
    * $Z_v$ に $i$ を追加する
    * $f_v = \texttt{true}$ ならば，$Z$ に $i$ を追加する

全体の時間計算量は $O(\displaystyle\sum_{i=1}^Q |S_i| \log ⁡Q)$ です．

[実装例 (Python)](https://atcoder.jp/contests/abc403/submissions/65219576)

---

### Preliminaries: The Trie

This problem is an exercise in using a **trie** (prefix tree). A trie is a rooted tree data structure for storing a set of strings so that operations involving prefixes can be done efficiently. Each node in the trie represents a character, and the path from the root to any node corresponds to a prefix (or complete string) in the set. Strings that share a common prefix share the path from the root up to the point of divergence.

Each node in the trie stores:

- The character it represents.
- A list (or map) of its children.
- A list of all input strings that are **accepted** at that node (i.e., whose full length matches the path from the root to that node).

For example, if the input list is  
$$
(S_1, S_2, S_3, S_4, S_5) = (\texttt{cat}, \texttt{car}, \texttt{car}, \texttt{do}, \texttt{dog}),
$$  
the trie looks like this (the number in the top right of each node is the count of strings accepted there):

![](https://img.atcoder.jp/abc403/e380ef79eaafae5446a7d9082739f777.png)

---

### Overview of the Solution

We keep **one** trie $T$ for all strings—whether they belong to set $X$ or set $Y$. Additionally, we maintain a set $Z$, defined as

> all strings in $Y$ that have some string in $X$ as a prefix.

The answer after each query is
$$
|Y| \;-\; |Z|.
$$
We need to update $Z$ efficiently as each new string $S_i$ arrives, either for $X$ or for $Y$.

---

### When do elements enter $Z$?

There are two cases in which a string from $Y$ becomes “forbidden” (i.e. is added to $Z$):

1. **Query type 1** (add to $X$):  
   A new $S_i\in X$ arrives and becomes a prefix of some existing $S_j\in Y$ (with $j<i$). In that case, $S_j$ must be added to $Z$.

2. **Query type 2** (add to $Y$):  
   A new $S_i\in Y$ arrives and has as a prefix some existing $S_j\in X$ (with $j<i$). Then $S_i$ must be added to $Z$.

We must handle both query types in total time 
$$
O\!\bigl(\sum_{i=1}^Q |S_i| \cdot \log Q\bigr).
$$

---

### Query Type 1: Adding $S_i$ to $X$

Suppose we insert $S_i$ into the trie and arrive at node $v$. We need to find all previously added $S_j\in Y$ that are accepted in the subtree rooted at $v$, and add them to $Z$. Scanning that entire subtree every time would be too slow.

Instead, we precompute for each node $v$ a list $Z_v$, defined as

> the set of indices $j$ of those $S_j\in Y$ such that node $v$ is on the path for $S_j$.

We build and maintain these lists as follows:

- Whenever we add a string $S_j$ to $Y$, we walk down the trie along its characters; for each node $v$ on that path, we insert $j$ into $Z_v$.

Then, when a new $S_i\in X$ arrives:

1. Insert $S_i$ into the trie, reaching node $v$.
2. Move every index in $Z_v$ into the global set $Z$, then clear $Z_v$.
3. Mark $f_v = \text{true}$ (see below for its use).

Although $Z_v$ could in principle grow large, each index $j$ is extracted from some $Z_v$ at most once—every time you remove it, it never returns. Since each $S_j$ has length $|S_j|$, the total work over all extractions is $O(\sum |S_j|)$. Hence, this handles all Query 1 operations in  
$$
O\!\bigl(\sum |S_i|\log Q\bigr).
$$

---

### Query Type 2: Adding $S_i$ to $Y$

When we insert a new $S_i\in Y$, we need to check whether it has any existing $X$-string as a prefix. Equivalently, we check if **any** node on the path for $S_i$ has already been marked by a previous $X$-insertion.

To support this, each node $v$ keeps a flag
$$
f_v = \text{“true if some }S_j\in X\text{ is accepted at }v\text{.”}
$$
When adding a string to $X$, we set $f_v=$ true at its terminal node $v$. Then, when adding $S_i$ to $Y$:

1. Walk down the trie along $S_i$.  
2. At each node $v$ on that path:  
   - Add $i$ to $Z_v$ (so future Query 1 insertions know about it).  
   - If $f_v=$ true, immediately add $i$ to the global $Z$.

This again takes $O(|S_i|\log Q)$ time for each string.

---

### Putting It All Together

Maintain:

- A single trie $T$.
- For each node $v$:
  - A dynamic list $Z_v$ of indices of $Y$-strings whose path passes through $v$.
  - A boolean flag $f_v$ indicating whether any $X$-string terminates at $v$.
- A global set $Z$ of “forbidden” $Y$-strings.

Process each query $i$ as follows:

- **If** it’s “add $S_i$ to $X$”:
  1. Insert $S_i$ into $T$, reaching node $v$.
  2. Move all indices in $Z_v$ into $Z$, then clear $Z_v$.
  3. Set $f_v = \text{true}$.
- **If** it’s “add $S_i$ to $Y$”:
  1. Insert $S_i$ into $T$, walking through nodes $v$ on its path.
  2. For each such $v$:
     - Append $i$ to $Z_v$.
     - If $f_v = \text{true}$, add $i$ to $Z$.

After each query, the answer is simply
$$
|Y| - |Z|.
$$

The total time over $Q$ queries is
$$
O\!\bigl(\sum_{i=1}^Q |S_i|\;\log Q\bigr).
$$

---

[An example Python implementation](https://atcoder.jp/contests/abc403/submissions/65219576)
