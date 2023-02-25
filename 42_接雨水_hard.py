"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

本解法属于单调栈解法，还有动态规划及演变出来的双指针
# 该题主要是分析清楚，对于下标i，所能接的雨水最大高度是，左右两边最大高度的最小值，所能存的雨水是这个最大高度减去
# 该位置的heightp[i]
# 维护一个单调栈，单调栈存储的是下标，从栈底到栈顶的下标对应的数组 height 递减，top下面一个元素是left
# 如果height【i] 比 栈顶top的高度大，则可以得到一个接水区域，该区域的宽度是i-left-1
# 高度是 min(heigth[left], height[i]) - height[top]
# 注意：为了得到left，需要将top出栈，在对top计算能接的雨水量后，left变成新的top，重复上述操作，直到栈变为空
# 在对下标i处计算能接的雨水量之后，将i入栈，继续遍历后面的下标

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        for i, h  in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack: #如果栈里只有一个top，即没有left，break
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        return ans
