#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
const int INF = 1e18 + 5;

map<ll, double> f;

double solve(ll N, int A, ll X, double Y){
    if (N == 0){
        return 0;
    }
    if (f.find(N) != f.end()){
        return f[N];
    }

    double res = INF;
    res = X + solve(N/A, A, X, Y);
    res = min(res, 
        1.2 * Y + 0.2 * (solve(N/2, A, X, Y) + solve(N/3, A, X, Y) + 
        solve(N/4, A, X, Y) + solve(N/5, A, X, Y) + solve(N/6, A, X, Y))
    );
    return f[N] = res;
}

int main(){
    ll N, X; double Y;
    int A;
    cin >> N >> A >> X >> Y;
    cout << fixed << setprecision(12) << solve(N, A, X, Y) << "\n";
    return 0;
}