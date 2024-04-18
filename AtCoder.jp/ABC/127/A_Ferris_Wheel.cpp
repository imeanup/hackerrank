#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b; cin >> a >> b;
    if (a < 6) cout << 0 << "\n";
    else if (a < 13) cout << b/2 << "\n";
    else cout << b << "\n";
    return 0;
}
