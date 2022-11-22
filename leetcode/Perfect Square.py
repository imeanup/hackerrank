import math

def CheckTwo(c):                             
    while c % 2 == 0: 
        c = c // 2
    
    while c % 5 == 0: 
        c = c // 5
    
    while c % 9 == 0: 
        c = c // 9

    if c % 3 == 0: 
        return False

    if c in (0,1,13,17): 
        return True

    i, j = 0, int(math.sqrt(c))

    while i <= j:
        if pow(i, 2) + pow(j, 2) == c: 
            return True
        
        if pow(i, 2) + pow(j, 2) < c: 
            i += 1
        
        if pow(i, 2) + pow(j, 2) > c: 
            j -= 1

    return  False

if __name__ == "__main__":

    n = int(input())
    i = 1
    while pow(i, 2) <= n:                             
        if pow(i, 2) == n: 
            print(1)                   
        i += 1  

    if CheckTwo(n): 
        print(2)

    while not n % 4: 
        n //= 4                         
    
    if n % 8 != 7: 
        print(3) 
    
    print(4)     
