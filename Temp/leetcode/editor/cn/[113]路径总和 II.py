# 113 路径总和 II
from collections import *
from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], targetSum: int) -> None:
        v = root.val
        self.path.append(v)
        if not root.left and not root.right and v == targetSum:
            self.ans.append(self.path.copy())  # copy!!!
            return
        if root.left:
            self.dfs(root.left, targetSum - v)
            self.path.pop()
        if root.right:
            self.dfs(root.right, targetSum - v)
            self.path.pop()

    def bfs(self, root: Optional[TreeNode], targetSum: int) -> None:
        q = deque()
        q.append((root, [root.val]))
        while q:
            node, path = q.popleft()
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    self.ans.append(path)
            if node.left:
                q.append((node.left, path + [node.left.val]))
            if node.right:
                q.append((node.right, path + [node.right.val]))

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        self.path = []
        # self.dfs(root, targetSum)
        self.bfs(root, targetSum)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)


# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点总数在范围 [0, 5000] 内 
#  -1000 <= Node.val <= 1000 
#  -1000 <= targetSum <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 回溯 二叉树 👍 1066 👎 0
