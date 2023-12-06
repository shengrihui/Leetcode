from typing import List
from collections import *
from itertools import *

# 题目：# 2数树数
# 题目链接：https://www.lanqiao.cn/problems/5128/learning/?contest_id=144

n, q = map(int, input().split())
for _ in range(q):
    s = input()
    p = len(s)  # 层数
    l, r = 1, 2 ** p
    for pp in s:
        if pp == "R":
            l = (l + r) // 2 + 1
        elif pp == "L":
            r = (l + r) // 2
    print(l)
"""
3 6
R
L
LL
LR
RL
RR
"""
