<!-- # A 問題 - [Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a)

**【問題概要】**
𝑁 個の足場があって、𝑖 番目の足場の高さは ℎ𝑖 です。
最初、足場 1 にカエルがいて、ぴょんぴょん跳ねながら足場 𝑁 へと向かいます。カエルは足場 𝑖 にいるときに

* 足場 𝑖 から足場 𝑖+1 へと移動する (そのコストは |ℎ𝑖−ℎ𝑖+1|)
* 足場 𝑖 から足場 𝑖+2 へと移動する (そのコストは |ℎ𝑖−ℎ𝑖+2|)

のいずれかの行動を選べます。カエルが足場 1 から足場 𝑁 へと移動するのに必要な最小コストを求めよ。

**【制約】**

* $2 \le N \le 10^5$

## 解法

再び A 問題について、今度は実装を見据えた考察をして行きます。DP テーブルの作り方はとても素直で、

* dp[ i ] := カエルが足場 i へと移動するのに必要な最小コスト

とすればよいでしょう (注意点として問題文は 1-indexed ですが、ここでは 0-indexed にしてみます)。そうするとまず初期条件は

* dp[ 0 ] = 0

になります。足場 0 からスタートするので、スタート時点でのコストは 0 です。

[![A1.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F8b2640e1-64dd-85e1-e15c-b3c32e81d290.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=18c94b4bc566c5d55cf94784900fe0fc)](https://camo.qiitausercontent.com/2b5f9cf114d94951250a853ab3d030941f4a4279/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f38623236343065312d363464642d383565312d653135632d6233633332653831643239302e6a706567)

次に DP 遷移を考えます。カエルのぴょんぴょんする方法を可視化すると、上図のような構造になっています。ここで

* 青色: 足場を飛ばさない
* 赤色: 足場を 1 個飛ばす

を表しています。図は 𝑁=7 の場合を描いていますが、カエルは図のノード 0 から、ノード 𝑁−1 まで「青色」「赤色」のいずれかの矢印を渡って進むことになります。そのような経路は何通りも考えられますが、そのうち最もコストが小さいものを選ぶ問題ということになります。

このままだとゴチャゴチャしているので、ノードを 1 個固定して、そのノードへの遷移としてどんなものが考えられるかを見てみましょう:

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F11df76c6-0e37-1864-1283-10b725ec040d.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8fb705e289c75ab061fcfe75efe9242c)](https://camo.qiitausercontent.com/b394d3d6bca8bf1060f5fb5b96f25b63e5b7a361/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f31316466373663362d306533372d313836342d313238332d3130623732356563303430642e6a706567)

一気に考えやすくなりました。ノード 𝑖 へと遷移する方法は

1. ノード 𝑖−1 から遷移して来る
2. ノード 𝑖−2 から遷移して来る

の 2 通りあることがわかります。ここで重要な仮定として「 **ノード 𝑖−2 やノード 𝑖−1 までの最適な進み方はわかっている** 」としましょう。すなわち、

* ノード 𝑖−1 まで最適な進み方をしたとき、ノード 𝑖−1 までの最小コストは dp[ i - 1 ]
* ノード 𝑖−2 まで最適な進み方をしたとき、ノード 𝑖−2 までの最小コストは dp[ i - 2 ]

という状態です。このとき、上記の 2 通りの遷移方法をそれぞれを採用したときの、ノード 𝑖 に到達したときのコストは

1. ノード 𝑖−1 から遷移して来た場合: dp[ i - 1 ] + abs( h[ i ] - h[ i - 1 ] )
2. ノード 𝑖−2 から遷移して来た場合: dp[ i - 2 ] + abs( h[ i ] - h[ i - 2 ] )

となります。このうちの小さい方が、ノード 𝑖 に到達するまでの最小コスト、すなわち dp[ i ] の値になります。以上の処理を実装すると、先に登場した chmin を用いて

```cpp
chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]));
chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]));
```

という風に書くことができます。あとはこれを各 𝑖=1,2,…,𝑁−1 に対して順にループを回していけばよいです。それにより、dp[ 1 ], dp[ 2 ], dp[ 3 ], ... の値が順々に決まって行きます。

注意点として、dp[ 1 ] について更新しようとしている場合には、「2 個前のノードがない」ので、上記の 2 通りの遷移のうち 2 番目の遷移はしないようにしています。

**【正解コードの一例】**

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }

