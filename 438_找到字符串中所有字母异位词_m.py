"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）、
    # 滑窗，
    # 创造数组来存储字符串和其中每种字符的数量
    # 对比滑窗的数量和字符的数量是否一致

"""

from typing import  List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):  #
            # 这下面两行就是为了框内的统计数量
            s_count[ord(s[i]) - 97] -= 1  # 前一个已经移除去了， 所以后面是添加i+1 而不是i
            s_count[ord(s[i + p_len]) - 97] += 1  # 后一个添加上

            if s_count == p_count:
                ans.append(i + 1)

        return ans
s = Solution()
long = "cbaebabacd"
sub = "abc"
a = s.findAnagrams(long, sub)
print(a)

