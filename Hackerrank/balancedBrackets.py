s = input()
stack = []
for i in s:
    if i in ["[", "{", "("]:
        stack.append(i)
    else:
        if len(stack) == 0:
             print("NO")
        else:
            pop_val = stack.pop()
            if i == ")" and pop_val != "(":
                print("NO")
            elif i == "}" and pop_val != "{":
                print("NO")
            elif i == "]" and pop_val != "[":
                print("NO")
if len(stack) == 0:
    print("YES")
else:
    print("NO")