const long long INF = 1LL << 60;

// 入力
int N;
long long h[100010];

// DP テーブル
long long dp[100010];

int main() {
    int N; cin >> N;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 100010; ++i) dp[i] = INF;

    // 初期条件
    dp[0] = 0;

    // ループ
    for (int i = 1; i < N; ++i) {
        chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]));
        if (i > 1) chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]));
    }

    // 答え
    cout << dp[N-1] << endl;
}
```

## 別解 1: 配る DP

今回は「貰う DP」の形で考えてみました。すなわち、「 **ノード 𝑖 への遷移方法を考える** 」という方向性で考えていました (「貰う DP」は「集める DP」と呼ぶこともあります)。

反対に通称「配る DP」と呼ばれる書き方もあります。すなわち、「 **ノード 𝑖 からの遷移方法を考える** 」という方向性です。その場合下図のような遷移を考えることになります。

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F34996fb1-55a3-4ccb-19e3-7ca5bb3654bd.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4dec42ef4dd661b164e83804c2c32592)](https://camo.qiitausercontent.com/f540a7a683c1e0e33af0f50855a88515043ea745/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f33343939366662312d353561332d346363622d313965332d3763613562623336353462642e6a706567)

「貰う DP」のときは「dp[ i - 2 ] や dp[ i - 1 ] の値がわかっているときに、dp[ i ] の値を更新する」という考え方でしたが、今回は「dp[ i ] の値はすでにわかっているときに、その値を用いて、dp[ i + 1 ] や dp[ i + 2 ] の値を更新します。

配る DP で更新処理を実装すると

```cpp
chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
```

という風になります。細かな違いはあれど、貰う DP とあまり大きくは変わらないですね。コード全体も大きくは変わらないです:

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

const long long INF = 1LL << 60;

// 入力
int N;
long long h[100010];

// DP テーブル
long long dp[100010];

int main() {
    int N; cin >> N;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 100010; ++i) dp[i] = INF;

    // 初期条件
    dp[0] = 0;

    // ループ
    for (int i = 0; i < N; ++i) {
        chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
        chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
    }

    // 答え
    cout << dp[N-1] << endl;
}
```

## 貰う DP と配る DP との違い

DP を書き始めたばかりの頃は、しばしば「貰う DP」と「配る DP」との違いに困惑してしまいます。しかし広い目で見るとほとんど一緒で、どちらの方法でも下図のようなグラフのすべての矢印について (矢印の根元を from、先端を to とします)

```
chmin(dp[to], dp[from] + (矢印の重み));
```

という更新を 1 回ずつ行っています。その更新の順番が違うだけです。なおこのような更新のことを専門用語で「 **緩和** 」と呼びます。緩和をするという考え方が DP の本質と言えるでしょう。最短路アルゴリズムとして知られる Bellman-Ford 法や Dijkstra 法も緩和フレームワークに則ったアルゴリズムなので DP の一種と言えます。

