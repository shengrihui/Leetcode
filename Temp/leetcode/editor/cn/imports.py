from typing import Optional, List
from itertools import *
from collections import *
from functools import *
from math import inf
import heapq
from bisect import *
import bisect

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
