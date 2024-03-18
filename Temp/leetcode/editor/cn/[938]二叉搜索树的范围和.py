# 938 二叉搜索树的范围和
# https://leetcode.cn/problems/range-sum-of-bst/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        while root:
            if root.left:
                predecessor = root.left
                # 当遍历完 root 的左子树，root 会通过之前进入左子树的时候设置的 predecessor 的 right 回到 root
                while predecessor.right and predecessor.right != root:  # 一直往右
                    predecessor = predecessor.right

                if predecessor.right == root:  # 遍历完了左子树，回到了 root，恢复原来的树结构
                    predecessor.right = None
                    ans += root.val if low <= root.val <= high else 0
                    root = root.right
                else:
                    predecessor.right = root  # 将 predecessor 的右指针指向 root
                    root = root.left  # 进入左子树
            else:  # root没有左子树，
                ans += root.val if low <= root.val <= high else 0
                root = root.right
        return ans

# leetcode submit region end(Prohibit modification and deletion)
