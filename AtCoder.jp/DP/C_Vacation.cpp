#include <bits/stdc++.h>
using namespace std;
using ll = int64_t;
template<class T> inline bool chmax(T &a, T b){if (a < b){ a = b; return true; } return false; }
const int MAX = 100005;
int N;
ll H[MAX][3];
ll dp[MAX][3];

int main(){
    cin >> N;
    for (int i = 1; i <= N; i++) for (int j = 0; j < 3; j++) cin >> H[i][j];
    for (int i = 1; i <= N; i++){
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + H[i][0];
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + H[i][1];
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + H[i][2];
    }

    ll res = 0;
    for (int j = 0; j < 3; j++){
        res = max(res, max(dp[N][0], max(dp[N][1], dp[N][2])));
    }
    cout << res << "\n";
    return 0;
}