## [F - Easiest Maze](https://atcoder.jp/contests/abc358/tasks/abc358_f)

<details><summary><b>Japanese Editorial</b></summary><br>

**解説**

---

解が存在するための $K$ の条件について考えます。まず、マス $(1, M), (N, M)$ 間の最短パスの長さを考えれば、$K \le N$ は明らかに必要です。

更に、突然ですがグリッドの各マスを以下のように市松模様に色分けしてみます。

![](https://img.atcoder.jp/abc358/4dc7c8003d9570ad5dd2f13714299293.png)

グリッド上のいかなるパスも赤 $\to$ 青 $\to$ 赤 $\to \dots$ のように違う色のマスを交互に通ること、マス $(1, M), (N, M)$ の色が等しいか異なるかは $N$ が奇数か偶数かによって定まることを考えると、$N$ と $K$ の偶奇は一致している必要があることがわかります。（例えば $N$ が偶数のとき、マス $(1, M), (N, M)$ の色は異なるため、入口から出口までの道順は赤 $\to$ 青 $\to$ 赤 $\to$ 青 $\to \dots \to$ 赤 $\to$青のようになり、必ず偶数個の頂点を通ります。）

逆に、$K \le N$ かつ $N$ と $K$ の偶奇が一致している場合必ず解を構築することができます。具体的には、以下の図のように、最短である長さ $N$ のパスから始めて $N, N+2, N+4, \dots$ とパスの長さを $2$ ずつ増やしていくことができます。

#### $N$ が偶数のとき

![](https://img.atcoder.jp/abc358/dfa31eb1f3d77d3757a4ab8f30a0861f.png)

#### $N$ が奇数のとき

![](https://img.atcoder.jp/abc358/2266837bf99f537640e139f973654b8c.png)

あとはこれを丁寧に実装すればよいです。ある程度の場合分けが必要になりますが、場合分けの内部で壁の配置を構築するのは大変なので、場合分け部分と壁の配置の構築を別々に行うことをお勧めします。下記の実装例では、まず入口から出口へのパスで通るマスの列を場合分けで構築したのち、一旦全ての場所に壁を建ててから、パス上で隣接するマス間の壁を取り除く、という実装方針を取っています。

実装例 (C++) :

</details><br>

**Explanation**

---

Let's consider the conditions for $K$ for which a solution exists. Firstly, by considering the shortest path between cells $(1, M)$ and $(N, M)$, it is clear that $K \le N$ is necessary.

Furthermore, let's suddenly color each cell of the grid in a checkerboard pattern as follows.

![](https://img.atcoder.jp/abc358/4dc7c8003d9570ad5dd2f13714299293.png)

Considering that any path on the grid alternates between red and blue cells (red $\to$ blue $\to$ red $\to \dots$), and that whether the colors of cells $(1, M)$ and $(N, M)$ are the same or different depends on whether $N$ is odd or even, we can see that the parity of $N$ and $K$ must match. (For example, when $N$ is even, the colors of cells $(1, M)$ and $(N, M)$ are different, so the path from the entrance to the exit alternates in color, requiring an even number of vertices.)

Conversely, if $K \le N$ and the parity of $N$ and $K$ match, it is always possible to construct a solution. Specifically, starting from the shortest path of length $N$, we can incrementally increase the path length by 2, resulting in lengths $N, N+2, N+4, \dots$.

#### When $N$ is even

![](https://img.atcoder.jp/abc358/dfa31eb1f3d77d3757a4ab8f30a0861f.png)

#### When $N$ is odd

![](https://img.atcoder.jp/abc358/2266837bf99f537640e139f973654b8c.png)

From there, it is necessary to implement this carefully. While some case distinctions are necessary, it is recommended to separate the process of constructing the wall configuration from the case distinctions to avoid complexity. In the implementation example below, the approach is to first construct the series of cells traversed by the path from the entrance to the exit through case distinctions, then build walls everywhere, and finally remove the walls between adjacent cells on the path.

Implementation Example (C++):

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    if (k < n or k % 2 != n % 2) {
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
    vector<pair<int, int>> path;
    k -= n;
    for (int i = 0; i < n - 1; i += 2) {
        if (i != n - 3) {
            int w = 1 + min(m - 1, k / 2);
            k -= (w - 1) * 2;
            for (int j = 0; j < w; j++) {
                path.emplace_back(i, m - 1 - j);
            }
            for (int j = 0; j < w; j++) {
                path.emplace_back(i + 1, m - w + j);
            }
        } else if (k <= (m - 1) * 2) {
            int w = 1 + k / 2;
            for (int j = 0; j < w; j++) {
                path.emplace_back(i, m - 1 - j);
            }
            for (int j = 0; j < w; j++) {
                path.emplace_back(i + 1, m - w + j);
            }
            path.emplace_back(i + 2, m - 1);
        } else {
            for (int j = 0; j < m; j++) {
                path.emplace_back(i, m - 1 - j);
            }
            k -= (m - 1) * 2;
            int j = 0;
            while (j < m) {
                if (k) {
                    path.emplace_back(i + 1, j);
                    path.emplace_back(i + 2, j);
                    path.emplace_back(i + 2, j + 1);
                    path.emplace_back(i + 1, j + 1);
                    j += 2;
                    k -= 2;
                } else {
                    path.emplace_back(i + 1, j);
                    j++;
                }
            }
            path.emplace_back(i + 2, m - 1);
        }
    }
    vector c(n, string(m - 1, '|'));
    vector r(n - 1, string(m, '-'));
    for (int i = 0; i < path.size() - 1; i++) {
        auto [x1, y1] = path[i];
        auto [x2, y2] = path[i + 1];
        if (x1 == x2) c[x1][min(y1, y2)] = '.';
        else r[min(x1, x2)][y1] = '.';
    }
    cout << string(2 * m - 1, '+') + "S+\n";
    for (int i = 0; i < n; i++) {
        cout << '+';
        for (int j = 0; j < m - 1; j++) cout << 'o' << c[i][j];
        cout << "o+\n";
        if (i < n - 1) {
            for (int j = 0; j < m; j++) cout << '+' << r[i][j];
            cout << "+\n";
        }
    }
    cout << string(2 * m - 1, '+') + "G+\n";
}
```
