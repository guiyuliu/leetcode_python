"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
链接：https://leetcode.cn/problems/unique-paths
本题主要是依靠初始化, 上边和左边一条边只能有一种路径到达的方法

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0]*n for _ in range(m)]
        for i in range(0,m): # 初始化，
            d[i][0] = 1
        for j in range(0,n):# 初始化，两条边
            d[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]
