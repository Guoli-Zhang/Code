"""
刷题34——面试题63：股票的最大利润

题目：
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
例如，一只股票在某些时间节点的价格位{9, 11, 8, 5, 7, 12, 16, 14}。如果我们能在价格为5
的时候买入并在价格为16时卖出，则能收获最大的利润11。

思路：
股票交易的利润来自股票买入和卖出价格的差价。当然，我们只能在买入某只股票之后才能卖出。
如果把股票的买入价和卖出价两个数字组成一个数对，那么利润就是这个数对的差值。因此，
最大的利润就是数组中所有数对的最大差值。

我们定义函数diff(i)为当卖出价为数组中第i个数字时可能获得的最大利润。显然，
当卖出价固定时，买入价越低获得的利润越大。也就是说，如果在扫描到数组中的第i个数字时，
只要我们能记住之前的i-1个数字中的最小值，就能算出在当前价位卖出时可能得到的最大利润。

综上，python代码如下：
"""

# 解法一
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         f = [0]
#         for i in range(1, len(prices)):
#             f.append(max(0, f[i-1]+prices[i]-prices[i-1]))
#         return max(f)


# 解法二（推荐）
def MaxDiff(nums):
    if not nums:
        return 0
    n = len(nums)
    min_value = nums[0]
    maxDiff = nums[1] - min_value
    for i in range(2, n):
        if nums[i - 1] < min_value:
            min_value = nums[i - 1]
        currentDiff = nums[i] - min_value
        if currentDiff > maxDiff:
            maxDiff = currentDiff

    return maxDiff


# select scode from excel where object = yuwen order_by Scode desc limit 2, 1;

