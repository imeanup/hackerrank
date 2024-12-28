#include<bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){if (a < b) {a = b;return 1;}return 0;}
template<class T> inline bool chmin(T &a, T b){if (a > b) {a = b;return 1;}return 0;}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<tuple<int, int, char>> f;
    rep(i, m){
        int x, y; char c;
        cin >> x >> y >> c;
        f.emplace_back(x, y, c);
    }
    sort(f.begin(), f.end());
    int min_y = 1 << 30;
    bool possible = true;
    for (auto[x, y, c] : f){
        if (c == 'W'){
            chmin(min_y, y);
        }
        else {
            if (y >= min_y)
                possible = false;
        }
    }
    cout <<(possible ? "Yes\n" : "No\n");
    return 0;
}
