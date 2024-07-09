# 216 组合总和 III
# https://leetcode.cn/problems/combination-sum-iii/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(i, left):
            if len(path) > k or left < 0 or i > 10:
                return
            if len(path) == k and left == 0:
                ans.append(path.copy())
                return
            # 不选
            dfs(i + 1, left)
            # 选
            path.append(i)
            dfs(i + 1, left - i)
            path.pop()

        path = []
        ans = []
        dfs(1, n)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
