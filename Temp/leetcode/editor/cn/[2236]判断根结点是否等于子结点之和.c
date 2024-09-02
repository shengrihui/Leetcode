// 2236 判断根结点是否等于子结点之和
// https://leetcode.cn/problems/root-equals-sum-of-children/

// leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool checkTree(struct TreeNode *root)
{
    return root->left->val + root->right->val == root->val;
}
// leetcode submit region end(Prohibit modification and deletion)
