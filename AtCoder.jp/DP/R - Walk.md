# [R - Walk](https://atcoder.jp/contests/dp/tasks/dp_r)

## **Explanation**

### **Problem Recap**

We are given a directed graph with $N$ vertices and an adjacency matrix $A$ where:
- $a_{i,j} = 1$ if there is a directed edge from $i$ to $j$
- $a_{i,j} = 0$ otherwise  
- $a_{i,i} = 0$ for all $i$

We need to count the total number of directed paths of exactly length $K$ in $G$ (counting paths that may traverse the same edge multiple times) modulo $10^9+7$.

### **Key Observation and Approach**

The key observation is that the $(i,j)$-th entry of the matrix $A^K$ (i.e. the $K$-th power of the adjacency matrix) represents the number of different paths of length $K$ from vertex $i$ to vertex $j$. Therefore, if we sum all the entries of $A^K$, we obtain the total number of directed paths of length $K$.

Since $K$ can be as large as $10^{18}$, we cannot multiply the matrix $A$ by itself $K$ times in a naive manner. Instead, we use **matrix exponentiation (binary exponentiation)** to compute $A^K$ in $O(\log K)$ multiplications.

---

## **DP Transition / Recurrence Relation**

We can think of the matrix exponentiation process as a dynamic programming (DP) recurrence. Define:

$$\text{dp}[k][i][j] = \text{number of paths of length } k \text{ from vertex } i \text{ to vertex } j.$$

Then, we have:

1. **Base Case:**
   $$
   \text{dp}[0][i][j] = 
   \begin{cases} 
   1 & \text{if } i = j, \\
   0 & \text{if } i \neq j.
   \end{cases}
   $$

   (This is equivalent to the identity matrix.)

3. **Recurrence:**
   For $k \ge 1$,

   $$\text{dp}[k][i][j] = \sum_{l=1}^{N} \text{dp}[k-1][i][l] \times a_{l,j}.$$
   
   This recurrence is exactly the definition of matrix multiplication, so $\text{dp}[k] = A^k$.

4. **Final Answer:**
   The total number of paths of length $K$ is the sum of all entries in $A^K$, i.e.,

   $$\text{answer} = \sum_{i=1}^{N} \sum_{j=1}^{N} (A^K)_{i,j} \mod (10^9+7).$$

### **Matrix Exponentiation Technique**

To compute $A^K$ efficiently:
- **Even $K$:** $A^K = \left(A^{K/2}\right)^2$
- **Odd $K$:** $A^K = A \times A^{K-1}$

We use binary exponentiation to perform these multiplications in $O(\log K)$ matrix multiplications. Since the matrix is $N \times N$ with $N \le 50$, each multiplication takes $O(N^3)$ time, which is efficient for the given constraints.

---

## **C++ Code**

Below is the complete C++ solution with detailed comments:

```cpp
#include <iostream>
#include <vector>
using namespace std;
 
// Modulo constant
const long long MOD = 1000000007;
 
// Define a type alias for matrices
typedef vector<vector<long long>> matrix;
 
// Function to multiply two matrices A and B modulo MOD
matrix multiplyMatrix(const matrix &A, const matrix &B) {
    int n = A.size();
    matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            if (A[i][k] != 0) { // Optimization: skip zeros
                for (int j = 0; j < n; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
    }
    return C;
}
 
// Function to perform matrix exponentiation: computes A^power modulo MOD
matrix powerMatrix(matrix A, long long power) {
    int n = A.size();
    // Initialize result as the identity matrix
    matrix result(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++){
        result[i][i] = 1;
    }
    // Binary exponentiation
    while(power > 0) {
        if(power & 1)
            result = multiplyMatrix(result, A);
        A = multiplyMatrix(A, A);
        power >>= 1;
    }
    return result;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    long long K;
    cin >> N >> K;
    
    // Read the adjacency matrix of the graph
    matrix A(N, vector<long long>(N, 0));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> A[i][j];
        }
    }
    
    // Compute A^K using matrix exponentiation
    matrix res = powerMatrix(A, K);
    
    // Sum all entries of the resulting matrix
    long long ans = 0;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            ans = (ans + res[i][j]) % MOD;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```

---

## **Summary**

1. **Observation:**  
   The number of paths of length $K$ from vertex $i$ to vertex $j$ is the $(i,j)$-th entry of $A^K$.

2. **DP/Recurrence Transition:**  

   $$\text{dp}[k][i][j] = \sum_{l=1}^{N} \text{dp}[k-1][i][l] \times a_{l,j}$$
   
   with the base case $\text{dp}[0] = I$ (identity matrix).

4. **Approach:**  
   Use binary (matrix) exponentiation to compute $A^K$ efficiently, then sum all the entries to obtain the final answer modulo $10^9+7$.

This method efficiently handles the constraints where $K$ can be as large as $10^{18}$ and $N$ is at most 50.


