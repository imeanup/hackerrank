# [F - Tile Distance](https://atcoder.jp/contests/abc353/tasks/abc353_f)


答えの上界として、$|S_x - T_x| + |S_y - T_y|$が考えられます（左右方向に $|S_x - T_x|$ だけ移動し、その後上下方向に $|S_y - T_y|$ だけ移動することで、この上界以下の値を達成できます）。

$K = 1$ のとき、これが答えと等しいことがすぐにわかります。

以下、$K \ge 2$ とします。

答えがこの上界より真に小さいとき、答えを実現する移動方法では大タイルを通ることがわかります（小タイルしか通らない場合、支払う通行料が上界と一致します）。

---

答えを実現する移動方法においてはじめに到達する大タイルと最後に到達する大タイルの組を全探索することを考えます。

はじめに到達する大タイルとしてありえるものは、

* $(S_x + 0.5, S_y + 0.5)$ が大タイルの上にあるなら、その大タイル
* そうでなければ、上下左右のそれぞれについて、その方向にのみ移動したときに最初に到達する $4$ つの大タイル

に限られます。 $(S_x + 0.5, S_y + 0.5)$ を含むタイルからそれぞれの大タイルへ移動するのにかかる通行料はすぐに計算できます（仮定より、それぞれの大タイルへ到達するまでに使うのは小タイルのみであるとしてよいことに注意してください。ここで計算された値がそれぞれの大タイルへ移動するのにかかる通行料の最小値でなくとも答えには影響ありません）。

同様に、最後に到達する大タイルとしてありえるものもたかだか $4$ つに限られ、それぞれの大タイルから $(T_x+0.5, T_y + 0.5)$ を含むタイルへ移動するのにかかる通行料も求めることができます。

そして、これらの組たかだか $16$ 通りに対して、それぞれの大タイル間を移動するのにかかる通行料の最小値を求められればよいです。

枝刈りをすることで調べる組の個数を減らすことができる場合もありますが、しなくても十分高速です。

---

$2$ つの大タイル間を移動するのにかかる通行料の最小値を求めることを考えます。

まず、一点を共有する $2$ つの大タイルは、$2$ の通行料を支払うことで行き来することができます。
また、$[i, i+K] \times [j, j+K]$ の大タイルと $[i+K, i+2K] \times [j, j+K]$ の大タイルを $K+1$ の通行料を支払うことで行き来することができ、$K = 2$ のときに限り考慮に入れる必要があります（上下方向も同様です）。

