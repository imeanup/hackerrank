from collections import Counter

if __name__ == '__main__':
    s = input()
    for c in Counter(sorted(s)).most_common(3):
        print(*c)
        
    # without using most_common() https://docs.python.org/3/library/collections.html#counter-objects
    
    # c = Counter(s)
    # lst = sorted(c.items(), key = lambda x:x[0])
    # lst = sorted(lst, key = lambda x: x[1], reverse=True)[:3]
    # print(lst)
