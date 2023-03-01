"""
在一个 n * m 的二维数组中，每一行都按照从左到右 非递减 的顺序排序，每一列都按照从上到下 非递减 的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


链接：https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
# 该题暴力法是n2的复杂度，因为没利用好逐渐递增的规则
# 从矩阵旋转一下,左下角开始看为二叉搜索树，往上即是往左，元素都比根小
# 往右就是都比根大，就可以操作index 往左或者往右

"""

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        i = n-1
        j = 0
        while i >= 0 and j < m:            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j +=1
            else:
                i -=1
        return False
