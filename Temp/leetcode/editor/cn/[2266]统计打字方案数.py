# 2266 统计打字方案数
# https://leetcode.cn/problems/count-number-of-texts/

# leetcode submit region begin(Prohibit modification and deletion)
MOD = 10 ** 9 + 7
a = [0, 1, 2, 4]
b = [0, 1, 2, 4, 8]
for i in range(10 ** 5 - 3):
    a.append((a[- 1] + a[- 2] + a[- 3]) % MOD)
    b.append((b[- 1] + b[- 2] + b[- 3] + b[- 4]) % MOD)


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        res = 1
        i = 0
        while i < n:
            st = i
            while i < n and pressedKeys[i] == pressedKeys[st]:
                i += 1
            k = pressedKeys[st]
            res = (res * (b[i - st] if k in "79" else a[i - st])) % MOD
        return res

# leetcode submit region end(Prohibit modification and deletion)
