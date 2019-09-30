# coding=utf-8

"""
简单的字符串反转
需要注意超过Integer的情况需要输出0
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xcopy = x
        xcopy = -xcopy if xcopy < 0 else xcopy
        # print xcopy

        result = 0
        while xcopy > 0:
            value = xcopy % 10
            xcopy /= 10
            result = result * 10 + value

        import math

        max_int = math.pow(2, 31) - 1
        min_int = -1 * math.pow(2, 31)

        result = -result if x < 0 else result
        # print min_int
        # print max_int
        # print result
        if min_int <= result <= max_int:
            pass
        else:
            result = 0

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(1234))
    print(sol.reverse(123456789))
    print(sol.reverse(-123456789))
