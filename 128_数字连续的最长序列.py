"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

先用一个hash表去重，
再循环遍历每个数字，找他相邻的数是否存在，不断找最大的，哈希表访问是o1的复杂度
。
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #未排序，考虑用特殊数据结构set
        num_set = set(nums)
        longest = 0

        for num in num_set:
            i = 1
            length = 1
            # 不应该前后双向寻找最长序列，会超时
            #只有当一个数是连续序列的 *第一个数* 的情况下才会进入内层循环
            if num-i in num_set:
                continue #不是第一个数，跳过
            while num+i in num_set:
                length += 1
                i += 1
            longest = max(length, longest)
        return longest
            
                  