[![A1.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2Fde3d8298-65c0-d652-a459-a1fc8b07e326.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=48f4273fd6350286294ff7d5672d4caf)](https://camo.qiitausercontent.com/84b3e45b6f81e5171f08915313bb7ddd760969d9/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f64653364383239382d363563302d643635322d613435392d6131666338623037653332362e6a706567)

今回のような DP で重要なことは、「貰う DP」でも「配る DP」でも

---

**ノード from からノード to への緩和を行うときは、
dp[from] の値の更新は完了している**

---

という点です。このルールさえ満たしていれば、どのような順番で緩和を行ってもいいわけです。このルールを保証できる代表的な緩和順として「貰う DP」と「配る DP」がある、という感じです。ただし、より高度な問題においては細かい違いが生じて来ることもあります。[この記事](https://qiita.com/drken/items/ace3142967c4f01d42e9#%E8%B2%B0%E3%81%86-dp-%E3%81%A8%E9%85%8D%E3%82%8B-dp-%E3%81%AE%E6%AF%94%E8%BC%83)にまとめてみたので、参考にしていただけたらと思います。

## 別解 2: メモ化再帰

この問題を見て、再帰的な関係式を立てたくなった方もいるのではないでしょうか。すなわち

```cpp
long long rec(int i) {
    // 足場 0 のコストは 0
    if (i == 0) return 0;

    // i-1, i-2 それぞれ試す
    long long res = INF;
    chmin(res, rec(i-1) + abs(h[i] - h[i - 1])); // 足場 i-1 から来た場合
    chmin(res, rec(i-2) + abs(h[i] - h[i - 2])); // 足場 i-2 から来た場合

    // 答えを返す
    return res;
}
```

という感じの再帰関数を用意しておいて、rec(N-1) を答えとして出力する考え方です。発想としては、

* 足場 N-1 までの最小コストを求めたい
* それは足場 N-2 までの最小コストや、足場 N-3 までの最小コストがわかっていればいいので、再帰的に解く
* ...
* 一般に足場 i までの最小コストを求める関数を作り、それは足場 i-1, i-2 までの最小コストがわかっていればいいので、それを再帰的に解く
* ...
* 最終的にはすべての再帰は足場 0 の場合に落ち着く。足場 0 の場合のコストは 0 なのでそれをリターンする

という感じです。実はこれでほとんど正解に近いのですが、このままだと計算時間が途方もないことになってしまいます。

---

フィボナッチ数列の値を再帰関数で求めるとき、メモして行かないと計算時間が爆発する

---

という話を聞いたことのある方も多いと思います。それとまったく同じ現象が起こってしまいます。下図は、最初に rec(5) を呼び出したときの再帰の様子を図示したものです。例えば rec(1) などは本来は 1 回計算すれば答えがわかって十分なはずなのに 5 回も呼び出されてしまっています。この図は rec(5) の場合であってまだおとなしいですが、rec(6), rec(7), ... と増やして行くと、関数が呼び出される回数が指数的に大きくなることが知られています。

[![A_fibonacchi.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F0e4dfed3-10b0-5bb6-9b66-214676a2b09e.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fa3f3e0303b8a4a16e0f1e3c76caf281)](https://camo.qiitausercontent.com/fe8a36727059c5014db86963253590f4d1a44642/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f30653464666564332d313062302d356262362d396236362d3231343637366132623039652e6a706567)

そこで対策として、

---

rec(i) が一度呼び出されてその答えがわかったならば、その時点で答えを**メモ**しておく

---

とするのが**メモ化再帰**です。それを踏まえて実装すると以下のようになります。実は rec(i) と書いているところを dp[i] と置き換えてみると、「貰う DP」とまったく同じことをしていることがわかります。慣れれば、ほとんどの問題に対しては「貰う DP」「配る DP」「メモ化再帰」とで大きな違いはないと感じられます。

なお、DP をはじめて触るときに、このように「再帰」の重複処理をメモする発想から入った方が馴染みやすいと感じる方もいれば、はじめから dp 配列を想起した方が馴染みやすい方もいるようです。

* dp 配列において dp[ i ] という式には、足場 i までの探索の結果がまとめられている
* rec(i) の探索結果は一度終了したらメモして使い回せばいい

というのは結局同じことをしているので、様々な DP に触れて行くことでいずれは、このような「 **探索過程をまとめる** 」という DP のイメージに集約されて行き、通常のボトムアップに for 文を回すような DP の書き方も、トップダウンにも思えるようなメモ化再帰の書き方も、有機的に結び付いて行くものと思います。

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

const long long INF = 1LL << 60;

// 入力
int N;
long long h[100010];

// メモ用の DP テーブル
long long dp[100010];

long long rec(int i) {
    // DP の値が更新されていたらそのままリターン
    if (dp[i] < INF) return dp[i];

    // 足場 0 のコストは 0
    if (i == 0) return 0;

    // i-1, i-2 それぞれ試す
    long long res = INF;
    chmin(res, rec(i-1) + abs(h[i] - h[i - 1])); // 足場 i-1 から来た場合
    if (i > 1) chmin(res, rec(i-2) + abs(h[i] - h[i - 2])); // 足場 i-2 から来た場合

    // 結果をメモしながら、返す
    return dp[i] = res;
}

int main() {
    int N; cin >> N;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 100010; ++i) dp[i] = INF;

    // 答え
    cout << rec(N-1) << endl;
}
```

## DP のコツ: 「再帰的な全探索」のイメージを磨こう！

DP に入門するためには、とにかく「 **再帰的に全探索することのイメージを磨きあげる** 」ことが重要だと言われます。たとえメモ化再帰ではなく、ボトムアップに for 文を回してテーブルを更新する DP を直接考えていたとしても、

* dp[ i ] には i 番目までの探索過程がまとめられている

ということの理解が重要だと思います (各書籍や [wikipedia](https://ja.wikipedia.org/wiki/%E5%8B%95%E7%9A%84%E8%A8%88%E7%94%BB%E6%B3%95) などで「 **部分構造最適性の利用** 」といった言葉でやたら難しく説明される部分ですね)。しばしば DP に対しては

* 全探索のメモ化としてとらえる
* 漸化式としてとらえる

の 2 つの大きな派閥に分かれる印象ですが、漸化式派も DP テーブルの各マス dp[ i ] に探索過程がまとめられているイメージを抱きながら問題を解いていると思うので、使い慣れている思考フォーマットが違うだけだと言えるでしょう。

まとめると、「再帰的な全探索」に対するイメージと勘の練度を高めて行くことが、DP を習得する上で重要だと思います。

## DP の計算量

DP は特別な最適化がほどこされたものでなければ、計算量の解析はとても簡単です。下図のようなグラフの各枝を順に 1 回ずつ緩和していく営みになりますので、計算量は

---

𝑂(𝑉+𝐸)　(𝑉 は DP テーブルのノード数、𝐸 はエッジ数)

[![A1.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2Fcd5f17c8-6afb-a991-78da-7a5527bccaf0.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=52794b115db800304ed7837dea9a6075)](https://camo.qiitausercontent.com/375b1d77f281a29cf62449cb8d9472cb653c8817/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f63643566313763382d366166622d613939312d373864612d3761353532376263636166302e6a706567)

---

となることがほとんどです。注意点として 𝑂(𝐸) ではなく 𝑂(𝑉+𝐸) としています。仮にエッジがまったくなかったとしても、ノード全体を見回す処理を書くことになりますので (メモ化再帰であればそうとは限らないですが...)、念のために 𝑂(𝑉+𝐸) と書いています。実際上はほとんどの場合で 𝑂(𝐸) と思って差し支えないです。今回の問題では

* 各ノードにつき (ノード数は 𝑁)
* 高々 2 通りの遷移

があるので、エッジ数は高々 2𝑁 以下です。よって計算量は 𝑂(𝑁) となります。ノード数が 𝑁 であっても計算量が 𝑂(𝑁2) となる場合もあることに注意が必要です。

## 類題

* [ABC 040 C - 柱柱柱柱柱](https://atcoder.jp/contests/abc040/tasks/abc040_c)　(まったく同じ問題ですね)
* [ABC 129 C - Typical Stairs](https://atcoder.jp/contests/abc129/tasks/abc129_c)　(数え上げですが良く似た構造の問題です)
* [AOJ 0168 観音堂](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0168)　(遷移が 2 種類から 3 種類になります) -->

---

# Problem A - [Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a)

**Problem Description**

There are $N$ platforms, and the height of the $i^{th}$ platform is $h_i$.
Initially, a frog is on platform $1$ and jumps to platform $N$ while hopping.
When the frog is on platform $i$:

* It can move from platform $i$ to platform $i+1$ (the cost is $|h_i - h_{i+1}|$)
* It can move from platform $i$ to platform $i+2$ (the cost is $|h_i - h_{i+2}|$)

Find the minimum cost required for the frog to move from platform $1$ to platform $N$.

**Constraints**

* $2 \le N \le 10^5$

## Approach

Once again, let's consider the implementation-focused analysis for problem A. The construction of the DP table is straightforward:

* $dp[i]$ := Minimum cost required for the frog to move to platform $i$

(Note: The problem statement is 1-indexed, but here we'll consider it as 0-indexed) 

So, the initial condition is:

* $dp[0] = 0$

because the frog starts at platform $0$, hence the cost at the starting point is $0$.

![A1.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F8b2640e1-64dd-85e1-e15c-b3c32e81d290.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=18c94b4bc566c5d55cf94784900fe0fc)

Next, let's think about the $DP$ transitions. Visualizing how the frog hops, we have the structure depicted in the above figure. Here,

* Blue arrows: Not skipping a platform
* Red arrows: Skipping one platform

The figure illustrates the case for $N = 7$, where the frog moves from node $0$ to node $N−1$ through either $\color{blue}blue$ or $\color{red}red$ arrows. Although there can be multiple such paths, we're interested in selecting the one with the minimum cost.

Now, to simplify things, let's fix one node and see what transitions are possible:

![Nodes.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F11df76c6-0e37-1864-1283-10b725ec040d.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8fb705e289c75ab061fcfe75efe9242c)

This makes things much easier to consider. There are two possible ways for the frog to transition to node $i$:

1. It hops from node $i−1$.
2. It hops from node $i−2$.

A critical assumption here is that **the optimal movement up to nodes $i−2$ and $i−1$ is known**. In other words,

* If the frog hops optimally up to node $i−1$, the minimum cost up to node $i−1$ is $dp[i - 1]$.
* If the frog hops optimally up to node $i−2$, the minimum cost up to node $i−2$ is $dp[i - 2]$.

At this point, the cost to reach node $i$, given the two options above, would be:

1. If it hopped from node $i−1$ : $dp[i - 1] + abs(h[i] - h[i - 1])$
2. If it hopped from node $i−2$ : $dp[i - 2] + abs(h[i] - h[i - 2])$

The minimum of these two is the minimum cost to reach node $i$, which is $dp[i]$. By implementing this logic, we can use `chmin` as follows:

```cpp
chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]));
chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]));
```

We repeat this process for each $i = 1, 2, \cdots , N−1$, and thus determine the values of $dp[1], dp[2], dp[3], \cdots, dp[N-1]$.

Note: When updating $dp[1]$, we do not perform the second transition since there's no node $2$ steps back.

**[Sample Code]**

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }

const long long INF = 1LL << 60;

// Input
int N;
long long h[100010];

// DP Table
long long dp[100010];

int main() {
    int N; cin >> N;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // Initialization (initialized to INF for minimization problem)
    for (int i = 0; i < 100010; ++i) dp[i] = INF;

    // Initial condition
    dp[0] = 0;

    // Loop
    for (int i = 1; i < N; ++i) {
        chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]));
        if (i > 1) chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]));
    }

    // Answer
    cout << dp[N-1] << endl;
}
```

