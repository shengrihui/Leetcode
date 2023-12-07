from typing import Optional, List
from collections import defaultdict, deque
from itertools import *
from functools import *
from math import inf
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
