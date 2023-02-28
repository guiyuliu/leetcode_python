"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
链接：https://leetcode.cn/problems/binary-search


# 二分有两种写法，现第一种，左闭右闭，也就是l r 分别为[0, n-1]
# 此时while循环l <=r, 因为左闭右闭所以 == 是有意义的
# 当mid > target的时候，right 要赋值为mid-1，因为当前nums[mid]一定不是target
# 同理l 要赋值为mid+1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        l = 0
        r = n-1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return -1
        
