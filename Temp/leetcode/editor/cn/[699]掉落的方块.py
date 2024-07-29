# 699 掉落的方块
# https://leetcode.cn/problems/falling-squares/
from imports import *


# 暴力枚举
#
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = len(positions)
        ans = [0] * n
        up = [h for _, h in positions]
        mx = 0
        for i, (left, side) in enumerate(positions):
            right = left + side
            for j in range(i):
                left_j, side_j = positions[j]
                right_j = left_j + side_j
                if left_j <= left < right_j or left_j < right <= right_j or left <= left_j < right_j <= right:
                    up[i] = max(up[i], up[j] + side)
            mx = max(mx, up[i])
            ans[i] = mx
        return ans


# leetcode submit region begin(Prohibit modification and deletion)

class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = 0  # 当前节点（区间）的值
        self.add = 0  # 懒标记，因为这题是求 max 并且只是修改值，所以 add == v


class SegmentTree:
    def __init__(self):
        self.root = Node(1, 10 ** 9)

    def modify(self, L, R, v, node=None):
        if not node:
            node = self.root
        if L <= node.l and node.r <= R:  # 要修改的范围已经完全包括节点的范围，修改节点的值并结束递归
            node.v = node.add = v
            return
        self.pushdown(node)  # 将 add 向下传递
        if L <= node.mid:
            self.modify(L, R, v, node.left)
        if R >= node.mid + 1:
            self.modify(L, R, v, node.right)
        self.pushup(node)  # 更新

    def query(self, L, R, node=None):
        if not node:
            node = self.root
        if L <= node.l and node.r <= R:  # 要修改的范围已经完全包括节点的范围，修改节点的值并结束递归
            return node.v
        # 查询的时候也需要
        # 原因 1：为了有左右子树可以递归
        # 原因 2：node 范围只包含了 [L,R]  的一部分或者全部，但 node.add 还没有传下去
        self.pushdown(node)
        left_v = self.query(L, R, node.left) if L <= node.mid else 0
        right_v = self.query(L, R, node.right) if R >= node.mid + 1 else 0
        return left_v if left_v > right_v else right_v

    def pushup(self, node):
        node.v = node.left.v if node.left.v > node.right.v else node.right.v

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
            # if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        if node.add:
            node.left.v = node.right.v = node.add
            node.left.add = node.right.add = node.add
            node.add = 0


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        seg = SegmentTree()
        ans = []
        mx = 0
        for left, w in positions:
            right = left + w - 1
            h = seg.query(left, right) + w  # [left,right] 的新高度
            mx = max(mx, h)
            ans.append(mx)
            seg.modify(left, right, h)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
