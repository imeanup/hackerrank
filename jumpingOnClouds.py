def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    i = 0
    while i < (len(c)-1):
        if i + 2 == len(c) or c[i + 2] == 1:
            i += 1
            jumps += 1
        else:
            i += 2
            jumps += 1
    return jumps
