template <typename T>
struct Line {
    mutable T k, m, p;
    bool operator<(const Line& other) const { return k < other.k; }
    bool operator<(T x) const { return p < x; }
};
template <typename T = long double>
struct DLC : multiset<Line<T>, less<>> {
    static const T inf = 0x7fffffffffffffffLL;
    
    T div(T a, T b) {
        return a/b - ((a^b) < 0 && a%b);
    }

    bool isect(typename multiset<Line<T>, less<>>::iterator x, 
               typename multiset<Line<T>, less<>>::iterator y) {
        if (y == this->end()) { x->p = inf; return false; }
        if (x->k == y->k) x->p = x->m > y->m ? inf : -inf;
        else x->p = div(y->m - x->m, x->k - y->k);
        return x->p >= y->p;
    }
    void add(T k, T m) {
        auto z = this->insert({k, m, 0}), y = z++, x = y;
        while(isect(y, z)) z = this->erase(z);
        if (x != this->begin() && isect(--x, y)) isect(x, y = this->erase(y));
        while ((y = x) != this->begin() && (--x)->p >= y->p) isect(x, this->erase(y));
    }
    T operator()(T x) {
        if (this->empty()) return 0;
        auto l = *this->lower_bound(x);
        return l.k * x + l.m;
    }
};
/* 
DLC<long long> lc; // Creates a container for long long
lc.add(slope, intercept);
long long result = lc(query_x);
*/
