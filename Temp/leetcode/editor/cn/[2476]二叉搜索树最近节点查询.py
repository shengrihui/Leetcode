# 2476 二叉搜索树最近节点查询
# https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ans = []
        order = self.Morris(root)
        n = len(order)
        for x in queries:
            a = bisect_right(order, x)
            b = bisect_left(order, x)
            ans.append([order[a - 1] if a != 0 else -1, order[b] if b != n else -1])
        return ans

    def Morris(self, root):
        order = []
        while root:
            if root.left:
                predecessor = root.left
                # 当遍历完 root 的左子树，root 会通过之前进入左子树的时候设置的 predecessor 的 right 回到 root
                while predecessor.right and predecessor.right != root:  # 一直往右
                    predecessor = predecessor.right

                if predecessor.right == root:  # 遍历完了左子树，回到了 root，恢复原来的树结构
                    predecessor.right = None
                    order.append(root.val)  # ******
                    root = root.right
                else:
                    predecessor.right = root  # 将 predecessor 的右指针指向 root
                    root = root.left  # 进入左子树
            else:  # root没有左子树，
                order.append(root.val)  # ******
                root = root.right
        # ****** 在每次进入右子树之前都输出值
        return order
# leetcode submit region end(Prohibit modification and deletion)
