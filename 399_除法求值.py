from typing import List
"""
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
返回 所有问题的答案 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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


