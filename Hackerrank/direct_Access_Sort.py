''' 
Two drawbacks: first, it cannot handle duplicate keys, and second, it cannot handle large key ranges. 
If u = O(n),linear algorithm.
Run time: O(u+n)
'''

def main():
  A = [6,0,2,0,1,3,4,6,1,3,2]
  print(direct_access_sort(A))
  B = [6, 0, 3, 1, 2, 4, 7, 10, 5]
  print(direct_access_sort(B))
  
  
def direct_access_sort(A):
  u = 1 + max([x for x in A])

  D = [None] * u
  for x in A:
      D[x] = x

  i = 0 
  for key in range(u):

  if D[key] is not None:
      A[i] = D[key]
      i += 1
          

if __name__ == "__main__":
  main()
