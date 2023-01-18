class DisjointSet:
  
    '''
    initializes the parent and rank arrays with n elements.
    '''
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    '''
     returns the representative element (root) of the set that x is an element of. 
     It uses path compression to make each element on the path a child of the representative element.
    '''
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    '''
    merges the sets that contain x and y, by making the representative element of one set a child of the other. 
    It uses union by rank to always make the representative element of the smaller tree a child of the representative element of the larger tree.
    '''
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                px, py = py, px
            self.parent[px] = py
            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1
    '''
    To check if two elements x and y are connected in a disjoint set data structure, we can check if their representative elements 
    (also known as roots) are the same. If the representative elements are the same, it means that x and y are in the same set and 
    are therefore connected.
    '''
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    '''
    Alternatively, you can check if the parent of x and y is the same, if it's the same then they are connected otherwise not.
    '''
    def isConnected(self, x, y):
        return self.parent[x] == self.parent[y]
    
    '''
    traverse from the element to its representative element (also known as root) and count the number of edges in the path.
    '''
    def height(self, x):
        h = 0
        while self.parent[x] != x:
            x = self.parent[x]
            h += 1
        return h
    '''
    Alternatively, use rank array for the calculation of height.
    '''
    def height(self, x):
        return self.rank[self.find(x)]
    '''
    iterate through the elements of the set and for each element find its representative element (root) and 
    increment the size of the set that the element belongs to. Finally, you can return the maximum size of the set.
    '''
    def width(self):
        width = 0
        set_size = [0] * len(self.parent)
        for i in range(len(self.parent)):
            set_size[self.find(i)] += 1
        width = max(set_size)
        return width
      
    def width(self):
        width = 0
        set_size = {}
        for i in range(len(self.parent)):
            rep = self.find(i)
            if rep in set_size:
                set_size[rep] += 1
            else:
                set_size[rep] = 1
        width = max(set_size.values())
        return width




'''
Path compression and union by rank are two techniques that can be used to improve the performance of the disjoint set data structure.

Path compression: Path compression is a technique that compresses the path from an element to its representative element by making 
each element on the path a child of the representative element. This reduces the height of the tree and improves the performance of 
the find operation.

Union by rank: Union by rank is a technique that is used to keep the height of the tree as small as possible. It works by always 
making the representative element of the smaller tree a child of the representative element of the larger tree.
'''
