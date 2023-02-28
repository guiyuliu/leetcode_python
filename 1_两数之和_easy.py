"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
利用暴力法肯定会超时，利用哈希表存储数以及其下标，然后判断target -i 是否在hash表中，因为hash表查找是O（1）的时间复杂度
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        for  idx ,i in enumerate(nums):
            if target - i in  hashtable:
                return [idx, hashtable[target-i]]
            hashtable[i] = idx
        return []

