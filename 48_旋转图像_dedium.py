"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
链接：https://leetcode.cn/problems/rotate-image

1. 技巧找规律解法
以对角线（左上<—>右下）为轴进行翻转，再对每行以中点左右翻转即可。

2. 一般规律解法
需要开辟一个新的数组，题目只是说不能返回新的数组，没说不能开辟

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix_new = copy.deepcopy(matrix)

        for i in range(0,n):
            for j in range(0,n):
                matrix_new[j][n-i-1] = matrix[i][j]

        #print("matrix new", matrix_new)
        # 注意这里， matrix = matrix_new并不会将matrix 赋值，必须对matrix中的每个元素赋值赋值，才能真正改变
        # 这是源于pythoncopy对于一个复杂对象的子对象并不会完全复制，什么是复杂对象的子对象呢？就比如序列里的嵌套序列，字典里的嵌套序列等都是     
        # 复杂对象的子对象。对于子对象，python会把它当作一个公共镜像存储起来，所有对他的复制都被当成一个引用
        matrix[:] = matrix_new
