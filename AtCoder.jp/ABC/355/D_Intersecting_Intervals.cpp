#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, n) for(int i=0;i<(n);i++)
#define repi(i, x, n) for(int i=x;i<(n);i++)
#define all(x) x.begin(), x.end()

struct T{
    ll l, r;
};

int main(){
    int n; cin >> n;
    vector<T> a(n);
    rep(i, n){
        cin >> a[i].l >> a[i].r;
    }
    sort(all(a), [](const T &a, const T &b){
        return a.l < b.l;
    });

    priority_queue<ll, vector<ll>, greater<ll>> pq;
    
    ll res = 0;

    for (const auto &e : a){
        while (!pq.empty() && pq.top() < e.l) pq.pop();
        res += pq.size();
        pq.push(e.r);
    }
    cout << res << endl;
    return 0;
}

// ====================SECOND APPROACH===============
struct T{
    ll pos;
    ll type;
};

int main(){
    int n; cin >> n;
    vector<T> a;
    rep(i, n){
        ll l, r; cin >> l >> r;
        a.push_back({l, 1});
        a.push_back({r, -1});
    }
    sort(all(a), [](const T &a, const T &b){
        if (a.pos == b.pos){
            return a.type > b.type;
        }
        return a.pos < b.pos;
    });

    ll res = 0, now = 0;

    for (const auto &e : a){
        if (e.type == 1){
            res += now;
            ++now;
        }
        else {
            --now;
        }
    } 
    cout << res << "\n";
    return 0;
}
