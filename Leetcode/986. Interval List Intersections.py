class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(A) and j < len(B):
            aStart, aEnd = A[i]
            bStart, bEnd = B[j]
            
            if aStart <= bEnd and bStart <= aEnd:
                ans.append([max(aStart,bStart), min(aEnd, bEnd)])
                
            if aEnd <= bEnd:
                i += 1
            else:
                j += 1
                
        return ans
            
