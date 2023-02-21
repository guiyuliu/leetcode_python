"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。
链接：https://leetcode.cn/problems/median-of-two-sorted-arrays

这题很多解法，还有二分查找的解法
解法-： 归并排序，两个有序数组的合并也是归并排序中的一部分，。然后根据奇数，还是偶数，返回中位数。
"""

def findMedianSortedArrays(nums1,nums2) -> float:
    merge = []
    l1 = len(nums1)
    l2 = len(nums2)
    i=0
    j=0
    if (l1 + l2) % 2 == 0:
        m = (l1 + l2) / 2 +1
    else:
        m = (l1 +l2+1) / 2
    m =int(m)
    print("m", m)

    while len(merge) < m :
        if i >= l1:
            merge.append(nums2[j])
            j += 1
            continue
        if j >= l2:
            merge.append(nums1[i])
            i+=1
            continue
        if nums1[i] <= nums2[j]:
            merge.append(nums1[i])
            i += 1
        else:
            merge.append(nums2[j])
            j += 1

    print("merge", merge)
    if (l1+l2) % 2 == 0:
        ret = (merge[-2] + merge[-1]) / 2
    else:
        ret = merge[-1]
    return ret

nums1 = []
nums2 = [2,3]
ret = findMedianSortedArrays(nums1,nums2)
print(ret)
