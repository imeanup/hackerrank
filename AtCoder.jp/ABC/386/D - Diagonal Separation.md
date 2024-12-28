## [D - Diagonal Separation](https://atcoder.jp/contests/abc386/tasks/abc386_d) 

条件を言い換えましょう．マス $(x, y)$ が黒のとき，一つ目の条件からマス $(x,1),(x,2),\dots ,(x,y)$ はすべて黒色である必要があります．さらに マス $(x,j)$ が黒色のとき，二つ目の条件からマス $(1,j),(2,j),\dots ,(x,j)$ はすべて黒色である必要があります．よって， マス $(x, y)$ が黒のとき，マス $(x, y)$ より左上にあるマス（マス $(i,j) (1\le i \le x, 1\le j \le y)$）はすべて黒色である必要があります．

これを踏まえたうえで，条件を満たすことができる必要十分条件は次のようになります．

* $C_i = W, C_j = B, X_j \le X_i, Y_j \le Y_i$ となる $(i,j)$ が存在しない．

必要条件は上の議論から明らかです．十分条件は以下のように構成することができます．

* マス $(x, y)$ について，$x \le X_i$ かつ $y \le Y_i$ かつ $C_i = B$ を満たす $i$ が存在するとき黒に， そうでないとき白で塗る

判定方法について考えます．愚直に調べると $O(M^2)$ かかってしまい間に合いません．すでに塗られているマスを $(X_i, Y_i)$ の辞書順にソートします．そうすると，$X_i \le X_j (i<j)$ （かつ $X_i = X_j$ のとき $Y_i < Y_j$）が成り立つため，条件は

* $C_i = W, C_j = B,Y_j \le Y_i$ となる $(i,j) (i<j)$ が存在しない．

のように言い換えることができます．これは，$i$ の昇順に見ていきながら $C_i = W$ であるような $i$ の $Y_i$ の最小値を管理することで判定することができます．

---


Let’s rephrase the conditions. When the cell $(x, y)$ is black, the first condition requires that the cells $(x, 1), (x, 2), \dots, (x, y)$ must all be black. Additionally, if the cell $(x, j)$ is black, the second condition requires that the cells $(1, j), (2, j), \dots, (x, j)$ must all be black. Therefore, when the cell $(x, y)$ is black, all the cells located in the top-left region of $(x, y)$ (cells $(i, j)$ where $1 \leq i \leq x, 1 \leq j \leq y$) must also be black.

Based on this, the necessary and sufficient condition to satisfy the requirements can be expressed as follows:

- There must not exist a pair $(i, j)$ such that $C_i = W, C_j = B, X_j \leq X_i, Y_j \leq Y_i$.

The necessity of this condition is clear from the discussion above. The sufficiency can be achieved as follows:

- For each cell $(x, y)$, paint it black if there exists an $i$ such that $x \leq X_i$, $y \leq Y_i$, and $C_i = B$. Otherwise, paint it white.

### Efficient Validation

If you check these conditions naively, it will take $O(M^2)$ time, which is too slow. To optimize, sort the already painted cells $(X_i, Y_i)$ in lexicographical order. After sorting, $X_i \leq X_j$ for $i < j$ (and $X_i = X_j$ implies $Y_i < Y_j$). Thus, the condition can be rephrased as:

- There must not exist a pair $(i, j)$ where $C_i = W, C_j = B, Y_j \leq Y_i$ for $i < j$.

This condition can be validated by processing $i$ in ascending order and maintaining the minimum value of $Y_i$ for indices $i$ where $C_i = W$.
