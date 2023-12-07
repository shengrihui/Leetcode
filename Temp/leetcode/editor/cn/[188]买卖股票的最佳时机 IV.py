# 188 买卖股票的最佳时机 IV
import heapq
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)


class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.length = high - low
        self.merge2next = self.merge2prev = self.length
        self.mn = self.length
        self.option = 0  # 1：向前合并，2：向后合并，初始设为0但不会是0，因为总会让他向前或者向后
        self.next = self.prev = None

    def update(self):
        self.length = self.high - self.low
        self.merge2next = self.merge2prev = self.length
        x2, y2 = self.low, self.high
        if self.prev:
            x1, y1 = self.prev.low, self.prev.high
            if x1 <= y1 <= x2 <= y2:
                self.merge2prev = 0
            elif x1 <= x2 <= y1 <= y2:
                self.merge2prev = y1 - x2
        if self.next:
            x3, y3 = self.next.low, self.next.high
            if x2 <= y2 <= x3 <= y3:
                self.merge2next = 0
            elif x2 <= x3 <= y2 <= y3:
                self.merge2next = y2 - x3
        # 如果向前合并和向后合并一样，那就如果前面有就向前合并，前面没有就向后合并
        if self.merge2prev <= self.merge2next and self.prev:
            self.mn, self.option = self.merge2prev, 1
        elif self.merge2prev >= self.merge2next and self.next:
            self.mn, self.option = self.merge2next, 2

    def __lt__(self, other):
        return self.mn < other.mn

    def delete(self):
        p = self.prev
        n = self.next
        if self.option == 1:
            p.high = max(self.high, p.high)
            # 不能直接 p.low = min(self.low, p.low)，因为当前这个是要被删除的，
            # 如果前一个的low比当前的大，合并之后的的high只能还是前一个的high
            # 下同
            p.low = min(self.low, p.low) if p.high == self.high else p.low
            p.next = n
            if n:
                n.prev = p
                n.update()
            p.update()
        elif self.option == 2:
            n.low = min(self.low, n.low)
            n.high = max(self.high, n.high) if n.low == self.low else n.high
            n.prev = p
            if p:
                p.next = n
                p.update()
            n.update()


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        is_increase = False  # 是否在增长区间
        a = []
        # high = low = 0
        for i in range(1, n):
            x, y = prices[i - 1], prices[i]
            if y > x:
                ans += y - x
                if not is_increase:  # x是最低点。当前不是在增长，那x是最低点，从x开始增长
                    is_increase = True
                    low = x
                if i == n - 1:
                    a.append(Interval(low, y))
            else:
                if is_increase:  # x是最高点
                    is_increase = False
                    a.append(Interval(low, x))

        cnt = len(a)
        if cnt == 0:  # 没有一个增长区间，返回0
            return ans

        for i in range(cnt):
            a[i].next = a[i + 1] if i < cnt - 1 else None
            a[i].prev = a[i - 1] if i > 0 else None
            a[i].update()

        heapq.heapify(a)

        while cnt > k:
            interval = heapq.heappop(a)
            mn = interval.mn
            ans -= mn
            interval.delete()
            heapq.heapify(a)
            cnt -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.maxProfit(k=1, prices=[1, 3, 5, 0, 6, 7, 0, 9, 10]))

# print(s.maxProfit(k=2, prices=[3, 3, 5, 0, 0, 3, 1, 4]))

# print(s.maxProfit(k=1, prices=[6, 1, 6, 4, 3, 0, 2]))

# print(17, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9])
# print(s.maxProfit(k=2, prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))

# print([5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0])
# print(s.maxProfit(k=2, prices=[5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]))

