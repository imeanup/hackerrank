import math, bintrees


class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def generate_first_k_a_b_sqrt2(k):
        # Initial for 0 + 0 * sqrt(2).
        candidates = bintrees.RBTree([(ABSqrt2(0, 0), None)])

        result = []
        while len(result) < k:
            next_smallest = candidates.pop_min()[0]
            result.append(next_smallest.val)
            # Add the enxt two numbers derived from next_smallest.
            candidates[ABSqrt2(next_smallest.a + 1, next_smallest.b)] = None
            candidates[ABSqrt2(next_smallest.a, next_smallest.b + 1)] = None
        return result
