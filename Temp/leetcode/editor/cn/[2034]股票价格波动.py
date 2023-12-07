# 2034 股票价格波动

# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedList


class StockPrice:

    def __init__(self):
        self.timePrice = {}
        self.maxTime = 0
        self.price = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timePrice:  # 如果当前这个时间之前记录过，将之前的price删掉
            self.price.discard(self.timePrice[timestamp])
        self.timePrice[timestamp] = price
        self.price.add(price)
        if timestamp > self.maxTime:
            self.maxTime = timestamp

    def current(self) -> int:
        return self.timePrice[self.maxTime]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# leetcode submit region end(Prohibit modification and deletion)
