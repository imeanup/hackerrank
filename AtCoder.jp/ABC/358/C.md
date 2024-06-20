## [C - Popcorn](https://atcoder.jp/contests/abc358/tasks/abc358_c)

<details><summary><b>Japanese Editorial</b></summary><br>

**解説**

---

各ポップコーン売り場について訪れるか訪れないか決めることを考えます。訪れるポップコーン売り場の選び方は $2^N$ 通りであり、本問題の制約下ではこれは最大で $10^3$ 通りなので、容易に全通り試すことができます。具体的には、訪れるポップコーン売り場の選び方それぞれに対して、その選び方で全ての味のポップコーンを買えるか判定し、買えるならば選んだ売り場の数を $x$ として $\text{ans} \gets \min(ans, x)$ と更新する、という処理を行えば良いです。

あとは実装の問題です。本問題のように「$N$ 個のものそれぞれについて選ぶか選ばないかを決める $2^N$ 通りを全探索する」という状況では、**bit 全探索**と呼ばれる手法がその実装の容易さから広く用いられています。これは、「$0, 1, \dots, N-1$ の番号がついた $N$ 個のものから $x_1, x_2, \dots, x_k$ の $k$ 個を選ぶ」という状態を「$2$ 進数表記で $x_1, x_2, \dots, x_k$ 桁目が $1$ であるような整数」に対応させると、$N$ 個のものからいくつかのものを選ぶ $2^N$ 通りが $0$ 以上 $2^N-1$ 以下の整数と一対一に対応するので、選び方を全探索する代わりに整数の方を全探索すればよい（そしてこれは簡単な for 文で実現できる）というものです。

整数から選び方を復元するには「整数 $x, k$ に対して、$x$ を $2$ 進数表記したときの $k$ 桁目を求める」という操作が必要になりますが、これはほとんどのプログラミング言語の備わるビット演算の機能を用いて簡単に実装できます。詳細は下記の実装例も参考にしてください。

実装例 (C++) :

</details><br>

**Explanation**

---

Consider determining whether to visit each popcorn stand or not. There are $2^N$ ways to choose which stands to visit, and under the constraints of this problem, this can be up to $10^3$ ways, making it feasible to try all possibilities. Specifically, for each possible selection of stands to visit, you check if all flavors of popcorn can be bought with that selection. If they can, you update the minimum number of stands required ($\text{ans} \gets \min(\text{ans}, x)$).

The problem then becomes one of implementation. In situations like this, where there are $N$ items and each can either be selected or not in $2^N$ ways, a method called **bit exploration** is widely used due to its ease of implementation. This method maps the state of "selecting $k$ items from $N$ items numbered $0, 1, \dots, N-1$" to an integer where the binary representation has 1s at the positions corresponding to the selected items. Thus, exploring all $2^N$ ways of selecting items is equivalent to exploring all integers from 0 to $2^N - 1$, which can be done with a simple for loop.

To recover the selection from an integer, you need the operation "determine the $k$th bit of integer $x$ in its binary representation". Most programming languages provide bitwise operations to implement this easily. Refer to the implementation example below for details.

Example implementation (C++):

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> s(n);
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    int ans = n;
    for (int bit = 0; bit < (1 << n); bit++) {
        vector<bool> exist(m);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (bit >> i & 1) {
                ++cnt;
                for (int j = 0; j < m; j++) {
                    if (s[i][j] == 'o') exist[j] = true;
                }
            }
        }
        bool all_exist = true;
        for (int j = 0; j < m; j++) {
            if (!exist[j]) all_exist = false;
        }
        if (all_exist) ans = min(ans, cnt);
    }
    cout << ans << endl;
}
```
