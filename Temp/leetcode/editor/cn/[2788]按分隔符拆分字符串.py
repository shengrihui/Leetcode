# 2788 按分隔符拆分字符串
# https://leetcode.cn/problems/split-strings-by-separator/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # ans = []
        # for w in words:
        #     for n in w.split(separator):
        #         if n:
        #             ans.append(n)
        # return ans
        return [ww for w in words for ww in w.split(separator) if ww]

# leetcode submit region end(Prohibit modification and deletion)
