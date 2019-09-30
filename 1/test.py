# coding=utf-8

__author__ = 'wangzr'

'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

import json

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


class point(object):
    def __init__(self, _lng, _lat):
        self.lng = _lng
        self.lat = _lat

    def __str__(self):
        # return str(self.lng) + "," + str(self.lat)
        return '{"lng":%f, "lat":%f}' % (self.lng, self.lat)


if __name__ == '__main__':
    geolist =[
        9827563,
        9870499,
        9900121,
        9908474,
        9914845,
        9927385,
        9932236,
        9937772,
        9941360,
        9954234,
        9961221,
        9964828,
        9973106,
        9981133,
        10011744,
        10142706,
        10293691,
        10346476,
        10390023,
        10443500,
        10486945,
        10530455,
        10574051,
        10617507,
        10670840,
        10714441,
        10758016,
        10801568,
        10845373,
        10898683,
        10942254,
        10986059,
        11029419,
        11072928,
        11126248,
        11169608,
        11213136
    ]
    for i in range(1, len(geolist)):
        print geolist[i] - geolist[i-1]

    # print(jsonStr)