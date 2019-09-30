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


from sklearn.dataseets import load_digits
if __name__ == '__main__':
    digits = load_digits()
    print(digits.data.shape)