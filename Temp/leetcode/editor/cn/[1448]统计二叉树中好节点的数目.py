# 1448 统计二叉树中好节点的数目
from collections import *
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], mx: int) -> None:
        if not root:
            return
        if root.val >= mx:
            mx = root.val
            self.ans += 1
        if root.left:
            self.dfs(root.left, mx)
        if root.right:
            self.dfs(root.right, mx)

    def bfs(self, root: Optional[TreeNode]) -> None:
        q = deque([(root, root.val)])
        while q:
            node, mx = q.popleft()
            if not node:
                continue
            if node.val >= mx:
                mx = node.val
                self.ans += 1
            if node.left:
                q.append((node.left, mx))
            if node.right:
                q.append((node.right, mx))

    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        # self.dfs(root, root.val)
        self.bfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)


# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。 
# 
#  「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [3,1,4,3,null,1,5]
# 输出：4
# 解释：图中蓝色节点为好节点。
# 根节点 (3) 永远是个好节点。
# 节点 4 -> (3,4) 是路径中的最大值。
# 节点 5 -> (3,4,5) 是路径中的最大值。
# 节点 3 -> (3,1,3) 是路径中的最大值。 
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [3,3,null,4,2]
# 输出：3
# 解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。 
# 
#  示例 3： 
# 
#  输入：root = [1]
# 输出：1
# 解释：根节点是好节点。 
# 
#  
# 
#  提示： 
# 
#  
#  二叉树中节点数目范围是 [1, 10^5] 。 
#  每个节点权值的范围是 [-10^4, 10^4] 。 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 152 👎 0
