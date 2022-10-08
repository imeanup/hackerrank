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

    def find(self, k):
        ...

    def insert(self, x):
        ...

    def delete(self, k):
        ...

    def find_min(self):
        ...

    def find_max(self):
        ...

    def find_next(self,k):
        ...

    def find_prev(self, k):
        ...

    def iter_order(self):
        ...
    
