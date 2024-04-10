# 105 从前序与中序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pi: int, pj: int, ii: int, ij: int) -> Optional[TreeNode]:
            if pi > pj:
                return None
            v = preorder[pi]  # 当前子树根节点的值
            node = TreeNode(val=v)
            m = inorder.index(v, ii, ij + 1)  # 根节点的值在在中序遍历中下标
            l = m - ii  # 左子树有多少节点
            node.left = dfs(pi + 1, pi + l, ii, m - 1)
            node.right = dfs(pi + l + 1, pj, m + 1, ij)
            return node

        n = len(preorder)
        return dfs(0, n - 1, 0, n - 1)

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         def dfs(pi: int, pj: int, ii: int, ij: int) -> Optional[TreeNode]:
#             return TreeNode(val=preorder[pi], left=dfs(pi + 1, pi + inorder.index(preorder[pi], ii, ij + 1) - ii, ii,
#                                                        inorder.index(preorder[pi], ii, ij + 1) - 1),
#                             right=dfs(pi + inorder.index(preorder[pi], ii, ij + 1) - ii + 1, pj,
#                                       inorder.index(preorder[pi], ii, ij + 1) + 1, ij)) if pi <= pj else None
#
#         return dfs(0, len(preorder) - 1, 0, len(preorder) - 1)

# leetcode submit region end(Prohibit modification and deletion)
