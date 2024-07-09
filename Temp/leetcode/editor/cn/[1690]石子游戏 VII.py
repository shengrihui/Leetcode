# 1690 石子游戏 VII
# https://leetcode.cn/problems/stone-game-vii/

# leetcode submit region begin(Prohibit modification and deletion)

# 设爱丽丝的得分为 A，鲍勃的得分为 B
# 爱丽丝要最大化 A-B，鲍勃要最小化 A-B，也就是最大化 B-A，
# 两个人都是要最大化「自己得分 - 对方得分」，
# 或者说是最大化这一轮先手得分 - 后手得分。
#
# 定义 dfs(i,j) 表示现在剩余石子序列为 si到sj 的情况最后的得分
# 枚举先手的选择 s[i] 和 s[j]
# 假设选择 s[j]，这一轮爱丽丝先手
# 爱丽丝的最终得分 A，这一轮得分为 a=pre_sum[j]-pre_sum[i]，鲍勃最终得分 B，dfs(i,j)=A-B
# 现在剩余石子为 si到sj-1，鲍勃先手了
# 鲍勃往后全部得分为 B'，爱丽丝往后全部得分A',
# A=A'+a,B=B',dfs(i,j-1)=B'-A'
# dfe(i,j)=A-B=(a+A')-B'=a-(B'-A')=a-dfs(i,j-1)
# 再另一种情况取最大值
# 所以，dfs(i,j)=max(pre_sum[j]-pre_sum[i]-dfs(i,j-1) , pre_sum[j+1]-pre_sum[i+1]-dfs(i+1,j))
# 边界： dfs(i,i)=0


# 记忆化搜索
"""
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        pre_sum = list(accumulate(stones, initial=0))
        @cache
        def dfs(i: int, j: int) -> int:
            if i == j: return 0
            return max(pre_sum[j] - pre_sum[i] - dfs(i, j - 1), pre_sum[j + 1] - pre_sum[i + 1] - dfs(i + 1, j))
        ans = dfs(0, len(stones) - 1)
        dfs.cache_clear()  # 防止爆内存
        return ans
"""


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        pre_sum = list(accumulate(stones, initial=0))
        # dp = [[0] * n for _ in range(n)]
        dp = [0] * n
        for i in range(n - 2, -1, -1):  # i=n-1 的时候只有 dp[n-1][n-1] 有值 =0
            for j in range(i + 1, n):
                # dp[i][j] = max(pre_sum[j] - pre_sum[i] - dp[i][j - 1], pre_sum[j + 1] - pre_sum[i + 1] - dp[i + 1][j])
                dp[j] = max(pre_sum[j] - pre_sum[i] - dp[j - 1], pre_sum[j + 1] - pre_sum[i + 1] - dp[j])
        # return dp[0][-1]
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
