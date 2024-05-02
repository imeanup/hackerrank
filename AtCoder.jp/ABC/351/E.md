# E - Jump Distance Sum

<!-- 点を原点を中心に $45$ 度回転し、 $\sqrt{2}$ 倍に拡大することを考えます。このとき、元々 $(X, Y)$ にあった点は $(X+Y, X-Y)$ に移動します。

ここで、移動後の各点 $P_i$ の座標を $(x_i, y_i)$ と書くことにします。 このとき、$x_i = X_i + Y_i, y_i = X_i - Y_i$ が成り立ちます。

次に、$\text{dist}(A, B)$ の定義がどうなるかについて考えます。
ウサギは元の定義で $(X, Y)$ から $(X+1, Y+1), (X+1, Y-1), (X-1, Y+1), (X-1, Y-1)$ にジャンプできていたため、これは、$(X+Y, X-Y)$ から $(X+Y+2, X-Y), (X+Y, X-Y+2), (X+Y, X-Y-2), (X+Y-2, X-Y)$ に到達するようになります。

$x = X+Y, y = X-Y$ と置き換えると、$(x, y)$ から $(x+2, y), (x, y+2), (x, y-2), (x-2, y)$ へ移動するようになります。

このときの$A$ から $B$ まで移動するのに必要なジャンプの回数の最小値（到達できない場合は $0$）が$\text{dist}(A, B)$ の定義となります。

以下、回転・拡大後の状態において問題を考えます。

すなわち、 $P_i = (x_i, y_i)$ とし、上のような形で $\text{dist}(A, B)$ を定義したときの $\sum_{i=1}^{N-1}\sum_{j = i+1}^{N} \text{dist}(P_i, P_j)$ の値を求めることを考えます。
これは明らかに元の問題の答えと一致します。

$A = (x_1, y_1), B = (x_2, y_2)$ のときの $\text{dist}(A, B)$ についてより具体的に考えます。 $x_1 \not\equiv x_2 (\mod 2)$ または $y_1 \not\equiv y_2 (\mod 2)$ のとき、ウサギは $A$ から $B$ へ移動できないため $\text{dist}(A, B) = 0$ となります。そうでないとき、これはマンハッタン距離のちょうど半分となるため、$\text{dist}(A, B) = \dfrac{1}{2}(|x_1-x_2| + |y_1 - y_2|)$ となります。

任意の $i$ について $x_i = y_i + 2Y_i \equiv y_i (\mod 2)$ であることに注意すると、$N$ 個の点は $x_i, y_i$ がともに偶数であるグループとともに奇数であるグループに分けることができ、相異なるグループに属する $2$ つの点 $A, B$ については $\text{dist}(A, B) = 0$ となり、同じグループに属する相異なる $2$ つの点については $\text{dist}(A, B) = \frac{1}{2}(|x_1-x_2| + |y_1-y_2|)$ となります。

$x_i, y_i$ がともに 偶数であるような点の集合を $E = \{E_1, E_2, \cdots, E_{|E|}\}$ とすると、$\sum_{i=1}^{|E|-1} \sum_{j = i+1}^{|E|} \text{dist}(P_{E_i}, P_{E_j}) = \dfrac{1}{2} \sum_{i=1}^{|E|-1} \sum_{j = i+1}^{|E|} |X_{E_j} - X_{E_i}| + \dfrac{1}{2} \sum_{i=1}^{|E|-1} \sum_{j = i+1}^{|E|} |y_{E_j} - y_{E_i}|$ となります。

$\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x_{E_j} - x_{E_i}|$ は、$(x_{E_1}, x_{E_2}, \cdots, x_{E_{|E|}})$ を昇順にソートした列を $(x'_{E_1}, x'_{E_2}, \cdots, x'_{E_{|E|}})$ として、

$\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x_{E_j} - x_{E_i}| = \sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x'_j - x'_i| = \sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} (x'_j - x'_i) = \sum_{i=1}^{|E|} (|E| + 1 - 2i)$ として求めることができます。

