# 543 二叉树的直径
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def depth(root):
            nonlocal ans
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            ans = max(ans, L + R)
            return max(L, R) + 1

        depth(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


# 给你一棵二叉树的根节点，返回该树的 直径 。 
# 
#  二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。 
# 
#  两节点之间路径的 长度 由它们之间边数表示。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,2]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 10⁴] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 1430 👎 0
