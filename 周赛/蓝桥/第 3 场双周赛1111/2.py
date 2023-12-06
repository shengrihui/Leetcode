from typing import List
from collections import *
from itertools import *

# 题目：# 2
# 题目链接：

N = int(input())
ws = list(map(int, input().split()))
ans = 0
for w in ws:
    ans += min((w - w // 10) if w >= 500 else w,
               (w - 150) if w >= 1000 else w,
               (w - w // 20) if w != 1111 else 0
               )
print(ans)

"""
3
666 1200 1111
"""