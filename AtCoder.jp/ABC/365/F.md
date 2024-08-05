## [F - Takahashi on Grid](https://atcoder.jp/contests/abc365/tasks/abc365_f) 

<details style="border: 1px solid black; padding: 10px;"><summary>Japanese editorial</summary><br>

まず、必要に応じて swap を行うことで $s_{x,i} \le t_{x,i}$ として構いません。

高橋くんは次のアルゴリズムに従って移動することで行動回数を最小にすることができます。

* はじめ、高橋くんがいるマスを $(x,y)=(s_{x,i},s_{y,i})$ とする。
* $x < t_{x,i}$ である限り、次を繰り返す。
  * $y < L_{x+1}$ ならマス $(x,y+1)$ に移動する。
  * $L_{x+1} \le y \le U_{x+1}$ ならマス $(x+1,y)$ に移動する。
  * $U_{x+1} < y$ ならマス $(x,y−1)$ に移動する。
* $y \ne t_{y,i}$ である限り、適切に移動する。

詳細な証明を述べることはしませんが、$x$ 方向の移動が可能なら先にしてしまって損をしないことをいうことで示すことができます。

このアルゴリズムのもとで、高橋くんが $x=A−1$ からスタートして $x=B$ へ移動することを考えます。 $y \in \Z$ について、高橋くんがマス $(A−1,y)$ にいる状態から上のアルゴリズムをはじめ、はじめて $x=B$ となったときのマスを $(B,f_{[A,B]}(y))$ とし、行動した回数を $g_{[A,B]}(y)$ とします（便宜上、$(A−1,y)$ はすべて空きマスとして扱います）。

このとき、ある $f=[f_L,f_U],g=[g_L,g_U] ,C$ が存在し、

* $f_{[A,B]}(y)= \text{clamp⁡}(y,f_L,f_U)$
* $g_{[A,B]}(y)= C + \max \{0, g_{L} - y, y − g_{U} \}$
* $f_L \ne f_U \vee g_L \ne g_U \implies f=g$


を満たします（ここで、$\text{clamp⁡} (x, a, b) := \min \{ \max⁡ \{x,a\},b\}$ です）。

<details style="border: 1px solid black; padding: 10px;"><summary>証明</summary><br>

区間 $[A,B]$ の幅についての帰納法によって示します。

$A=B$ のとき、$f = g = [L_B,U_B], C=1$ とすると条件を満たします。

$A < B$ のとき、$$f_{[A,B]}(y)= \text{clamp⁡}(f_{[A,B−1]}(y), L_B, U_B)$$

および

$$
g_{[A,B]}(y)= 1 + g_{[A,B−1]}(y) + \max \{0,L_B − f_{[A,B−1]}(y), f_{[A,B−1]}(y) − U_B \}
$$ 

が成り立ちます。

帰納法の仮定より、$f_{[A,B−1]} ,g_{[A,B−1]}$ に対して上の条件を満たす区間 $f,g$ と整数 $C$ を取ることができます。

$\text{clamp}$ 関数は合成について閉じているため、$f_{[A,B]}(y) = \text{clamp⁡}(y, \overline{f}_L,\overline{f}_U)$ なる $\overline{f} = [\overline{f}_L, \overline{f}_U]$ が存在します。

$\overline{f}_L \ne \overline{f}_U$ ならば $\overline{f} = f \cap [L_B,U_B]$ が成り立ち、$f_L \ne f_U$ が必要なので $f = g$ が成り立ちます。 $f_L,f_U,L_B,U_B$ と $y$ との大小関係を考えることで $g_{[A,B]}(y) = \rm C + 1 + \max⁡\{0,\overline{f}_L − y, y − \overline{f}_U \}$ が成り立つことがわかります。

$\overline{f}_{L}= \overline{f}_{U}$ かつ $f_L \ne f_U$ ならば、$f \cap [L_B,U_B] = \emptyset$ です。$f$ と $[L_B,U_B]$ の大小に応じて、$g_L,g_U$ のいずれか一方を $\overline{g}$ として $g_{[A,B]}(y) = \overline{\rm C} + ∣ y − \overline{g}∣$ となります。

