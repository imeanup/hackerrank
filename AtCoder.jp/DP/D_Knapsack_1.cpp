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
const ll INF = INT_MAX;
/* 
ll knapSack(int W, vector<ll> wt, vector<ll> val, int n) {
    ll dp[W+1];
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i < n + 1; i++) {
        for (int w = W; w >= 0; w--) {
            if (wt[i-1] <= w){
                dp[w] = max(
                    dp[w],
                    dp[w-wt[i-1]] + val[i-1]
                );
            }
        }
    }
    return dp[W];
} */

int main() {
    int N, W; cin >> N >> W;
    vector<ll> wt(N+1);
    vector<ll> val(N+1);
    vector<vector<ll>> dp(N+1, vector<ll>(W+1, -1));
    for (int i = 0; i < N; i++){
        cin >> wt[i] >> val[i];
    }
    function<ll(int, int)> knapSack = [&](int W, int i) -> ll{
        if (i == 0 || W == 0) return 0;
        if (dp[i][W] != -1) return dp[i][W];
        if (wt[i-1] > W) dp[i][W] = knapSack(W, i-1);
        else {
            dp[i][W] = max(val[i-1] + knapSack(W-wt[i-1], i-1),
                        knapSack(W, i-1));
        }
        return dp[i][W];
    };
    cout << knapSack(W, N) << "\n";
    return 0;
}
