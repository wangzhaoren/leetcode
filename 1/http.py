# coding=utf-8

__author__ = 'wangzr'

'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [];
        # print(nums);
        sortedlist = sorted(nums);
        # print(sortedlist);

        for indexA, itemA in enumerate(sortedlist):
            # print(indexA, itemA);
            if len(result) > 0:
                break;
            for indexB in range(indexA + 1, len(sortedlist)):
                itemB = sortedlist[indexB];
                # print(indexB, itemB);
                if itemA + itemB == target:
                    result = self.getIndex(nums, itemA, itemB)
                    break;
                elif itemA + itemB > target:
                    break;

        return result;

    def getIndex(self, nums, itemA, itemB):
        result = [];
        for index, item in enumerate(nums):
            if itemA == item:
                result.append(index + 1);
            elif itemB == item:
                result.append(index + 1);

        return result;


import urllib
import urllib2
import re

# get接口调用
def httpGet():
    get_url = "http://10.10.3.63/test?id=123&name=nba"
    cookie_headers = {
            "Cookie" : "person_id=2468"
    }
    req = urllib2.Request(url=get_url,headers=cookie_headers)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    # print res

# post接口调用
if __name__ == '__main__':
    # line_name=482&image2.x=27&image2.y=14
    args_data = {
        'line_name': 482,
        'image2.x': 27,
        'image2.y': 14
    }
    args_data_urlencode = urllib.urlencode(args_data)
    post_url = "http://old.hzbus.cn/content/busline/line_search.jsp"
    cookie_headers = {
        "Referer": "http://old.hzbus.cn/content/busline/busframe.jsp"
    }
    req = urllib2.Request(url=post_url, data=args_data_urlencode, headers=cookie_headers)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    # print res

    # 获取出夏令和冬令时间
    # dir_pattern = r"<!--.*end_stop=.*>-->[^.]+(.*)[^.]+<!--<\/a>-->[^.]+<hr size=0>[^.]+<!--.*end_stop=.*>-->[^.]+(.*)[^.]+<!--<\/a>-->"
    dir_pattern = r"<!--.*end_stop=.*>-->[^.]+(.*)[^.]+<!--<\/a>-->[^.]+<hr size=0>[^.]+<!--.*end_stop=.*>-->[^.]+(.*)[^.]+<!--<\/a>-->"
    time_pattern = r"<td.*FDE55B.*font color=.*>.+<hr size=0>.*<\/font><\/td>"
    # dir_list = re.findall(dir_pattern, res, re.M)
    # print dir_list
    time_list = re.findall(time_pattern, res, re.M)
    print time_list
