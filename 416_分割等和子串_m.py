"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

此题是背包问题的转化，相当于从数组中拿一堆数，要求数的价值是 sum/2
背包问题可以用二维dp，dp[i][j] ，dp[i][j]表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和恰好等于 j
，对于「0-1 背包问题」而言就是「当前考虑到的数字选与不选」。
不选择 nums[i]，如果在 [0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j ，那么 dp[i][j] = true；
选择 nums[i]，如果在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]。

状态转移方程：
dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

压缩成一维： 必须逆序！

一维逆序，是0-1背包，一维不逆序，是完全背包。
，因为i每加1代表新的一行开始，由于dp[j-num[i]]每次都得使用的是上一行的数据。
但是如果你正序的话，那么你在计算dp[j]的时候用到的dp[j-num[i]]是本行的，而不是上一行的，所以用逆序，逆序用到的dp[j-num[i]]是上一行的


"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]  # 取不取第i个物体，
        
        return dp[target]
