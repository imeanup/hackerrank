def count_substring(A, S):
    count = 0
    for _ in range(len(A)):
        nA = A[_ : _ + len(S)]
        if nA == S:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