```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = unsigned long long;
#define rep(i, x) for(int i = 0; i < int(x); i++)
#define all(x) (x).begin(), (x).end()
template<class T> inline bool chmax(T &a, T b){ if(a < b){ a = b; return true; } return false; }
template<class T> inline bool chmin(T &a, T b){ if(a > b){ a = b; return true; } return false; }

// https://github.com/atcoder/live_library/blob/master/mint.cpp
const int mod = 1000000007;
struct mint {
    ll x; // using unsigned long long as defined in the template
    mint(ll x=0):x((x % mod + mod) % mod){}
    mint operator-() const { return mint(-x); }
    mint& operator+=(const mint a) {
        if((x += a.x) >= mod) x -= mod;
        return *this;
    }
    mint& operator-=(const mint a) {
        if((x += mod - a.x) >= mod) x -= mod;
        return *this;
    }
    mint& operator*=(const mint a) { (x *= a.x) %= mod; return *this; }
    mint operator+(const mint a) const { return mint(*this) += a; }
    mint operator-(const mint a) const { return mint(*this) -= a; }
    mint operator*(const mint a) const { return mint(*this) *= a; }
    mint pow(ll t) const {
        if(!t) return 1;
        mint a = pow(t >> 1);
        a *= a;
        if(t & 1) a *= *this;
        return a;
    }
    // for prime mod
    mint inv() const { return pow(mod - 2); }
    mint& operator/=(const mint a) { return *this *= a.inv(); }
    mint operator/(const mint a) const { return mint(*this) /= a; }
};
istream& operator>>(istream& is, mint& a){ return is >> a.x; }
ostream& operator<<(ostream& os, const mint& a){ return os << a.x; }

// Atcoder: live_library/mat.cpp
template<typename T>
struct Matrix {
    int h, w;
    vector<vector<T>> d;
    Matrix() {}
    Matrix(int h, int w, T val = 0) : h(h), w(w), d(h, vector<T>(w, val)) {}
    
    Matrix& unit() {
        assert(h == w);
        for (int i = 0; i < h; i++) 
            d[i][i] = 1;
        return *this;
    }
    const vector<T>& operator[](int i) const { return d[i]; }
    vector<T>& operator[](int i) { return d[i]; }
    
    // Matrix multiplication
    Matrix operator*(const Matrix &a) const {
        assert(w == a.h);
        Matrix r(h, a.w, 0);
        for (int i = 0; i < h; i++)
            for (int k = 0; k < w; k++)
                for (int j = 0; j < a.w; j++)
                    r[i][j] += d[i][k] * a[k][j];
        return r;
    }
    
    // Matrix exponentiation (binary exponentiation)
    Matrix pow(long long t) const {
        assert(h == w);
        if(!t) return Matrix(h, h, 0).unit();
        if(t == 1) return *this;
        Matrix r = pow(t >> 1);
        r = r * r;
        if(t & 1) r = r * (*this);
        return r;
    }
    
    // Determinant (unused for this problem)
    mint det() {
        assert(h == w);
        mint res = 1;
        for (int k = 0; k < h; k++){
            for (int i = k; i < h; i++){
                if(i != k) {
                    swap(d[i], d[k]);
                    res = -res;
                }
            }
            if(d[k][k] == 0) return 0;
            res *= d[k][k];
            mint inv = mint(1) / d[k][k];
            for (int j = 0; j < h; j++)
                d[k][j] *= inv;
            for (int i = k + 1; i < h; i++){
                mint c = d[i][k];
                for (int j = k; j < h; j++)
                    d[i][j] -= d[k][j] * c;
            }
        }
        return res;
    }
};

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    ll k;
    cin >> n >> k;
    
    // Read the adjacency matrix for the graph
    Matrix<mint> A(n, n, mint(0));
    rep(i, n) {
        rep(j, n) {
            int x;
            cin >> x;
            A[i][j] = mint(x);
        }
    }
    
    // Compute A^k using binary (matrix) exponentiation
    Matrix<mint> B = A.pow(k);
    
    // Sum all entries of the matrix B to count all paths of length k
    mint ans = 0;
    rep(i, n) {
        rep(j, n) {
            ans += B[i][j];
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```

### **Explanation and DP Transitions**

1. **Graph Representation & Matrix Exponentiation:**
   - The given graph is represented by an adjacency matrix `A` of size $n \times n$ where $A[i][j] = 1$ indicates a directed edge from vertex $i$ to $j$.
   - The number of directed paths of length $k$ from vertex $i$ to vertex $j$ is given by the $(i,j)$-th entry of the matrix $A^k$.

2. **DP Transition (Matrix Multiplication):**
   - We define a DP state $\text{dp}[k]$ corresponding to the matrix $A^k$.
   - The recurrence (DP transition) is given by:
     $$A^k = A^{k/2} \times A^{k/2} \quad \text{if } k \text{ is even},$$
     $$A^k = A \times A^{k-1} \quad \text{if } k \text{ is odd}.$$
   - This is implemented in the `pow` function of the `Matrix` struct using binary exponentiation.

3. **Final Answer:**
   - After computing $B = A^k$, the answer is the sum of all entries in $B$ (i.e. the total number of directed paths of length $k$ in the graph) modulo $10^9+7$.

This solution efficiently handles the large exponent $k$ (up to $10^{18}$) with $O(\log k)$ matrix multiplications, each taking $O(n^3)$ time, which is acceptable for $n \le 50$.
