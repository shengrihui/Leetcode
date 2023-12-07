# 1038 从二叉搜索树到更大和树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(root: TreeNode) -> None:
            nonlocal s
            if root.right:
                helper(root.right)
            s += root.val
            root.val = s
            if root.left:
                helper(root.left)

        s = 0
        helper(root)
        return root

# leetcode submit region end(Prohibit modification and deletion)


