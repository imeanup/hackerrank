# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sumFreq = {}
        maxFreq = 0
        maxFreqSums = []

        def findTreeSum(node):
            nonlocal sumFreq, maxFreq
            if not node:
                return 0
            leftSum = findTreeSum(node.left)
            rightSum = findTreeSum(node.right)

            currSum = node.val + leftSum + rightSum
            sumFreq[currSum] = sumFreq.get(currSum, 0) + 1
            maxFreq = max(maxFreq, sumFreq[currSum])

            return currSum

        findTreeSum(root)
        # print(sumFreq)
        for s in sumFreq:
            if sumFreq[s] == maxFreq:
                maxFreqSums.append(s)

        # print(maxFreqSums)
        return maxFreqSums
      
      

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sumFreq = {}
        maxFreq = 0
        maxFreqSums = []

        def findTreeSum(node):
            if not node:
                return 0
            leftSum = findTreeSum(node.left)
            rightSum = findTreeSum(node.right)

            return node.val + leftSum + rightSum

        def preOrder(node):
            nonlocal sumFreq, maxFreq
            if not node:
                return
            currSum = findTreeSum(node)
            sumFreq[currSum] = sumFreq.get(currSum, 0) + 1
            maxFreq = max(maxFreq, sumFreq[currSum])

            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        print(sumFreq)
        for s in sumFreq:
            if sumFreq[s] == maxFreq:
                maxFreqSums.append(s)

        print(maxFreqSums)
        return maxFreqSums
