## [B - Seek Grid](https://atcoder.jp/contests/abc391/tasks/abc391_b)


この問題は，$4$ 重の for ループによる全探索によって解くことができます．

まず，$a,b$ を $1,\dots , N−M+1$ の範囲で全探索します．$a,b$ を固定したときに，それが条件を満たすかどうかをさらに $2$ 重の for ループにより判定します． 具体的には，$i,j$ を $1, \dots, M$ の範囲で全探索し，$S_{a+i−1, b+j−1} \ne T_{i,j}$ となる $i,j$ が $1$ つでも存在するかどうか判定します．そのような $i,j$ が存在しなければ，その時点で見ている $a, b$ が答えです．

---

This problem can be solved using a **brute-force approach** with four nested `for` loops.  

First, we iterate over all possible values of $a, b$ in the range $1, \dots, N - M + 1$.  
For each fixed pair $(a, b)$, we check whether it satisfies the given conditions using another two nested `for` loops.  

Specifically, we iterate over $i, j$ in the range $1, \dots, M$ and check if there exists at least one pair where $S_{a+i−1, b+j−1} \ne T_{i,j}$.  

- If such an $i, j$ exists, the current $(a, b)$ is invalid.  
- If no such $i, j$ exists, then the current $(a, b)$ satisfies the conditions, and it is the answer.

---

実装例 (Python)

```py
N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
for a in range(N - M + 1):
    for b in range(N - M + 1):
        ok = True
        for i in range(M):
            for j in range(M):
                if S[a + i][b + j] != T[i][j]:
                    ok = False
        if ok:
            print(a + 1, b + 1)

```

実装例 (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<string> S(N), T(M);
    for (auto& x : S) cin >> x;
    for (auto& x : T) cin >> x;

    for (int a = 0; a <= N - M; ++a) {
        for (int b = 0; b <= N - M; ++b) {
            bool ok = true;
            for (int i = 0; i < M; ++i) {
                for (int j = 0; j < M; ++j) {
                    if (S[a + i][b + j] != T[i][j]) {
                        ok = false;
                    }
                }
            }
            if (ok) {
                cout << a + 1 << " " << b + 1 << endl;
            }
        }
    }
}

```
