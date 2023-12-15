# 117 填充每个节点的下一个右侧节点指针 II

# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root  # head指向下一层第一个
        while head:
            p = head  # p在当前层
            head = prev = None  # head,prev指在下一层
            while p:  # 遍历当前层
                for cur in [p.left, p.right]:
                    if cur:
                        if not head:  # 下一层的头还没有
                            head = cur
                            prev = head
                            continue
                        prev.next = cur
                        prev = cur
                p = p.next  # p 这个层已经是链表了
        return root

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         cur = root
#         while cur:
#             nxt = dummy = ListNode()  # 下一层的链表
#             while cur:  # 遍历当前层的链表
#                 for p in [cur.left,cur.right]:
#                     if p:
#                         nxt.next = p  # 下一层的相邻节点连起来
#                         nxt = p
#                 cur = cur.next  # 当前层链表的下一个节点
#             cur = dummy.next  # 下一层链表的头节点
#         return root

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/solutions/2510360/san-chong-fang-fa-dfsbfsbfslian-biao-fu-1bmqp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# leetcode submit region end(Prohibit modification and deletion)
