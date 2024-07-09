# 116 填充每个节点的下一个右侧节点指针
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
                p = p.next
        return root
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     if not root:
    #         return None
    #     q = deque([root])
    #     while q:
    #         m = len(q)
    #         for i in range(m):
    #             node = q.popleft()
    #             if i < m - 1:
    #                 node.next = q[0]
    #             if node.left: q.append(node.left)
    #             if node.right: q.append(node.right)
    #     return root
# leetcode submit region end(Prohibit modification and deletion)
