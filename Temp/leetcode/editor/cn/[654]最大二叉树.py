# 654 最大二叉树
# https://leetcode.cn/problems/maximum-binary-tree/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return None
#         mx, idx = nums[0], 0
#         for i, x in enumerate(nums):
#             if x > mx:
#                 mx, idx = x, i
#         return TreeNode(val=mx, left=self.constructMaximumBinaryTree(nums[:idx]),
#                         right=self.constructMaximumBinaryTree(nums[idx + 1:]))

TreeNode.__lt__ = lambda x, y: x.val < y.val


# 从左往右遍历数组，
# 遇到一个比栈顶还要小的，先直接入栈，
# 遇到一个大的（叫他tx），那么开启循环，直到遇到更大的停止并将这个入栈（单调递减栈）
# 在循环的过程中，每一个出栈（叫他ti)的节点，都是下一个出栈的节点（叫他tj）的右儿子
# 因为在数组中，ti 是在 tj 的右边，并且 ti < tj
# 循环最后一个出栈（叫他tk）的，是 tx 的左儿子
# 因为在数组中，tk 是在 tx 的左边，并且 tx > tk
# 遍历完数组之后，还要将栈里剩下的节点加入到树中（右斜树）
# 为了方便代码，在 nums 后面加一个1001，这样遍历完了就可以输出了
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        st = []
        nums.append(1001)
        for x in nums:
            t = TreeNode(x)
            son = None
            while st and t > st[-1]:
                parent = st.pop()
                parent.right = son
                son = parent
            t.left = son
            st.append(t)
        return st[0].left
# leetcode submit region end(Prohibit modification and deletion)
