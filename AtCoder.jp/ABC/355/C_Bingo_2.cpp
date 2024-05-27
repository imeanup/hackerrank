#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i=0;i<(n);i++)
#define repi(i, x, n) for(int i=x;i<(n);i++)
#define all(x) x.begin(), x.end()

int main(){
    int n, t; cin >> n >> t;

    vector<int> row(n, 0), col(n, 0);
    int diag1 = 0, diag2 = 0;
    
    rep(i, t){
        int a; cin >> a;
        int r = (a - 1) / n;
        int c = (a - 1) % n;

        row[r]++;
        col[c]++;

        if (r == c) diag1++;
        if (r+c == n-1) diag2++;

        if (row[r] == n || col[c] == n || diag1 == n || diag2 == n){
            cout << i+1 << endl;
            return 0;
        }
    }
    cout << -1 << "\n";
    return 0;
}