def main():
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    counting(A)
    print(A)


def counting(A):
    u = 1 + max([x for x in A])
    D = [[] for _ in range(u)]
    for x in A:
        D[x].append(x)
    i = 0
    for chain in D: 
        for x in chain:
            A[i] = x
            i += 1


if __name__ == "__main__":
    main()
