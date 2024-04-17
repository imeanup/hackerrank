n, k = map(int, input().split())
k -= 1
s = input().strip()
res = ""
for i in range(n):
    if i == k:
        res += s[i].lower()
    else:
        res += s[i]
print(res)