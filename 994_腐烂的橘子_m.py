"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
链接：https://leetcode.cn/problems/rotting-oranges

# 思路： 这种需要一圈一圈往外传播的一般用BFS解， 先找到起始所有腐烂的橘子，然后循环处理，
# 把新腐烂的橘子加入下一次循环的队列中， 当下一次循环的队列为空时，说明不能继续腐烂了， 
# 最后判断一下还有没有新鲜的橘子，如果有，就返回-1，否则返回分钟数
    
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = list()
        ans = 0
        time = 0
        D = [[0,-1], [0, 1], [1,0],[-1, 0]]
        # 将最初腐烂的橘子放入队列中
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j, time])
        while queue:
            i, j, time = queue.pop(0) # 腐烂的橘子有多个, 也不用管，此时有time这个flag
            for d in D:
                loc_i = i+d[0] 
                loc_j = j+d[1] 
                if  0 <= loc_i <m and 0 <= loc_j < n and grid[loc_i][loc_j] == 1:
                    grid[loc_i][loc_j]  = 2
                    queue.append([loc_i, loc_j, time+1])
        for g in grid:
            if 1 in g:
                return -1
        return time

            

