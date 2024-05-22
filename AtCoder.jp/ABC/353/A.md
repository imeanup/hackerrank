## A - Buildings

<!-- 初心者の方へ

* プログラミングの学習を始めたばかりで何から手をつけるべきかわからない方は、まずは [practice contest](https://atcoder.jp/contests/practice/) の問題A「Welcome to AtCoder」をお試しください。言語ごとに解答例が掲載されています。
* また、プログラミングコンテストの問題に慣れていない方は、 [AtCoder Beginners Selection](https://atcoder.jp/contests/abs) の問題をいくつか試すことをおすすめします。
* [C++入門 AtCoder Programming Guide for beginners (APG4b)](https://atcoder.jp/contests/APG4b) は、競技プログラミングのための C++ 入門用コンテンツです。


for 文を用いて、$i = 2, 3, \cdots , N$ の順に $H_i > H_1$ かを確認しましょう。

そのような $i$ が見つかれば、その時点でその $i$ を出力してコードを終了すればよいです。見つからない場合は $-1$ を出力します。

多くのプログラミング言語では 0-indexed が用いられていることに注意してください。

実装例 (C++): -->

<details><summary><b> For Beginners </b></summary>

* If you are just starting to learn programming and are unsure where to begin, try problem A "Welcome to AtCoder" in the [practice contest](https://atcoder.jp/contests/practice/). Example solutions are provided for each language.
* If you are not familiar with programming contest problems, it is recommended to try some problems from the [AtCoder Beginners Selection](https://atcoder.jp/contests/abs).
* The [C++ Introduction AtCoder Programming Guide for Beginners (APG4b)](https://atcoder.jp/contests/APG4b) is an introductory content for competitive programming using C++.

</details><br>

Using a for loop, let's check if $H_i > H_1$ in the order of $i = 2, 3, \cdots, N$.

If such an $i$ is found, you should output that $i$ at that point and terminate the code. If not found, output -1.

Note that many programming languages use 0-indexing.

Implementation example (C++):

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> h(n);
  for(int i = 0; i < n; i++) cin >> h[i];
  for(int i = 1; i < n; i++) {
    if(h[i] > h[0]) {
      cout << i + 1 << endl;
      return 0;
    }
  }
  cout << -1 << endl;
}
```