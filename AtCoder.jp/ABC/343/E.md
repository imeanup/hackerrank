
## [E - 7x7x7](https://atcoder.jp/contests/abc343/tasks/abc343_e)

<details><summary>Japanese Editorial</summary><br>

**解説**

---

領域同士の相対的な位置関係だけが大事なので、$1$ つの領域の位置を固定してしまっても問題ありません。以下、$C_1$ の位置を $a_1 = b_1 = c_1 = 0$ と固定します。

ここで、以下の事実が成り立ちます。

* 事実：「$C_1$ と $C_i (i = 2, 3)$ は共通部分を持つ（体積が正の領域を共有するか、辺や頂点で接するかのいずれかである）」という条件を追加しても、解の存在性には影響を与えない（つまり、元の問題において解が存在するならば、この条件を追加したとしても解が必ず存在する）。

なぜなら、$C_1$ と $C_i$ が共通部分を持たない場合、 $V_1, V_2, V_3$ の値を変えることなく、$C_i$ を $C_1$ と接する位置まで移動させることができるからです。「$C_1$ と $C_2$、$C_2$ と $C_3$ がそれぞれ共通部分を持ち、$C_1$ と $C_3$ は共通部分を持たない」のようなケースにおいては $C_3$ を動かせない可能性があるのではないかと思われるかもしれませんが、その場合、$C_1$ と $C_2$ の位置を交換し、$a_1 = b_1 = c_1 = 0$ となるように全体を平行移動してしまえば問題ありません。

この事実によれば、$a_2, b_2, c_2, a_3, b_3, c_3$ の絶対値は $7$ 以下としてしまってよく、考えられる候補は $15^6 \approx 10^7$ 通り程度になります。あとは、 $a_2, b_2, c_2, a_3, b_3, c_3$ の値を $1$ つ固定したとき、ちょうど $1$ 個 / $2$ 個 / $3$ 個の立方体に含まれる領域の体積が高速に求められればよいです。

まず前提として、$2$ つの立方体 $C_i, C_j$ の共通部分の体積 $V(C_i \cap C_j)$は、共通部分を表す式が

* $\max\{a_i, a_j\} \le x \le \min\{a_i + 7, a_j + 7\}$ かつ
* $\max\{b_i, b_j\} \le y \le \min\{b_i+7, b+j+7\}$ かつ
* $\max\{c_i, c_j\} \le z \le \min\{c_i+7, c_j+7\}$

であることから、 $\max\{0, \min\{a_i, a_j\} + 7 - \max\{a_i, a_j\}\} \times \max\{0, \min\{b_i, b_j\} + 7 - \max\{b_i, b_j\}}\times \max\{0, \min\{c_i, c_j\} + 7 -\max\{c_i, c_j\}\}$ と求めることができます。

$3$ つの立方体 $C_i, C_j, C_k$ の共通部分の体積 $V(C_i \cap C_j \cap C_k)$ についても同様です。

次に、ちょうど $i$ 個の立方体に含まれる領域の体積を $v_i$ としたとき、$v_1, v_2, v_3$ は包除原理のような考え方を用いて以下のように求められます。

* $v_3 = V(C_1\cap C_2 \cap C_3)$
* $v_2 = V(C_1 \cap C_2) + V(C_1 \cap C_3) + V(C_2 \cap C_3) - 3v_3$
* $v_1 = 3\times 7^3 - 2v_2 - 3v_3$

よって、$a_2, b_2, c_2, a_3, b_3, c_3$ の候補全てに対して上述の方法で $v_1, v_2, v_3$ を求め、$V_1, V_2, V_3$ と一致するかを確認することで本問題を解くことができます。

##### おまけ

実は、$a_2, b_2, c_2, a_3, b_3, c_3$ の値の探索範囲は $[-1, 7]$ まで絞っても問題ないことが実験的に示せます。立方体の一辺の長さへの依存性や理論的証明の有無については不明です。

実装例 (C++) :

</details><br>

### Explanation

---

Since only the relative positions between the regions matter, we can fix the position of one region without any problem. Below, we fix the position of $C_1$ at $a_1 = b_1 = c_1 = 0$.

Here, the following fact holds:

* Fact: Adding the condition that “$C_1$ and $C_i$ (for $i = 2, 3$) share a common part (either sharing a positive volume region or touching at an edge or vertex)” does not affect the existence of a solution (i.e., if a solution exists in the original problem, a solution will still exist even with this additional condition).

