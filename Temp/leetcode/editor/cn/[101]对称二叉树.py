# 101 对称二叉树
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 递归方式
        def check(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
            if r1 is None and r2 is None:
                return True
            if r1 and not r2 or not r1 and r2 or r1.val != r2.val:
                return False
            return r1.val == r2.val and check(r1.left, r2.right) and check(r1.right, r2.left)

        return check(root.left, root.right)
        # 栈方式
        """
        st = [(root.left, root.right)]
        while st:
            r1, r2 = st.pop()
            if r1 is None and r2 is None:
                continue
            if r1 and not r2 or not r1 and r2 or r1.val != r2.val:
                return False
            st.append((r1.left, r2.right))
            st.append((r1.right, r2.left))
        return True
        """
# leetcode submit region end(Prohibit modification and deletion)


