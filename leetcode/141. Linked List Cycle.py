# https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan&id=data-structure-i

'''
Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm.

The basic idea is to have two pointers, one (the "tortoise") that moves one step at a time, 
and another (the "hare") that moves two steps at a time. If there is a cycle in the list, 
the hare will eventually catch up to the tortoise, and we can return true. 
If the hare reaches the end of the list without catching up to the tortoise, we can return false.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
