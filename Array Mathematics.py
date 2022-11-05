import numpy

N, M = map(int, input().split())

A = list(input().split() for _ in range(N))
B = list(input().split() for _ in range(N))

a = numpy.array(A, int)
b = numpy.array(B, int)

print(a+b, a-b, a*b, a//b, a%b, a**b, sep="\n")
