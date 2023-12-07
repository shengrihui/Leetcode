# 94 二叉树的中序遍历
from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#
#         def trace(node):
#             if not node:
#                 return
#             trace(node.left)
#             ans.append(node.val)
#             trace(node.right)
#
#         trace(root)
#         return ans


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         st = []
#         while st or root:
#             while root:  # 一直往左，将 root 及其左边的孩子全部入栈
#                 st.append(root)
#                 root = root.left
#             node = st.pop()
#             ans.append(node.val)
#             root = node.right  # root 指针指向右边去
#         return ans


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法三：Morris 中序遍历
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        predecessor = None  # 用它去指向当前子树的根的前驱节点（中序遍历）
        while root:
            if root.left:
                predecessor = root.left
                # 两个条件
                # 1. predecessor.right 已经空
                # 2. 在遍历完左子树后回到 root ，这时候 root  的前驱节点的 right 已经指向 root 了，要及时退出
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                # while 结束之后，predecessor 指向 root 的前驱节点
                if predecessor.right == root:  # 已经指向 root 说明左子树访问完了
                    predecessor.right = None  # 恢复一下
                    ans.append(root.val)
                    root = root.right
                else:  # 将它的 right 指向 root
                    predecessor.right = root
                    root = root.left
            else:  # 没有左子树了，当前这个是根/树叶
                ans.append(root.val)
                root = root.right  # 要么它是真的右子树，要么就是中序遍历的根
        return ans

# leetcode submit region end(Prohibit modification and deletion)
