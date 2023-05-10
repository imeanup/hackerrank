# https://leetcode.com/problems/find-k-closest-elements/description/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            gap = abs(i - x)
            
            if len(heap) < k:
                heapq.heappush(heap, [-abs(i-x), i])
                
            elif gap < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [-gap, i])
                
            elif gap == -heap[0][0] and i < heap[0][1]:
                heapq.heappop(heap)
                heapq.heappush(heap, [-gap, i])

        return [x[1] for x in sorted(heap, key = lambda x:x[1])]
        
        
class Solution:
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
      i = 0; j = len(arr) - k
      while i < j:
          m = i + (j-i)//2
          if x - arr[m] > arr[m+k] - x:
              i = m + 1
          else:
              j = m
      return arr[i:i+k]
      
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        R = bisect.bisect_left(arr, x)
        L = R - 1
        while k:
            if R >= n or L >= 0 and x - arr[L] <= arr[R] - x:
                L -= 1
            else:
                R += 1
            k -= 1
        return arr[L+1:R]
            
        
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = len(arr) - 1
        while R - L >= k:
            if x - arr[L] <= arr[R] - x:
                R -= 1
            else:
                L += 1
        return arr[L:R+1]
