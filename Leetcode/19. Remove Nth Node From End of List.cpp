/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *start = new ListNode();
        start = head;
        ListNode *first = start;
        ListNode *second = start;
        for (int i = 0; i < n; i++){
            first = first->next;
        }
        if (first == nullptr){
            return start->next;
        }
        while (first != nullptr && first->next != nullptr){
            first = first->next;
            second = second->next;
        }
        second->next = second->next->next;
        return head;

    }
};
