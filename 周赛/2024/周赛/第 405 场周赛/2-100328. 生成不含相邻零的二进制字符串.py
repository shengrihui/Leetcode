# 第 405 场周赛 第 2 题
# 题目：100328. 生成不含相邻零的二进制字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-405/problems/generate-binary-strings-without-adjacent-zeros/
# 题库：https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros

from typing import List


# 回溯
class Solution:
    def validStrings(self, n: int) -> List[str]:
        def dfs():
            if len(path) == n:
                ans.append("".join(path))
                return
            for c in "01":
                if path[-1] == "0" and c == "0":
                    continue
                path.append(c)
                dfs()
                path.pop()

        ans = []
        path = ["1"]
        dfs()
        path = ["0"]
        dfs()
        return ans


# 二进制（不如回溯快）
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        mask = (1 << n) - 1
        for i in range(1 << n):
            x = mask ^ i  # 和 n 个 1 异或得到 i 取反并且长度为 n 的结果
            if x & (x >> 1) == 0:
                ans.append(f"{i:0{n}b}")
        return ans


s = Solution()
examples = [
    (dict(n=3), ["010", "011", "101", "110", "111"]),
    (dict(n=1), ["0", "1"]),
]
for e, a in examples:
    print(a, e)
    print(s.validStrings(**e))
