#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()

struct DSU {
    vector<int> parent;
    vector<int> size;
    int components = 0;

    DSU(int n = -1) {
        if (n >= 0)
            init(n);
    }

    void init(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        size.assign(n, 1);
        components = n;
    }

    int find(int x) {
        return x == parent[x] ? x : parent[x] = find(parent[x]);
    }

    bool unite(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y)
            return false;

        if (size[x] < size[y])
            swap(x, y);

        size[x] += size[y];
        parent[y] = x;
        components--;
        return true;
    }
};

int main() {
    int n, q; cin >> n >> q;
    int m = 10;
    vector<DSU> uf(m+1, DSU(n));
    vector<int> num(m+1);
    rep(qi, n-1+q){
        int a, b, c; cin >> a >> b >> c;
        a--, b--;
        for(int i = c; i <= m; i++){
            if (uf[i].find(a) == uf[i].find(b)) continue;
            num[i]++;
            uf[i].unite(a, b);
        }

        if (qi < n-1) continue;
        int ans = 0;
        for(int i=1; i<=m;i++){
            ans += i*(num[i]-num[i-1]);
        }
        cout << ans << "\n";
    }
    return 0;
}
