
## [C - Triple Attack](https://atcoder.jp/contests/abc368/tasks/abc368_c)

<details style="border: 1px solid black; padding: 10px;"><summary><b>Japanese</b></summary><br>

「体力が 1 以上である最も前の敵」を以下では単に「先頭の敵」と呼ぶことにする。

先頭の敵の体力が $5$ 以上であるとき、現在の $T$ の値によらず、次の $3$ 回の行動で先頭の敵の体力を $5$ 減らすことができます。先頭の敵の体力を $H$ とすると、この3回1セットの行動は $\lfloor \dfrac{H}{5} \rfloor$ セット繰り返されます。この部分をまとめて処理し、残りを愚直にシミュレーションすることで、$O(N)$ で答えを求めることができます。 

</details><br>

In the following explanation, we will refer to "the first enemy whose health is 1 or more" simply as "the leading enemy."

When the leading enemy's health is 5 or more, regardless of the current value of $T$, you can reduce the leading enemy's health by 5 over the next 3 actions. If the health of the leading enemy is $H$, this set of 3 actions will be repeated $\lfloor \dfrac{H}{5} \rfloor$ times. By handling this part collectively and simulating the remainder straightforwardly, you can obtain the answer in $O(N)$ time.

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()

int main() {
    int n; cin >> n;
    vector<ll> h(n);
    rep(i, n) cin >> h[i];
    ll t = 0;

    rep(i, n) {
        ll rem = h[i]/5;
        t += rem*3;
        h[i] -= rem * 5;
        while (h[i] > 0){
            t++;
            if (t%3 == 0) h[i] -= 3;
            else h[i]--;
        }
    }
    cout << t << "\n";
    return 0;
}
```

</details><br>
