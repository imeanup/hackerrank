def average(array):
    # your code goes here
    s = set(array)
    j = 0
    for i in s:
        j += i
    avg = f"{j/len(s):.3f}"
    return avg
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
