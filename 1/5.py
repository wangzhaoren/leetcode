# coding:utf-8
"""
给定一个字符串S，找出S的最长回文子串
解法一 [O(n2)]
在每一个字符和字符间的空隙上放置一个分割线，然后向分割线的两边依次扩展检测是否满足回文串的要求（字符相等）；
解法二 [O(n2)]
动态规划
dp[i,j]:表示S.substr[i,j]是否是回文串
dp[i,i]=true
dp[i,i+1]=(s[i]==s[i+1])
dp[i-1, j+1] = dp[i,j] && s[i-1]==s[j+1]
解法三
充分利用回文串的对称性
如果当前以center为中心的回文串半径为R[center],其最右边界为max_right=center+R[center]
则在[center+1,center+R]区间的点i(其对称点j为center*2-i)
R[i]=R[j] if (i + R[j] < max_right)
R[i]=max_right - i if (i + R[j] > max_right)
R[i]=max_right - i if (i + R[j] == max_right) 不确定是否是最大值，需要继续扩展
https://www.felix021.com/blog/read.php?2040
解法四
后缀数组 TODO
"""
class Solution(object):
    resultbeg = 0
    resultend = 0
    resultLen = 0

    def check_best_result(self, left, right):
        if self.resultLen < right - left + 1:
            self.resultLen = right - left + 1
            self.resultbeg = left
            self.resultend = right
            # print "resultStr=%s" % s[resultbeg:resultend+1]


    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        slist = list(s)
        # print slist
        # 选取中心线的位置
        for line in range(0, size, 1):
            # 以当前字符为中心，向两边展开
            left = line
            while left >= 0:
                if (size - line) * 2 + 1 <= self.resultLen:
                    break
                right = line + line - left
                if right >= size:
                    break
                if slist[left] != slist[right]:
                    break
                else:
                    self.check_best_result(left, right)
                    # if self.resultLen < right - left + 1:
                    #     self.resultLen = right - left + 1
                    #     self.resultbeg = left
                    #     self.resultend = right
                left -= 1

            # 以当前字符后面的空格为中心，向两边展开
            left = line
            while left >= 0:
                if (size - line) * 2 <= self.resultLen:
                    break
                right = line + line + 1 - left
                if right >= size:
                    break
                if slist[left] != slist[right]:
                    break
                else:
                    self.check_best_result(left, right)
                    # if self.resultLen < right - left + 1:
                    #     self.resultLen = right - left + 1
                    #     self.resultbeg = left
                    #     self.resultend = right

                left -= 1

        return s[self.resultbeg:self.resultend+1]

    def longestPalindrome2(self, s):
        slen = len(s)
        dp = [[0 for i in range(slen)] for j in range(slen)]
        for i in range(0, slen):
            dp[i][i] = 1
        for i in range(0, slen-1):
                dp[i][i+1] = 1 if s[i] == s[i+1] else 0

        # for i in range(slen):
        #     for j in range(slen):
        #         print dp[i][j],
        #     print '\n'

        for center in range(0, slen-1):
            for size in range(1, slen):
                left = center-size
                right = center + size
                if (left < 0) or (right >= slen):
                    break
                if (s[left] == s[right]) and (dp[left+1][right-1] == 1):
                    dp[left][right] = 1
                    if right - left + 1 > self.resultLen:
                        self.resultLen = right - left + 1
                        self.resultbeg = left
                        self.resultend = right
                else:
                    break

            for size in range(1, slen):
                left = center-size
                right = center + 1 + size
                if (left < 0) or (right >= slen):
                    break
                if (s[left] == s[right]) and (dp[left+1][right-1] == 1):
                    dp[left][right] = 1
                    if right - left + 1 > self.resultLen:
                        self.resultLen = right - left + 1
                        self.resultbeg = left
                        self.resultend = right
                else:
                    break

        return s[self.resultbeg:self.resultend+1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = len(s)
        slist = ['^']
        for i in range(slen):
            slist.append('#')
            slist.append(s[i])
        slist.append('#')
        slist.append('$')
        slist_len = len(slist) - 1

        radius = [0 for i in range(slist_len)]
        max_right = 0  # 当前最大的半径
        max_center = 0  # 当前最大半径的中心
        for center in range(1, slist_len, 1):
            # 判断该点是否可以根据对称性求得一个基础或者最大半径（是否在圆内）
            if center < max_right:
                center_mirror = max_center * 2 - center
                if max_right - center > radius[center_mirror]:
                    radius[center] = radius[center_mirror]
                elif max_right - center < radius[center_mirror]:
                    radius[center] = max_right - center
                else:  # 需要继续扩展
                    radius[center] = max_right - center

            # 尝试向两边扩展
            left = center - radius[center]
            right = center + radius[center]
            while slist[left] == slist[right]:
                radius[center] += 1
                left -= 1
                right += 1

            if max_right < center + radius[center]:
                max_right = center + radius[center]  # 最右边界
                max_center = center  # 最右边界的中心

            # 得到当前的最大半径后，更新后续的最优值，这里可以优化，
            # 维护一个可以覆盖到的最大半径即可，无需每次得到一个最大半径后，就跟新后续的最优值
            # for i in range(center+1, max_right, 1):
            #     j = center + center - i
            #     if radius[j] < max_right - i:
            #         radius[i] = radius[j]  # 不需要继续扩展，最优解
            #     elif radius[j] > max_right - i:
            #         radius[i] = max_right - i  # 不需要继续扩展，最优解
            #     else:
            #         radius[i] = -1 * (max_right - i)  # 需要继续扩展

        self.resultLen = 0
        for center in range(1, slist_len, 1):
            if self.resultLen < radius[center]:
                self.resultLen = radius[center]
                self.resultbeg = center - radius[center] + 1
                self.resultend = center + radius[center]

        result = []
        for center in range(self.resultbeg, self.resultend):
            if slist[center] != '#' and slist[center] != '$' and slist[center] != '^':
                result.append(slist[center])

        return "".join(result)

if __name__ == '__main__':
    obj = Solution()
#     print obj.longestPalindrome("")
#     print obj.longestPalindrome("aba")
#     print obj.longestPalindrome("babcbad")
#     print obj.longestPalindrome("kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd")
#     print obj.longestPalindrome("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    print obj.longestPalindrome("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
