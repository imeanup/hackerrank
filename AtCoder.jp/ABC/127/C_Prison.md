## C: Prison

<!-- ### 考え方 1

各 $i = 1, 2, \cdots, N$ について、$i$ 番目の $ID$ カードで全てのゲートを通過できるかを考えます。すると、全て の $j = 1, 2, \cdots, M$ について、 $_L_j \le i \le R_j$ であるときに限り $i$ 番目の $ID$ カードで全てのゲートを通過でき ます。このような $i$ の個数を数え上げることで答えを求めることができますが、このままでは時間計算量が $O(NM)$ となり間に合いません。

そこで、各 $i$ について、全ての $j$ について $L_j \le i \le R_j$ が成り立つかを高速に判定したいです。この条
件は、
$$i \ge L_1, L_2, \cdots , L_M$$

かつ
$$i \le R_1, R_2, \cdots , R_M$$

と表すことができます。すなわち、

$$
L′ = \max \{L_1, L_2, \cdots, L_M \} \\
R′ = \min \{R_1, R_2, \cdots , R_M\}
$$

とすると、各条件は $L′ \le i \le R′$ と表すことができます。このような $i$ の個数が答えになります。これは $L′ \le R′$ のとき $R′ − L′ + 1$、そうでないとき $0$ です。時間計算量は $O(M)$ です。

### 考え方 2

全ゲートを通過できる $ID$ カードの番号は区間 (連番) になります。また、全ゲートを通過できる $ID$ カー ドは、$M − 1$ 番目までの全ゲートに通過できる $ID$ カードのうち $M$ 番目のゲートにも通過できるものです。

そこで、$i$ 番目までの全ゲートに通過できる $ID$ カードの番号を $l_i, l_i + 1, \cdots , r_i$ とします。すると、$l_{i+1}, r_{i+1}$ は $l_i, r_i$ から計算できます。初期値も適当に、$l_0 = 1, r_0 = N$ や $l_1 = L_1, r_1 = R_1$ とすれば $l_M, r_M$ を時間計 算量 $O(M)$ で計算することができます。考え方 $1$ と同様に、$l_M \le i \le r_M$ であるような $i$ の個数が答えにな ります。 -->

### Approach 1

For each $i = 1, 2, \cdots, N$, we consider whether all gates can be passed with the $i$-th $\text{ID}$ card. Then, for all $j = 1, 2, \cdots, M$, the $i$-th $\text{ID}$ card can pass all gates only if $L_j \le i \le R_j$. We can find the answer by counting the number of such $i$, but the time complexity would be $O(NM)$ which is not feasible.

To speed up the process, we want to quickly determine whether the condition $L_j \le i \le R_j$ holds for each $i$. This condition can be expressed as:

$$i \ge L_1, L_2, \cdots , L_M$$

and

$$i \le R_1, R_2, \cdots , R_M$$

In other words,

$$
L' = \max \{L_1, L_2, \cdots, L_M \} \\
R' = \min \{R_1, R_2, \cdots , R_M\}
$$

So, each condition can be represented as $L' \le i \le R'$. The number of such $i$ becomes the answer. It is $R' - L' + 1$ when $L' \le R'$, otherwise $0$. The time complexity is $O(M)$.

### Approach 2

The numbers of the ID cards that can pass through all gates form intervals (sequences of consecutive numbers). Moreover, an ID card that can pass through all gates must also be able to pass through the $M$-th gate among those that can pass through the first $M-1$ gates.

Therefore, let's denote the numbers of the ID cards that can pass through the first $i$ gates as $l_i, l_i + 1, \cdots , r_i$. Then, $l_{i+1}, r_{i+1}$ can be calculated from $l_i, r_i$. We can initialize them suitably, such as $l_0 = 1, r_0 = N$ or $l_1 = L_1, r_1 = R_1$, and then compute $l_M, r_M$ with a time complexity of $O(M)$. Similar to Approach 1, the number of $i$ such that $l_M \le i \le r_M$ becomes the answer.