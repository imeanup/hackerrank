# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            # Shifting num by 1 (or multiplying with 2) and adding the curr val using OR
            num = (num << 1) | head.next.val
            head = head.next
        return num

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num

  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        num = []
        def inOrder(node):
            nonlocal num
            if node:
                num.append(str(node.val))
                inOrder(node.next)
        inOrder(head)
        # print(num)
        return int("".join(num), 2)