$f_L=f_U$ ならば、$f_{[A,B−1]}$ は定数関数です。$g_{[A,B]}$ は $g_{[A,B−1]}$ に定数を足したものとなるので、示されました。

</details><br>

区間 $[A,B]$ に対して $f_{[A,B]}, g_{[A,B]}$ を表す $f,g,\rm C$ を対応させることを考えます。

隣接する区間に対応する $(f_1, g_1, \rm C_1), (f_2,g_2,\rm C_2)$ が与えられたときにそれらを合併した区間に対応する $(f, g, \rm C)$ を高速に求めることができれば、この問題をセグメント木などを用いて解くことができます。

<details style="border: 1px solid black; padding: 10px;"><summary>余談：処理がセグメント木などで扱える条件</summary><br>

隣接する区間の合併に対応する処理がセグメント木で扱えることは、「セグメント木ではモノイドを処理できる」という定式化だけでは説明できません。 ですが、一般に隣接区間の合併に対応する処理はセグメント木などで扱うことができます（圏による定式化が有名です）。

</details><br>

今回の場合は、処理に関して区間が隣接していることを用いていないので、一般の $(f_1,g_1,\rm C_1),(f_2,g_2, \rm C_2)$ に対しても合併が定義できます。 この処理がモノイドになっているため、これを確かめることで「モノイドが乗る」という定式化のもとでセグメント木などで処理できることを確認できます。


具体的には、$f_1= [f_{L, 1}, f_{U, 1}], g_1=[g_{L, 1}, g_{U,1}],f_2=[f_{L,2},f_{U,2}],g_2=[g_{L,2},g_{U,2}]$ とすると、$$f =[\text{clamp⁡}(f_{L,1},f_{L,2},f_{U,2}),\text{clamp⁡}(f_{U,1},f_{L,2}, f_{U,2})]$$ および $$g =[\text{clamp⁡}(g_{L,2}, g_{L,1}, g_{U,1}), \text{clamp⁡}(g_{U,2},g_{L,1}, g_{U,1})]$$ と計算することができます。 $\rm C$ については、$y = g_L$ としたときの移動回数が求める $C$ になります。

よって、区間の合併は $O(1)$ 時間でできることがわかりました。

列に対して更新がないためより高速なデータ構造を用いることもできますが、セグメント木を用いた $O(N+ Q\log ⁡N)$ 時間などで十分高速です。

実装例は以下のようになります。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <atcoder/segtree>

