#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}

void run_case();

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tests; cin >> tests;
    while (tests-- > 0){
        run_case();
    }
    return 0;
}

void run_case(){
    int n, k;
    cin >> n >> k;
    vector<vector<P>> g(n);
    rep(i, n-1) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        g[u].emplace_back(v, 2*i);
        g[v].emplace_back(u, 2*i+1);
    }

    vector dp(2*(n-1), vector<int>(k, -1));
    vector cnt(n, vector<int>(k, 0));
    vector<int> ans(n, -1);
    deque<tuple<int, int, int>> dq;

    dq.emplace_back(0, 0, -1);
    
    while (!dq.empty()) {
        auto [d, v, e] = dq.back();
        dq.pop_back();
        int r = d%k;
        if(r == 0 && ans[v] == -1) ans[v] = d/k;
        
        if(cnt[v][r] == 2) continue;
        cnt[v][r]++;
        for(auto [u, e2] : g[v]){
            if(e2 == (e^1) && r != 0) continue;
            int nd = d+1;
            int nr = nd%k;
            if(dp[e2][nr] == -1) {
                dp[e2][nr] = d+1;
                dq.emplace_front(nd, u, e2);
            }
        }
    }
    for(int i = 1; i < n; i++) {
        cout << ans[i] << " ";
    }
    cout << "\n";
}
