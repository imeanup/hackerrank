## [C - 403 Forbidden](https://atcoder.jp/contests/abc403/tasks/abc403_c)


### クエリ $1$ と $3$ のみがある場合

各ユーザ $X$ について，ユーザ $X$ が閲覧できるコンテストページの集合を $S_X$ とします．クエリ $1$ では，$S_X$ に $Y$ を追加します．クエリ $3$ では，$S_X$ に $Y$ が含まれているかどうか判定すればよいです．

$S_X$ の要素数は最大で $M$ 個になるため，$S_X$ を配列を使って管理した場合，$S_X$ に $Y$ が含まれているかの判定にクエリあたり $O(M)$ 時間かかります．よって，時間計算量は全体で $O(QM)$ となり，実行時間制限に間に合いません．

そこで，集合を効率的に管理するデータ構造を用いる必要があります．そのようなデータ構造はほとんどの言語で標準機能として提供されており，C++ と Python では `set` として利用することができます．`set` を使った場合，クエリ $1$ とクエリ $3$ の処理をクエリあたり $O(\log ⁡M)$ 時間で行うことができます．全体の時間計算量は $O(Q|log⁡ M)$ となり，十分高速です．

### クエリ $2$ もある場合

クエリ $2$ において，$1$ から $M$ をすべて $S_X$ に追加してしまうと，クエリあたり $O(M \log ⁡M)$ の時間がかかり，非効率的です．そこで，ユーザ $X$ がすべてのページを閲覧できるかどうかのフラグ $f_X$ を管理しておきます．すると，クエリ $2$ の処理は $f_X$ を $\texttt{true}$ に設定するだけでクエリあたり $O(1)$ 時間になります．

このとき，クエリ $3$ の処理は以下のように修正されます．

* $f_X=\texttt{true}$ ならば，ユーザ $X$ はすべてのコンテストページを閲覧できるので， `Yes` を出力する
* そうでないとき，$S_X$ に $Y$ が含まれているならば `Yes` を，そうでないならば `No` を出力する．

[実装例 (C++)](https://atcoder.jp/contests/abc403/submissions/65218114)

[実装例 (Python)](https://atcoder.jp/contests/abc403/submissions/65083795)

---


### When Only Queries 1 and 3 Exist

For each user $X$, let $S_X$ be the set of contest pages that user $X$ can view.  
- **Query 1**: add page $Y$ to $S_X$.  
- **Query 3**: check whether $Y$ is in $S_X$.

Since $\lvert S_X\rvert$ can grow up to $M$, managing $S_X$ with a simple array means that each membership check (Query 3) takes $O(M)$ time, yielding an overall $O(QM)$ algorithm which is too slow.

Instead, use a data structure that supports insertions and membership tests in $O(\log M)$ time. Most languages provide this out of the box: in C++ and Python you can use a `set`. With a `set`, both Query 1 and Query 3 run in $O(\log M)$ time each, for a total of $O(Q\log M)$, which is fast enough.

---

### When Query 2 Is Also Present

Query 2 asks us to grant user $X$ access to **all** pages $1$ through $M$.  Naïvely inserting every page into $S_X$ would cost $O(M\log M)$ time per query, which is impractical.  Instead, maintain a boolean flag  
$$
f_X = \begin{cases}
\texttt{true}, & \text{if user }X\text{ has been granted access to all pages},\\
\texttt{false}, & \text{otherwise}.
\end{cases}
$$
Processing **Query 2** then reduces to setting $f_X = \texttt{true}$ in $O(1)$ time.

With this flag, we revise **Query 3** as follows:

1. If $f_X = \texttt{true}$, output `Yes` (user $X$ can view every contest page).  
2. Otherwise, check if $Y\in S_X$:  
   - If yes, output `Yes`.  
   - If no, output `No`.  

---

[Example implementation (C++)](https://atcoder.jp/contests/abc403/submissions/65218114)  
[Example implementation (Python)](https://atcoder.jp/contests/abc403/submissions/65083795)
