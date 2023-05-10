if __name__ == '__main__':
    L = []
    ml = []
    N = int(input())
    for _ in range(N):
        n = input().split()
        L.append(n)
        
    for _ in L:
        if _[0] == "insert":
            ml.insert(int(_[1]), int(_[2]))
        elif _[0] == "print":
            print(ml)
        elif _[0] == "remove":
            ml.remove(int(_[1]))
        elif _[0] == "append":
            ml.append(int(_[1]))
        elif _[0] == "sort":
            ml.sort()
        elif _[0] == "pop":
            ml.pop()
        elif _[0] == "reverse":
            ml.reverse()
