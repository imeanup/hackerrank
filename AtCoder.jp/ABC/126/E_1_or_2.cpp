#include <bits/stdc++.h>
using namespace std;

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
    int n, m; cin >> n >> m;
    union_find uf(n);

    for (int i = 0; i < m; i++){
        int x, y, z; cin >> x >> y >> z;
        x--, y--;
        uf.unite(x, y);
    }
    set<int> s;
    for (int i = 0; i < n; i++){
        s.insert(uf.find(i));
    }
    cout << s.size() << "\n";
    return 0;
}