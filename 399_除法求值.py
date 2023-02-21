from typing import List
"""
399 除法求值
给出a/b ， b/c的值，求queries中 a/c的值，如果不存在就返回-1

建图+dfs ， 用dfs 算累计路径的值

思路，本题是建图+dfs
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 建图，邻接表，是用dict中套dict
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        # 用dfs，维护一个visited矩阵
        def dfs(s, t) -> int:
            if s not in graph:
                return -1
            if s == t:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)

                    if v != -1:
                        return graph[s][node] * v
            # 如果找不到，就返回-1
            return -1

        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res


s = Solution()
a =[["a","b"],["b","c"]]
b = [2.0,3.0]
c = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
x = s.calcEquation(a,b,c)
print(x)


