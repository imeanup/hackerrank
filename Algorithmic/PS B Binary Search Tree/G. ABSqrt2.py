from cgitb import reset
import math, bintrees


class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def generate_first_k_a_b_sqrt2(k):  # Time: O(k lg k); Space: O(k)
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

    def generate_first_k_a_b_sqrt2(k):  # Time: O(n)
        # will store the first k numbers of the form a + b sqrt(2)
        cand = [ABSqrt2(0, 0)]
        i = j = 0
        for _ in range(1, k):
            cand_i_plus_1 = ABSqrt2(cand[i].a + 1, cand[i].b)
            cand_j_plus_sqrt2 = ABSqrt2(cand[j].a, cand[j].b + 1)
            cand.append(min(cand_i_plus_1, cand_j_plus_sqrt2))
            if cand_i_plus_1.val == cand[-1].val:
                i += 1
            if cand_j_plus_sqrt2.val == cand[-1].val:
                j += 1
        return [a.val for a in cand]
