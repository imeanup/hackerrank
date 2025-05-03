## [D - Goin' to the Zoo](https://atcoder.jp/contests/abc404/tasks/abc404_d)

同じ動物園に $3$ 度以上行く必要はありません。よって各動物園に行く回数が $0,1,2$ のいずれであるかを $3^N$ 通り全探索することで答えを求めることができます。

動物園に行く回数を決めたとき、各動物を何度見ることになるかは愚直に回数を数えることで $O(NM)$ で求めることができるため、計算量は全体で $O(3^N NM)$ になります。

---

You never need to visit the same zoo three or more times.  Hence you can brute‑force over all $3^N$ possibilities where for each zoo you choose to go 0, 1, or 2 times.

Once you’ve fixed the visit counts, you can determine how many times each animal is seen by simply counting across all visits in $O(NM)$ time.  Therefore, the overall time complexity is

$$
O\bigl(3^N \times N \times M\bigr).
$$
