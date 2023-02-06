# https://leetcode.com/problems/shuffle-the-array/description/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans =[]
        for i,j in zip(nums[:n],nums[n:]):
            ans.append(i)
            ans.append(j)
        return ans    
        
        
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans =[]    
        L = nums[n:]
        R = nums[:n]
        # print(L, R)
        for i in range(n):
            ans.append(R[i])
            ans.append(L[i])
            
        return ans    
