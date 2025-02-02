## [F - K-th Largest Triplet](https://atcoder.jp/contests/abc391/tasks/abc391_f)

**解説1**

---

$A,B,C$ をそれぞれ降順ソートしておきます． $f(i,j,k)= A_iB_j + B_jC_k + C_kA_i$ とします．

$K$ が $K \le 5\times 10^5$ と小さいことを利用して，上位 $K$ 個を列挙することを考えます．重要な事実として

$$
f(i,j,k) \ge f(i+1,j,k),f(i,j,k) \ge f(i,j+1,k),f(i,j,k) \ge f(i,j,k+1)
$$

が成り立ちます．よって，大きい方から値を列挙していったときに，必ず $f(i,j,k)$ が列挙された後に $f(i+1,j,k),f(i,j+1,k),f(i,j,k+1)$ が列挙されることが分かります．

これを踏まえれば，以下のアルゴリズムで解くことができます．

1. 優先度付きキュー $Q$ を用意し， $Q$ に $(f(1,1,1),1,1,1)$ を追加する．
2. 以下を $K$ 回繰り返す．
   * $Q$ の最大値を $(val,i,j,k)$ とする．$Q$ から $(val,i,j,k)$ を削除したうえで，$Q$ に $(f(i+1,j,k),i+1,j,k),(f(i,j+1,k),i,j+1,k),(f(i,j,k+1),i,j,k+1)$ を（まだ $Q$ に追加していなかったら）追加する．

計算量は $O(N\log⁡ N+ K \log⁡ K)$ です．

（Python の優先度付きキューは最小値を管理するため，以下の実装例では $hq$ には $f(i,j,k)$ を $−1$ 倍して追加し，22 行目の出力時に $−1$ 倍することで元に戻しています．）

```py
from heapq import heappop, heappush

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

s = set()
hq = []

def add(i, j, k):
    if i < N and j < N and k < N and (i, j, k) not in s:
        s.add((i, j, k))
        heappush(hq, (-(A[i] * B[j] + B[j] * C[k] + C[k] * A[i]), i, j, k))

add(0, 0, 0)
for t in range(K):
    val, i, j, k = heappop(hq)
    if t == K - 1:
        print(-val)
    add(i + 1, j, k)
    add(i, j + 1, k)
    add(i, j, k + 1)
```

**解説2**

---

$A,B,C$ をそれぞれ降順ソートしておきます． $f(i,j,k)=A_iB_j + B_jC_k + C_kA_i$ とします．

答えを二分探索します．判定問題として $f(i,j,k) \ge \text{mid}$ を満たす $(i,j,k)$ が $K$ 個あるか？が高速に求められれば良いです．

判定問題を愚直で解こうとすると $O(N^3)$ かかり間に合いませんが，枝刈りをすることで計算量を落とすことができます．

$$
f(i,j,k) \ge f(i+1,j,k), f(i,j,k) \ge f(i,j+1,k),f(i,j,k) \ge f(i,j,k+1)
$$

が成り立つことを利用すると，次のような判定関数のコードを書くことができます．

```cpp
bool check(long long mid) {
    int cnt = 0;
    for (int i = 1; i <= N; i++) {
        if (f(i, 1, 1) < mid) break;  // もし f(i, 1, 1) が mid より小さいならば i のループを打ち切る
        for (int j = 1; j <= N; j++) {
            if (f(i, j, 1) < mid) break;  // もし f(i, j, 1) が mid より小さいならば j のループを打ち切る
            for (int k = 1; k <= N; k++) {
                if (f(i, j, k) < mid) break;  // もし f(i, j, k) が mid より小さいならば k のループを打ち切る
                cnt += 1;
                if (cnt == K) return true;  // もし cnt が K ならば true を返す
            }
        }
    }
    return false  // false を返す
}
```

これにより，判定関数の中でループが回る回数を $O(K)$ 回に減らすことができます．よって，この問題を計算量 $O(N \log⁡ N + K(\log⁡ \max⁡ A + \log⁡ \max⁡ B + \log⁡ \max⁡ C))$ で解くことができます．

```cpp
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

def f(i, j, k):
    return A[i] * B[j] + B[j] * C[k] + C[k] * A[i]

def calc(mid):
    cnt = 0
    for i in range(N):
        if f(i, 0, 0) < mid:
            break
        for j in range(N):
            if f(i, j, 0) < mid:
                break
            for k in range(N):
                if f(i, j, k) >= mid:
                    cnt += 1
                    if cnt == K:
                        return True
                else:
                    break
    return False

ok, ng = 0, 3 * 10**18 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if calc(mid):
        ok = mid
    else:
        ng = mid

print(ok)
```

**解説3**

---

A,B,C$ をそれぞれ降順ソートしておきます． $f(i,j,k) = A_iB_j + B_jC_k + C_kA_i$ とします．

$$
f(i,j,k) \ge f(i+1,j,k), f(i,j,k) \ge f(i,j+1,k),f(i,j,k) \ge f(i,j,k+1)
$$

が成り立つことにより，答えとしてあり得る $(i,j,k)$ の組は $ijk \le K$ を満たします．よってこれらを満たす組 $(i,j,k)$ それぞれについて $f(i,j,k)$ を計算し，この中で $K$ 番目に大きいものを求めればよいです．

