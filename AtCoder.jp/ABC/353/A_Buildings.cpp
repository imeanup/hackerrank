#include <bits/stdc++.h>
using namespace std;

#define rep(i, x) for(int i=0;i<x;i++)

int main(){
    int n; cin >> n;
    vector<int> H(n);
    rep(i, n) cin >> H[i];
    for (int i=1; i<n;i++){
        if (H[i] > H[0]) {
            cout << i + 1 << "\n";
            return 0;
        }
    }
    cout << -1 << "\n";
    return 0;
}