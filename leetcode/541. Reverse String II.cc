class Solution {
public:
    string reverseStr(string s, int k) {
        int n = s.length();
        char a[n + 1];
        strcpy(a, s.c_str());

        int len = s.size();
        for (int i = 0; i < len; i += 2*k){
            int m = i, n = min(i + k - 1, len - 1);
            while (m < n){
                char tmp = a[m];
                a[m++] = a[n];
                a[n--] = tmp;
            }
        }
        cout << a << endl;
        return string(a);
    }
};
