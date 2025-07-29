#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}
const int INF = 1001001001;

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
    vector<P> edges; 
    vector<vector<P>> g(n); // to, edge_id 

    rep(i, n-1) {
        int a, b;
        cin >> a >> b;
        a--, b--;
        edges.emplace_back(a, b);
        g[a].emplace_back(b, i);
        g[b].emplace_back(a, n-1+i);
    }
    
    vector dist((n-1)*2, vector<int>(k, INF));
    vector cnt(n, vector<int>(k));
    queue<P> q;
    auto push = [&](int ei, int d) {
        int w = d%k;
        if (dist[ei][w] != INF) return;
        dist[ei][w] = d;
        q.emplace(ei, d);
    };
    for(auto [to, ei] : g[0]) push(ei, 1);
    while (q.size()) {
        auto [ei, d] = q.front();
        q.pop();
        int v;
        {
            auto [a, b] = edges[ei%(n-1)];
            if (ei < n-1) v = b; else v = a;
        }
        if((++cnt[v][d%k]) <= 2) {
            for(auto [to, ej] : g[v]) {
                if(d%k != 0 && ei%(n-1) == ej%(n-1)) continue;
                push(ej, d+1);
            }
        }
    }

    vector<int> ans(n, INF);
    rep(i, (n-1)*2) {
        auto [a, b] = edges[i%(n-1)];
        if(i >= n-1) swap(a, b);
        ans[b] = min(ans[b], dist[i][0]);
    }

    for(int i = 1; i < n; i++) {
        if(ans[i] == INF) ans[i] = -1;
        else ans[i] /= k;
        cout << ans[i] << " ";
    }
    cout << "\n";
}
