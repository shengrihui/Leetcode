# LCR 151 彩灯装饰记录 III
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        row, nxt = 0, 1  # 当前行，下一行
        qs = [deque(), deque()]
        if root:
            qs[row].append(root)
        while qs[row]:
            row_record = []
            while qs[row]:
                if row & 1 == 0:  # 从左往右读，在 nxt 右边加入
                    node = qs[row].popleft()
                    if node.left: qs[nxt].append(node.left)
                    if node.right: qs[nxt].append(node.right)
                else:  # 从右往左读，在 nxt 左边加入
                    node = qs[row].pop()
                    if node.right: qs[nxt].appendleft(node.right)
                    if node.left: qs[nxt].appendleft(node.left)
                row_record.append(node.val)
            ans.append(row_record)
            row, nxt = nxt, row
        return ans
# leetcode submit region end(Prohibit modification and deletion)
