

## [B - Grid Rotation](https://atcoder.jp/contests/abc404/tasks/abc404_b)

回転操作を行わない場合、$S$ と $T$ で一致していないマスの個数が答えです。

マスの色を塗り替える操作と、グリッド全体を回転する操作は、順序を入れ替えても構いません。よってグリッド全体を回転する操作は最初に行うとしてよいです。 回転する操作を行う回数が $0,1,2,3$ 回のいずれであるかを $4$ 通り全て試すことでこの問題を解くことができます。


---

If you perform no rotations, the answer is simply the number of cells where $S$ and $T$ differ.

The operations of repainting individual cells and rotating the entire grid commute, so you may assume all grid‑rotation steps happen first.  There are only four possible rotation counts—0, 1, 2, or 3 (each representing a 90° clockwise turn)—so you can solve the problem by trying all four and taking the minimum mismatch count.
