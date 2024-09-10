// 671 二叉树中第二小的节点
// https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/


//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int findSecondMinimumValue(struct TreeNode* root) {
    if (!root->left) return -1;
    int mn = root->val;
    int left = root->left->val != mn ? root->left->val : findSecondMinimumValue(root->left);
    int right = root->right->val != mn ? root->right->val : findSecondMinimumValue(root->right);
    return left != -1 && right != -1 ? (left < right ? left : right) : (left > right ? left : right);
}
//leetcode submit region end(Prohibit modification and deletion)
