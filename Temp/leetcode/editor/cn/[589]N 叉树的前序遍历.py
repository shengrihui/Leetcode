# 589 N 叉树的前序遍历
# https://leetcode.cn/problems/n-ary-tree-preorder-traversal/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def f(root: 'Node') -> None:
            nonlocal ans
            if not root:
                return
            ans.append(root.val)
            for node in root.children:
                f(node)

        ans = []
        f(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