ex = [70, 4, 83, 56, 94, 72, 78, 43, 2, 86, 65, 100, 94, 56, 41, 66, 3, 33, 10, 3, 45, 94, 15, 12, 78, 60, 58, 0, 58,
      15, 21, 7, 11, 41, 12, 96, 83, 77, 47, 62, 27, 19, 40, 63, 30, 4, 77, 52, 17, 57, 21, 66, 63, 29, 51, 40, 37, 6,
      44, 42, 92, 16, 64, 33, 31, 51, 36, 0, 29, 95, 92, 35, 66, 91, 19, 21, 100, 95, 40, 61, 15, 83, 31, 55, 59, 84,
      21, 99, 45, 64, 90, 25, 40, 6, 41, 5, 25, 52, 59, 61, 51, 37, 92, 90, 20, 20, 96, 66, 79, 28, 83, 60, 91, 30, 52,
      55, 1, 99, 8, 68, 14, 84, 59, 5, 34, 93, 25, 10, 93, 21, 35, 66, 88, 20, 97, 25, 63, 80, 20, 86, 33, 53, 43, 86,
      53, 55, 61, 77, 9, 2, 56, 78, 43, 19, 68, 69, 49, 1, 6, 5, 82, 46, 24, 33, 85, 24, 56, 51, 45, 100, 94, 26, 15,
      33, 35, 59, 25, 65, 32, 26, 93, 73, 0, 40, 92, 56, 76, 18, 2, 45, 64, 66, 64, 39, 77, 1, 55, 90, 10, 27, 85, 40,
      95, 78, 39, 40, 62, 30, 12, 57, 84, 95, 86, 57, 41, 52, 77, 17, 9, 15, 33, 17, 68, 63, 59, 40, 5, 63, 30, 86, 57,
      5, 55, 47, 0, 92, 95, 100, 25, 79, 84, 93, 83, 93, 18, 20, 32, 63, 65, 56, 68, 7, 31, 100, 88, 93, 11, 43, 20, 13,
      54, 34, 29, 90, 50, 24, 13, 44, 89, 57, 65, 95, 58, 32, 67, 38, 2, 41, 4, 63, 56, 88, 39, 57, 10, 1, 97, 98, 25,
      45, 96, 35, 22, 0, 37, 74, 98, 14, 37, 77, 54, 40, 17, 9, 28, 83, 13, 92, 3, 8, 60, 52, 64, 8, 87, 77, 96, 70, 61,
      3, 96, 83, 56, 5, 99, 81, 94, 3, 38, 91, 55, 83, 15, 30, 39, 54, 79, 55, 86, 85, 32, 27, 20, 74, 91, 99, 100, 46,
      69, 77, 34, 97, 0, 50, 51, 21, 12, 3, 84, 84, 48, 69, 94, 28, 64, 36, 70, 34, 70, 11, 89, 58, 6, 90, 86, 4, 97,
      63, 10, 37, 48, 68, 30, 29, 53, 4, 91, 7, 56, 63, 22, 93, 69, 93, 1, 85, 11, 20, 41, 36, 66, 67, 57, 76, 85, 37,
      80, 99, 63, 23, 71, 11, 73, 41, 48, 54, 61, 49, 91, 97, 60, 38, 99, 8, 17, 2, 5, 56, 3, 69, 90, 62, 75, 76, 55,
      71, 83, 34, 2, 36, 56, 40, 15, 62, 39, 78, 7, 37, 58, 22, 64, 59, 80, 16, 2, 34, 83, 43, 40, 39, 38, 35, 89, 72,
      56, 77, 78, 14, 45, 0, 57, 32, 82, 93, 96, 3, 51, 27, 36, 38, 1, 19, 66, 98, 93, 91, 18, 95, 93, 39, 12, 40, 73,
      100, 17, 72, 93, 25, 35, 45, 91, 78, 13, 97, 56, 40, 69, 86, 69, 99, 4, 36, 36, 82, 35, 52, 12, 46, 74, 57, 65,
      91, 51, 41, 42, 17, 78, 49, 75, 9, 23, 65, 44, 47, 93, 84, 70, 19, 22, 57, 27, 84, 57, 85, 2, 61, 17, 90, 34, 49,
      74, 64, 46, 61, 0, 28, 57, 78, 75, 31, 27, 24, 10, 93, 34, 19, 75, 53, 17, 26, 2, 41, 89, 79, 37, 14, 93, 55, 74,
      11, 77, 60, 61, 2, 68, 0, 15, 12, 47, 12, 48, 57, 73, 17, 18, 11, 83, 38, 5, 36, 53, 94, 40, 48, 81, 53, 32, 53,
      12, 21, 90, 100, 32, 29, 94, 92, 83, 80, 36, 73, 59, 61, 43, 100, 36, 71, 89, 9, 24, 56, 7, 48, 34, 58, 0, 43, 34,
      18, 1, 29, 97, 70, 92, 88, 0, 48, 51, 53, 0, 50, 21, 91, 23, 34, 49, 19, 17, 9, 23, 43, 87, 72, 39, 17, 17, 97,
      14, 29, 4, 10, 84, 10, 33, 100, 86, 43, 20, 22, 58, 90, 70, 48, 23, 75, 4, 66, 97, 95, 1, 80, 24, 43, 97, 15, 38,
      53, 55, 86, 63, 40, 7, 26, 60, 95, 12, 98, 15, 95, 71, 86, 46, 33, 68, 32, 86, 89, 18, 88, 97, 32, 42, 5, 57, 13,
      1, 23, 34, 37, 13, 65, 13, 47, 55, 85, 37, 57, 14, 89, 94, 57, 13, 6, 98, 47, 52, 51, 19, 99, 42, 1, 19, 74, 60,
      8, 48, 28, 65, 6, 12, 57, 49, 27, 95, 1, 2, 10, 25, 49, 68, 57, 32, 99, 24, 19, 25, 32, 89, 88, 73, 96, 57, 14,
      65, 34, 8, 82, 9, 94, 91, 19, 53, 61, 70, 54, 4, 66, 26, 8, 63, 62, 9, 20, 42, 17, 52, 97, 51, 53, 19, 48, 76, 40,
      80, 6, 1, 89, 52, 70, 38, 95, 62, 24, 88, 64, 42, 61, 6, 50, 91, 87, 69, 13, 58, 43, 98, 19, 94, 65, 56, 72, 20,
      72, 92, 85, 58, 46, 67, 2, 23, 88, 58, 25, 88, 18, 92, 46, 15, 18, 37, 9, 90, 2, 38, 0, 16, 86, 44, 69, 71, 70,
      30, 38, 17, 69, 69, 80, 73, 79, 56, 17, 95, 12, 37, 43, 5, 5, 6, 42, 16, 44, 22, 62, 37, 86, 8, 51, 73, 46, 44,
      15, 98, 54, 22, 47, 28, 11, 75, 52, 49, 38, 84, 55, 3, 69, 100, 54, 66, 6, 23, 98, 22, 99, 21, 74, 75, 33, 67, 8,
      80, 90, 23, 46, 93, 69, 85, 46, 87, 76, 93, 38, 77, 37, 72, 35, 3, 82, 11, 67, 46, 53, 29, 60, 33, 12, 62, 23, 27,
      72, 35, 63, 68, 14, 35, 27, 98, 94, 65, 3, 13, 48, 83, 27, 84, 86, 49, 31, 63, 40, 12, 34, 79, 61, 47, 29, 33, 52,
      100, 85, 38, 24, 1, 16, 62, 89, 36, 74, 9, 49, 62, 89]