int main() {
    using namespace std;
    // x の区間 [A, B] に入って出ていくときの動きとコストを表す構造
    // 入るときの y 座標の値を入れると (出るときの y 座標, 移動回数) を返す
    struct block{
        unsigned fL, fU;
        unsigned gL, gU;
        unsigned long C;
        pair<unsigned, unsigned long> operator()(unsigned y) const {
            return {clamp(y, fL, fU), C + max(y, gL) - min(y, gU)};
        }
    };
    // セグメント木の定義
    // 二項演算は区間の合併
    using segment_tree = atcoder::segtree<block, [](const block& lhs, const block& rhs) -> block {
        // 区間の合併はがんばる
        const auto new_fL{clamp(lhs.fL, rhs.fL, rhs.fU)}, new_fU{clamp(lhs.fU, rhs.fL, rhs.fU)};
        const auto new_gL{clamp(rhs.gL, lhs.gL, lhs.gU)}, new_gU{clamp(rhs.gU, lhs.gL, lhs.gU)};
        const auto new_C{lhs.C + rhs(lhs(new_gU).first).second};
        return {new_fL, new_fU, new_gL, new_gU, new_C};
    }, []{
        // 単位元は全面素通し
        return block{0, 1000000001, 0, 1000000001, 0};
    }>;

    unsigned N;
    cin >> N;
    vector<block> intervals(N);
    for(auto&& [fL, fU, gL, gU, C] : intervals){
        unsigned L, U;
        cin >> L >> U;
        // [L, U] が空いている列に対応する値を作る
        fL = gL = L;
        fU = gU = U;
        C = 1;
    }
    segment_tree seg_tree{intervals};

    unsigned Q;
    cin >> Q;
    for(unsigned i{}; i < Q; ++i){
        unsigned sx, sy, tx, ty;
        cin >> sx >> sy >> tx >> ty;
        if (sx > tx){
            swap(sx, tx);
            swap(sy, ty);
        }
        // [sx, tx] に sy から入ったときの (出てくる y 座標, 移動回数)
        const auto& [out, cost]{seg_tree.prod(sx, tx)(sy)};
        // 最後に y 座標を調節して出力
        cout << max(out, ty) - min(out, ty) + cost << endl;
    }

    return 0;
}
```

</details><br>


First, if necessary, perform swaps so that $s_{x,i} \le t_{x,i}$.

Takahashi can minimize the number of moves by following this algorithm:

* Initially, Takahashi is at cell $(x,y) = (s_{x,i}, s_{y,i})$.
* As long as $x < t_{x,i}$, repeat the following:
  * If $y < L_{x+1}$, move to cell $(x, y+1)$.
  * If $L_{x+1} \le y \le U_{x+1}$, move to cell $(x+1, y)$.
  * If $U_{x+1} < y$, move to cell $(x, y-1)$.
* As long as $y \ne t_{y,i}$, move accordingly.

While we won't go into a detailed proof, it can be shown that if moving in the $x$ direction is possible, doing so first will not be disadvantageous.

Under this algorithm, consider Takahashi starting from $x = A-1$ and moving to $x = B$. For $y \in Z$, starting from cell $(A-1, y)$ and applying the above algorithm until $x$ first becomes $B$, let the cell be $(B, f_{[A,B]}(y))$ and the number of moves be $g_{[A,B]}(y)$ (for convenience, all cells $(A-1, y)$ are treated as empty).

In this case, there exist some $f=[f_L,f_U], g=[g_L,g_U], C$ such that:

* $f_{[A,B]}(y)= \text{clamp}(y, f_L, f_U)$
* $g_{[A,B]}(y)= C + \max \{0, g_{L} - y, y - g_{U} \}$
* $f_L \ne f_U \vee g_L \ne g_U \implies f=g$

Here, $\text{clamp}(x, a, b) := \min \{ \max \{x, a\}, b\}$.

<details style="border: 1px solid black; padding: 10px;"><summary>Proof</summary><br>

We prove this by induction on the width of the interval $[A,B]$.

When $A=B$, if we set $f = g = [L_B, U_B], C=1$, the conditions are satisfied.

When $A < B$,
$$f_{[A,B]}(y)= \text{clamp}(f_{[A,B-1]}(y), L_B, U_B)$$

and

$$
g_{[A,B]}(y)= 1 + g_{[A,B-1]}(y) + \max \{0, L_B - f_{[A,B-1]}(y), f_{[A,B-1]}(y) - U_B \}
$$ 

By the induction hypothesis, there exist intervals $f, g$ and an integer $C$ that satisfy the above conditions for $f_{[A,B-1]}, g_{[A,B-1]}$.

Since the clamp function is closed under composition, there exists $\overline{f} = [\overline{f}_L, \overline{f}_U]$ such that $f_{[A,B]}(y) = \text{clamp}(y, \overline{f}_L, \overline{f}_U)$.

If $\overline{f}_L \ne \overline{f}_U$, then $\overline{f} = f \cap [L_B, U_B]$ holds, and since $f_L \ne f_U$ is necessary, $f = g$. Considering the relationships between $f_L, f_U, L_B, U_B$, and $y$, we see that $g_{[A,B]}(y) = \rm C + 1 + \max \{0, \overline{f}_L - y, y - \overline{f}_U \}$.

If $\overline{f}_L = \overline{f}_U$ and $f_L \ne f_U$, then $f \cap [L_B, U_B] = \emptyset$. Depending on the relationship between $f$ and $[L_B, U_B]$, $g_L$ or $g_U$ will be $\overline{g}$, and $g_{[A,B]}(y) = \overline{\rm C} + |y - \overline{g}|$.

If $f_L = f_U$, then $f_{[A,B-1]}$ is a constant function. Since $g_{[A,B]}$ is $g_{[A,B-1]}$ plus a constant, it has been shown.

</details><br>

Consider associating $f_{[A,B]}, g_{[A,B]}$ with $f, g, \rm C$ for the interval $[A,B]$.

If we can quickly determine $(f, g, \rm C)$ corresponding to the merged interval of adjacent intervals $(f_1, g_1, \rm C_1), (f_2, g_2, \rm C_2)$, we can solve this problem using segment trees or similar data structures.

<details style="border: 1px solid black; padding: 10px;"><summary>Note: Conditions for Handling with Segment Trees</summary><br>

The fact that the merging process corresponding to adjacent intervals can be handled with segment trees cannot be explained simply by saying "monoids can be processed with segment trees". However, in general, the merging process corresponding to adjacent intervals can be handled with segment trees (this is famously formalized in terms of category theory).

</details><br>

In this case, since the processing does not use the fact that the intervals are adjacent, merging can be defined for general $(f_1, g_1, \rm C_1), (f_2, g_2, \rm C_2)$. Since this processing forms a monoid, we can verify that it can be handled with segment trees under the formalization of "monoids".

Specifically, for $f_1= [f_{L, 1}, f_{U, 1}], g_1=[g_{L, 1}, g_{U,1}], f_2=[f_{L,2},f_{U,2}], g_2=[g_{L,2},g_{U,2}]$, we can compute
$$f =[\text{clamp}(f_{L,1}, f_{L,2}, f_{U,2}), \text{clamp}(f_{U,1}, f_{L,2}, f_{U,2})]$$ 
and
$$g =[\text{clamp}(g_{L,2}, g_{L,1}, g_{U,1}), \text{clamp}(g_{U,2}, g_{L,1}, g_{U,1})]$$ 
$\rm C$ can be determined by the number of moves required when $y = g_L$.

Therefore, merging intervals can be done in $O(1)$ time.

Since there are no updates to the sequence, faster data structures can be used, but using a segment tree with $O(N + Q\log N)$ time complexity is sufficiently fast.

An implementation example is as follows.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <atcoder/segtree>

int main() {
    using namespace std;
    // Structure representing the movement and cost when entering and exiting the interval [A, B] for x
    // Takes the y-coordinate value when entering and returns (y-coordinate when exiting, number of moves)
    struct block{
        unsigned fL, fU;
        unsigned gL, gU;
        unsigned long C;
        pair<unsigned, unsigned long> operator()(unsigned y) const {
            return {clamp(y, fL, fU), C + max(y, gL) - min(y, gU)};
        }
    };
    // Definition of the segment tree
    // The binary operation is the merging of intervals
    using segment_tree = atcoder::segtree<block, [](const block& lhs, const block& rhs) -> block {
        // Merging intervals is done with effort
        const auto new_fL{clamp(lhs.fL, rhs.fL, rhs.fU)}, new_fU{clamp(lhs.fU, rhs.fL, rhs.fU)};
        const auto new_gL{clamp(rhs.gL, lhs.gL, lhs.gU)}, new_gU{clamp(rhs.gU, lhs.gL, lhs.gU)};
        const auto new_C{lhs.C + rhs(lhs(new_gU).first).second};
        return {new_fL, new_fU, new_gL, new_gU, new_C};
    }, []{
        // The identity element allows passage through all
        return block{0, 1000000001, 0, 1000000001, 0};
    }>;

    unsigned N;
    cin >> N;
    vector<block> intervals(N);
    for(auto&& [fL, fU, gL, gU, C] : intervals){
        unsigned L, U;
        cin >> L >> U;
        // Create the value corresponding to an empty column [L, U]
        fL = gL = L;
        fU = gU = U;
        C = 1;
    }
    segment_tree seg_tree{intervals};

    unsigned Q;
    cin >> Q;
    for(unsigned i{}; i < Q; ++i){
        unsigned sx, sy, tx, ty;
        cin >> sx >> sy >> tx >> ty;
        if (sx > tx){
            swap(sx, tx);
            swap(sy, ty);
        }
        // (y-coordinate when exiting, number of moves) when entering from sy at [sx, tx]
        const auto& [out, cost]{seg_tree.prod(sx, tx)(sy)};
        // Finally adjust the y-coordinate and output
        cout << max(out, ty) - min(out, ty) + cost << endl;
    }

    return 0;
}
```
