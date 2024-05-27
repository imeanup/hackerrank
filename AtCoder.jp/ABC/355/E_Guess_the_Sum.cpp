#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;

#define rep(i, n) for(int i=0;i<(n);i++)
const int INF = 1001001001; 

int main(){
    int n, l, r; cin >> n >> l >> r;
    int M = 1 << n;
    r++;
    vector<int> dist(M+1, INF), pre(M+1, -1);
    queue<int> q;
    q.push(l), dist[l] = 0;
    while (!q.empty()){
        int v = q.front();
        q.pop();

        auto push = [&](int to) {
            if (to < 0 || to > M) return;
            if (dist[to] != INF) return;
            dist[to] = dist[v] + 1;
            pre[to] = v;
            q.push(to);
        };

        rep(i, n+1) {
            push(v - (1 << i));
            push(v + (1 << i));
            if(v >> i & 1) break;
        }
    }

    int ans = 0;
    auto query = [&](int s, int t){
        int sign = 1;
        if (s > t) swap(s, t), sign = -1;
        {
            int i = 0, j = s, w = t-s;
            while (w % 2 == 0){
                j >>= 1, w >>= 1, i++;
            }
            cout << "? " << i << " " << j << endl;
        }
        int x; cin >> x;
        ans = (ans + sign * x + 100) % 100;
    };
    while (r != l){
        query(pre[r], r);
        r = pre[r];
    }
    cout << "! " << ans << "\n";
    return 0;
}