$ijk \le K$ を満たす組の個数は $O(K\log⁡^2 K)$ 個あります．（$K = 5\times 10^5$ のとき $48094156\approx 4.8\times 10^7$ 個です．） 長さ $O(K\log^⁡2 K)$ の列をソートするのはおそらく間に合いませんが，`c++` であれば `nth_element` を用いて $K$ 番目に大きい要素を求めれば，高速な言語であれば間に合います．

補足：$ijk \le K$ を満たす組の個数が $O(K \log^⁡2 K)$ であることは $\int_{1}^{K}(\int_{1}^{\frac{K}{1}}(\int_{1}^{\frac{K}{(xy)}}1 dz) dy) dx = O(K\log^⁡2 K)$ より従います．

---

> kyopro_friends

**公式解説1の補足**

---

この記事では index は 0 始まりとします。

[公式解説1](https://atcoder.jp/contests/abc391/editorial/12085) では、 $(i,j,k)$ が $Q$ に入っているかどうかを判定していますが、 キューへの追加の仕方を工夫することでその処理は省略することができます。

具体的には次の通りです。

1. 優先度付きキュー $Q$ を用意し， $Q$ に $(f(0,0,0),0,0,0)$ を追加する。
2. 以下を $K$ 回繰り返す。
   * $Q$ の最大値を $(val,i,j,k)$ とする．$Q$ から $(val,i,j,k)$ を削除し、
     * $j=0$ かつ $k=0$ なら $Q$ に $(f(i+1,j,k),i+1,j,k)$ を追加する
     * $k = 0$ なら $Q$ に $(f(i,j+1,k),i,j+1,k)$ を追加する
     * $Q$ に $(f(i,j,k+1),i,j,k+1)$ を追加する

実装例(Python)

```py
from heapq import heappop, heappush

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

hq = []


def add(i, j, k):
    if i < N and j < N and k < N:
        heappush(hq, (-(A[i] * B[j] + B[j] * C[k] + C[k] * A[i]), i, j, k))


add(0, 0, 0)
for t in range(K):
    val, i, j, k = heappop(hq)
    if t == K - 1:
        print(-val)
    if j==0 and k==0: add(i + 1, j, k)
    if k==0: add(i, j + 1, k)
    add(i, j, k + 1)
```

---


> Kiri8128

**$O(K^{(\frac{2}{3})} \log N \log M)$ 解法**

---

$A_i, B_i, C_i \le M (= 10^9)$ として、 $O(K^{(\frac{2}{3})} \cdot \log ⁡N \cdot \log ⁡M)$ 解法を紹介します。

答えに関する二分探索を考えることで、 $x$ を固定したときに $A_i B_j + B_j C_k + C_k A_i \ge x$ となる $(i,j,k)$ の組が $K$ 個以上あるかどうかを判定する問題に帰着できます。

以下、この判定問題を考えます。

添え字 $i,j,k$ をすべて調べると正しい答えが得られますが、計算回数が多くなる可能性があるのでうまく枝刈りをしたいです。 $i,j,k$ を昇順に並べ替えたものを $i' \le j' \le k'$ とします。 このとき i′3≤K**i**′**3**≤**K** かつ i′⋅j′2≤K**i**′**⋅**j**′**2**≤**K が成立する範囲のみを調べても結果が変わらないことが分かります。

証明

[公式解説1](https://atcoder.jp/contests/abc391/editorial/12085) で書かれているとおり、添え字について単調性があることに注意します。r=⌊K1/3⌋**r**=**⌊**K**1**/**3**⌋ とします。ここで (r+1)3>K**(**r**+**1**)**3**>**K に注意します。また f(i,j,k)=AiBj+BjCk+CkAi**f**(**i**,**j**,**k**)**=**A**i****B**j****+**B**j****C**k****+**C**k****A**i**** とします。

前者の条件（ i′3≤K**i**′**3**≤**K** ）は、 「 i>r**i**>**r** かつ j>r**j**>**r** かつ k>r**k**>**r** の範囲を調べなくて良い」と等価です。この範囲の最小のものは f(r+1,r+1,r+1)**f**(**r**+**1**,**r**+**1**,**r**+**1**) です。 この値は、 i,j,k**i**,**j**,**k** を i≤r+1,j≤r+1,k≤r+1**i**≤**r**+**1**,**j**≤**r**+**1**,**k**≤**r**+**1** の範囲を動かしたときの最小値なので、これらを除いても上位 K**K** 個には影響がないことが分かります。

後者についても同様に示せます。

略証

すなわち、 i′=1,2,⋯,⌊K1/3⌋**i**′**=**1**,**2**,**⋯**,**⌊**K**1**/**3**⌋** 、 j′=1,2,⋯,⌊Ki′⌋**j**′**=**1**,**2**,**⋯**,**⌊**i**′**K******⌋ の範囲のみ調べれば十分です。 この決め方は O(K2/3)**O**(**K**2**/**3**)** あります。


**∫**1**K**1**/**3****t**K** **d**t**=**2**(**K**2**/**3**−**K**1**/**2**)**∈**O**(**K**2**/**3**)**


**i**′**,**j**′** を決めると k′**k**′ に関する二分探索で条件を満たす k′**k**′ の個数が分かります。

添え字 i,j,k**i**,**j**,**k** の大小関係をすべて試し、重複がないようにカウントすることで、 O(K2/3⋅log⁡N)**O**(**K**2**/**3**⋅**log**N**) で判定問題を解くことができます。

全体の計算量は O(K2/3⋅log⁡N⋅log⁡M)**O**(**K**2**/**3**⋅**log**N**⋅**lo**g**M**) です。
