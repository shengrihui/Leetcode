# 2591 将钱分给最多的儿童


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:  # 没有任何方案
            return -1
        money -= children  # 每人都分1
        eight = money // 7  # 可以分到8美元的
        if eight > children or eight == children and money % 7:  # 每个人都能分到8美元后还有多都给一个人
            return children - 1
        if money % 7 == 3 and children - eight == 1:  # 只有一个人分到4美元
            return eight - 1
        return eight
    # leetcode submit region end(Prohibit modification and deletion)

# 给你一个整数 money ，表示你总共有的钱数（单位为美元）和另一个整数 children ，表示你要将钱分配给多少个儿童。
# 
#  你需要按照如下规则分配： 
# 
#  
#  所有的钱都必须被分配。 
#  每个儿童至少获得 1 美元。 
#  没有人获得 4 美元。 
#  
# 
#  请你按照上述规则分配金钱，并返回 最多 有多少个儿童获得 恰好 8 美元。如果没有任何分配方案，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：money = 20, children = 3
# 输出：1
# 解释：
# 最多获得 8 美元的儿童数为 1 。一种分配方案为：
# - 给第一个儿童分配 8 美元。
# - 给第二个儿童分配 9 美元。
# - 给第三个儿童分配 3 美元。
# 没有分配方案能让获得 8 美元的儿童数超过 1 。
#  
# 
#  示例 2： 
# 
#  输入：money = 16, children = 2
# 输出：2
# 解释：每个儿童都可以获得 8 美元。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= money <= 200 
#  2 <= children <= 30 
#  
# 
#  Related Topics 贪心 数学 👍 24 👎 0
