# 144 二叉树的前序遍历
# https://leetcode.cn/problems/binary-tree-preorder-traversal/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def f(root: Optional[TreeNode]) -> None:
            if not root:
                return
            ans.append(root.val)
            f(root.left)
            f(root.right)

        ans = []
        f(root)
        return ans
"""

# 迭代
# 当前节点不为空，加入答案，加入栈，更新“当前节点”
# 保证了栈中的节点都不为空
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        node = root
        while st or node:
            while node:
                ans.append(node.val)
                st.append(node)
                node = node.left
            node = st.pop()
            node = node.right
        return ans

# leetcode submit region end(Prohibit modification and deletion)
