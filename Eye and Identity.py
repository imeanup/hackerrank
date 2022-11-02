import numpy


numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

print(numpy.eye(N,M))
