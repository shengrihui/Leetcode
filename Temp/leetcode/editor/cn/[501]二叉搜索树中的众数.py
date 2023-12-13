# 501 二叉搜索树中的众数
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        pre, cnt, mx_cnt = -inf, 0, 0

        def mid(root: Optional[TreeNode]) -> None:
            nonlocal ans, pre, cnt, mx_cnt
            if not root:
                return None
            mid(root.left)
            x = root.val
            if x == pre:
                cnt += 1
            else:
                if cnt > mx_cnt:
                    mx_cnt = cnt
                    ans = [pre]
                elif cnt == mx_cnt:
                    ans.append(pre)
                cnt = 1
                pre = x
            mid(root.right)

        mid(root)
        if cnt > mx_cnt:
            ans = [pre]
        elif cnt == mx_cnt:
            ans.append(pre)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
