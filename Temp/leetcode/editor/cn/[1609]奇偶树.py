# 1609 奇偶树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 0)])
        row = 0
        while q:
            pre = inf if row & 1 else 0
            while q and q[0][1] == row:
                node, _ = q.popleft()
                v = node.val
                # if row & 1 == 0 and v & 1 and v > pre or \
                #         row & 1 and v & 1 == 0 and v < pre:
                if (row & 1) ^ (v & 1) and (v < pre if row & 1 else v > pre):
                    pre = v
                    if node.left:
                        q.append((node.left, row + 1))
                    if node.right:
                        q.append((node.right, row + 1))
                else:
                    return False
            row += 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
