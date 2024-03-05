# 232 用栈实现队列
# https://leetcode.cn/problems/implement-queue-using-stacks/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        self._inStack = []
        self._outStack = []

    def _in2out(self):
        # 输入栈的元素去输出栈，输出栈空的时候用
        while self._inStack:
            self._outStack.append(self._inStack.pop())

    def push(self, x: int) -> None:
        self._inStack.append(x)

    def pop(self) -> int:
        if not self._outStack:
            self._in2out()
        return self._outStack.pop()

    def peek(self) -> int:
        if not self._outStack:
            self._in2out()
        return self._outStack[-1]

    def empty(self) -> bool:
        # 两个都为空返回 True
        return not self._inStack and not self._outStack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
