"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

异或操作： 如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。
a 异或 0 = a
a 异或 a = 0
满足交换律和结合律

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = i ^ ans
        return ans
