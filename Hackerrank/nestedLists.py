if __name__ == '__main__':
    
    A = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        A.append([name,score])
    
    set = set()
    
    for k,v in A:
        set.add(v)
    sort = sorted(set)
    
    for k, v in sorted(A, key=lambda s:s[0]):
        if v == sort[1]:
            print(k)
        
