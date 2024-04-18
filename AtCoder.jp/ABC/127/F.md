<!-- ## F: Absolute Minima

$N$ 個の関数が与えられており、$f(x) = \sum N_{i=1}^N (|x - a_i| + b_i)$ となっている時を考えます。まず、$f(x) = \sum_{i=1}^N |x-a_i| + \sum_{i=1}^N b_i $ と分解でき、項 $\sum_{i=1}^N b_i$ は定数であるため、最小値を考える際には影響を与えない 事が分かります。よって、$\sum_{i=1}^N |x- a_i|$ の最小値を与える x を求め、その最小値に $\sum_{i=1}^N b_i$ を足したものを 出力すれば良いです。

以下、簡単のため、$\{a_i\}$ が昇順に整列されていると仮定し、$a_0 = −\infty, a_{N+1} = \infty$ とおくことにします。

$\sum^N_{i=1} |x − a_i|$ の最小値はどのようにして求めれば良いでしょうか？今、$i$ 番目の絶対値関数 $|x − a_i|$ は $x < a_i$ において傾き $−1$ の $1$ 次関数、$x > a_i$ において傾き $1$ の $1$ 次関数になっています。$1$ 次関数同士を足 し合わせても $1$ 次関数になる事を考えると、$i = 0, \cdots , N$ それぞれにおいて、区間 $[a_i, a_{i+1}]$ 内で $f(x)$ は $1$ 次 関数と見做すことができます。

更に、$x$ が小さいほど、$N$ 個の関数の内、傾きが $−1$ であるような絶対値関数が増え、$x$ が大きいほど傾き が $1$ であるような絶対値関数が増えることを考えると、$f(x)$ の各区間 $[a_i, a_{i+1}]$ 内における $1$ 次関数の傾きは 単調に増加します（これは凸関数の和は凸関数ということから考えても良いです）。よって、これは凸関数で あり、傾きが $0$ であるような区間（実際には $1$ 点のみからなる区間になっている可能性もあります）を求め、その区間内の点を $1$ つ出力すれば良い、ということが分かります。

傾きが $0$ であるような区間をどのようにして求めれば良いでしょうか？ここで、絶対値関数 $|x − a_i|$ にお
いて、傾きの変化点は $x = a_i$ であり、$x = a_i$ を “またいだ” 時に傾きが $2$ だけ増えることに注目します。こ のことは、複数の絶対値関数を足し合わせても変わることはありません。すなわち、関数 $f(x)$ においても、$x = a_i$ を “またいだ” 際、傾きは $2$ だけ増加します（ただし、同じ絶対値関数が複数含まれる時、すなわち $a_i = a_j$ となる $i, j$ が存在するような場合には、含まれる個数分だけ増加することに注意してください）。

そして、区間 $[a_0 = −\infty, a_1]$ において、$f(x)$ の傾きは $−N$ であるため、大雑把に言えば、$\dfrac{N}{2}$ 個の変化点を “またぐ” と傾きが $0$ となることが分かります。すなわち、昇順に並べた全ての変化点の内、ちょうど真ん中 にある変化点（$N$ が偶数の場合には真ん中にある $2$ つの変化点の間）において $f(x)$ は傾きが $0$ となり、最小 値を取ります。

この計算方法を実装する際には、変化点をソートした状態で格納してくれるデータ構造（以下セットと呼
ぶ）を $2$ 個用います（例えば C++ では multiset です）。片方のセットには昇順に並べた変化点の内、左半分 を、もう片方のセットには右半分を全て管理させます。この時、$1$ つ目のセットの最右点と $2$ つ目のセットの 最左点の間の区間において $f(x)$ は傾き $0$ となります。

更新クエリ $(a_i, b_i)$ が来た際には、値 $a_i$ を $2$ 個、元と同じ条件（左半分を片方のセット、右半分をもう片方 のセット）を満たすよう適切にセットに挿入すれば良いです（変化点をあえて $2$ 個挿入することによって、「$1$ つの変化点につき傾きが $1$ 変わる」と思うことが出来、シンプルになります）。