同様に $y$ 座標についても計算することで、$\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} \text{dist}(P_{E_i},P_{E_j})$ を求めることができ、さらに $x_i, y_i$ がともに 奇数であるような点の集合についても同様のものを計算して足し合わせることで最終的な答えを得ることができます。

計算量は $2$ つのグループの $x, y$ 座標をそれぞれソートするため $O(N\log N)$ の計算量がかかり、その後の計算は $O(N)$ でできるため、全体で $O(N\log N)$ で答えを求めることができ、十分に高速です。よって、この問題を解くことができました。

c++ による実装例: -->


Let's consider rotating a point about the origin by $45$ degrees and scaling it by a factor of $\sqrt{2} \ ^*$. In this case, a point originally at $(X, Y)$ will move to $(X+Y, X-Y)$.

Let's denote the coordinates of each moved point $P_i$ as $(x_i, y_i)$. Then, we have $x_i = X_i + Y_i$ and $y_i = X_i - Y_i$.

Next, let's consider what the definition of $\text{dist}(A, B)$ becomes. Since the rabbit could jump from $(X, Y)$ to $(X+1, Y+1), (X+1, Y-1), (X-1, Y+1), (X-1, Y-1)$ in the original definition, it will now be able to reach $(X+Y+2, X-Y), (X+Y, X-Y+2), (X+Y, X-Y-2), (X+Y-2, X-Y)$ from $(X+Y, X-Y)$.

Replacing $x = X+Y$ and $y = X-Y$, this becomes moving from $(x, y)$ to $(x+2, y), (x, y+2), (x, y-2), (x-2, y)$.

In this case, the minimum number of jumps required to move from $A$ to $B$ (or $0$ if unreachable) becomes the definition of $\text{dist}(A, B)$.

Below, we consider the problem in the context of the rotated and enlarged state.

Let $ P_i = (x_i, y_i) $, and consider finding the value of $ \sum_{i=1}^{N-1}\sum_{j = i+1}^{N} \text{dist}(P_i, P_j) $ when defined as above. This clearly matches the answer to the original problem.

For $ A = (x_1, y_1) $ and $ B = (x_2, y_2) $, let's consider $ \text{dist}(A, B) $ more specifically. When $ x_1 \not\equiv x_2 (\mod 2) $ or $ y_1 \not\equiv y_2 (\mod 2) $, the rabbit cannot move from $ A $ to $ B $, so $ \text{dist}(A, B) = 0 $. Otherwise, it is exactly half the Manhattan distance, so $ \text{dist}(A, B) = \frac{1}{2}(|x_1-x_2| + |y_1 - y_2|) $.

Note that for any $ i $, $ x_i = y_i + 2Y_i $ implies $ x_i \equiv y_i (\mod 2) $. Therefore, the $ N $ points can be divided into groups where both $ x_i $ and $ y_i $ are even, and those where they are both odd. For any two points $ A, B $ belonging to different groups, $ \text{dist}(A, B) = 0 $, and for distinct points belonging to the same group, $ \text{dist}(A, B) = \frac{1}{2}(|x_1-x_2| + |y_1-y_2|) $.

Let $ E = \{E_1, E_2, \cdots, E_{|E|}\} $ be the set of points where both $ x_i $ and $ y_i $ are **even**. Then, 

$$
\sum_{i=1}^{|E|-1} \sum_{j = i+1}^{|E|} \text{dist}(P_{E_i}, P_{E_j}) = \frac{1}{2} \sum_{i=1}^{|E|-1} \sum_{j = i+1}^{|E|} |x_{E_j} - x_{E_i}| + \frac{1}{2} \sum_{i=1}^{|E|-1} \sum_{j = i+1}^{|E|} |y_{E_j} - y_{E_i}|
$$

