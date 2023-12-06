# 2816 翻倍以链表形式表示的数字
from typing import List, Optional
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 递归
# class Solution:
#     def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:  # 递归边界，最后一位的后面，返回一个空的节点
#             return ListNode(0, None)
#         r = self.doubleIt(head.next)
#         # 如果低位有进位，则 c 是进位值
#         # 如果没有进位（返回的就是原本的下一个节点），进位 c 是 0
#         c = 0 if r == head.next else r.val
#         v = head.val * 2 + c
#         head.val = v % 10
#         carry = v // 10
#         return head if carry == 0 else ListNode(carry, head)

# 一次遍历
# 进位只会发生在 下一个数>4 的时候
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        p = head
        while p:
            p.val = (p.val * 2) % 10
            if p.next and p.next.val > 4:
                p.val += 1
            p = p.next
        return head
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个 非空 链表的头节点 head ，表示一个不含前导零的非负数整数。 
# 
#  将链表 翻倍 后，返回头节点 head 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,8,9]
# 输出：[3,7,8]
# 解释：上图中给出的链表，表示数字 189 。返回的链表表示数字 189 * 2 = 378 。 
# 
#  示例 2： 
#  
#  
# 输入：head = [9,9,9]
# 输出：[1,9,9,8]
# 解释：上图中给出的链表，表示数字 999 。返回的链表表示数字 999 * 2 = 1998 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [1, 10⁴] 内 
#  0 <= Node.val <= 9 
#  生成的输入满足：链表表示一个不含前导零的数字，除了数字 0 本身。 
#  
# 
#  Related Topics 栈 链表 数学 👍 14 👎 0
