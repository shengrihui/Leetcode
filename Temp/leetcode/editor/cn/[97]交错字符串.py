# 97 交错字符串
# https://leetcode.cn/problems/interleaving-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i: int, j: int) -> bool:
            if i >= n1  and j >= n2 :
                return True
            if i < n1 and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < n2 and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            return False

        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        return dfs(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.isInterleave("a", "", "c"))
