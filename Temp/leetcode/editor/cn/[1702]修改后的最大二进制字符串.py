# 1702 修改后的最大二进制字符串
# https://leetcode.cn/problems/maximum-binary-string-after-change/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        first0 = binary.find("0")  # 第一个 0 的位置
        z = binary.count("0")
        # if first0 == -1 or first0 == n - 1:  # 没有 0 或者 0 在最后一个
        #     return binary
        if z <= 1:
            return binary
        z = z - 1 + first0  # 答案 0 的位置
        ans = ["1"] * n
        ans[z] = "0"
        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)
