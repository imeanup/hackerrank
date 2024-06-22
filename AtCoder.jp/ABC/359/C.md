## [C - Tile Distance 2](https://atcoder.jp/contests/abc359/tasks/abc359_c)

> [Link](https://atcoder.jp/contests/abc359/editorial/10264)

<details><summary>Japanese Editorial</summary><br>

簡単のため、スタートとゴールはタイルの左側にあることにしてよいです（つまり、$S_x + S_y$ が奇数なら $S_x$ を $1$ 減らしておきます）。

<details><summary>論理的な導出</summary><br>

タイルの左側と右側は自由に行き来できるので、左側を出発して左側へ到着する移動を一塊として考えます。

交通量を $1$ 支払うことで次の $2$ つの行動のどちらかができます。

* 上下方向に $1$ 移動し、左右方向に $1$ 移動する
* 左右方向に $2$ 移動する

前者を $a$ 回、後者を $b$ 回 $(0 \le a, 0 \le b)$ 行うことで $(S_x, S_y)$ から $(T_x, T_y)$ へ移動できたとします。

このとき、次が成り立ちます。

* $|S_y -T_y| \le a$
* $|S_x - T_y| \le a + 2b$
* $a > 0$ もしくは $S_x - T_x \equiv 2b (\mod 4)$

逆に、非負整数の組 $(a, b)$ が上の条件を満たすならば、前者を $a$ 回と後者を $b$ 回行うことで $(S_x, S_y)$ から $(T_x, T_y)$ へ移動できます。

よって、$0 \le a, 0 \le b$ と上の条件のもとで通行料 $a+b$ を最小化したいです。

$0 \le b, |S_y - T_y| \le a$ より、$$|S_y - T_y| \le a+b \to (1)$$ が必要です。 $|S_y - T_y| \le a, |S_x-T_x| \le a+2b$ より、$$\dfrac{|S_y-T_y| + |S_x - T_x|}{2} \le a+b \to (2)$$ が必要です。

逆に、$(a, b) = \Big(|S_y-T_y|, \max\Big\{0, \dfrac{|S_x-T_x| - |S_y - T_y|}{2} \Big\} \Big)$ はすべての条件を満たし、$(1), (2)$ のどちらかが等号で成立します。

</details><br>

よって、求める通行料の最小値は 

$$
\max \Big\{ |S_y - T_y|, \dfrac{|S_x - T_x| + |S_y - T_y|}{2} \Big\} = \dfrac{|S_y-T_y| + \max \{|S_x-T_x|,|S_y - T_y| \}}{2}
$$ 

のように表せることがわかります。
折りたたみ部で述べたように条件を整理することによって導出することもできますが、小さなケースで実験し、規則性を予測・証明することでもこの式を導出することができるでしょう。
下の図のように平面を少し変形することでも、この式を思いつきやすくなるかもしれません。

![](https://img.atcoder.jp/abc359/9b9d2cb917f49fa8d42c30e481b0daa3.png)

実装例は以下のようになります。

</details><br>

For simplicity, we can assume that the start and goal are on the left side of the tile (i.e., if $S_x + S_y$ is odd, we reduce $S_x$ by 1).

<details><summary>Logical Derivation</summary><br>

Since we can freely move between the left and right sides of the tile, we consider movements starting from the left side and arriving at the left side as a single chunk.

By paying a travel cost of 1, you can perform one of the following two actions:

* Move 1 step vertically and 1 step horizontally
* Move 2 steps horizontally

Suppose we perform the first action $a$ times and the second action $b$ times $(0 \le a, 0 \le b)$ to move from $(S_x, S_y)$ to $(T_x, T_y)$.

In this case, the following holds:

* $|S_y - T_y| \le a$
* $|S_x - T_x| \le a + 2b$
* $a > 0$ or $S_x - T_x \equiv 2b \ (\mod \ 4)$

Conversely, if the pair of non-negative integers $(a, b)$ satisfies the above conditions, then by performing the first action $a$ times and the second action $b$ times, you can move from $(S_x, S_y)$ to $(T_x, T_y)$.

Therefore, we want to minimize the travel cost $a + b$ under the conditions $0 \le a, 0 \le b$.

Since $0 \le b, |S_y - T_y| \le a$, we need
$$|S_y - T_y| \le a + b \to (1)$$
From $|S_y - T_y| \le a, |S_x - T_x| \le a + 2b$, we also need
$$\frac{|S_y - T_y| + |S_x - T_x|}{2} \le a + b \to (2)$$

Conversely, $(a, b) = \large{(}|S_y - T_y|, \max\large{\{}(0, \frac{|S_x - T_x| - |S_y - T_y|}{2}\large{\}}\large{)}$ satisfies all conditions, and either (1) or (2) holds as an equality.

</details><br>

Therefore, the minimum travel cost can be expressed as:

$$\max \large{\{} |S_y - T_y|, \frac{|S_x - T_x| + |S_y - T_y|}{2} \large{\}} = \frac{|S_y - T_y| + \max \{|S_x - T_x|, |S_y - T_y|\}}{2}$$

As mentioned in the collapsible section, you can derive this by organizing the conditions, but you can also derive this formula by experimenting with small cases, predicting regularities, and proving them. It might also help to come up with this formula by slightly transforming the plane, as shown in the diagram below.

![Diagram](https://img.atcoder.jp/abc359/9b9d2cb917f49fa8d42c30e481b0daa3.png)

An example implementation is as follows.

```cpp
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    long Sx, Sy, Tx, Ty;
    cin >> Sx >> Sy >> Tx >> Ty;

    // Align to the left side of the tile.
    if ((Sx + Sy) % 2 == 1) {
        --Sx;
    }
    if ((Tx + Ty) % 2 == 1) {
        --Tx;
    }

    // The answer is (|Sy - Ty| + max(|Sx - Tx|, |Sy - Ty|)) / 2
    long Dx = abs(Sx - Tx);
    long Dy = abs(Sy - Ty);
    
    cout << (Dy + max(Dx, Dy)) / 2 << endl;
    return 0;
}
```
