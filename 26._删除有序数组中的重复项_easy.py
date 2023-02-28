"""
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针，一前一后，
        n = len(nums)
        i = 0
        for j in range(n):
            # 当 i，j所指的值相等时，j就直接一直向前
            # 当 i ，j不等时，才把j移动到i的后面一位
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]
        return i+1