## Solution 1: Forward DP

This time, I considered the problem in the form of "receiving DP". That is, I was thinking in the direction of "considering the transition to node 𝑖" (receiving DP is also sometimes referred to as "accumulating DP").

Conversely, there is also a writing style called "forward DP". That is, it's the direction of "considering the transition from node $i$". In that case, we would consider transitions like the one in the diagram below:

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F34996fb1-55a3-4ccb-19e3-7ca5bb3654bd.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4dec42ef4dd661b164e83804c2c32592)](https://camo.qiitausercontent.com/f540a7a683c1e0e33af0f50855a88515043ea745/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f33343939366662312d353561332d346363622d313965332d3763613562623336353462642e6a706567)

When we were using "receiving DP", we were updating the value of $dp[i]$ based on the idea of "updating $dp[i]$ when the values of $dp[i - 2]$ or $dp[i - 1]$ are known". But this time, with "forward DP", we update the values of $dp[i + 1]$ or $dp[i + 2]$ when the value of $dp[i]$ is already known.

Implementing the update process with forward DP looks like this:

```cpp
chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
```

It's not very different from receiving DP, although there are some subtle differences. The entire code doesn't change much either:

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

const long long INF = 1LL << 60;

// 入力
int N;
long long h[100010];

// DP テーブル
long long dp[100010];

int main() {
    int N; cin >> N;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 100010; ++i) dp[i] = INF;

    // 初期条件
    dp[0] = 0;

    // ループ
    for (int i = 0; i < N; ++i) {
        chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]));
        chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]));
    }

    // 答え
    cout << dp[N-1] << endl;
}
```

## Difference between "Receiving DP" and "Forward DP"

When you're just starting out with DP, you often find yourself confused about the difference between "receiving DP" and "forward DP". But if you look at it broadly, they are almost the same. In both methods, you are performing the following update for all arrows in the graph (with the root of the arrow as "from" and the tip as "to"):

```cpp
chmin(dp[to], dp[from] + (weight of the arrow));
```

The only difference lies in the order of these updates. These updates are often referred to by the technical term "**relaxation**". It can be said that the concept of relaxation is essential to DP. Algorithms like Bellman-Ford and Dijkstra, known as shortest path algorithms, also follow the relaxation framework, so they can be considered as types of DP.

In DP like the one in this case, the important thing is that whether it's "receiving DP" or "forward DP",

---

**When performing relaxation from node "from" to node "to", the update of dp[from] has already been completed.**

---

As long as this rule is satisfied, you can perform relaxation in any order. "Receiving DP" and "forward DP" are typical relaxation orders that guarantee this rule. However, in more advanced problems, there may be some subtle differences. I've summarized them in [this article](https://qiita.com/drken/items/ace3142967c4f01d42e9#%E8%B2%B0%E3%81%86-dp-%E3%81%A8%E9%85%8D%E3%82%8B-dp-%E3%81%AE%E6%AF%94%E8%BC%83), so feel free to check it out for reference.

## Solution 2: Memoization with Recursion

Looking at this problem, some of you might want to establish a recursive relationship. That is,

```cpp
long long rec(int i) {
    // Cost at node 0 is 0
    if (i == 0) return 0;

    // Try i-1 and i-2 respectively
    long long res = INF;
    chmin(res, rec(i-1) + abs(h[i] - h[i - 1])); // When coming from node i-1
    chmin(res, rec(i-2) + abs(h[i] - h[i - 2])); // When coming from node i-2

    // Return the answer
    return res;
}
```

This is the approach of preparing a recursive function like the one above and outputting $rec(N-1)$ as the answer. The idea is:

* We want to find the minimum cost up to step $N-1$.
* This can be done recursively if we know the minimum costs up to steps $N-2$, $N-3$, and so on.
* ...
* Generally, we create a function to find the minimum cost up to step $i$, which recursively solves the minimum costs up to steps $i-1$ and $i-2$.
* ...
* Ultimately, all recursions converge to the case of step $0$. Since the cost at step $0$ is $0$, we return this value.

That's the idea. In fact, this is almost close to the correct solution, but if left as it is, the computation time becomes enormous.

---

When calculating the values of the Fibonacci sequence using a recursive function, if you don't memoize, the computation time explodes.

---

<!-- Many of you may have heard about the need to memoize when calculating Fibonacci sequence values using a recursive function, as computation time explodes otherwise. -->

 The same phenomenon occurs here. The diagram below illustrates the recursion when rec(5) is initially called. For example, rec(1) should ideally be calculated once to obtain the answer, yet it is called five times. This diagram shows the case for rec(5), which is still relatively calm, but as we increase to rec(6), rec(7), and so on, the number of function calls grows exponentially, as is well known.

[![A_fibonacchi.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2F0e4dfed3-10b0-5bb6-9b66-214676a2b09e.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fa3f3e0303b8a4a16e0f1e3c76caf281)](https://camo.qiitausercontent.com/fe8a36727059c5014db86963253590f4d1a44642/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f30653464666564332d313062302d356262362d396236362d3231343637366132623039652e6a706567)

To address this issue,

---

If $rec(i)$ is called once and its answer is known, then memoize the answer at that point.

---

This is what we call **memoization**. Implementing this, we realize it's exactly the same as "top-down DP" when we replace $rec(i)$ with $dp[i]$. With practice, you'll find that there's not much difference between "top-down DP," "bottom-up DP," and "memoization" for most problems.

When starting to learn DP, some may find it easier to understand by first considering the idea of "memoizing" duplicate recursive calculations, while others might feel more comfortable immediately thinking of `dp` arrays.

- In the $dp$ array, the expression $dp[i]$ summarizes the results of exploring up to position $i$.
- Once the result of $rec(i)$ is obtained, it can be memoized and reused.

Ultimately, they are doing the same thing. By encountering various DP problems, you'll eventually realize that they all converge to the concept of "**summarizing exploration processes**" in DP. Whether it's the typical bottom-up DP with loops or the memoization method that seems more like top-down, they organically connect and complement each other.

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

const long long INF = 1LL << 60;

// 入力
int N;
long long h[100010];

// メモ用の DP テーブル
long long dp[100010];

long long rec(int i) {
    // DP の値が更新されていたらそのままリターン
    if (dp[i] < INF) return dp[i];

    // 足場 0 のコストは 0
    if (i == 0) return 0;

    // i-1, i-2 それぞれ試す
    long long res = INF;
    chmin(res, rec(i-1) + abs(h[i] - h[i - 1])); // 足場 i-1 から来た場合
    if (i > 1) chmin(res, rec(i-2) + abs(h[i] - h[i - 2])); // 足場 i-2 から来た場合

    // 結果をメモしながら、返す
    return dp[i] = res;
}

int main() {
    int N; cin >> N;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 100010; ++i) dp[i] = INF;

    // 答え
    cout << rec(N-1) << endl;
}
```

