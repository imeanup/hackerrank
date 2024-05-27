#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i=0;i<(n);i++)
#define repi(i, x, n) for(int i=x;i<(n);i++)
#define all(x) x.begin(), x.end()

int main(){
    int n, m; cin >> n >> m;
    vector<int> a(n), b(m), c(n+m);

    rep(i, n) cin >> a[i];
    rep(i, m) cin >> b[i];
    merge(all(a), all(b), c.begin());
    sort(all(c));
    unordered_set<int> setA(all(a));

    repi(i, 1, n+m){
        if (setA.count(c[i]) && setA.count(c[i-1])){
            cout << "Yes" << "\n";
            return 0;
        }
    }   
    cout << "No" << "\n";
    return 0;
}