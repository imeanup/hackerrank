#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
template<class T> inline bool chmax(T &a, T b){
    if (a < b) {
        a = b;
        return 1;
    }
    return 0;
}
template<class T> inline bool chmin(T &a, T b){
    if (a > b) {
        a = b;
        return 1;
    }
    return 0;
}
#define rep(i, x) for (int i = 0; i < (x); ++i)
#define repi(i, x, y) for (int i = (x); i < (y); ++i)
#define all(x) x.begin(), x.end()

const ll INF = (1LL << 60);

int N;
ll H[100010], dp[100010];

int main(){
    cin >> N;
    rep (i, N) cin >> H[i];
    rep (i, 100010) dp[i] = INF;
    function<ll(int)> rec = [&] (int i) -> ll {
        if (dp[i] < INF) return dp[i];
        if (i == 0) return 0;
        ll res = INF;
        chmin(res, rec(i-1) + abs(H[i] - H[i-1]));
        if (i > 1) chmin(res, rec(i-2) + abs(H[i] - H[i-2]));
        return dp[i] = res;
    };
    cout << rec(N-1) << "\n";
    return 0;
}