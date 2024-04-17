#include <bits/stdc++.h>
using namespace std;

using ll = int64_t;
const ll MIN = -(1e12 + 5);

map<ll, ll> seen, mp, cnt;

ll solve(int n, ll k, vector<ll> &A){
    if (seen[k]) return mp[k];

    if (k == 0){
        ll res = accumulate(A.begin(), A.end(), 0ll);
        seen[k] = 1;
        mp[k] = res;
        return res;
    }
    ll g = 1;
    while (2 * g <= k) g *= 2;

    ll res = solve(n, g-1, A);
    res = max(res, solve(n, k-g, A) + g * (n-2*cnt[g]));
    seen[k] = 1;
    mp[k] = res;

    return res;
}

int main(){
    int n; ll k;
    cin >> n >> k;
    vector<ll> A(n);
    for (int i = 0; i < n; i++){
        cin >> A[i];
        ll g = 1;
        for (int d = 0; d < 41; d++){
            if (g & A[i]) cnt[g]++;
            g = g * 2;
        }
    }    
    cout << solve(n, k, A) << "\n";
    return 0;
}

