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
    # 递归
    # def findMode(self, root: Optional[TreeNode]) -> List[int]:
    #     ans = []
    #     pre, cnt, mx_cnt = -inf, 0, 0
    #
    #     def mid(root: Optional[TreeNode]) -> None:
    #         nonlocal ans, pre, cnt, mx_cnt
    #         if not root:
    #             return None
    #         mid(root.left)
    #         x = root.val
    #         if x == pre:
    #             cnt += 1
    #         else:
    #             if cnt > mx_cnt:
    #                 mx_cnt = cnt
    #                 ans = [pre]
    #             elif cnt == mx_cnt:
    #                 ans.append(pre)
    #             cnt = 1
    #             pre = x
    #         mid(root.right)
    #
    #     mid(root)
    #     if cnt > mx_cnt:
    #         ans = [pre]
    #     elif cnt == mx_cnt:
    #         ans.append(pre)
    #     return ans

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        pre, cnt, mx_cnt = 0, 0, 0

        # update 和上面方法的区别：
        # 在 cnt 与 mx_cmt 比较的时候，上一个方法的 cnt 代表的是 pre 的数量
        # 而 update 方法代表的就是当前 x 的数量
        # 因此在最后不用另外再来一遍
        def update(x: int) -> None:
            nonlocal pre, ans, cnt, mx_cnt
            if x == pre:
                cnt += 1
            else:
                cnt = 1
                pre = x
            if cnt == mx_cnt:
                ans.append(x)
            elif cnt > mx_cnt:
                mx_cnt = cnt
                ans = [x]

        # Morris
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
            update(root.val)
            root = root.right

        # 迭代
        """
        st = []
        while st or root:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            update(root.val)
            root = root.right
        """
        return ans
# leetcode submit region end(Prohibit modification and deletion)
