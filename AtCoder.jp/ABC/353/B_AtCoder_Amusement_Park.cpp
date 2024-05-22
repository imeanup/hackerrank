#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, K; cin >> N >> K;
    int empty_seat = K, cnt = 1;
    for (int i = 0; i < N; i++){
        int a; cin >> a;
        if (empty_seat < a){
            empty_seat = K;
            cnt++;
        }
        empty_seat -= a;
    }
    cout << cnt << endl;
    return 0;
}