"""

给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
----

双指针 ，主要是要分奇偶数

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in range(n): # 遍历回文中心点
            for j in range(2): # j =0， 中心点是一个点，j=1 中心点是两个点
                l = i
                r = i+j
                while l >= 0 and r<n and  s[l] == s[r]:
                    ret +=1
                    l -=1
                    r += 1
        return ret

s = Solution()
a=s.countSubstrings("abc")
print(a)