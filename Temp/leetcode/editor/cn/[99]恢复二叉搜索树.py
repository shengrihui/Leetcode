# 99 恢复二叉搜索树
# https://leetcode.cn/problems/recover-binary-search-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#
#         def mid_travel(node: Optional[TreeNode]) -> None:
#             nonlocal err1, err2, a, b
#             if not node:
#                 return
#             mid_travel(node.left)
#             a, b = b, node
#             if a and b and a.val > b.val:
#                 if not err1:
#                     err1, err2 = a, b
#                 else:
#                     err2 = b
#             mid_travel(node.right)
#
#         a, b = None, None
#         err1, err2 = None, None
#         mid_travel(root)
#         err1.val, err2.val = err2.val, err1.val

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a, b = None, None
        err1, err2 = None, None
        # predecessor = None  # root，根的前驱节点，根的左子树的最右节点

        while root:
            if root.left:
                predecessor = root.left
                # 当遍历完 root 的左子树，root 会通过之前进入左子树的时候设置的 predecessor 的 right 回到 root
                while predecessor.right and predecessor.right != root:  # 一直往右
                    predecessor = predecessor.right

                if predecessor.right == root:  # 遍历完了左子树，回到了 root，恢复原来的树结构
                    predecessor.right = None
                else:
                    predecessor.right = root  # 将 predecessor 的右指针指向 root
                    root = root.left  # 进入左子树
                    continue
            # root 不去左子树，要去右子树，
            # 在这里处理 寻找错误位置 的逻辑
            a, b = b, root
            if a and b and a.val > b.val:
                if not err1:
                    err1, err2 = a, b
                else:
                    err2 = b
            root = root.right
        # 交换两个错误位置
        err1.val, err2.val = err2.val, err1.val
# leetcode submit region end(Prohibit modification and deletion)
