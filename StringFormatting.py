def print_formatted(num):
    # your code goes here
    l = len(bin(num)[2:])
    for n in range(1, num+1):
        print(str(n).rjust(l),oct(n)[2:].rjust(l),hex(n).upper()[2:].rjust(l),bin(n)[2:].rjust(l))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
