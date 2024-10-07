## [E - Sensor Optimization Dilemma 2](https://atcoder.jp/contests/abc374/tasks/abc374_e)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese</b></summary><br>

この問題は、 $W$ の「最小値を最大化」する問題です。

競技プログラミングにおいて、「最小値を最大化」(または「最大値を最小化」) する問題は、答えとなる値を仮に決め打って、その値が達成可能かを判定しながら二分探索する (いわゆる **決め打ち二分探索** ) テクニックがしばしば有効です。

現に、今回は決め打ち二分探索を用いてこの問題を解くことができます。 以下の判定問題を解くことを考えましょう。

> 予算を $X$ 円までかけることができるとき、製造能力を $w$ 以上にできるか?

この問題を解くためには、全ての $i$ について $W_i \ge w$ とするための最小の金額を求めれば良いことになります。以降、次の問題を考えます。

> 工程 $i$ で製品を $w$ 個以上処理できるようにするためにかかる最小の費用はいくらか?

実は、以下の事柄が成り立ちます。

> 工程 $i$ を $w$ 個以上処理できる機械の導入方法のうち最小の金額を達成するものでは、次の少なくとも一方が満たされる。
>
> * 機械 $S_i$ が $B_i$ 台以下しか導入されない。
> * 機械 $T_i$ が $A_i$ 台以下しか導入されない。

証明:
上記を言い換えると、次のようになります。

* 最適解において、機械 $S_i, T_i$ のどちらかについて、 $A_i B_i$ 個分以下の処理能力しか持たせなくて良い。

$B_i$ 台の機械 $S_i$ と $A_i$ 台の機械 $T_i$ はどちらも $A_i B_i$ 個分の処理能力であり、この $2$ つは相互に交換可能である。ならば、この $2$ つのうちコストの安いものに交換できる限り交換すればよい。このことを言い換えると上記の事柄となる。

この事柄を使うことで、「機械 $S_i$ の個数を $B_i$ 以下で全探索」「機械 $T_i$ の個数を $A_i$ 以下で全探索」するとこの問題を時間計算量 $O(A_i + B_i)$ で解くことができます。

元の問題に戻ります。 元の問題は以下の構造で解くことができます。

* この問題の答え $w$ を二分探索する。
  * 全ての $i=1,2,\dots ,N$ について、 $W_i \ge w$ とするための最小金額を足し合わせる。
  * その金額が $X$ 以下なら答えは $w$ 以上であり、そうでないとき答えは $w$ 未満である。

制約から、答えは $10^9$ 以下であることが証明できるので、この範囲で二分探索すればよいです。

時間計算量は $O(N(A_i+B_i)\log ⁡(X(A_i+B_i)))$ です。

</details><br>

This problem is about "maximizing the minimum value" of $W$.

In competitive programming, problems involving "maximizing the minimum value" (or "minimizing the maximum value") can often be solved using a technique known as **binary search on the answer**. This involves fixing a tentative value for the answer and then determining if it is achievable.

Indeed, this problem can be solved using binary search on the answer. Let's consider solving the following decision problem:

> Can the production capacity be increased to at least $w$ if the budget is limited to $X$ yen?

To solve this, we need to find the minimum cost required to ensure $W_i \ge w$ for all $i$. Now, consider the following problem:

> What is the minimum cost required to ensure that the production process $i$ can handle at least $w$ units?

In fact, the following holds true:

> In the method that achieves the minimum cost for making process $i$ handle at least $w$ units, at least one of the following conditions will be satisfied:
>
> * No more than $B_i$ units of machine $S_i$ are introduced.
> * No more than $A_i$ units of machine $T_i$ are introduced.

Proof: 
Rephrased, this means:

* In the optimal solution, it is sufficient to limit the capacity of either machine $S_i$ or machine $T_i$ to no more than $A_i B_i$ units.

Both $B_i$ units of machine $S_i$ and $A_i$ units of machine $T_i$ provide a processing capacity of $A_i B_i$, and these two are interchangeable. Therefore, it is optimal to replace one with the cheaper option as long as possible. This rephrasing leads to the above condition.

By using this condition, we can solve the problem for each $i$ in time complexity $O(A_i + B_i)$ by exhaustively searching for the number of machines $S_i$ (limited to $B_i$) and the number of machines $T_i$ (limited to $A_i$).

Returning to the original problem, it can be solved with the following structure:

* Perform a binary search for the answer $w$.
  * For each $i = 1, 2, \dots, N$, calculate the minimum cost to ensure $W_i \ge w$.
  * If the total cost is less than or equal to $X$, the answer is at least $w$; otherwise, the answer is less than $w$.

Based on the constraints, it can be proven that the answer is less than or equal to $10^9$, so we can perform binary search within this range.

The time complexity is $O(N(A_i + B_i) \log(X(A_i + B_i)))$.
