# 117 填充每个节点的下一个右侧节点指针 II
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq

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
            p = head  # p在当前层走
            head = prev = None  # head,prev指在下一层
            while p:  # 遍历当前层
                for cur in [p.left, p.right]:
                    if cur:
                        if not head:  # 下一层的头还米有
                            head = cur
                            prev = head
                            continue
                        prev.next = cur
                        prev = cur
                p = p.next
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


# 给定一个二叉树： 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指
# 针连接），'#' 表示每层的末尾。 
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 6000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。 
#  
# 
#  
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 链表 二叉树 👍 785 👎 0
