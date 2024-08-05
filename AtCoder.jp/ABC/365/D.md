## [D - AtCoder Janken 3](https://atcoder.jp/contests/abc365/tasks/abc365_d) 

<details><summary>Japanese editorial</summary><br>

$dp⁡_i[H] (H \in \{$`R`, `P`, `S`$\})$ を、

* $dp_i[H] := i$ 回目に出した手が $H$ であるような $i$ 回目までの手の出し方で高橋くんが出す手の条件を満たすものに対する、青木くんに勝った回数の最大値

として定義します（ここで、便宜上 $dp_{⁡0}[H]=0$ とします）。

高橋くんが $i$ 回目に出すことができた手は、青木くんが $i$ 回目に出した手と高橋くんが $i-1$ 回目に出した手のみから決まります。

よって、 $dp⁡_i[H] (H \in \{$`R`, `P`, `S`$\})$ は $dp_{⁡i−1} ($H \in \{$`R`, `P`, `S`$\})$（および $S_i$ の値）から求めることができます。

具体的には、$janken(a, b)$ を $a$ が $b$ に勝つなら $1$ 、あいこなら $0$ 、負けるなら $-1$ となる関数として、

$$
dp_i[H] = \begin{cases}
\max_{H' \ne H} dp_{i-1}[H'] & (janken(H, S_i) = 0) \\
1+\max_{H' \ne H} dp_{i-1}[H'] & (janken(H, S_i) = 1) \\
0 & (janken(H, S_i) = -1)
\end{cases}
$$

とするとよいです（負けるときの DP テーブルの値を $\infty$ にしてもよいですが、$0$ としても正しい値が得られることが証明できます）。

実装例は以下のようになります。

<details><summary>C++</summary><br>

```cpp
#include <iostream>
#include <array>
#include <algorithm>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;
    string S;
    cin >> S;

    array<unsigned, 3> dp{};
    auto&& [rock, scissors, paper]{dp};

    for(const auto c : S){
        // 直前に出していなかった手を出すことができる
        dp = {max(scissors, paper), max(rock, paper), max(rock, scissors)};
        // 負ける手を出すことはできない = 勝ち数の最大値を 0 にする
        // 勝つ手を出したら最大値 +1
        if (c == 'R') {
            scissors = 0;
            ++paper;
        } else if (c == 'S') {
            paper = 0;
            ++rock;
        } else if (c == 'P') {
            rock = 0;
            ++scissors;
        }
    }

    cout << ranges::max(dp) << endl;

    return 0;
}

```

</details>

</details>

#### English


Define $dp_i[H] (H \in \{$`R`, `P`, `S`$\})$ as:

* $dp_i[H] := i$ The maximum number of times Aoki has been defeated by Takahashi up to the $i$-th move, given that the move on the $i$-th turn was $H$ and all conditions of Takahashi's moves are satisfied.

Here, for convenience, we set $dp_{⁡0} [H]=0$.

The move Takahashi can make on the $i$-th turn is determined only by the move Aoki made on the $i$-th turn and the move Takahashi made on the $(i-1)$-th turn.

Therefore, $dp⁡_i[H] (H \in \{$`R`, `P`, `S`$\})$ can be derived from $dp_{⁡i−1} (H \in \{$`R`, `P`, `S`$\})$ and the value of $S_i$.

Specifically, let $janken(a, b)$ be a function that returns $1$ if $a$ wins against $b$, $0$ if it's a draw, and $-1$ if $a$ loses to $b$. Then,

$$
dp_i[H] = \begin{cases}
\max_{H' \ne H} dp_{i-1}[H'] & (janken(H, S_i) = 0) \\
1+\max_{H' \ne H} dp_{i-1}[H'] & (janken(H, S_i) = 1) \\
0 & (janken(H, S_i) = -1)
\end{cases}
$$

(This approach works even if we set the value of the DP table when losing to $\infty$, but it can be proven that setting it to $0$ will still yield the correct value).

An implementation example is as follows.

<details><summary>C++</summary><br>

```cpp
#include <iostream>
#include <array>
#include <algorithm>

int main() {
    using namespace std;
    unsigned N;
    cin >> N;
    string S;
    cin >> S;

    array<unsigned, 3> dp{};
    auto&& [rock, scissors, paper]{dp};

    for(const auto c : S){
        // You can make a move that was not made immediately before
        dp = {max(scissors, paper), max(rock, paper), max(rock, scissors)};
        // You cannot make a losing move = set the maximum win count to 0
        // If you make a winning move, increase the maximum value by 1
        if (c == 'R') {
            scissors = 0;
            ++paper;
        } else if (c == 'S') {
            paper = 0;
            ++rock;
        } else if (c == 'P') {
            rock = 0;
            ++scissors;
        }
    }

    cout << ranges::max(dp) << endl;

    return 0;
}

```

</details>
