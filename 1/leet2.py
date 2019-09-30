# coding=utf-8

__author__ = 'wangzr'

"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        addition = 0;
        result = None;
        currentnode = result;
        while (l1 is not None) or (l2 is not None) or (addition != 0):
            sum = addition;
            if l1 is not None:
                sum += l1.val;
                l1 = l1.next;
            if l2 is not None:
                sum += l2.val;
                l2 = l2.next;

            if sum >= 10:
                sum -= 10;
                addition = 1;
            else:
                addition = 0;

            if result is None:
                result = ListNode(sum);
                currentnode = result;
            else:
                currentnode.next = ListNode(sum);
                currentnode = currentnode.next;

        return result;


if __name__ == '__main__':
    sol = Solution();
    listA = ListNode(2);
    currA = listA;
    currA.next = ListNode(4);
    # currA = currA.next;
    # currA.next = ListNode(3);

    listB = ListNode(5);
    currA = listB;
    currA.next = ListNode(6);
    currA = currA.next;
    currA.next = ListNode(4);



    listC = sol.addTwoNumbers(listA, listB);
    currA = listC;
    while(currA is not None):
        print(currA.val);
        currA = currA.next;
