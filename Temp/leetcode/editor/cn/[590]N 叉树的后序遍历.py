# 590 N 叉树的后序遍历
# https://leetcode.cn/problems/n-ary-tree-postorder-traversal/

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def f(root):
            if not root:
                return
            for node in root.children:
                f(node)
            nonlocal ans
            ans.append(root.val)

        f(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
