<!-- ## D: Integer Cards

書き換える操作は好きな順番で行っても構いません。なぜなら、同じカードに対して $2$ 回以上書き換える のは無駄だからです。また、$C_i$ に $B_i$ 枚まで書き換える操作は、$C_i$ に $1$ 個まで書き換える操作を $B_i$ 回行え ると考えます。各 $C_i$ を $B_i$ 個ずつ並べた列を $D_1, D_2, \cdots , D_{\sum B_i}$ とします。すると、操作は「選んだことの ない $i$ を選んで $1$ 枚まで $D_i$ に書き換える」と考えることができます。同じカードに対して $2$ 回以上書き換 えるのは無駄なので、この操作は合計で $N$ 回しか行いません。したがって、$D_i$ の大きい方から $N$ 個まで取 り出した列を新しい $D$ として考えても構いません。

$X$ 枚書き換えるとします。すると、書き換え元は小さい方から $X$ 枚書き換えるのが最適です。書き換え先 は $D_i$ の大きいものから順に $X$ 個選ぶのが最適です。$X$ を 1 ずらすことによって書き換え元と書き換え先 はそれぞれ $1$ つずつしか変化しないため、$X$ を順に捜査することで $O(M \log M + N \log N)$ の計算時間で解 くことができます。

実 装 で は 、$D$ の 大 き い 方 か ら $N$ 個 ま で 取 り 出 す 部 分 が 難 し い か も し れ ま せ ん 。こ れ は 、$(B_1, C_1), \cdots ,(B_M, C_M)$ を $C_i$ の大きい順にソートして$^{*1}$ 配列 $D$ が $N$ 未満である間 $C_i$ を $B_i$ 個ま で $1$ 個ずつ $D$ に追加していく実装が楽でしょう。

最適な $X$ を求めることもできます。$A, D$ をソートして $A_1 \le A_2 \le \cdots \le A_N$ かつ $D_1 \ge D_2 \ge \cdots \ge D_{|D|}$ とします。すると、前述のアルゴリズムでは $X$ を $i − 1$ から $i$ にずらすことによって合計値は $D_i − A_i$ 変化 しますが、$D_i − A_i$ は単調非増加なので $D_i − A_i \ge 0$ すなわち $D_i \ge A_i$ である間だけ操作を続けるのが最適
です。すなわち、そのような $i$ の最大値 (なければ $0$) を $X$ とするのが最適です。

### 別解

残す整数と書き換え先とする整数を合計で $N$ 個選んで $N$ 個の整数の合計を最大化することを考えます。 $(X_1, Y_1), \cdots ,(X_{N+M}, Y_{N+M})$ を $(1, A_1), \cdots ,(1, A_N ),(B_1, C_1), \cdots ,(B_M, C_M)$ とすると、問題は「整数 $Y_i$ を $X_i$ 個まで選ぶことができ、合計 $N$ 個の整数を選ぶときその和の最大値を求めてください」となります。これ は、$Y_i$ の大きい順に合計 $N$ 個となるように選ぶのが最適です。この方法では $O((N + M) \log(N + M))$ の
時間計算量で求めることができます。

---
$^{*1}$ C++ 言語では $(C_i, B_i)$ の $pair$ を降順にソートする実装が簡単です。より読みやすいコードを書きたいなら構造体を用いると良 いでしょう。 -->

## D: Integer Cards

The rewriting operations can be performed in any order. This is because rewriting the same card more than once is redundant. Also, the operation to rewrite up to $B_i$ cards for $C_i$ can be considered as performing the operation to rewrite one card for $C_i$ up to $B_i$ times. Let's arrange each $C_i$ in a sequence of $B_i$ each, denoted as $D_1, D_2, \cdots , D_{\sum B_i}$. Then, the operation can be interpreted as "selecting an unused index $i$ and rewriting $D_i$ with one card". Since rewriting the same card more than twice is wasteful, this operation is performed only $N$ times in total. Therefore, it's also acceptable to consider a new sequence $D$ by selecting the largest $N$ elements from $D$.

Let's assume we rewrite $X$ cards. Then, it's optimal to rewrite the smallest $X$ cards as the source and choose the largest $X$ cards as the destination. Since shifting $X$ doesn't change the source and destination except by one each time, we can solve this in $O(M \log M + N \log N)$ time by traversing $X$ sequentially.

In implementation, it might be challenging to select and extract the largest $N$ elements from $D$. An easier approach would be to sort $(B_1, C_1), \cdots ,(B_M, C_M)$ in descending order of $C_i$ and add one card for each $C_i$ up to $B_i$ until the size of array $D$ is less than $N$.

You can also determine the optimal value of $X$. Sort $A$ and $D$ such that $A_1 \le A_2 \le \cdots \le A_N$ and $D_1 \ge D_2 \ge \cdots \ge D_{|D|}$. Then, in the algorithm mentioned above, the total value changes by $D_i - A_i$ by shifting $X$ from $i-1$ to $i$. Since $D_i - A_i$ is non-decreasing, it's optimal to continue the operation as long as $D_i - A_i \ge 0$, or equivalently, $D_i \ge A_i$. Thus, the optimal $X$ is the maximum value of such $i$ (or $0$ if none). 

### Alternative Solution

We consider selecting $N$ integers to maximize the sum of $N$ integers by choosing $N$ integers to keep and rewrite. Let $(X_1, Y_1), \cdots ,(X_{N+M}, Y_{N+M})$ be $(1, A_1), \cdots ,(1, A_N ),(B_1, C_1), \cdots ,(B_M, C_M)$. Then, the problem becomes "choose $Y_i$ up to $X_i$ times, and find the maximum sum when selecting a total of $N$ integers". It's optimal to select $N$ integers in decreasing order of $Y_i$. This approach allows us to find the solution in $O((N + M) \log(N + M))$ time complexity.

---
$^{*1}$ In C++ language, implementing sorting of pairs $(C_i, B_i)$ in descending order is straightforward. Using a structure would be better if you aim for more readable code.