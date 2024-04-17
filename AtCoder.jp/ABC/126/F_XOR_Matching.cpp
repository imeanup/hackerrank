#include <bits/stdc++.h>
using namespace std;

int main(){
    int m, k; cin >> m >> k;

    if (m == 0) {
        if (k == 0){
            cout << "0 0" << "\n";
            return 0;
        }
        else {
            cout << -1 << "\n";
            return 0;
        }
    }
    if (m == 1) {
        if (k == 0){
            cout << "0 0 1 1" << "\n";
            return 0;
        }
        else {
            cout << -1 << "\n";
            return 0;
        }
    }
    if (k >= (1 << m)) {
        cout << -1 << "\n";
        return 0;
    }
    if (k == 0) {
        for (int i = 0; i < (1 << m); i++){
            cout << i << " ";
        }

        for (int i = (1 << m)-1; i >= 0; i--){
            cout << i << " ";
        }
        cout << "\n";
        return 0;
    }
    vector<pair<int, int>> v;
    for (int i = 0; i < (1 << m); i++){
        v.emplace_back(min(i, i^k), max(i, i^k));
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    for (int i = 0; i < v.size(); i += 2){
        cout << v[i].first << " " << v[i].second << " "
        << v[i+1].first << " " << v[i+1].second << " "
        << v[i].second << " " << v[i].first << " "
        << v[i+1].second << " " << v[i+1].first << " ";
    }
    cout << "\n";

    return 0;
}