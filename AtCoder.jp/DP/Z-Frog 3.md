# [Z - Frog 3](https://atcoder.jp/contests/dp/tasks/dp_z)

#### Analysis and DP formation

**Goal**: Find the minimum cost to travel from stone $1$ to $N$. The cost to jump from stone $j$ to stone $i$ is $(h_i-h_j)^2+C$.

DP Relation: Let $dp[i]$ be the minimum cost to reach stone $i$.


$$
dp[i] = \min_{1 \le j < i} \{ dp[j] + (h_i - h_j)^2 + C \}
$$


$$
dp[i] = \min_{1 \le j < i} \{ dp[j] + h_i^2 - 2h_ih_j + h_j^2 + C \}
$$

We can separate the terms that depends on i (current), j(previous), and both:

$$
dp[i] = h_i^2 + C + \min_{1 \le j < i} \{ \underbrace{-2h_j}_{\text{slope } m_j} \cdot \underbrace{h_i}_{\text{input } x} + \underbrace{(dp[j] + h_j^2)}_{\text{intercept } c_j} \}
$$

This takes the form of a line equation $y = mx+c$:

1. **Slope** $(m_j)$: $-2h_j$
2. **Y-intercept** $(c_j)$ : $dp[j] + h_j^2$
3. **Query variable** $(x)$: $h_i$

To find $dp[i]$, we need to fing the line from the previous stones $j$ that gives the **minimum** $y$ value for the current $x = h_i$.

#### Why Convex Hull Trick?

Since we are taking the mimimum of several linear functions $(y = mx+c)$, the "lower boundary" of these lines forms a convex shape.

* The problem guarantees $h_1 \lt h_2\lt \cdots \lt h_N$.
* Monotonic Slopes: Since $h_j$ is increasing, the slopes $(m_j = -2h_j)$ are strictly decreasing.
* Monotonic Queries: The query points $(x = h_i)$ are strictly increasing.

Because both slopes and queries are monotonic, we can use the Deque (Linear Time) implementation of CHT.

<details style="border: 1px solid black; padding: 10px;"><summary>C++</summary>
  
```cpp
template<typename T = long long>
struct CHT {
    struct Line {
        T a, b;
        Line(T a = 0, T b = 0): a(a), b(b) {}
        T operator()(T x) const { return a*x + b; }
    };
    deque<Line> hull;
    void add(T a, T b) {
        Line nl(a,b);
        while (hull.size() >= 2) {
            const Line& x = hull[hull.size()-2];
            const Line& y = hull.back();
            if ((nl.a - y.a) * (x.b - y.b) < (y.a - x.a) * (y.b - nl.b)) break;
            hull.pop_back();
        }
        hull.push_back(nl);
    }
    T operator()(ll x) { // decreasing order 
        T res = hull[0](x);
        while (hull.size() >= 2) {
            T cur = hull[1](x);
            if (cur > res) break; // both (not similar abc289_g, x is increasing order)
            res = cur;
            hull.pop_front();
        }
        return res;
    }
};
using ll = long long;
signed main(){
    int n; 
    ll c;
    cin >> n >> c;
    vector<ll> h(n);
    for(ll &x:h) cin >> x;
    /*
    vector<ll> dp(n); 
    dp[0] = 0;
    */
    ll ans = 0;
    CHT<ll> cht;
    cht.add(-2*h[0], ans + h[0]*h[0]);
    // cht.add(-2*h[0], dp[0] + h[0]*h[0]);

    for(int i = 1; i < n; i++) {
        ans = cht(h[i]) + c + h[i]*h[i];
        cht.add(-2*h[i], ans + h[i]*h[i]);
        // dp[i] = cht(h[i]) + c + h[i]*h[i];
        // cht.add(-2*h[i], dp[i] + h[i]*h[i]);
    }
    // cout << dp[n-1] << endl;
    cout << ans << endl;
}
```

</details><br>