The expression $\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x_{E_j} - x_{E_i}| $ can be obtained by sorting the sequence $(x_{E_1}, x_{E_2}, \cdots, x_{E_{|E|}}) $ in ascending order to obtain $(x'_{E_1}, x'_{E_2}, \cdots, x'_{E_{|E|}}) $, and then computing:

$$
\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x_{E_j} - x_{E_i}| = \sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x'_j - x'_i| = \sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} (x'_j - x'_i) = \sum_{i=1}^{|E|} (2i-1-|E|)x'_i
$$

<details><summary><b> Why?</b> </summary>

The expression $$\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x_{E_j} - x_{E_i}|$$ is the sum of absolute differences between all pairs of elements in the set E. This is equivalent to the sum of distances between all pairs of points in a one-dimensional space.

To simplify this expression, we can sort the sequence $(x_{E_1}, x_{E_2}, \cdots, x_{E_{|E|}})$ in ascending order to obtain $(x'_{E_1}, x'_{E_2}, \cdots, x'_{E_{|E|}})$.

Now, consider the sorted sequence. The absolute difference between each element and the elements that come after it in the sequence can be represented as a sum of the form $(x'_j - x'_i)$ for all $j>i$.

This sum can be rewritten as a sum over all elements in the sequence, where each element is multiplied by the difference between the number of elements that come after it and the number of elements that come before it. This is represented as $(2i-1-|E|)x'_i$.

Here's why:
- For each element $x'_i$, there are $i-1$ elements before it and $|E|-i$ elements after it in the sorted sequence.
- When calculating the sum of absolute differences, $x'_i$ is subtracted $(i-1)$ times (for each element before it) and added $|E|-i$ times (for each element after it).
- Therefore, the net contribution of $x'_i$ to the sum is $(2i-1-|E|)x'_i$.

So, the expression $$\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} |x_{E_j} - x_{E_i}|$$ simplifies to $$\sum_{i=1}^{|E|} (2i-1-|E|)x'_i$$.

</details><br>

Similarly, by computing for the **$y $-coordinates** as well, we can obtain $\sum_{i=1}^{|E|-1} \sum_{j=i+1}^{|E|} \text{dist}(P_{E_i},P_{E_j}) $. Adding the same computation for the set of points where both $x_i $ and $y_i $ are **odd**, we can get the final answer.

The time complexity involves sorting the $x $ and $y $ coordinates of the two groups, which requires $O(N\log N)$ operations. The subsequent calculations can be done in $O(N)$ time, resulting in an overall time complexity of $O(N\log N)$. Therefore, we can solve this problem efficiently. 

Example implementation in C++:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(void){
	int n,sz;
	long long x,y,ans=0;
	vector<long long>a[4];
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>x>>y;
		if((x+y)%2==0){
			a[0].push_back(x+y);
			a[1].push_back(x-y);
		}
		else{
			a[2].push_back(x+y);
			a[3].push_back(x-y);
		}
	}
	for(int i=0;i<4;i++){
		sort(a[i].begin(),a[i].end());
		sz=a[i].size();
		for(int j=0;j<sz;j++)ans+=a[i][j]*(2*j+1-sz);
	}
	cout<<(ans/2)<<endl;
	return 0;
}

```

$^*$ Consider a right angled triangle with height and base $1$, then the hypotenus is $\sqrt{2}$.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < (x); ++i)

ll f(vector<int> x){
    int n = x.size();
    sort(x.begin(), x.end());
    ll res = 0;
    rep(i, n){
        ll nc = +i - (n - i - 1);
        res += nc * x[i];
    }
    return res/2;
}

int main(){
    int N; cin >> N;
    vector<vector<int>>xs(2), ys(2);
    rep(i, N){
        int X, Y; cin >> X >> Y;
        int x = X + Y, y = X - Y;
        xs[x%2].push_back(x);
        ys[x%2].push_back(y);
    }

    ll ans = 0;
    rep(i, 2){
        ans += f(xs[i]) + f(ys[i]);
    }
    cout << ans << endl;
    return 0;
}
```


---

