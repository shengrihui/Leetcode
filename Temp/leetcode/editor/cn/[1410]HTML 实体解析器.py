# 1410 HTML 实体解析器


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace("&quot;", "\"").replace("&apos;", "'").replace("&gt;", ">").replace(
            "&lt;", "<").replace("&frasl;", "/").replace("&amp;", "&")

# leetcode submit region end(Prohibit modification and deletion)
