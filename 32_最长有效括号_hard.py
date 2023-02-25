"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

# 动态规划
# 有效的子串一定以')' 结尾， 以'（'结尾的自传对应的dp值必定为0，
# 只需要求解右括号 在dp数组中对应位置的值
# 当i-1 = “(” 时， dp[i-1] 无效，或者说为0， 此时 dp[i] = dp[i-1]+2
# i-1 = ")"时，以 i-1结束的子串长度为dp[i-1], 那么这个子串前面必须为“(” 才能保证成立,因此可以加上2
# 此时 dp[i]= dp[i-1] + dp[i-dp[i-1]-2] +2 
# 以上两种情况可以合并，因为当i-1 = “(” 时 dp[i-1]为0
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0]*n
        for i in range(n):
            if s[i] == ")"  and  i -dp[i-1] -1 >= 0 and s[i-dp[i-1]-1] == "(":
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] +2 
        return max(dp)
