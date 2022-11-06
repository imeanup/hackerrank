import string as s

def print_rangoli(n):
    # your code goes here
    l = s.ascii_lowercase
    x = l[n-1::-1] + l[1: n]
    # print(x)
    char = "-".join(x)
    # print(char)
    m = len("-".join(x))
    # print(m)
    for i in range(1, n):
        print(("-".join(l[n-1:n-i:-1]+l[n-i:n])).center(m, "-"))
    # print(char)
    for i in range(n, 0, -1):
        print(("-".join(l[n-1:n-i:-1]+l[n-i:n])).center(m, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
