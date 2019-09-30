# coding=utf-8

__author__ = 'wangzr'

'''
Median of Two Sorted Arrays My Submissions Question
Total Accepted: 70929 Total Submissions: 407885 Difficulty: Hard
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Subscribe to see which companies asked this question

Submission Details
2078 / 2078 test cases passed.
Status: Accepted
Runtime: 144 ms
Submitted: 0 minutes ago
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.len1 = len(nums1)
        self.len2 = len(nums2)
        self.num1 = nums1;
        self.num2 = nums2;
        index1 = int((self.len1 + self.len2) / 2);
        index2 = int((self.len1 + self.len2 - 1) / 2);

        # from [beg1, end1] and [beg2, end2] find the (index) one
        result = 0.0000;
        if index1 >= 0 and index2 >= 0:
            result += self.DFS(0, self.len1 - 1, 0, self.len2 - 1, index1);
            result += self.DFS(0, self.len1 - 1, 0, self.len2 - 1, index2);

        return result / 2;

    def DFS(self, beg1, end1, beg2, end2, index):

        if end1 >= beg1:
            mid1 = int((beg1 + end1) / 2);
            # print(mid1);
        else:
            return self.num2[beg2 + index];

        if end2 >= beg2:
            mid2 = int((beg2 + end2) / 2);
            # print(mid2);
        else:
            return self.num1[beg1 + index];

        if self.getCount(beg1, mid1) + self.getCount(beg2, mid2) > (index + 1):
            #
            if self.num1[mid1] > self.num2[mid2]:
                return self.DFS(beg1, mid1 - 1, beg2, end2, index)
            elif self.num1[mid1] < self.num2[mid2]:
                return self.DFS(beg1, end1, beg2, mid2 - 1, index)
            else:
                return self.DFS(beg1, mid1, beg2, mid2 - 1, index)

        elif self.getCount(beg1, mid1) + self.getCount(beg2, mid2) < (index + 1):
            if self.num1[mid1] >= self.num2[mid2]:
                index -= self.getCount(beg2, mid2);
                return self.DFS(beg1, end1, mid2 + 1, end2, index);
            elif self.num1[mid1] < self.num2[mid2]:
                index -= self.getCount(beg1, mid1);
                return self.DFS(mid1 + 1, end1, beg2, end2, index);
            else:
                index -= self.getCount(beg2, mid2) + self.getCount(beg1, mid1);
                return self.DFS(mid1 + 1, end1, mid2 + 1, end2, index);

        else:
            # (mid1-beg1+1) + (mid2-beg2+1)== (index+1)
            if self.num1[mid1] > self.num2[mid2]:
                index -= self.getCount(beg2, mid2);
                return self.DFS(beg1, mid1, mid2 + 1, end2, index);
            elif self.num1[mid1] < self.num2[mid2]:
                index -= self.getCount(beg1, mid1);
                return self.DFS(mid1 + 1, end1, beg2, mid2, index);
            else:
                return max(self.num1[mid1], self.num2[mid2]);

    def getCount(self, beg, end):
        if end >= beg:
            return end - beg + 1;
        else:
            return 0;


if __name__ == '__main__':
    sol = Solution();
    print(sol.findMedianSortedArrays([1, 3, 5], [2, 4, 6]));
    print(sol.findMedianSortedArrays([1, 3], [2, 4, 6]));
    print(sol.findMedianSortedArrays([1, 3, 5], [2, 4]));
    print(sol.findMedianSortedArrays([1], [2]));
