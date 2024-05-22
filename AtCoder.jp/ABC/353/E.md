# [E - Yet Another Sigma Problem](https://atcoder.jp/contests/abc353/tasks/abc353_e)

<!-- この問題は Trie 木と呼ばれるデータ構造を用いて解くことが出来ます。

$S_i$ と $S_j$ の最長共通接頭辞の長さは、$S_i$ と $S_j$ の共通する接頭辞の個数と等しいです。例えば、`abc` と `abde` の最長共通接頭辞の長さは $2$ で、共通する接頭辞は `a` と `ab` の $2$ つです。

つまり、各 $j = 2, \cdots, N$ で全ての $S_j$ の接頭辞 $T$ を調べ、$T$ を接頭辞とする $S_i (1 \le i < j)$ の個数が求まればよいです。

これは $i = 1, 2, \cdots , N$ の順に $S_i$ を Trie 木に追加し、各ノードではそのノードが表す文字列を接頭辞として含む文字列の個数を情報として管理すればよいです。

実装例(C++): -->

This problem can be solved using a data structure called a Trie.

The length of the longest common prefix between $S_i$ and $S_j$ is equal to the number of common prefixes between $S_i$ and $S_j$. For example, the longest common prefix length between `abc` and `abde` is 2, with the common prefixes being `a` and `ab`.

Thus, for each $j = 2, \cdots, N$, we need to examine all prefixes $T$ of $S_j$ and determine the number of $S_i$ (where $1 \le i < j$) that have $T$ as a prefix.

This can be achieved by adding each $S_i$ to the Trie in order of $i = 1, 2, \cdots, N$, while maintaining the count of strings that include the string represented by each node as a prefix.

Implementation example (C++):

```cpp
#include <bits/stdc++.h>
using namespace std;

struct trie {
  using ar = array<int, 26>;
  vector<ar> pos;
  ar def;
  int now_sz;
  long long ans;
  vector<int> cnt;
  trie() = default;
  trie(int len) {
    pos.reserve(len + 1);
    cnt.reserve(len + 1);
    def.fill(-1);
    now_sz = ans = 0;
    make_node();
  }
  int make_node() {
    pos.push_back(def);
    cnt.push_back(0);
    return now_sz++;
  }
  void add(string &s) {
    int now = 0;
    for(int i = 0; i < (int)s.size(); i++) {
      int d = s[i] - 'a';
      int &nx = pos[now][d];
      if(nx == -1)
        nx = make_node();
      now = nx;
      ans += cnt[now]++;
    }
  }
};

int main() {
  int n;
  cin >> n;
  trie tr(300000);
  for(int i = 0; i < n; i++) {
    string s;
    cin >> s;
    tr.add(s);
  }
  cout << tr.ans << endl;
}
```