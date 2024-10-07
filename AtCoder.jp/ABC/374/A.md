## [A - Takahashi san 2](https://atcoder.jp/contests/abc374/tasks/abc374_a)


<details><summary>Japanese</summary><br>

文字列の最後から $3$ 文字の部分文字列を取り出し、それが `san` と一致しているか判定し、そうであるならば `Yes` 、ないならば `No` を出力すれば良いです。

部分文字列を取り出す関数は C++ や pythonでは標準ライブラリや記法の形で定義されています。

他には、文字列の長さを $N$ としたとき、 問題文の条件は（ $S$ の $N-2$ 文字目が `s` ）かつ（ $S$ の $N-1$ 文字目が `a` ）かつ（ $S$ の $N$ 文字目が `n` ）と言い換えることができるため、これを判定しても良いです。

c++ による実装例:

</details><br>

You need to extract the last 3 characters of the string and check if they match `san`. If they do, output `Yes`; otherwise, output `No`.

In C++ or Python, the function to extract substrings is defined as part of the standard library or notation.

Alternatively, if the length of the string is $N$, the condition in the problem can be rephrased as: (the $(N-2)^{th}$ character of $S$ is `s`) and (the $(N-1)^{th}$ character of $S$ is `a`) and (the $N^{th}$ character of $S$ is `n`). You can use this to perform the check as well.

Example implementation in C++:

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    if (s.substr(s.size() - 3) == "san"){
        cout << "Yes\n";
    }
    else cout << "No\n";
    return 0;
}
```
