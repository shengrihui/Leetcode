# 2671 频率跟踪器
# https://leetcode.cn/problems/frequency-tracker/


# leetcode submit region begin(Prohibit modification and deletion)
class FrequencyTracker:

    def __init__(self):
        self.cnt = Counter()
        self.freq_cnt = Counter()

    def add(self, number: int) -> None:
        self.freq_cnt[self.cnt[number]] -= 1
        self.cnt[number] += 1
        self.freq_cnt[self.cnt[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.cnt[number] == 0:
            return
        self.freq_cnt[self.cnt[number]] -= 1
        self.cnt[number] -= 1
        self.freq_cnt[self.cnt[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_cnt[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
# leetcode submit region end(Prohibit modification and deletion)
