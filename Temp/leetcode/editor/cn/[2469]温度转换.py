# 2469 温度转换
# https://leetcode.cn/problems/convert-the-temperature/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertTemperature(self, 摄氏度: float) -> List[float]:
        return [摄氏度 + 273.15, 摄氏度 * 1.80 + 32.00]
# leetcode submit region end(Prohibit modification and deletion)
