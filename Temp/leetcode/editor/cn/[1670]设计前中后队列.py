# 1670 设计前中后队列
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
# class FrontMiddleBackQueue:
#
#     def __init__(self):
#         self.left = deque()
#         self.right = deque()
#
#     def pushFront(self, val: int) -> None:
#         self.left.appendleft(val)
#         self.modify()
#
#     def pushMiddle(self, val: int) -> None:
#         self.left.append(val)
#         self.modify()
#
#     def pushBack(self, val: int) -> None:
#         self.right.append(val)
#         self.modify()
#
#     def popFront(self) -> int:
#         if len(self.left) == 0:
#             if len(self.right) == 0:
#                 return -1
#             x = self.right.popleft()
#         else:
#             x = self.left.popleft()
#         self.modify()
#         return x
#
#     def popMiddle(self) -> int:
#         if len(self.left) == 0:
#             if len(self.right) == 0:
#                 return -1
#             x = self.right.popleft()
#         else:
#             if len(self.left) == len(self.right):
#                 x = self.left.pop()
#             else:
#                 x = self.right.popleft()
#         self.modify()
#         return x
#
#     def popBack(self) -> int:
#         if len(self.right) == 0:
#             return -1
#         x = self.right.pop()
#         self.modify()
#         return x
#
#     def modify(self):
#         while len(self.left) < len(self.right) - 1:
#             self.left.append(self.right.popleft())
#         while len(self.left) > len(self.right):
#             self.right.appendleft(self.left.pop())

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    __slots__ = ("val", "prev", "next")

    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class FrontMiddleBackQueue:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        # 奇数的时候，要删除的那个，插入的后一个
        # 偶数的时候，要删除的后一个，插入的后一个
        self.mid = self.tail
        self.length = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def pushFront(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.length += 1
        if self.length % 2 == 1:
            self.mid = self.mid.prev

    def pushMiddle(self, val: int) -> None:
        node = Node(val)
        node.next = self.mid
        node.prev = self.mid.prev
        node.next.prev = node
        node.prev.next = node
        self.length += 1
        if self.length % 2 == 1:
            self.mid = self.mid.prev

    def pushBack(self, val: int) -> None:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        node.next.prev = node
        node.prev.next = node
        self.length += 1
        if self.length == 1:
            self.mid = self.mid.prev
        if self.length % 2 ==0:
            self.mid = self.mid.next

    def popFront(self) -> int:
        if self.length == 0:
            return -1
        p = self.head.next
        self.head.next = p.next
        p.next.prev = self.head
        v = p.val
        self.length -= 1
        # 变成偶数了 5->4 mid后移
        if self.length % 2 == 0:
            self.mid = self.mid.next
        del p
        return v

    def popMiddle(self) -> int:
        if self.length == 0:
            return -1
        p = self.mid if self.length % 2 == 1 else self.mid.prev
        p.prev.next = p.next
        p.next.prev = p.prev
        v = p.val
        self.length -= 1
        if self.length % 2 == 0:
            self.mid = p.next
        del p
        return v

    def popBack(self) -> int:
        if self.length == 0:
            return -1
        p = self.tail.prev
        self.tail.prev = p.prev
        p.prev.next = self.tail
        v = p.val
        self.length -= 1
        if self.length == 0:
            self.mid = self.tail
        if self.length % 2 == 1:
            self.mid = self.mid.prev
        del p
        return v

    def show(self):
        p = self.head.next
        print("list: ", end="")
        while p != self.tail:
            print(p.val, end=",")
            p = p.next
        print()
        print("mid", self.mid.val)


# leetcode submit region end(Prohibit modification and deletion)

"""
["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle"]
[[],[1],[2],[3],[4]]
["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]
[[],[1],[2],[3],[4],[],[],[],[],[]]
["FrontMiddleBackQueue","pushFront","pushFront","pushFront","pushFront","popBack","popBack","popBack","popBack"]
[[],[1],[2],[3],[4],[],[],[],[]]
["FrontMiddleBackQueue","pushMiddle","pushMiddle","pushMiddle","popMiddle","popMiddle","popMiddle"]
[[],[1],[2],[3],[],[],[]]
["FrontMiddleBackQueue","pushBack","popMiddle"]
[[],[10],[]]
["FrontMiddleBackQueue","pushMiddle","popBack","popMiddle","popMiddle","pushBack","pushFront","popFront","pushMiddle","pushMiddle","popMiddle","popMiddle","pushMiddle","popMiddle","pushMiddle"]
[[],[874835],[],[],[],[319750],[782168],[],[16473],[495349],[],[],[596131],[],[583563]]

"""
# q = FrontMiddleBackQueue()
# calls =["pushBack","popMiddle"]
#
# args = [[10],[]]
# for m_name, arg in zip(calls, args):
#     m = q.__getattribute__(m_name)
#     print(m_name, arg)
#     print("ret", m(*arg))
#     q.show()
#     print()

# 请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。
# 
#  请你完成 FrontMiddleBack 类： 
# 
#  
#  FrontMiddleBack() 初始化队列。 
#  void pushFront(int val) 将 val 添加到队列的 最前面 。 
#  void pushMiddle(int val) 将 val 添加到队列的 正中间 。 
#  void pushBack(int val) 将 val 添加到队里的 最后面 。 
#  int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 
#  int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 
#  int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。 
#  
# 
#  请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说： 
# 
#  
#  将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。 
#  从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", 
# "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# 输出：
# [null, null, null, null, null, 1, 3, 4, 2, -1]
# 
# 解释：
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // 返回 1 -> [4, 3, 2]
# q.popMiddle();    // 返回 3 -> [4, 2]
# q.popMiddle();    // 返回 4 -> [2]
# q.popBack();      // 返回 2 -> []
# q.popFront();     // 返回 -1 -> [] （队列为空）
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= val <= 10⁹ 
#  最多调用 1000 次 pushFront， pushMiddle， pushBack， popFront， popMiddle 和 popBack 。 
# 
#  
# 
#  Related Topics 设计 队列 数组 链表 数据流 👍 41 👎 0
