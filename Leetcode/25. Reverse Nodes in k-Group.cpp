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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *pre = dummy;
        ListNode *cur = head;
        int cnt = 0;
        while (cur != nullptr){
            cnt++;
            if (cnt%k == 0){
                pre = reverse(pre, cur->next);
                cur = pre->next;
            }
            else{
                cur = cur->next;
            }       
        }
        return dummy->next;
    }

    ListNode *reverse(ListNode *start, ListNode *end){
        ListNode *prev, *curr, *nxt;
        prev = start;
        curr = start->next;
        nxt = start->next;
        while (curr != end){
            nxt = curr->next;
            curr->next= prev;
            prev = curr;
            curr = nxt;
        }
        start->next->next = curr;
        ListNode *tmp = start->next;
        start->next = prev;
        return tmp;
    }
};
