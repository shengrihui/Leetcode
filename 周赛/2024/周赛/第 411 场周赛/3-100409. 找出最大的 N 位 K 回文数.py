# 第 411 场周赛 第 3 题
# 题目：100409. 找出最大的 N 位 K 回文数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-411/problems/find-the-largest-palindrome-divisible-by-k/
# 题库：https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        # 预处理
        # pow10[i] = (10 ^ i) % k
        # pow[i] = pow[i-1] * 10
        # pow10[i] = pow10[i-1] * 10 % k
        pow10 = [1] * n
        for i in range(1, n):
            pow10[i] = pow10[i - 1] * 10 % k

        # 一共 n 位，最右边第 0 位，最左边第 n-1 位
        # m 是过了一半的位置，奇数偶数统一起来就是 (n+1)//2
        m = (n + 1) // 2
        ans = [None] * n

        # 填了数字之后第 i 位对 k 取模的结果是 j
        # 填完了如果 j 是 0 说明找到了一个可行答案
        # 一个图的问题：从 (0,0) 能否到 (m,0)，并记录一路上填的数字，
        # 填的时候倒序保证最大
        vis = [[True] * k for _ in range(m + 1)]  # vis[i][j] 能否到 (m,0)，先假设能到

        def dfs(i: int, j: int) -> bool:
            if i == m:
                return j == 0
            for d in range(9, -1, -1):
                # 计算 i 和镜像位 n-1-i 填 d 后的 j
                if n % 2 and i == m - 1:  # 奇数个的正中间
                    j2 = (j + d * pow10[i]) % k
                else:
                    j2 = (j + d * pow10[i] + d * pow10[n - i - 1]) % k
                if vis[i + 1][j2] and dfs(i + 1, j2):
                    ans[i] = ans[n - i - 1] = str(d)
                    return True
            vis[i][j] = False  # (i,j) 到不了 (m,0)
            return False

        dfs(0, 0)
        return "".join(ans)


s = Solution()
examples = [
    (dict(n=3, k=5), "595"),
    (dict(n=1, k=4), "8"),
    (dict(n=5, k=6), "89898"),
]
for e, a in examples:
    print(a, e)
    print(s.largestPalindrome(**e))
