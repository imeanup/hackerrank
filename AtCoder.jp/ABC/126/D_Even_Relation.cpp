#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int, int>>> g;
vector<int> color;

void dfs(int v, int p, int c){
    color[v] = c;
    for (auto [u, w] : g[v]){
        if (u == p) continue;
        if (w & 1) dfs(u, v, c ^ 1);
        else dfs(u, v, c);
    }
}

int main(){
    int n; cin >> n;
    g.resize(n);
    
    for (int i = 0; i < n-1; i++){
        int u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }
    color.resize(n);
    dfs(0, -1, 0);
    for (int x : color) cout << x << "\n";
    return 0;
}