"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
 [3,2,3,1,2,4,5,5,6], k = 4
 
 
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        high = len(nums) -1
        return self.quickSelect(nums, 0, high, k)

    def quickSelect(self, nums, low, high, k):
        i = low
        location = low -1  # loc指向最小的位置的末端
        pivot = nums[high]
        while (i < high):
            if nums[i] <= pivot:
                location +=1
                nums[location], nums[i] = nums[i], nums[location]
            i +=1
        p = location +1
        nums[p], nums[high] = nums[high], nums[p] # 前面都是快速排序
        
        #  快速选择
        left_length = high - p +1
        # 如果左边的长度等于k ，就直接返回
        if  left_length  == k:
            return nums[p]
        # 如果左边的长度大于k，在右边找
        if left_length > k:
            return self.quickSelect(nums, p+1, high, k )
        else:
        # 如果左边的长度小于k， 在左边找，注意，此时要变成k-left_length 大的数
            return self.quickSelect(nums, low, p-1, k-left_length)
