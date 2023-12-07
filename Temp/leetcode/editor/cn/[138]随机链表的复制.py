# 138 随机链表的复制
from typing import Optional

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 哈希表
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if not head:
        #     return None
        # new_head = Node()
        # p, q = head, new_head
        # mp = dict()  # 原链表的节点与新链表的节点的对应关系
        # while p:
        #     q.val = p.val
        #     if p.next:
        #         q.next = Node()
        #     mp[p] = q
        #     p = p.next
        #     q = q.next
        # p, q = head, new_head
        # while p:
        #     q.random = mp.get(p.random, None)
        #     p = p.next
        #     q = q.next
        # return new_head
        dummy = Node()
        p, q = head, dummy
        mp = dict()
        while p:
            q.next = Node(val=p.val)
            mp[p] = q.next
            p, q = p.next, q.next
        p, q = head, dummy.next
        while p:
            q.random = mp.get(p.random, None)
            p, q = p.next, q.next
        return dummy.next
"""


# 原地
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # 将原链表的每一个都复制一份到它的后面
        # 原：1 2 3 4
        # 后：1 1 2 2 3 3 4 4
        p = head
        while p:
            n = Node(x=p.val, next=p.next)
            p.next = n
            p = n.next
        # 构建复制出来的节点的 random
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # 构造答案
        dummy = Node(-1)
        p = head
        q = dummy
        while p:
            q.next = p.next
            if p.next:
                p.next = p.next.next
            p = p.next
            q = q.next
        q.next = None
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
