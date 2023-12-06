from typing import List
from collections import *
from itertools import *

# 题目：# 奇怪的线段
# 题目链接：

n,q=map(int,input().split())
m=2*(10**5)+5
diff=[0]*m
for _ in range(n):
    l,r =map(int,input().split())
    diff[l]+=1
    diff[r+1]-=1
for i in range(1,m):
    diff[i]+=diff[i-1]

