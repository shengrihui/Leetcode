# 2276 统计区间中的整数数目
# https://leetcode.cn/problems/count-integers-in-intervals/


# leetcode submit region begin(Prohibit modification and deletion)
class CountIntervals:
    __slots__ = ('left', 'right', 'l', 'r', 'cnt', 'size')

    def __init__(self, l=1, r=1_000_000_000):
        self.left = self.right = None  # 左右子树
        self.l, self.r = l, r  # 左右边界
        self.size, self.cnt = r - l + 1, 0

    def add(self, left: int, right: int) -> None:
        if self.cnt == self.size:
            return  # self 已被完整覆盖，无需执行任何操作

        # 当前节点的的范围 [self.l, self.r] 完全在要添加的区间 [left, right] 之中
        if left <= self.l and self.r <= right:
            self.cnt = self.size
            return

        # 动态开点，创建左右子树
        mid = (self.l + self.r) // 2
        if not self.left:
            self.left = CountIntervals(self.l, mid)
            # if not self.right:
            self.right = CountIntervals(mid + 1, self.r)

        # 统计 self 的数量
        # 更新
        if left <= mid:
            self.left.add(left, right)
        if right > mid:
            self.right.add(left, right)

        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt


# 灵神
"""
class CountIntervals:
    __slots__ = 'left', 'right', 'l', 'r', 'cnt'

    def __init__(self, l=1, r=10):
        self.left = self.right = None
        self.l, self.r, self.cnt = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.cnt == self.r - self.l + 1: return  # self 已被完整覆盖，无需执行任何操作
        if l <= self.l and self.r <= r:  # self 已被区间 [l,r] 完整覆盖，不再继续递归
            self.cnt = self.r - self.l + 1
            return
        mid = (self.l + self.r) // 2
        if self.left is None: self.left = CountIntervals(self.l, mid)  # 动态开点
        if self.right is None: self.right = CountIntervals(mid + 1, self.r)  # 动态开点
        if l <= mid: self.left.add(l, r)
        if mid < r: self.right.add(l, r)
        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt
"""
# 链表
"""
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.prev = None
        self.next = None

class CountIntervals:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev =  self.tail, self.head
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        if left > self.tail.prev.right:
            self.insert(self.tail.prev, Node(left, right))
            self.cnt += right - left + 1
            return
        p = self.head
        while p.next != self.tail and p.next.right < left:
            p = p.next
        # print(f"add, p got to {p.left} {p.right}")
        # self.print_all()
        if p.next == self.tail or p.next.left > right:
            self.insert(p, Node(left, right))
            self.cnt += right - left + 1
        else:
            if left < p.next.left:
                self.cnt += p.next.left - left
                p.next.left = left
            if p.next.right < right:
                self.update(p.next, right)
    
    def update(self, node, right):
        p = node
        # self.print_all()
        while p.next != self.tail and right >= p.next.left:
            p = p.next
            self.cnt -= p.right - p.left + 1
        right = max(right, p.right)
        self.cnt += right - node.right
        node.right = right
        node.next = p.next
        node.next.prev = node
    
    def insert(self, p, node):
        node.next = p.next
        node.next.prev = node
        p.next = node
        node.prev = p

    def count(self) -> int:
        return self.cnt
"""
# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
# leetcode submit region end(Prohibit modification and deletion)


obj = CountIntervals()
obj.add(2, 7)
