# 225 用队列实现栈
# https://leetcode.cn/problems/implement-stack-using-queues/


# leetcode submit region begin(Prohibit modification and deletion)
from queue import Queue


class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        tmp = Queue()
        while True:
            x = self.q.get()
            # print(x,self.q.queue)
            if not self.q.empty():
                tmp.put(x)
            else:
                break
        self.q = tmp
        return x

    def top(self) -> int:
        return self.q.queue[-1]

    def empty(self) -> bool:
        return self.q.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
