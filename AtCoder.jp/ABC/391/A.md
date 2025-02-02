## [A - Lucky Direction](https://atcoder.jp/contests/abc391/tasks/abc391_a)

> sotanishy

AtCoder をはじめたばかりで何をしたらよいか分からない方は、まずは [practice contest](https://atcoder.jp/contests/practice/) の問題A「Welcome to AtCoder」を解いてみてください。基本的な入出力の方法が載っています。 また、プログラミングコンテストの問題に慣れていない方は、[AtCoder Beginners Selection](https://atcoder.jp/contests/abs) の問題をいくつか解いてみることをおすすめします。

---

### 解法 1

この問題は，$8$ 通りの場合分けにより解くことができます． `N` の反対は `S`, `SE` の反対は `NW`，…… といったルールを全 $8$ 通り列挙して， if 文により場合分けをすればよいです．

実装例 (Python3)


```py
D = input()
if D == "N":
    print("S")
elif D == "S":
    print("N")
elif D == "E":
    print("W")
elif D == "W":
    print("E")
elif D == "NE":
    print("SW")
elif D == "NW":
    print("SE")
elif D == "SE":
    print("NW")
elif D == "SW":
    print("NE")

```

### 解法 2

$D$ を $1$ 文字ずつ反転させることを考えれば，$4$ 通りの場合分けで済みます．for 文を用いれば，$D$ が $1$ 文字である場合と $2$ 文字である場合を統一的に扱うことができます．

実装例 (Python3)

```py
D = input()
ans = ""
for d in D:
    if d == "N":
        ans += "S"
    elif d == "S":
        ans += "N"
    elif d == "E":
        ans += "W"
    elif d == "W":
        ans += "E"
print(ans)

```

実装例 (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string D;
    cin >> D;
    string ans = "";
    for (char d : D) {
        if (d == 'N') {
            ans += 'S';
        } else if (d == 'S') {
            ans += 'N';
        } else if (d == 'E') {
            ans += 'W';
        } else if (d == 'W') {
            ans += 'E';
        }
    }
    cout << ans << endl;
}

```


---

If you're new to AtCoder and unsure where to start, try solving problem A, **"Welcome to AtCoder"**, in the [practice contest](https://atcoder.jp/contests/practice/). It covers basic input and output methods.  
Additionally, if you're unfamiliar with programming contest problems, it's recommended to solve a few problems from the [AtCoder Beginners Selection](https://atcoder.jp/contests/abs).

---

### Solution 1

This problem can be solved using **8 case distinctions**.  

Each direction has an **opposite direction** (e.g., `"N"` is opposite to `"S"`, `"SE"` is opposite to `"NW"`, etc.).  
By listing all **8 cases** and using `if` statements, we can determine the opposite direction.

Implementation (Python3)

```py
D = input()
if D == "N":
    print("S")
elif D == "S":
    print("N")
elif D == "E":
    print("W")
elif D == "W":
    print("E")
elif D == "NE":
    print("SW")
elif D == "NW":
    print("SE")
elif D == "SE":
    print("NW")
elif D == "SW":
    print("NE")
```

---

Solution 2

Instead of handling **8 cases separately**, we can reverse each character in $D$, reducing the problem to just **4 case distinctions**.  
Using a `for` loop, we can handle both **single-character (e.g., `"N"`)** and **two-character (e.g., `"NE"`)** inputs uniformly.

Implementation (Python3)

```py
D = input()
ans = ""
for d in D:
    if d == "N":
        ans += "S"
    elif d == "S":
        ans += "N"
    elif d == "E":
        ans += "W"
    elif d == "W":
        ans += "E"
print(ans)
```

Implementation (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string D;
    cin >> D;
    string ans = "";
    for (char d : D) {
        if (d == 'N') {
            ans += 'S';
        } else if (d == 'S') {
            ans += 'N';
        } else if (d == 'E') {
            ans += 'W';
        } else if (d == 'W') {
            ans += 'E';
        }
    }
    cout << ans << endl;
}
```
