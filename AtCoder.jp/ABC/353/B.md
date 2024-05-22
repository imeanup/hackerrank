## B - AtCoder Amusement Park

<!-- 待機列を先頭から見て、次のような情報を繰り返し更新することでこの問題を解くことができます。

* 現在の空席の個数
* これまでに何回アトラクションをスタートしたか

for 文や if 文をうまく使うことで、これらの情報を正しく更新することができます。

グループごとに「そのまま誘導する」「アトラクションを $1$ 回スタートさせたあとに誘導する」のどちらかを行うと考えることで実装の見通しが立ちやすくなるかもしれません。

実装例は以下のようになります。 -->

You can solve this problem by repeatedly updating the following information as you examine the queue from the front:

* The current number of available seats
* The number of times the attraction has started so far

By effectively using for loops and if statements, you can correctly update this information.

Considering for each group whether to "directly guide them" or "start the attraction once and then guide them" might help clarify the implementation.

An implementation example is as follows:

```cpp
#include <iostream>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    
    // はじめ、空席は K 個、スタートした回数は 0 回
    int empty_sheets = K, start_count = 0;
    
    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a; // 人数を入力
        if (empty_sheets < a) { // 空席が足りなければ
            ++start_count; // スタートして
            empty_sheets = K; // 空席を K 個に
        }
        empty_sheets -= a; // a 人座る
    }
    ++start_count; // 最後に 1 回スタートする
    
    cout << start_count << endl;
    
    return 0;
}
```

```py
N, K = map(int, input().split())

A = list(map(int, input().split()))

empty_sheets = K # はじめ、空席は K 個
start_count = 0 # スタートした回数は 0 回

for a in A:
    if empty_sheets < a: # 空席が足りなければ
        start_count += 1 # スタートして
        empty_sheets = K # 空席を K 個にする
    empty_sheets -= a # a 人座る
    
start_count += 1 # 最後に 1 回スタートする

print(start_count)
```