# 2652 倍数求和


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)
        # m = n//3
        # 3+6+...+3m=m(3+3m)//2=3m(1+m)//2
        # s = 0
        # for x in [3, 5, 7, 105]:
        #     m = n // x
        #     s += x * m * (1 + m) // 2
        # for x in [15, 21, 35]:
        #     m = n // x
        #     s -= x * m * (1 + m) // 2
        # return s
        return sum((-1) ** i * x * (n // x) * (1 + n // x) // 2 for i, x in enumerate([3, 15, 5, 35, 7, 21, 105]))
# leetcode submit region end(Prohibit modification and deletion)


# 给你一个正整数 n ，请你计算在 [1，n] 范围内能被 3、5、7 整除的所有整数之和。 
# 
#  返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 7
# 输出：21
# 解释：在 [1, 7] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7 。数字之和为 21 。
#  
# 
#  示例 2： 
# 
#  输入：n = 10
# 输出：40
# 解释：在 [1, 10] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9、10 。数字之和为 40 。
#  
# 
#  示例 3： 
# 
#  输入：n = 9
# 输出：30
# 解释：在 [1, 9] 范围内能被 3、5、7 整除的所有整数分别是 3、5、6、7、9 。数字之和为 30 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10³ 
#  
# 
#  Related Topics 数学 👍 10 👎 0
