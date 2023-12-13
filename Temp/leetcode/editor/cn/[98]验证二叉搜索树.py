# 98 验证二叉搜索树
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         a = -inf
#
#         def midTrace(node) -> bool:
#             nonlocal a
#             if node.left and not midTrace(node.left):
#                 return False
#             if node.val <= a:
#                 return False
#             a = node.val
#             if node.right and not midTrace(node.right):
#                 return False
#             return True
#
#         return midTrace(root)

# https://www.bilibili.com/video/BV14G411P7C1/?spm_id_from=333.788&vd_source=16586319d2fce84d328b49945668eb44
# 前序遍历
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left: int = -inf, right: int = inf) -> bool:
        if not root:
            return True
        x = root.val
        # 当前节点要 left < x < right，左子树的范围是 (left,x) 右子树(x,right)
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)
"""

# 中序遍历
"""
class Solution:
    pre = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:  # 当前节点小于等于上一个节点，不是升序，不是二叉搜索树
            return False
        self.pre = root.val  # 更新 pre
        return self.isValidBST(root.right)
"""


# 后序遍历

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(root: Optional[TreeNode]) -> (int, int):
            if not root:
                return inf, -inf  # 归回去以后，根一定不在范围内
            x = root.val
            l_min, l_max = f(root.left)
            r_min, r_max = f(root.right)
            if x <= l_max or x >= r_min:  # 不是二叉搜索树
                return -inf, inf  # 归回去之后根一定在在这个范围内，就一定不是二叉搜索树了
            return min(l_min, x), max(x, r_max)  # 要与x取最小/大值，因为左/右子树可能没有

        return f(root)[0] != -inf  # f(root)[1] != inf
# leetcode submit region end(Prohibit modification and deletion)
