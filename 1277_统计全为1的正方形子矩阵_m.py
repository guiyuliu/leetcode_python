"""
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

# 该题跟221题，统计边长最大的正方形思路一致，221题 dp 矩阵中装的是能取得的最大的边长X
# x也是里面正方形的个数(1,2,3,4), 211题目是返回最大的x，本题将x累加即可
# 至于动态规划的公式 dp[i][j]， 是以ij为右下角的最大正方形，这题画个图能明白递推公式，记下来即可
也就是dp[i][j] = min(dp[i][j-1], dp[i-1][j],dp[i-1][j-1])+1
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp =  [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j],dp[i-1][j-1])+1
                ans += dp[i][j]
        return ans
