// 2181 合并零之间的节点
// https://leetcode.cn/problems/merge-nodes-in-between-zeros/


//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeNodes(struct ListNode* head) {
    struct ListNode* tail = head;
    struct ListNode* cur = tail->next;
    while (cur->next) {
        if (cur->val) { // cur 值不为 0 加到 tail 里
            tail->val += cur->val;
        } else { // 遇到 0 了，tail 后移并置 0
            tail = tail->next;
            tail->val = 0;
        }
        cur = cur->next; // cur 后移
    }

    // free
    cur = tail->next;
    while (cur) {
        tail->next = cur->next;
        free(cur);
        cur = tail->next;
    }
    return head;
}
//leetcode submit region end(Prohibit modification and deletion)
