import numpy

v = input().split()
N, M, P = int(v[0]), int(v[1]), int(v[2])

n = []
for i in range(N):
    n.append(list(map(int, input().split())))
m = []
for i in range(M):
    m.append(list(map(int, input().split())))
    
A, B = numpy.array(n), numpy.array(m)
print(numpy.concatenate((A, B), axis = 0))