print(s.maxProfit(k=29, prices=ex))

"""
2
[2,4,1]
2
[3,2,6,5,0,3]
2
[3,3,5,0,0,3,1,4]
1
[6,1,6,4,3,0,2]
2
[1,2,4,2,5,7,2,4,9,0,9]
2
[5,2,3,2,6,6,2,9,1,0,7,4,5,0]
2
[1,9,6,9,1,7,1,1,5,9,9,9]
29
[70,4,83,56,94,72,78,43,2,86,65,100,94,56,41,66,3,33,10,3,45,94,15,12,78,60,58,0,58,15,21,7,11,41,12,96,83,77,47,62,27,19,40,63,30,4,77,52,17,57,21,66,63,29,51,40,37,6,44,42,92,16,64,33,31,51,36,0,29,95,92,35,66,91,19,21,100,95,40,61,15,83,31,55,59,84,21,99,45,64,90,25,40,6,41,5,25,52,59,61,51,37,92,90,20,20,96,66,79,28,83,60,91,30,52,55,1,99,8,68,14,84,59,5,34,93,25,10,93,21,35,66,88,20,97,25,63,80,20,86,33,53,43,86,53,55,61,77,9,2,56,78,43,19,68,69,49,1,6,5,82,46,24,33,85,24,56,51,45,100,94,26,15,33,35,59,25,65,32,26,93,73,0,40,92,56,76,18,2,45,64,66,64,39,77,1,55,90,10,27,85,40,95,78,39,40,62,30,12,57,84,95,86,57,41,52,77,17,9,15,33,17,68,63,59,40,5,63,30,86,57,5,55,47,0,92,95,100,25,79,84,93,83,93,18,20,32,63,65,56,68,7,31,100,88,93,11,43,20,13,54,34,29,90,50,24,13,44,89,57,65,95,58,32,67,38,2,41,4,63,56,88,39,57,10,1,97,98,25,45,96,35,22,0,37,74,98,14,37,77,54,40,17,9,28,83,13,92,3,8,60,52,64,8,87,77,96,70,61,3,96,83,56,5,99,81,94,3,38,91,55,83,15,30,39,54,79,55,86,85,32,27,20,74,91,99,100,46,69,77,34,97,0,50,51,21,12,3,84,84,48,69,94,28,64,36,70,34,70,11,89,58,6,90,86,4,97,63,10,37,48,68,30,29,53,4,91,7,56,63,22,93,69,93,1,85,11,20,41,36,66,67,57,76,85,37,80,99,63,23,71,11,73,41,48,54,61,49,91,97,60,38,99,8,17,2,5,56,3,69,90,62,75,76,55,71,83,34,2,36,56,40,15,62,39,78,7,37,58,22,64,59,80,16,2,34,83,43,40,39,38,35,89,72,56,77,78,14,45,0,57,32,82,93,96,3,51,27,36,38,1,19,66,98,93,91,18,95,93,39,12,40,73,100,17,72,93,25,35,45,91,78,13,97,56,40,69,86,69,99,4,36,36,82,35,52,12,46,74,57,65,91,51,41,42,17,78,49,75,9,23,65,44,47,93,84,70,19,22,57,27,84,57,85,2,61,17,90,34,49,74,64,46,61,0,28,57,78,75,31,27,24,10,93,34,19,75,53,17,26,2,41,89,79,37,14,93,55,74,11,77,60,61,2,68,0,15,12,47,12,48,57,73,17,18,11,83,38,5,36,53,94,40,48,81,53,32,53,12,21,90,100,32,29,94,92,83,80,36,73,59,61,43,100,36,71,89,9,24,56,7,48,34,58,0,43,34,18,1,29,97,70,92,88,0,48,51,53,0,50,21,91,23,34,49,19,17,9,23,43,87,72,39,17,17,97,14,29,4,10,84,10,33,100,86,43,20,22,58,90,70,48,23,75,4,66,97,95,1,80,24,43,97,15,38,53,55,86,63,40,7,26,60,95,12,98,15,95,71,86,46,33,68,32,86,89,18,88,97,32,42,5,57,13,1,23,34,37,13,65,13,47,55,85,37,57,14,89,94,57,13,6,98,47,52,51,19,99,42,1,19,74,60,8,48,28,65,6,12,57,49,27,95,1,2,10,25,49,68,57,32,99,24,19,25,32,89,88,73,96,57,14,65,34,8,82,9,94,91,19,53,61,70,54,4,66,26,8,63,62,9,20,42,17,52,97,51,53,19,48,76,40,80,6,1,89,52,70,38,95,62,24,88,64,42,61,6,50,91,87,69,13,58,43,98,19,94,65,56,72,20,72,92,85,58,46,67,2,23,88,58,25,88,18,92,46,15,18,37,9,90,2,38,0,16,86,44,69,71,70,30,38,17,69,69,80,73,79,56,17,95,12,37,43,5,5,6,42,16,44,22,62,37,86,8,51,73,46,44,15,98,54,22,47,28,11,75,52,49,38,84,55,3,69,100,54,66,6,23,98,22,99,21,74,75,33,67,8,80,90,23,46,93,69,85,46,87,76,93,38,77,37,72,35,3,82,11,67,46,53,29,60,33,12,62,23,27,72,35,63,68,14,35,27,98,94,65,3,13,48,83,27,84,86,49,31,63,40,12,34,79,61,47,29,33,52,100,85,38,24,1,16,62,89,36,74,9,49,62,89]
1
[1, 3, 5, 0, 6, 7, 0, 9, 10]


"""

# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。 
# 
#  示例 2： 
# 
#  
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 
# 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= 100 
#  1 <= prices.length <= 1000 
#  0 <= prices[i] <= 1000 
#  
# 
#  Related Topics 数组 动态规划 👍 1059 👎 0
