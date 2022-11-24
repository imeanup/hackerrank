#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here
        n = len(nums)
        LDS = [1] * n
        LIS = [1] * n
        MX = 0
        
        for i in range(1, n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                        
        for i in reversed(range(n-1)):
            for j in reversed(range(i + 1, n)):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
                    
        for i in range(n):
            MX = max(MX, (LIS[i] + LDS[i] - 1))
            
            
        return MX

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends
