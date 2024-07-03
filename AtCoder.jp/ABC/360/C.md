## [C - Move It](https://atcoder.jp/contests/abc360/tasks/abc360_c)

<details><summary><b>Japanese Editorial</b></summary>

すべての箱に荷物が $1$ 個ずつある状態にするには、少なくとも $2$ 個以上荷物があるすべての箱について、箱に荷物を $1$ 個だけ残してそれ以外の荷物を移動させる必要があります。

$2$ 個以上の荷物がある箱 $i$ に入っている $k(2 \le k)$ 個の荷物の重さを $w_1, w_2, \dots, w_k$ とすると、移動させる必要のある荷物の重さの最小値は、$\sum_{i=1}^{k} w_i - \max(w)$ です。 つまり、すべての箱に荷物が $1$ 個ずつある状態にするには $2$ 個以上の荷物がある箱について、この値の総和がかかるコストとしてありえる最小値となります。

また、この最小値を達成することができます。荷物も箱も互いに $N$ 個ずつあるため、移動させる必要がある荷物の個数は何も入っていない箱の個数と一致します。そのため、移動させる荷物を任意の何も入っていない箱に入れることですべての箱に荷物が $1$ つずつ入っている状態にすることができます。

実際に実装する際には、各箱に入っている荷物の重さの最大値を管理し、それらの総和をを $N$ 個の荷物の重さの総和から引くことで答えを求めることができます。

実装例(C++):



```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n), w(n);
    vector<int> max_weight(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        cin >> w[i];

    for (int i = 0; i < n; ++i){
        a[i]--;
        max_weight[a[i]]=max(max_weight[a[i]],w[i]);
    }

    const int sum_w=accumulate(w.begin(),w.end(),0);
    const int sum_max=accumulate(max_weight.begin(),max_weight.end(),0);
    cout << sum_w-sum_max << endl;
}
```

</details><br>


To achieve a state where each box contains exactly one item, for all boxes that have at least 2 items, you need to leave one item in the box and move the rest of the items elsewhere.

Let the weights of the $k$ items (where $k \ge 2$) in box $i$ be $w_1, w_2, \dots, w_k$. The minimum weight of the items that need to be moved is $\sum_{i=1}^{k} w_i - \max(w)$. In other words, to achieve a state where each box contains exactly one item, the total cost is the sum of this value for all boxes that have at least 2 items.

Additionally, it is possible to achieve this minimum value. Since there are $N$ boxes and $N$ items, the number of items that need to be moved equals the number of empty boxes. Therefore, by moving the items to any of the empty boxes, you can ensure that each box contains exactly one item.

In actual implementation, you can keep track of the maximum weight of the items in each box, and subtract their sum from the total weight of the $N$ items to get the answer.

Example implementation (C++):

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n), w(n);
    vector<int> max_weight(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        cin >> w[i];

    for (int i = 0; i < n; ++i){
        a[i]--;
        max_weight[a[i]]=max(max_weight[a[i]],w[i]);
    }

    const int sum_w=accumulate(w.begin(),w.end(),0);
    const int sum_max=accumulate(max_weight.begin(),max_weight.end(),0);
    cout << sum_w-sum_max << endl;
}
```
