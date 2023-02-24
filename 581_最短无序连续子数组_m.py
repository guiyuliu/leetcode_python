"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
链接：https://leetcode.cn/problems/shortest-unsorted-continuous-subarray
"""
from typing import  List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 左边维护一个最大值，右边维护一个最小值
        # 把数组分为ABC三段，那么A段的每一个数都比BC段中最小的数minn， 每次移动i，都可以O(1)的更新minn，这样可以确定left
        # 同理C段的每一个数都比段最大的数maxn 大
        # (我想的浅了一步，只想A比B小了)， right 是从0 开始更新， left 是从n-1 开始更新，有点反直觉
        #
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            if minn < nums[n - i - 1]:  #
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        return 0 if right == -1 else right - left + 1


s = Solution()
a = [2,6,4,8,10,9,15]
res = s.findUnsortedSubarray(a)
print(res)


