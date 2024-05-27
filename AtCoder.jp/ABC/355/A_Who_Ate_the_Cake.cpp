#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b; cin >> a >> b;
    if (a == b){
        cout << -1 << "\n";
        return 0;
    }
    cout << (a^b) << endl;
    return 0;
}