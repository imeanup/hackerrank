## [F - Operate K](https://atcoder.jp/contests/abc386/tasks/abc386_f) 

この問題で文字列を $S$ から $T$ に変換するのに必要な最小の操作回数 $d(S,T)$ は、**[レーベンシュタイン距離](https://ja.wikipedia.org/wiki/%E3%83%AC%E3%83%BC%E3%83%99%E3%83%B3%E3%82%B7%E3%83%A5%E3%82%BF%E3%82%A4%E3%83%B3%E8%B7%9D%E9%9B%A2)** や **編集距離** といった名前でよく知られています。
この問題は、「 $d(S,T) \le K$ か判定せよ」と言い換えられます。

編集距離の求め方として、次のような DP がよく知られています。(検索すれば非常に多くの解説がヒットします)

> $dp[i][j]=$ { $S$ の先頭 i**i** 文字からなる文字列と $T$ の先頭 j**j** 文字からなる文字列との編集距離 } としたい。
>
> $dp[0][0]=0$ 、その他の $i,j$ について $dp[i][j]= \infty$ から始め、 $i,j$ 昇順の 2 重ループ中で次のように遷移する。
>
> * $dp[i][j] = \min⁡(dp[i−1][j]+1, dp[i][j−1]+1, dp[i−1][j−1]+C)$
>   * $C = 0$,  if $S_i = T_j$
>   * $C = 1$, otherwise
>
> 以上の DP を行うと、所望の DP テーブルが得られる。

これで、この問題を時間計算量 $O(|S||T|)$ で解けました。
しかし、今回の制約上この解法では実行時間制限に間に合いません。

ただ、この解法を少し変えることでこの問題に正解できます。

今回の問題で問われているものは、 $d(S,T) \le K$ かどうかであり、更に $K \le 20$ と制約されています。
例えば、 $dp[10][50]$ のようなものを考えてみましょう。これは $S$ の先頭 $10$ 文字からなる文字列と $T$ の先頭 $50$ 文字からなる文字列との編集距離ですが、文字列の長さを合わせる必要があることから、 (文字列によらず) この値は $40$ 以上です。

DP 中で遷移を行った際に遷移元から遷移先へと動く時に値が小さくなることはないので、 $K\le 20$ と制約されている状況下で「 $d(S,T) \le K$ か?」という判定を行うのに $dp[10][50]$ のように明らかに $K$ を超えている場所を調べる必要はないことが分かります。

すると、各 $dp[i]$ について $dp[i][i−K]$ から $dp[i][i+K]$ の範囲のみを正しく計算していれば 、その範囲外を $dp[i][j]= \infty$ と見なすことで「 $d(S,T) \le K$ か? 」の判定問題を解けることも分かります。
このように DP テーブルの一部のみを正確に計算することで、この問題に時間計算量 $O(|S|K)$ で正解できます。実装上は $S$ と $T$ の長さの差が $K$ を超えるケースに注意してください。

---

The minimum number of operations $d(S, T)$ required to transform the string $S$ into $T$ is commonly known as the **Levenshtein distance** or **edit distance**. This problem can be rephrased as: "Determine if $d(S, T) \le K$".

To compute the edit distance, a well-known dynamic programming (DP) approach is as follows. (Many explanations can be found online with a quick search.)

> Let $dp[i][j]$ represent the edit distance between the first $i$ characters of $S$ and the first $j$ characters of $T$.
>
> Initialize $dp[0][0] = 0$, and for all other $i, j$, initialize $dp[i][j] = \infty$. Then, update the DP table using a double loop with $i$ and $j$ in ascending order, as follows:
>
> * $dp[i][j] = \min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + C)$
>   * $C = 0$, if $S_i = T_j$
>   * $C = 1$, otherwise
>
> After running this DP, the desired DP table will be obtained.

Using this approach, the problem can be solved in $O(|S| |T|)$ time. However, given the problem's constraints, this solution won’t meet the time limit.

However, a slight modification of this approach allows us to solve the problem correctly.

The key question in this problem is whether $d(S, T) \le K$, with the additional constraint that $K \le 20$. 

For example, consider $dp[10][50]$, which represents the edit distance between the first 10 characters of $S$ and the first 50 characters of $T$. Since the lengths of the strings must match, this value will be at least 40, regardless of the actual strings.

Once we perform a transition in the DP process, the value never decreases as we move from the source to the target. Therefore, in the context of $K \le 20$, we don’t need to check places like $dp[10][50]$, which clearly exceed $K$.

Thus, for each $dp[i]$, it is enough to compute the values within the range $dp[i][i-K]$ to $dp[i][i+K]$ correctly, and treat values outside this range as $dp[i][j] = \infty$. This allows us to solve the "Is $d(S, T) \le K$?" problem efficiently.

By calculating only a part of the DP table accurately, we can solve the problem in $O(|S| K)$ time. In the implementation, special attention should be given to cases where the difference in the lengths of $S$ and $T$ exceeds $K$.
