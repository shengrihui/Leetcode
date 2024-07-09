# 2129 将标题首字母大写
# https://leetcode.cn/problems/capitalize-the-title/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # ans = []
        # for word in title.split():
        #     if len(word) <= 2:
        #         ans.append(word.lower())
        #     else:
        #         ans.append(word[0].upper() + word[1:].lower())
        # return " ".join(ans)
        return " ".join(
            [word[0].upper() + word[1:].lower() if len(word) > 2 else word.lower() for word in title.split()])
# leetcode submit region end(Prohibit modification and deletion)
