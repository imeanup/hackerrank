#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < (n); ++i)
using ll = long long;

int main(){
    int n, q; cin >> n >> q;
    int x = 0;
    const int mod = 998244353;
    vector<int> par(n, -1);
    vector<vector<int>> to(n);
    vector<int> root(n), sz(n, 1);
    rep (i, n) root[i] = i;

    rep (qi, q) {
        ll A, B, C; cin >> A >> B >> C;
        int type = (A * (x+1)%mod)%2 + 1;
        int a = (B * (x+1)%mod)%n;
        int b = (C * (x+1)%mod)%n;

        if (type == 1){
            if (sz[root[a]] < sz[root[b]]) swap(a, b);
            sz[root[a]] += sz[root[b]];
            auto dfs = [&] (auto dfs, int v, int p = -1) -> void {
                par[v] = p;
                root[v] = root[a];
                for (int u : to[v]) if (u != p){
                        dfs(dfs, u, v);
                    }
            };
            dfs(dfs, b);
            par[b] = a;
            to[a].push_back(b);
            to[b].push_back(a);
        }
        else {
            int ans = -1;
            int pa = par[a], pb = par[b];
            if (pa == pb && pa != -1) ans = pa;
            else if (pa != -1 && par[pa] == b) ans = pa;
            else if (pb != -1 && par[pb] == a) ans = pb;
            ans++;
            cout << ans << "\n";
            x = ans;
        }
    }
    return 0;
}