"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
链接：https://leetcode.cn/problems/number-of-islands

# 典型dfs，每一块向四个方向染色，染完后直接退出，ret+=1

"""

class Solution(object):
    def numIslands(self, grid):
        ret = 0
        # dfs 输入
        def dfs(grid, i,j):
            #dfs 递归结束的条件
            if i < 0 or i >= len(grid) or j <0 or j >= len(grid[0]):
                return 
            if grid[i][j] == "0" or grid[i][j] == "2":
                return
            grid[i][j] = "2"
            dfs(grid,i, j+1)
            dfs(grid,i+1, j)
            dfs(grid,i-1,j)
            dfs(grid, i, j-1)

        # 如何统计岛屿的数量
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i,j)
                    ret +=1
        return ret
