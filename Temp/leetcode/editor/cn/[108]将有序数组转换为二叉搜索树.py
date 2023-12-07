# 108 将有序数组转换为二叉搜索树
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def f(l: int, r: int) -> Optional[TreeNode]:
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            if l == r:
                return node
            if l != mid:
                node.left = f(l, mid - 1)
            node.right = f(mid + 1, r)
            return node

        return f(0, len(nums) - 1)
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。 
# 
#  高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 
#  
# 
#  示例 2： 
#  
#  
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 按 严格递增 顺序排列 
#  
# 
#  Related Topics 树 二叉搜索树 数组 分治 二叉树 👍 1440 👎 0
