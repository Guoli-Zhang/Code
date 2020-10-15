class Solution:
    def sumNums(self, n:int) -> int:
        return n and (n + self.sumNums(n - 1))
        # n > 1 and self.sumNums(n - 1)
        # self.result += n
        # return self.result
        #
print(Solution().sumNums(10))

print(sum(range(1, 10)))