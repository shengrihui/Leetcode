import heapq
from bisect import *
from collections import Counter, defaultdict, deque
from functools import *
from heapq import *
from itertools import *
from math import comb, gcd, inf, isqrt, lcm, sqrt
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    @cache
    def f(tree: Optional[TreeNode], L: Optional[List], a: List[int]) -> int:
        pass


    nums = [1, 2, 3]
    t = deque()
    t = Counter()
    t = defaultdict(int)
    s = list(accumulate(nums))
    b = bisect_left(nums, 3)
    b = bisect.bisect_left(nums, 3)
    heappush(nums, 3)
    b = heapq.heappop(nums)
    a = inf
    a = gcd(2, 3)
    a = comb(2, 3)
    a = lcm(2, 3)
    a = sqrt(9)
    a = isqrt(9)
