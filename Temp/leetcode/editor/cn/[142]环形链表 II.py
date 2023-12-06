# 142 环形链表 II
from typing import List, Optional
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 设 head 到环的入口是 a，
        # 入口到相遇点长度是 b，
        # 相遇点到入口是 c，
        # 环长度 b+c
        # 快指针走的是慢指针的两倍，2(a+b)=a+b+k(b+c)
        # 2(a+b)=a+b+b+c+(k-1)(b+c)
        # a-c=(k-1)(b+c)
        # 这意味着，让慢指针和 head 都走 c 步，慢指针到了环的入口，之后两个一起走
        # 一定会相遇，相遇点就是环入口
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None
# leetcode submit region end(Prohibit modification and deletion)


# 给定一个链表的头节点 head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到
# 链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。 
# 
#  不允许修改 链表。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围在范围 [0, 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  pos 的值为 -1 或者链表中的一个有效索引 
#  
# 
#  
# 
#  进阶：你是否可以使用 O(1) 空间解决此题？ 
# 
#  Related Topics 哈希表 链表 双指针 👍 2402 👎 0
