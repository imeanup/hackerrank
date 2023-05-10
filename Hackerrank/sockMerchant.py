def main():
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n, ar))

def sockMerchant(n, ar):
    # Write your code here
    counter = 0
    lst = list()
    for i in ar:
        if i not in lst:
            lst.append(i)
        else:
            counter += 1
            lst.remove(i)
    return counter

if __name__ == "__main__":
    main()
