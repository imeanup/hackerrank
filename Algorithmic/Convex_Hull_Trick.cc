template<typename T = long double>
struct CHT {
    struct Line {
        T m, c;
        Line(T m = 0, T c = 0): m(m), c(c) {}
        T operator()(T x) const { return m*x + c; } // y = mx + c;
    };

    deque<Line> hull;
    void add(T m, T c) {
        Line nl(m, c);
        while (hull.size() >= 2) {
            const Line& x = hull[hull.size()-2];
            const Line& y = hull.back();
            if ((nl.m - y.m) * (x.c - y.c) < (y.m - x.m) * (y.c - nl.c)) break;
            hull.pop_back();
        }
        hull.push_back(nl);
    }
    T operator()(T x) {
        T res = hull[0](x);
        while (hull.size() >= 2) {
            T cur = hull[1](x);
            if (cur < res) break; /* NOTE: x asc (cur < res), x dsc (cur >= res) */
            res = cur;
            hull.pop_front();
        }
        return res;
    }
};

/*
CHT<long long> cht; // default uses long double
cht.add(x, y);
cht(query_x)
*/
