"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
strs = ["flower","flow","flight"]
这题思路主要是外层是最短的
只要有不符合的，马上退出
"""

def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    m = min(len(i) for i in strs)
    for i in range(m):
        for j in range(len(strs)):
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]
    return strs[0][:m]
