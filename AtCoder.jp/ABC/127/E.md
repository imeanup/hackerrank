## E: Cell Distance

<!-- $N \times M$ のマス目のうち $K$ マス選ぶ時のマンハッタン距離の和を求めよという問題です。式は明らかに $X$ と $Y$ について独立なので、$X$ の差の絶対値の和と $Y$ の差の絶対値の和をそれぞれ求めることにします。

以下では $X$ の差について考えます。ある $2$ マスの組み合わせを固定したとき、これら以外から $K − 2$ マ ス選ぶ場合全てに $1$ 度ずつこれらの差が寄与するので、この組を固定して考えると $(^{N×M−2}_{K−2})$ 通りあります。

さらに、$X$ が同じ場合は差が $0$ なので、$X$ が異なると仮定すると、$X$ の差の絶対値が $d$ となるように $2$ マ ス選ぶ方法は $(N − d) × M^2$ 通りあります。これを全ての $d$ に対して足し合わせると $X$ についての答えが 求まります。$Y$ についても $N$ と $M$ を入れ替えると同様に解くことができ、時間計算量としては二項係数を 求めるパートがボトルネックとなり $O(NM)$ でこの問題が解けました。 -->

This problem asks for the sum of Manhattan distances when selecting $K$ cells out of an $N \times M$ grid. Since the equation clearly depends independently on $X$ and $Y$, we'll calculate the sum of absolute differences for $X$ and $Y$ separately.

Let's consider the differences in $X$. When fixing a pair of two cells, each pair contributes to the sum of differences for the remaining $K - 2$ cells exactly once. Therefore, when considering fixed pairs, there are ${N \times M - 2 \choose K - 2}$ possibilities.

Furthermore, when $X$ is the same, the difference is $0$. So, assuming $X$ is different, there are $(N - d) \times M^2$ ways to select pairs with an absolute difference of $d$. Summing this over all possible values of $d$ gives the answer for $X$. Similarly, by swapping $N$ and $M$ for $Y$, we can solve for $Y$. The computational bottleneck lies in calculating binomial coefficients, and with a time complexity of $O(NM)$, this problem can be solved.