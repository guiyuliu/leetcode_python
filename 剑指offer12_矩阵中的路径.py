"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

回溯法，用dfs 实现

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def check(i,j, k):
            # 表示判断以网格的（i, j ）出发，还能否找到work[k:]之后的所有字符
            if board[i][j] != word[k]: # 如果当前字母不是第k个字符，直接return false
                return False
            if k == len(word)-1: # 如果已经是最后一个字符了，return True
                return True
        
            visited.add((i,j)) #
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k+1):
                            result = True 
                            break
            visited.remove((i,j)) # 讲访问过的位置再移除，这是回溯法的精髓！
            return result

        h = len(board)
        w = len(board[0])
        visited = set() # 设置一个set，添加访问过得位置，访问完了在删除
        for i in range(h):
            for j in range(w):
                # 对每一个位置都调用函数check(i,j, 0)进行检查，只要有一处返回true，就说明网格中能找到对应的单词，否则返回false
                if check(i, j, 0):
                    return True
        return False
