# 1094 拼车
from typing import List, Optional
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a = [0] * 1001
        for n, f, t in trips:
            a[f] += n
            a[t] -= n
        if a[0] > capacity:
            return False
        for i in range(1, 1001):
            a[i] += a[i - 1]
            if a[i] > capacity:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)


# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向） 
# 
#  给定整数 capacity 和一个数组 trips , trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有
#  numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。 
# 
#  当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
#  
# 
#  示例 2： 
# 
#  
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= trips.length <= 1000 
#  trips[i].length == 3 
#  1 <= numPassengersi <= 100 
#  0 <= fromi < toi <= 1000 
#  1 <= capacity <= 10⁵ 
#  
# 
#  Related Topics 数组 前缀和 排序 模拟 堆（优先队列） 👍 309 👎 0
