"""
给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

 由于质因子 5的个数不会大于质因子 2 的个数（具体证明见方法二），我们可以仅考虑质因子 5的个数
 因此是[1,n]中5的个数 之和
 
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans
