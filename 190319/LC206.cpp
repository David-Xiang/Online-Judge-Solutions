// LeetCode 206
// Reverse Linked List
#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct ListNode{
    int val;
    ListNode *next;
    ListNode(): val(0), next(NULL) {}
    ListNode(int x): val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *now, *pre, *tmp;
        pre = NULL;
        now = head;
        if (head == NULL) // special case: head is NULL!
            return NULL;
        tmp = head->next;
        if (tmp == NULL)
            return now;

        while(true) {
            now->next = pre;
            pre = now;
            now = tmp;
            if (tmp->next == NULL){
                tmp->next = pre;
                return now;
            }
            tmp = tmp->next;
        }

    }
};

int main(){
    ListNode l[10];
    for (int i = 0; i < 10; i++){
        l[i].val = i;
        if (i < 9)
            l[i].next = &l[i+1];
    }
    ListNode* p = &l[0];
    while(p!= NULL){
        cout << p->val << endl;
        p = p->next;
    }

    p = &l[0];

    //reverse
    Solution s;
    p =  s.reverseList(p);
    while(p != NULL){
        cout << p->val << endl;
        p = p->next;
    }
    return 0;
}