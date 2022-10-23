from Binary_Tree import Binary_Node, Binary_Tree


class BST_Node(Binary_Node):
    def subtree_find(A, k):  # O(h)
        if k < A.item:
            if A.left:
                return A.left.subtree_find(k)
        elif k > A.item:
            if A.right:
                return A.right.subtree_find(k)
        else:
            return A
        return None

    def subtree_find_next(A, k):  # O(h)
        if A.item <= k:
            if A.right:
                return A.right.subtree_find_next(k)
            else:
                return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B:
                return B
        return A

    def subtree_find_prev(A, k):  # O(h)
        if A.item >= k:
            if A.left:
                return A.left.subtree_find_prev(k)
            else:
                return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B:
                return B
        return A

    def subtree_insert(A, B):  # O(h)
        if B.item < A.item:
            if A.left:
                A.left.subtree_insert(B)
            else:
                A.subtree_insert_before(B)
        elif B.item > A.item:
            if A.right:
                A.right.subtree_insert(B)
            else:
                A.subtree_insert_after(B)
        else:
            A.item = B.item


class Binary_Tree_Set(Binary_Tree):
    def __init__(self, Node_Type=BST_Node):  # O(1)
        super().__init__(Node_Type)

    def iter_order(self):  # O(n)
        yield from self

    def build(self, A):  # O(n log n)
        for x in A:
            self.insert(x)

    def find_min(self):  # O(h)
        if self.root:
            return self.root.subtree_first().item

    def find_max(self):  # O(h)
        if self.root:
            return self.root.subtree_last().item

    def find(self, k):  # O(h)
        if self.root:
            node = self.root.subtree_find(k)
            if node:
                return node.item

    def find_next(self, k):  # O(h)
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:
                return node.item

    def find_prev(self, k):  # O(h)
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node:
                return node.item

    def insert(self, x):  # O(h)
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None:
                return False
        else:
            self.root = new_node
        self.size += 1
        return True

    def delete(self, k):  # O(h)
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_extract()
        if ext.parent is None:
            self.root = None
        self.size -= 1
        return ext.item


if __name__ == "__main__":
    T = Binary_Tree_Set()
    T.build([10, 6, 8, 5, 1, 3])
    print(f"\n* Tree *\n\n {T}")

    T.insert(2)
    T.insert(4)
    T.insert(12)
    T.insert(29)

    print(f"\n* Tree after insertion *\n\n {T}")

    T.delete(10)
    print(f"\n* Tree after deletion *\n\n {T}")

    max = T.find_max()
    min = T.find_min()
    print(f"max: {max} min: {min}")

    find_prev = T.find_prev(10)
    find_next = T.find_next(10)

    print(f"Find Prev: {find_prev}, Find next: {find_next}")

    # find = T.find(int(input("\nFind Value:   ")))
    # print(f"\nFind present? {find}\n")