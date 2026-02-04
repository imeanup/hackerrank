template<typename T, bool MIN_MODE = true> 
struct LiChao {
    using U = typename conditional<is_integral<T>::value, __int128, T>::type;

    struct Line {
        T m, c;
        Line() {
            if constexpr (MIN_MODE) m = 0; c = numeric_limits<T>::max();
            else m = 0; c = numeric_limits<T>::lowest();
        }
        Line(T _m, T _c) : m(_m), c(_c) {}
        T operator()(T x) const { return (T)((U)m*x + c); }
    };

    vector<T> xs;
    vector<Line> st;
    int n;
    
    LiChao() {}
    LiChao(vector<T> _xs) { init(std::move(_xs)); }
    
    void init(vector<T> _xs) {
        xs = std::move(_xs);
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        n = (int)xs.size();
        st.assign(4*n+5, Line());
    }

    bool beats(const Line& a, const Line& b, T x) const {
        if constexpr (MIN_MODE) return a(x) < b(x);
        else return a(x) > b(x);
    }

    void add(T m, T c) { _add(Line(m, c), 1, 0, n-1); }

    void _add(Line nl, int p, int l, int r) {
        int m = (l + r) >> 1;
        bool nmid = beats(nl, st[p], xs[m]);
        if (nmid) swap(st[p], nl);
        if (l == r) return;
        if (beats(nl, st[p], xs[l])) _add(nl, p << 1, l, m);
        else if (beats(nl, st[p], xs[r])) _add(nl, p << 1 | 1, m+1, r);
    }

    T operator()(T x) const {
        auto it = lower_bound(xs.begin(), xs.end(), x);
        if (it == xs.end() && !xs.empty()) it = prev(xs.end());
        int idx = int(it - xs.begin());
        return query(idx, 1, 0, n-1, x);
    }

    T query(int idx, int p, int l, int r, T x) const {
        T res = st[p](x);
        if (l == r) return res;
        int m = (l + r) >> 1;
        T child_res;
        if (idx <= m) child_res = query(idx, p << 1, l, m, x);
        else child_res = query(idx, p << 1 | 1, m+1, r, x);
        return (MIN_MODE ? min(res, child_res) : max(res, child_res));
    }
};

/*
vector<long long> x = {1, 5, 10, 20};
LiChao<long long> lc(x);
// LiChao<long long, false> lc_max(x); 
// false = Max Mode, will return -inf (default) if no line cover the query,
// otherwise max value.
lc.add(2, 5); // y = 2x+5
query = lc(5);
// x \in [-10^9, 10^9]
*/
