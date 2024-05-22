#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
#define rep(i, x) for(int i=0;i<(x);i++)
#define repi(i, x, y) for(int i=(x); i<(y); i++)
const ll MAX = 1e8;


int main(){
    int N; cin >> N;
    vector<ll> A(N);
    rep(i, N) cin >> A[i];
    sort(A.begin(), A.end());
    ll f = 0;
    int r = N - 1;
    rep(i, N) f += A[i] * 1ll * (N-1);
    rep(i, N){
        while (r >= 0 && A[i] + A[r] >= MAX){
            r--;
        }
        f -= ll(N - max(r, i)-1) * MAX;
    }
    cout << f << endl;
    return 0;
}