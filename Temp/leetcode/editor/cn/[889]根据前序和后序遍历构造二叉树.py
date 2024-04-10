# 889 根据前序和后序遍历构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 如果只有一个子树，那是左子树
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(i1: int, j1: int, i2: int, j2: int) -> Optional[TreeNode]:
            if i1 > j1:
                return None
            node = TreeNode(val=preorder[i1])
            if i1 == j1:
                return node
            m = postorder.index(preorder[i1 + 1], i2, j2 + 1)
            l = m - i2 + 1  # 左子树有多少节点
            node.left = build(i1 + 1, i1 + l, i2, m)
            node.right = build(i1 + l + 1, j1, m + 1, j2 - 1)
            return node

        n = len(postorder)
        return build(0, n - 1, 0, n - 1)


# 如果只有一个子树，那是右子树
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(i1: int, j1: int, i2: int, j2: int) -> Optional[TreeNode]:
            if i1 > j1:
                return None
            node = TreeNode(val=preorder[i1])
            if i2 == j2:
                return node
            m = preorder.index(postorder[j2 - 1], i1, j1 + 1)
            r = j1 - m + 1  # 右子树有多少节点
            node.left = build(i1 + 1, m - 1, i2, j2 - r - 1)
            node.right = build(m, j1, j2 - r, j2 - 1)
            return node

        n = len(postorder)
        return build(0, n - 1, 0, n - 1)

# leetcode submit region end(Prohibit modification and deletion)
