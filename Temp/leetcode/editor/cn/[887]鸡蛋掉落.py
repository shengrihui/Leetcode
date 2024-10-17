# 887 鸡蛋掉落
# https://leetcode.cn/problems/super-egg-drop/


# leetcode submit region begin(Prohibit modification and deletion)
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int, j: int) -> int:
    if i == 0 or j == 0:
        return 0
    return dfs(i - 1, j) + dfs(i - 1, j - 1) + 1

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        for i in count(1):  # 从 1 开始枚举 i
            if dfs(i, k) >= n:
                return i
# leetcode submit region end(Prohibit modification and deletion)