## Tips for DP: Refine Your Mental Image of "Recursive Exploration"!

To get started with DP, it's often said that refining your mental image of "**recursive exploration**" is crucial. Even if you're not directly considering DP with memoization, and instead are thinking about DP where you iterate through a `for` loop bottom-up to update the table:

* Understanding that $dp[i]$ contains the exploration process up to the $i^{th}$ position is important.

This understanding is crucial (often explained in books and on Wikipedia as the "utilization of optimal substructure"). While there's often a divide in the DP community between those who see it as:

* Memoization of exhaustive search
* Recurrence relations

Both factions likely approach problems with the mental image that the exploration process is summarized in each cell $dp[i]$ of the DP table. So, it's mostly a matter of different thought formats you're accustomed to.

In summary, refining your mental image and intuition about "recursive exploration" is crucial for mastering DP.

## Computational Complexity of DP

Unless DP has special optimizations applied, analyzing its computational complexity is straightforward. Since it involves relaxing each edge of a graph like the one below once:

---

$O(V + E)$　($V$ is the number of nodes in the DP table, $E$ is the number of edges)

[![A1.jpg](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F182963%2Fcd5f17c8-6afb-a991-78da-7a5527bccaf0.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=52794b115db800304ed7837dea9a6075)](https://camo.qiitausercontent.com/375b1d77f281a29cf62449cb8d9472cb653c8817/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3138323936332f63643566313763382d366166622d613939312d373864612d3761353532376263636166302e6a706567)

---

This is mostly the case. Note that it's written as $O(V + E)$ instead of $O(E)$. Even if there were no edges at all, you'd still have to iterate through all the nodes (although this might not be the case with memoization recursion...), so it's written as $O(V + E)$ just to be safe. In practice, it's almost always safe to consider it as $O(E)$. In this problem:

* For each node (with $N$ nodes in total),
* There are at most $2$ possible transitions,

so the number of edges is at most $2N$. Therefore, the complexity is $O(N)$. However, it's important to note that there are cases where even if the number of nodes is $N$, the complexity could be $O(N^2)$.

## Similar Problems

* [ABC 040 C - Building](https://atcoder.jp/contests/abc040/tasks/abc040_c) (The same problem)
* [ABC 129 C - Typical Stairs](https://atcoder.jp/contests/abc129/tasks/abc129_c) (Similar problem with counting, but with a similar structure)
* [AOJ 0168 Kannon](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0168) (Transitions go from 2 to 3 types)

> This is translate from editorial qiita
