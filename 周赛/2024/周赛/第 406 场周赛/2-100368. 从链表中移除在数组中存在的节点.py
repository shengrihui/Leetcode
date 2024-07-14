# 第 406 场周赛 第 2 题
# 题目：100368. 从链表中移除在数组中存在的节点
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-406/problems/delete-nodes-from-linked-list-present-in-array/
# 题库：https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array

from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummp = ListNode(next=head)
        p = dummp
        while p.next:
            if p.next.val in nums:
                p.next = p.next.next
            else:
                p = p.next
        return dummp.next


s = Solution()
examples = [
]
for e, a in examples:
    print(a, e)
    print(s.getSmallestString(**e))