さて、最小値を与える点は分かったので、具体的な最小値を求めます。これは、
* 新しく挿入された点が、元々最小値を与えた区間に含まれるならば $0$
* 区間から外れているならば、区間の端点との距離（どちらか短い方）

を元の最小値に足したものになります。

以上から、更新・求値両方を高々定数回のセットの操作のみによって実現する事ができ、$O(Q \log Q)$ で問
題を解くことができます。また、凸性に基づいた値自体に対する三分探索や、Binary Indexed Tree を用いた 変化点の個数に関する二分探索を行う解法も存在します。 -->

## F: Absolute Minima

Let's consider the case where we have $N$ functions given by $f(x) = \sum_{i=1}^N (|x - a_i| + b_i)$. First, we can decompose $f(x)$ as $f(x) = \sum_{i=1}^N |x-a_i| + \sum_{i=1}^N b_i$, and since the term $\sum_{i=1}^N b_i$ is a constant, it doesn't affect the minimum value. Therefore, we only need to consider finding the minimum value of $\sum_{i=1}^N |x- a_i|$, and then adding $\sum_{i=1}^N b_i$ to that minimum value.

For simplicity, let's assume that $\{a_i\}$ is sorted in ascending order, and we define $a_0 = -\infty$ and $a_{N+1} = \infty$.

How can we find the minimum value of $\sum_{i=1}^N |x - a_i|$? Each absolute value function $|x - a_i|$ is a linear function with slope $-1$ for $x < a_i$ and slope $1$ for $x > a_i$. When we add multiple linear functions together, the result remains a linear function. Therefore, within each interval $[a_i, a_{i+1}]$, $f(x)$ can be considered a linear function.

Furthermore, considering that as $x$ decreases, the number of absolute value functions with a slope of $-1$ increases, and as $x$ increases, the number of absolute value functions with a slope of $1$ increases, the slope of the linear functions within each interval $[a_i, a_{i+1}]$ monotonically increases. Therefore, $f(x)$ is convex, and we need to find the intervals where the slope is zero to determine the minimum value.

How can we find the intervals where the slope is zero? Notice that the change point of the slope in the absolute value function $|x - a_i|$ is at $x = a_i$, and the slope increases by $2$ when crossing $x = a_i$. This property holds true even when adding multiple absolute value functions together. Therefore, in function $f(x)$, the slope increases by $2$ each time it crosses $x = a_i$ (except when there are multiple occurrences of the same absolute value function, i.e., when $a_i = a_j$ for some $i$ and $j$, in which case the increase is proportional to the number of occurrences).

In the interval $[a_0 = -\infty, a_1]$, the slope of $f(x)$ is $-N$. Roughly speaking, we can expect that there will be approximately $\frac{N}{2}$ change points where the slope becomes zero. Therefore, the point that lies exactly in the middle (or between two points if $N$ is even) among all the change points in ascending order will be the point where $f(x)$ has a slope of zero and reaches its minimum value.

To implement this calculation, we can use two data structures (referred to as sets): one to store the change points on the left side and the other to store those on the right side. When a query $(a_i, b_i)$ is received, we insert the value $a_i$ twice into the sets to maintain the condition mentioned earlier. 

Now that we have found the point that gives the minimum value, we can determine the specific minimum value:
- If the newly inserted point is within the originally identified interval, the minimum value is $0$.
- If the point is outside the interval, the minimum value is the distance to the nearest endpoint of the interval.

By using only a constant number of set operations for both updates and queries, we can solve the problem in $O(Q \log Q)$ time. Additionally, there are other solutions based on convexity, such as ternary search on the function value itself or binary search on the number of change points using a Binary Indexed Tree.

[Link 1](https://codeforces.com/blog/entry/67227?#comment-513489)
