# LCP 24 数字游戏
# https://leetcode.cn/problems/5TxKeK/


# leetcode submit region begin(Prohibit modification and deletion)
# # 转换
# 将 nums 中的5个数 x0,x1,x2,x3,x4 变成 a0,a0+1,a0+2,a0+3,a0+4
# 操作次数即为 |x0-a0| + |x1-(a0+1)| + |x2-(a0+2)| + |x3-(a0+3)| + |x4-(a0+4)| 
# = |x0-a0| + |(x1-1)-a0| + |(x2-2)-a0| + |(x4-4)-a0| + |(x4-4)-a0|
# 记 bi = xi - i
# 问题转换为：
# 将 b 数组的数都变为同一个数的最少操作次数。
#
# # 中位数谈心
# 将 b 数组的数都变为 中位数 的操作次数最少。
# 
# # 具体方法
# left right 分别维护前缀 nums[0..i] 中较小的一半和较大的一半
# left_sum right_sum 分别表示两个的和
# left 是大根堆，堆顶 left[0] 是最大的
# right 是小根堆，堆顶 right[0] 是最小的
# 遍历 nums，for i,b in enumerate(nums) 
# b -= i
# 当前缀数量是奇数时 i%2==0
# 此时 left 和 right 大小一样，
# 让 b 先入 left ，再将 left 弹出的入 right
# 此时中位数为 right[0]
# 操作次数 = right_sum - right[0] - left_sum
# 当前缀数量是偶数时 
# 此时 left 比 right 少一个数，（两个堆中的数的数量是奇数）
# 让 b 先入 right ，再将 right 弹出的入 left （这相当于 left 中元素多了一个）
# 操作次数 = right_sum - left_ sum


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        MOD = 1_000_000_007
        n = len(nums)
        left = []
        right = []
        ans = [0] * n
        left_sum = right_sum = 0
        for i, b in enumerate(nums):
            b -= i
            if i % 2 == 0:  # 前缀长度是奇数
                left_sum += b
                t = -heappushpop(left, -b)  # 将 b 入堆然后弹出堆顶
                left_sum -= t
                heappush(right, t)
                right_sum += t  # 入 right
                ans[i] = (right_sum - right[0] - left_sum) % MOD
            else:
                right_sum += b
                t = heappushpop(right, b)
                right_sum -= t
                heappush(left, -t)
                left_sum += t
                ans[i] = (right_sum - left_sum) % MOD
        return ans
# leetcode submit region end(Prohibit modification and deletion)
