from random import randint

class Hash_Table_Set:
    def __init__(self, r = 200):    # O(1)
        self.chain_Set = Set_from_Seq(Linked_List_Seq)
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2**31 - 1
        self.a = randint(1, self.p - 1) 
        self._compute_bounds()
        self._resize(0)

    def __len__(self):              # O(1)
        return self.size

    def __iter__(self):             # O(n)
        for X in self.A:
            yield from X

    def  build(self, X):            # O(n)
        for x in X:
            self.insert(x)

    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m

    def _compute_bounds(self):       # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) * 100*100 // (self.r * self.r)

    def _resize(self, n):            # O(n)
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100:
                f += 1
                #f = ceil(r / 100)
            m = max(n, 1) * f
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                A[h].insert(x)
            self.A = A
            self._compute_bounds()


    def find(self, k):              # O(1)e
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)


    def insert(self, x):            # O(1)ae
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        added = self.A[h].insert(x)
        if added:
            self.size += 1
        return added


    def delete(self, k):            # O(1)ae
        assert len(self) > 0
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x

    def find_min(self):             # O(n)
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out

    
    def find_max(self):             # O(n)
        out = None
        for x in self:
            if (out is None) or (x.key > out.key):
                out = x
        return out

    
    def find_next(self,k):          # O(n)
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out

    
    def find_prev(self, k):         # O(n)
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out

    
    def iter_order(self):           # O(n^2)
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)