This is because, if $C_1$ and $C_i$ do not share a common part, $C_i$ can be moved to a position touching $C_1$ without changing the values of $V_1, V_2, V_3$. You might think that in cases where “$C_1$ and $C_2$ share a common part, and $C_2$ and $C_3$ share a common part, but $C_1$ and $C_3$ do not share a common part,” it might not be possible to move $C_3$. However, in such cases, swapping the positions of $C_1$ and $C_2$ and then translating the entire configuration so that $a_1 = b_1 = c_1 = 0$ will resolve the issue.

According to this fact, the absolute values of $a_2, b_2, c_2, a_3, b_3, c_3$ can be at most 7, resulting in approximately $15^6 \approx 10^7$ candidates. After this, when fixing the values of $a_2, b_2, c_2, a_3, b_3, c_3$, it suffices to quickly calculate the volume of the regions included in exactly 1, 2, or 3 cubes.

First, as a premise, the volume of the intersection of two cubes $C_i$ and $C_j$, $V(C_i \cap C_j)$, can be obtained from the following expression representing the intersection:

* $\max\{a_i, a_j\} \le x \le \min\{a_i + 7, a_j + 7\}$ and
* $\max\{b_i, b_j\} \le y \le \min\{b_i + 7, b_j + 7\}$ and
* $\max\{c_i, c_j\} \le z \le \min\{c_i + 7, c_j + 7\}$,

which results in

$$
\max\{0, \min\{a_i + 7, a_j + 7\} - \max\{a_i, a_j\}\} \times \max\{0, \min\{b_i + 7, b_j + 7\} - \max\{b_i, b_j\}\} \times \max\{0, \min\{c_i + 7, c_j + 7\} - \max\{c_i, c_j\}\}.
$$

The same logic applies to the volume of the intersection of three cubes $C_i, C_j, C_k$, $V(C_i \cap C_j \cap C_k)$.

Next, when defining the volume of regions included in exactly $i$ cubes as $v_i$, $v_1, v_2, v_3$ can be calculated using the principle of inclusion-exclusion as follows:

* $v_3 = V(C_1 \cap C_2 \cap C_3)$
* $v_2 = V(C_1 \cap C_2) + V(C_1 \cap C_3) + V(C_2 \cap C_3) - 3v_3$
* $v_1 = 3 \times 7^3 - 2v_2 - 3v_3$

Thus, by calculating $v_1, v_2, v_3$ for all candidates of $a_2, b_2, c_2, a_3, b_3, c_3$ using the above method, we can check if they match $V_1, V_2, V_3$, and solve the problem.

##### Extra

It can be experimentally shown that the search range for $a_2, b_2, c_2, a_3, b_3, c_3$ can be narrowed down to $[-1, 7]$ without any problem. The dependency on the cube edge length or theoretical proof is unclear.

**Example implementation:**

<details><summary><b>C++</b></summary>

```cpp
#include<bits/stdc++.h>

using namespace std;

int f(int a1, int b1, int c1, int a2, int b2, int c2) {
    int res = 1;
    res *= max(0, min(a1, a2) + 7 - max(a1, a2));
    res *= max(0, min(b1, b2) + 7 - max(b1, b2));
    res *= max(0, min(c1, c2) + 7 - max(c1, c2));
    return res;
}

int f(int a1, int b1, int c1, int a2, int b2, int c2, int a3, int b3, int c3) {
    int res = 1;
    res *= max(0, min({a1, a2, a3}) + 7 - max({a1, a2, a3}));
    res *= max(0, min({b1, b2, b3}) + 7 - max({b1, b2, b3}));
    res *= max(0, min({c1, c2, c3}) + 7 - max({c1, c2, c3}));
    return res;
}

int main() {
    int v1, v2, v3;
    cin >> v1 >> v2 >> v3;
    for (int a2 = -7; a2 <= 7; a2++) {
        for (int b2 = -7; b2 <= 7; b2++) {
            for (int c2 = -7; c2 <= 7; c2++) {
                for (int a3 = -7; a3 <= 7; a3++) {
                    for (int b3 = -7; b3 <= 7; b3++) {
                        for (int c3 = -7; c3 <= 7; c3++) {
                            int nv3 = f(0, 0, 0, a2, b2, c2, a3, b3, c3);
                            int nv2 = f(0, 0, 0, a2, b2, c2) + f(0, 0, 0, a3, b3, c3) + f(a2, b2, c2, a3, b3, c3) -
                                      nv3 * 3;
                            int nv1 = 3 * 7 * 7 * 7 - nv2 * 2 - nv3 * 3;
                            if (v1 != nv1 or v2 != nv2 or v3 != nv3) continue;
                            printf("Yes\n0 0 0 %d %d %d %d %d %d\n", a2, b2, c2, a3, b3, c3);
                            return 0;
                        }
                    }
                }
            }
        }
    }
    cout << "No" << endl;
}

```

</details>