cube = lambda x: pow(x, 3)# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    def fib(i):
        if i in [0,1]:
            return i
        return fib(i-1)+fib(i-2)
    
    return [fib(i) for i in range(n)]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
