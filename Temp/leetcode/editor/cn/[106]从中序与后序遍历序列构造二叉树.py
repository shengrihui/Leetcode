# 106 从中序与后序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def builder(pi: int, pj: int, ii: int, ij: int) -> Optional[TreeNode]:
            if pi > pj:
                return None
            v = postorder[pj]  # 当前子树根节点的值
            node = TreeNode(val=v)
            m = inorder.index(v, ii, ij + 1)  # 根节点的值在在中序遍历中下标
            l = m - ii  # 左子树有多少节点
            node.left = builder(pi, pi + l - 1, ii, m - 1)
            node.right = builder(pi + l, pj - 1, m + 1, ij)
            return node

        n = len(postorder)
        return builder(0, n - 1, 0, n - 1)
# leetcode submit region end(Prohibit modification and deletion)
