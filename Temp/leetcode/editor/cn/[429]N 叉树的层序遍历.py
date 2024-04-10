# 429 N 叉树的层序遍历
# https://leetcode.cn/problems/n-ary-tree-level-order-traversal/
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                q.extend(node.children)
                row.append(node.val)
            ans.append(row)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
