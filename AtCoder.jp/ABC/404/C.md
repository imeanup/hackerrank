# [C - Cycle Graph?](https://atcoder.jp/contests/abc404/tasks/abc404_c)

与えられたグラフがサイクルグラフであることの必要十分条件は次の2つをともに満たすことです

* 全ての頂点の次数が $2$ である
* 連結である

これはDFS/BFS/Union-Findなどを用いることで判定することができます。

#### 想定誤解法1

* 全ての頂点の次数が $2$ である

反例

```
6 6
1 2
2 3
3 1
4 5
5 6
6 4
```

#### 想定誤解法2

* 連結である
* $N=M$ である

反例

```
4 4
1 2
2 3
3 1
1 4
```

---

A graph is a cycle graph if and only if **both** of the following conditions hold:

* Every vertex has degree 2.
* The graph is connected.

You can check these with a simple DFS/BFS or Union–Find.

#### Common Wrong Approach 1

* Check only that every vertex has degree 2.

**Counterexample:**

```
6 6
1 2
2 3
3 1
4 5
5 6
6 4
```

Here each vertex has degree 2, but the graph is two disjoint triangles, not one single cycle.

#### Common Wrong Approach 2

* Check that the graph is connected.
* Check that $N = M$.

**Counterexample:**

```
4 4
1 2
2 3
3 1
1 4
```

This graph is connected and has $N=M=4$, but vertex 4 has degree 1, so it is not a cycle.
****
