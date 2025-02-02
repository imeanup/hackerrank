## [C - Pigeonhole Query](https://atcoder.jp/contests/abc391/tasks/abc391_c)

> toam

この問題は

* それぞれの鳩がどの巣にいるか
* それぞれの巣に鳩が何匹いるか
* 鳩が複数いる巣が何個あるか

を管理することで解くことができます．鳩 $i$ がいる巣を $pos[i]$，巣 $i$ にいる鳩の数を $cnt[i]$，鳩が複数いる巣の数を $ans$ とします．クエリ $2$ では $ans$ を出力すればよいです．

クエリ $1$ について考えます．鳩 $P$ の移動によって $ans$ が変わるのは以下の $2$ つが考えられます．

* もともと鳩 $P$ がいた巣にいる鳩の数が $2$ から $1$ に減ったとき
* 鳩 $P$ が巣 $H$ に移動したあとに，巣 $H$ にいる鳩の数が $1$ から $2$ に増えたとき

これを踏まえたうえで，鳩 $P$ の移動に応じて $pos, cnt, ans$ を変更すればよいです．詳しくは実装例をご覧ください．

```py
N, Q = map(int, input().split())
ans = 0
cnt = [0] + [1] * N
pos = list(range(N + 1))
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1:]
        # 鳩 P は移動する前は巣 pos[P] にいる
        # 鳩 P が移動することで 巣 pos[P] にいる鳩の数が 2 から 1 に減る場合, ans を 1 減らす
        if cnt[pos[P]] == 2:
            ans -= 1
        # 巣 pos[P] の鳩の数を 1 減らす
        cnt[pos[P]] -= 1

        # 鳩 P がいる巣を H に変更する
        pos[P] = H
        # 巣 H の鳩の数を 1 増やす
        cnt[pos[P]] += 1
        # 鳩 P が移動することで 巣 H にいる鳩の数が 1 から 2 に増える場合，ans を 1 増やす
        if cnt[pos[P]] == 2:
            ans += 1
    else:
        print(ans)

```

---

This problem can be solved by keeping track of the following:

- Which nest each pigeon is in  
- The number of pigeons in each nest  
- The number of nests that contain multiple pigeons  

Let $pos[i]$ be the nest where pigeon $i$ is located, $cnt[i]$ be the number of pigeons in nest $i$, and $ans$ be the number of nests that contain multiple pigeons.  

For **Query 2**, simply output $ans$.  

For **Query 1**, the value of $ans$ changes in the following two cases:

1. When the number of pigeons in the original nest of pigeon $P$ decreases from 2 to 1.  
2. When the number of pigeons in the new nest $H$ increases from 1 to 2 after pigeon $P$ moves.  

Considering the above, we update $pos, cnt, ans$ accordingly when pigeon $P$ moves. See the implementation example for details.  

### Implementation Example (Python):

```py
N, Q = map(int, input().split())
ans = 0
cnt = [0] + [1] * N
pos = list(range(N + 1))

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1:]
        # Pigeon P was originally in nest pos[P]
        # If Pigeon's movement reduces the pigeon count in pos[P] from 2 to 1, decrease ans
        if cnt[pos[P]] == 2:
            ans -= 1
        # Decrease the pigeon count in pos[P]
        cnt[pos[P]] -= 1

        # Update the nest for pigeon P to H
        pos[P] = H
        # Increase the pigeon count in nest H
        cnt[pos[P]] += 1
        # If Pigeon's movement increases the pigeon count in H from 1 to 2, increase ans
        if cnt[pos[P]] == 2:
            ans += 1
    else:
        print(ans)
```
