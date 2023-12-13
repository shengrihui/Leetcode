# 1373 二叉搜索子树的最大键值和
# https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # 因为要分别统计左右子树的键值和，再加上根节点，所以采用后序遍历
        def f(root: Optional[TreeNode]) -> (int, int, int):
            if not root:
                return inf, -inf, 0
            l_min, l_max, l_sum = f(root.left)
            r_min, r_max, r_sum = f(root.right)
            x = root.val
            s = x + l_sum + r_sum
            if x <= l_max or x >= r_min:
                return -inf, inf, s  # 不是二叉搜索树了，第三个无所谓了
            nonlocal ans
            ans = max(ans, s)
            return min(x, l_min), max(x, r_max), s

        ans = 0
        f(root)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

"""
[4,8,null,6,1,9,null,-5,4,null,null,null,-3,null,10]
[        4,
    8,                null,
   6,           1,
  9, null,     -5,       4,
null,null,   null,-3,null,10]
[1,null,10,-5,20]
[   1,
null,10,
    -5,20]
"""
