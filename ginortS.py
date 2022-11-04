# Enter your code here. Read input from STDIN. Print output to STDOUT

s = sorted(input())
lower = ""
upper = ""
odd = ""
even = ""
for i in s:
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i
    elif int(i) % 2 != 0:
        odd += i
    elif int(i) % 2 == 0:
        even += i

print(lower+upper+odd+even)
