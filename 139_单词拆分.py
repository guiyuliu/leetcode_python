"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
动态规划题，双层循环

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for j in range(1, len(s)+1):
            for i in range(0,j):
                # dp[j] = dp[i] & check(s[i:j])
                    if  dp[i] and  (s[i:j] in wordDict):
                        dp[j] = True
                        break
        return dp[len(s)]