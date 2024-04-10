# 145 二叉树的后序遍历
# https://leetcode.cn/problems/binary-tree-postorder-traversal/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def f(root: Optional[TreeNode]) -> None:
            if not root:
                return
            f(root.left)
            f(root.right)
            ans.append(root.val)

        ans = []
        f(root)
        return ans
"""


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        node = root
        while st or node:
            while node:
                st.append(node)
                node = node.left
            node = st.pop()
            ans.append(node.val)
            node = node.right
        return ans

# leetcode submit region end(Prohibit modification and deletion)
