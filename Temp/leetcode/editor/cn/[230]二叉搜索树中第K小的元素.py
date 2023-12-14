# 230 二叉搜索树中第K小的元素
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     cnt = 0
    #
    #     def mid(root: Optional[TreeNode]) -> int:
    #         if not root:
    #             return inf
    #         l = mid(root.left)
    #         if l != inf:
    #             return l
    #         nonlocal cnt
    #         # 当前节点是第 cnt 个
    #         cnt += 1
    #         if cnt == k:
    #             return root.val
    #         return mid(root.right)
    #
    #     return mid(root)

    # 迭代
    # 向左之前将当前 root 入栈
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     st = []
    #     while root or st:
    #         while root:
    #             st.append(root)
    #             root = root.left
    #         k -= 1
    #         root = st.pop()
    #         if k == 0:
    #             return root.val
    #         root = root.right

    # Morris
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if predecessor.right == root:
                    predecessor.right = None
                else:
                    predecessor.right = root
                    root = root.left
                    continue
            k -= 1
            if k == 0:
                return root.val
            root = root.right

# leetcode submit region end(Prohibit modification and deletion)
