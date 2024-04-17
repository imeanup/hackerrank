#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, k; cin >> n >> k;

    double res = 0;
    for (int i = 1; i <= n; i++){
        double temp = 1.0 / n;
        int now = i;
        while (now < k){
            now *= 2;
            temp /= 2;
        }
        res += temp;
    }
    cout << setprecision(12) << res << "\n";
    return 0;
}