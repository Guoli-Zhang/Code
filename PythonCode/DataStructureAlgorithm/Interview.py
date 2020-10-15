"""
1、青蛙跳台阶问题
一只青蛙要跳上 n 层高的台阶，一次能跳一级，也可以跳两级，请问这只青蛙有多少种跳上这个 n
层高台阶的方法？
思路分析：
方法 1:递归
设青蛙跳上 n 级台阶有 f(n)种方法，把这 n 种方法分为两大类，第一种最后一次跳了一级台阶，这
类方法共有 f(n-1)种，第二种最后一次跳了两级台阶，这种方法共有 f(n-2)种，则得出递推公式
f(n)=f(n-1)+f(n-2)，显然，f(1)=1，f(2)=2，递推公式如下：
* 这种方法虽然代码简单，但效率低，会超出时间上限*
代码实现如下：
"""


class Solution(object):
    # @param:{integer} n
    # @return:{integer}
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2(object):
    # @param:{integer} n
    # @return:{integer}
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        a, b, c = 1, 2, 3
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c


class Solution3(object):
    def climbStairs(self, n):
        def fact(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        total = 0
        for i in range(int(n / 2 + 1)):
            total += int(fact(i + n - 2 * i) / fact(i) / fact(n - 2 * i))
        return total


class Solution4(object):
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 1:
            return 1
        arr = [1, 1, 0]  # look here, arr[0] = 1, arr[1] = 2
        for i in range(2, n + 1):
            arr[2] = arr[0] + arr[1]
            arr[0], arr[1] = arr[1], arr[2]
        return arr[2]


if __name__ == "__main__":
    # a = Solution()
    # b = a.climbStairs(10)
    # print(b)

    # a = Solution2()
    # c = a.climbStairs(10)
    # print(c)

    a = Solution3()
    c = a.climbStairs(10)
    print(c)
