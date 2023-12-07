# 520 检测大写字母


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        a = [c.isupper() for c in word]
        return all(a) or not any(a) or a[0] and not any(a[1:])
# leetcode submit region end(Prohibit modification and deletion)
