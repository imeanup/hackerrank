#include <bits/stdc++.h>
using namespace std;
string S;
vector<int> match;

char flip(char c){
    if ('A' <= c && c <= 'Z'){
        return (c - 'A' + 'a');
    }
    return (c - 'a' + 'A');
}

void f(int l, int r, int d){
    if (d == 0){
        while (l <= r){
            if (S[l] == '(') {
                f(l+1, match[l] - 1, 1);
                l = match[l];
            }
            else {
                cout << S[l];
            }
            l++;
        }
    }
    else {
        while (l <= r){
            if (S[r] == ')'){
                f(match[r] + 1, r - 1, 0);
                r = match[r];
            }
            else {
                cout << S[r];
            }
            r--;
        }
    }
}

int main(){
    cin >> S;
    int n = S.size();
    match.resize(n);

    for (auto &ch : match) ch -= 1;

    int depth = 0;
    stack<int> st;
    for (int i = 0; i < n; i++){
        if (S[i] == '('){
            st.push(i);
            depth++;
        }
        else if (S[i] == ')') {
            match[i] = st.top();
            match[st.top()] = i;
            st.pop(); 
            depth--;
        }
        else if (depth % 2){
            S[i] = flip(S[i]);
        }
    }   

    f(0, n-1, 0);

    return 0;
}