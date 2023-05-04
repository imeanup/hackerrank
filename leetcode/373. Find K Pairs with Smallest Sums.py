class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 and not nums2:
            return []
        heap = []
        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        # print("heap: ", heap)

        res = []
        while k > 0 and heap:
            sum_, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
     
            if j+1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            k -= 1
            
        return res
