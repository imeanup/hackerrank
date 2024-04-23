#include <bits/stdc++.h>
using namespace std;

using ll = int64_t;

struct union_find {
    vector<int> parent;
    vector<int> size;
    int components = 0;

    union_find(int n = -1) {
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

int main(){
    int N, M; cin >> N >> M;
    union_find uf(N);
    for (int i = 0; i < M; i++){
        int a, b; cin >> a >> b;
        a--, b--;
        uf.unite(a, b);
    }
    ll res = -M;
    for (int i = 0; i < N; i++){
        if (uf.find(i) == i){
            ll n = uf.size[i];
            res += n * (n-1)/2;
        }
    }
    cout << (res) << "\n";
    return 0;
}
