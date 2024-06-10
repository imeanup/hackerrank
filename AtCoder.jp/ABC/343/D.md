## [D - Diversity of Scores](https://atcoder.jp/contests/abc343/tasks/abc343_d)

<details><summary><b>Japanese </b></summary>

**解説**

---

$N$ 人の選手たちの得点を多重集合として管理しながら、$1, 2, \dots, T$ 秒後に起きる得点の変動を順に処理していけばよいです。

多重集合を管理できるデータ構造はいくつか存在しますが、この問題では **連想配列** （C++ の `std::map`, `std::unordered_map` や python の dictionary など）と呼ばれるデータ構造が有用です。連想配列は通常の配列を拡張したようなもので、通常の配列では添字として $0, 1, 2, \dots$ と連続する整数を用いるのに対し、連想配列では添字に好きな値を用いることができます。初期状態では添字が一つも存在せず、添字の追加・削除、特定の添字に対応する値の変更、サイズ（添字の種類数）の取得などの操作が高速に（定数時間やサイズの対数時間などで）行えます。

本問題では、現在の選手たちの得点に現れる各値を添字として用い、添字 $x$ に対応する値として得点が $x$ である選手の人数を保持すればよいです。具体的なアルゴリズムは以下の通りです。

1. 連想配列 $M$ を用意する。
2. $M$ に添字 $0$ を追加し、$M[0] = N$ とする。
3. 各選手の現在の得点を保持する配列 $C = (C_1, C_2, \dots, C_N)$ を用意し、全ての要素を $0$ で初期化する。
4. $i = 1, 2, \dots, T$ の順に以下を行う。
   1. $M[C_{A_i}]$ を $1$ 減らす。
   2. $M[C_{A_i}]$ が $0$ になったならば、 $M$ から添字 $C_{A_i}$ を削除する。
   3. $C_{A_i}$ に $B_i$ を足す。
   4. $M$ に添字 $C_{A_i}$ が存在しないならば追加し、$M[C_{A_i}] = 0$ とする。
   5. $M[CA_i]$ を $1$ 増やす。
   6. 現在の $M$ のサイズ（添字の種類数）を出力する。

計算量は、下記の実装例のように C++ の `std::map` を用いた場合 $O(N + T\log N)$ になります。

実装例 (C++) :

</details><br>

**Explanation**

---

We need to manage the scores of $N$ players as a multiset and process the score changes that occur at each of the $1, 2, \dots, T$ seconds sequentially.

Several data structures can manage a multiset, but for this problem, an **associative array** (such as C++'s `std::map` or `std::unordered_map`, or Python's dictionary) is useful. An associative array is an extension of a regular array where, instead of using consecutive integers $0, 1, 2, \dots$ as indices, you can use any desired values as indices. Initially, it contains no indices, and operations such as adding/deleting indices, changing values corresponding to specific indices, and obtaining the size (number of distinct indices) can be performed quickly (in constant time or logarithmic time in the size).

In this problem, we use the current score values of the players as indices and maintain the number of players with each score as the value corresponding to each index. The specific algorithm is as follows:

1. Prepare an associative array $M$.
2. Add the index $0$ to $M$ and set $M[0] = N$.
3. Prepare an array $C = (C_1, C_2, \dots, C_N)$ to hold the current scores of each player and initialize all elements to $0$.
4. For $i = 1, 2, \dots, T$, perform the following:
   1. Decrease $M[C_{A_i}]$ by $1$.
   2. If $M[C_{A_i}]$ becomes $0$, remove the index $C_{A_i}$ from $M$.
   3. Add $B_i$ to $C_{A_i}$.
   4. If the index $C_{A_i}$ does not exist in $M$, add it and set $M[C_{A_i}] = 0$.
   5. Increase $M[C_{A_i}]$ by $1$.
   6. Output the current size of $M$ (the number of distinct indices).

The time complexity is $O(N + T\log N)$ when using `std::map` in C++, as shown in the implementation example below.

Example implementation (C++):

```cpp
#include<bits/stdc++.h>

using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, t;
    cin >> n >> t;
    vector<ll> score(n);
    map<ll, int> mp;
    mp[0] = n;
    for (int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        --a;
        if (--mp[score[a]] == 0) mp.erase(score[a]);
        score[a] += b;
        ++mp[score[a]];
        cout << mp.size() << '\n';
    }
}

```