![](https://img.atcoder.jp/abc353/8202414d852f152deec2212178393888.png)

以上より、$[aK, (a+1)K] \times [bK, (b+1)K]$ の大タイルから $[cK, (c+1)K] \times [dK, (d+1)K]$ の大タイルへ移動するのにかかる通行料の最小値は以下のように書けます。

* $K = 2$ のとき、$|a-c| + |b-d| + \Big|\frac{|a-c| - |b-d|}{2}\Big|$
* $K \ne 2$ のとき、$|a-c| + |b-d| + \Big| |a-c| - |b-d| \Big| = |a+b-c-d| + |a-b-c+d|$

これを用いることでこの問題を解くことができます。

実装例は以下のようになります。

```cpp
#include <iostream>
#include <vector>
#include <tuple>

int main() {
    using namespace std;
    
    unsigned long K;
    cin >> K;
    unsigned long Sx, Sy, Tx, Ty;
    cin >> Sx >> Sy >> Tx >> Ty;
    // K ずつ右上にずらしておく
    Sx += K;
    Sy += K;
    Tx += K;
    Ty += K;
    
    // 上界を入れておく
    unsigned long dist{max(Tx, Sx) - min(Tx, Sx) + max(Ty, Sy) - min(Ty, Sy)};
    
    // 1 < K のとき、大タイルを経由する移動を考える
    if(1 < K){
        vector<tuple<unsigned long, unsigned long, unsigned long>> large_start; // はじめに到達する大タイルの候補
        if(((Sx / K) ^ (Sy / K)) & 1) // 開始位置が大タイルなら
            large_start.emplace_back(Sx / K, Sy / K, 0); // その大タイル
        else{ // そうでなければ、四方向いずれかで最も近い大タイルが候補
            large_start.emplace_back(Sx / K - 1, Sy / K, 1 + Sx % K); // 左
            large_start.emplace_back(Sx / K + 1, Sy / K, K - Sx % K); // 右
            large_start.emplace_back(Sx / K, Sy / K - 1, 1 + Sy % K); // 下
            large_start.emplace_back(Sx / K, Sy / K + 1, K - Sy % K); // 上
        }

        vector<tuple<unsigned long, unsigned long, unsigned long>> large_goal; // 最後に到達する大タイルの候補
        if(((Tx / K) ^ (Ty / K)) & 1) // 終了位置が大タイルなら
            large_goal.emplace_back(Tx / K, Ty / K, 0); // その大タイル
        else{ // そうでなければ、四方向いずれかで最も近い大タイルが候補
            large_goal.emplace_back(Tx / K - 1, Ty / K, 1 + Tx % K); // 左
            large_goal.emplace_back(Tx / K + 1, Ty / K, K - Tx % K); // 右
            large_goal.emplace_back(Tx / K, Ty / K - 1, 1 + Ty % K); // 下
            large_goal.emplace_back(Tx / K, Ty / K + 1, K - Ty % K); // 上
        }

        // K = 2 かどうかで場合分け
        if(K == 2)
            for(const auto& [x, y, d1] : large_start)
                for(const auto& [z, w, d2] : large_goal){
                    const auto x_diff{max(x, z) - min(x, z)};
                    const auto y_diff{max(y, w) - min(y, w)};
                    dist = min(dist, d1 + d2 + x_diff + y_diff + (max(x_diff, y_diff) - min(x_diff, y_diff)) / 2);
                }
        else
            for(const auto& [x, y, d1] : large_start)
                for(const auto& [z, w, d2] : large_goal)
                    dist = min(dist, d1 + d2 + max(x + y, z + w) - min(x + y, z + w) + max(x + w, z + y) - min(x + w, z + y));
    }
    cout << dist << endl;
    return 0;
}
```

---

The upper bound of the answer can be considered as $|S_x - T_x| + |S_y - T_y|$ (moving horizontally by $|S_x - T_x|$ and then vertically by $|S_y - T_y|$ to achieve a value not exceeding this upper bound).

When $K = 1$, this is immediately seen to be equal to the answer.

From here, consider $K \ge 2$.

If the answer is strictly smaller than this upper bound, it implies that the method of movement realizing the answer involves passing through a large tile (if only small tiles are passed through, the toll paid would match the upper bound).

---

Next, consider exhaustively searching for the pair of large tiles first reached and last reached by the movement method that realizes the answer.

The possible large tiles initially reached are limited to:

* The large tile if $(S_x + 0.5, S_y + 0.5)$ is on a large tile.
* Otherwise, the four large tiles that are first reached by moving solely in each of the four directions (up, down, left, right).

The toll required to move from the tile containing $(S_x + 0.5, S_y + 0.5)$ to each large tile can be immediately calculated (note that it is assumed from the premise that only small tiles are used until reaching each large tile. The values calculated here do not affect the answer even if they are not the minimum toll to reach each large tile).

Similarly, the possible large tiles last reached are also limited to at most four, and the toll required to move from each large tile to the tile containing $(T_x + 0.5, T_y + 0.5)$ can also be calculated.

For each of these at most 16 pairs, we need to determine the minimum toll required to move between the large tiles.

Although it is possible to reduce the number of pairs to examine through pruning, it is sufficiently fast even without doing so.

---

Consider determining the minimum toll required to move between two large tiles.

First, two large tiles that share a point can be moved between by paying a toll of 2.
Also, the large tile $[i, i+K] \times [j, j+K]$ and the large tile $[i+K, i+2K] \times [j, j+K]$ can be moved between by paying a toll of $K+1$, which only needs to be considered when $K = 2$ (similarly for the vertical direction).

![](https://img.atcoder.jp/abc353/8202414d852f152deec2212178393888.png)

Based on this, the minimum toll required to move from the large tile $[aK, (a+1)K] \times [bK, (b+1)K]$ to the large tile $[cK, (c+1)K] \times [dK, (d+1)K]$ can be expressed as follows:

* When $K = 2$, $|a-c| + |b-d| + \Big|\frac{|a-c| - |b-d|}{2}\Big|$
* When $K \ne 2$, $|a-c| + |b-d| + \Big| |a-c| - |b-d| \Big| = |a+b-c-d| + |a-b-c+d|$

By using this, the problem can be solved.

An implementation example is as follows:

```cpp
#include <iostream>
#include <vector>
#include <tuple>

int main() {
    using namespace std;
    
    unsigned long K;
    cin >> K;
    unsigned long Sx, Sy, Tx, Ty;
    cin >> Sx >> Sy >> Tx >> Ty;
    // Shift right and up by K
    Sx += K;
    Sy += K;
    Tx += K;
    Ty += K;
    
    // Set the upper bound
    unsigned long dist{max(Tx, Sx) - min(Tx, Sx) + max(Ty, Sy) - min(Ty, Sy)};
    
    // Consider movement via large tiles for K > 1
    if(1 < K){
        vector<tuple<unsigned long, unsigned long, unsigned long>> large_start; // Candidates for the first large tile reached
        if(((Sx / K) ^ (Sy / K)) & 1) // If the start position is on a large tile
            large_start.emplace_back(Sx / K, Sy / K, 0); // That large tile
        else{ // Otherwise, the nearest large tile in each of the four directions is a candidate
            large_start.emplace_back(Sx / K - 1, Sy / K, 1 + Sx % K); // Left
            large_start.emplace_back(Sx / K + 1, Sy / K, K - Sx % K); // Right
            large_start.emplace_back(Sx / K, Sy / K - 1, 1 + Sy % K); // Down
            large_start.emplace_back(Sx / K, Sy / K + 1, K - Sy % K); // Up
        }

        vector<tuple<unsigned long, unsigned long, unsigned long>> large_goal; // Candidates for the last large tile reached
        if(((Tx / K) ^ (Ty / K)) & 1) // If the end position is on a large tile
            large_goal.emplace_back(Tx / K, Ty / K, 0); // That large tile
        else{ // Otherwise, the nearest large tile in each of the four directions is a candidate
            large_goal.emplace_back(Tx / K - 1, Ty / K, 1 + Tx % K); // Left
            large_goal.emplace_back(Tx / K + 1, Ty / K, K - Tx % K); // Right
            large_goal.emplace_back(Tx / K, Ty / K - 1, 1 + Ty % K); // Down
            large_goal.emplace_back(Tx / K, Ty / K + 1, K - Ty % K); // Up
        }

        // Distinguish based on whether K = 2
        if(K == 2)
            for(const auto& [x, y, d1] : large_start)
                for(const auto& [z, w, d2] : large_goal){
                    const auto x_diff{max(x, z) - min(x, z)};
                    const auto y_diff{max(y, w) - min(y, w)};
                    dist = min(dist, d1 + d2 + x_diff + y_diff + (max(x_diff, y_diff) - min(x_diff, y_diff)) / 2);
                }
        else
            for(const auto& [x, y, d1] : large_start)
                for(const auto& [z, w, d2] : large_goal)
                    dist = min(dist, d1 + d2 + max(x + y, z + w) - min(x + y, z + w) + max(x + w, z + y) - min(x + w, z + y));
    }
    cout << dist << endl;
    return 0;
}
```