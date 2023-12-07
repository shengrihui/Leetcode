# 901 股票价格跨度


# leetcode submit region begin(Prohibit modification and deletion)
class StockSpanner:

    def __init__(self):
        self.st = [(123456, -1)]
        self.day = 0

    def next(self, price: int) -> int:
        while price >= self.st[-1][0]:
            self.st.pop()
        ret = self.day - self.st[-1][-1]
        self.st.append((price, self.day))
        self.day += 1
        return ret

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# leetcode submit region end(Prohibit modification and deletion)
