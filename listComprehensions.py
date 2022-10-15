''' https://www.hackerrank.com/challenges/list-comprehensions '''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []
    for i in range(int(x) + 1):
        for j in range(int(y)+1):
            for k in range(int(z)+1):
                if i + j + k != n:
                    list.append([i, j, k])
                    
    print(list)
