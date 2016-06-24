"""
模拟
每次增量为step1=(n-i-1)*2和step2=(i*2)
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        result = ""
        slen = len(s)
        for i in range(0, numRows, 1):
            if 0 == i or numRows - 1 == i:
                for j in range(i, slen, numRows + numRows - 2):
                    result += s[j]
            else:
                step1 = numRows + numRows - 2 - i - i
                step2 = 2 * i
                j = i
                while j < slen:
                    result += s[j]
                    j += step1
                    if j < slen: result += s[j]
                    j += step2
                    # if j < slen: result += s[j]
        return result


if __name__ == '__main__':
    obj = Solution()
    print obj.convert("ABCDE", 4)
    # print obj.convert("PAYPALISHIRING", 4)
    # print obj.convert("PAYPALISHIRING", 1)
    # print obj.convert("PAYPALISHIRING", 2)
