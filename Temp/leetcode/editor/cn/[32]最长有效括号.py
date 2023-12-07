# 32 最长有效括号


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        t = 0
        n = len(s)
        dp = [0] * (n + 1)  # dp[i]：以i结尾的这一串合法的括号个数
        for i, c in enumerate(s):
            # 没提到的情况，dp[i+1]都是默认0
            if c == "(":
                t += 1
            else:
                if t > 0:
                    t -= 1
                    dp[i + 1] = dp[i] + 1
                    dp[i + 1] += dp[i + 1 - 2 * dp[i + 1]]  # 这一串的闭合个数加上紧挨着上一个的闭合个数（如果有）
        return max(dp) * 2


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]  # Initialize stack with -1 to handle edge case

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()  # 弹出栈顶的 (
                if len(stack) == 0:  # 如果这个时候栈空了，出现在第一个就是) ,然后上一行给弹出了
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])  # C++里是stack.top()

        return maxans

# leetcode submit region end(Prohibit modification and deletion)


# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] 为 '(' 或 ')' 
#  
# 
#  Related Topics 栈 字符串 动态规划 👍 2381 👎 0
