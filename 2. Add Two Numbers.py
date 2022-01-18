"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.
You may assume the two numbers do not contain any leading zero, except
the number 0 itself.
"""
from functools import reduce


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        number_one = self.get_number(l1)
        number_two = self.get_number(l2)
        result = list(map(lambda x: int(x), str(number_one + number_two)))
        result[0] = ListNode(val=result[0])
        return reduce(lambda x, y: ListNode(val=y, next=x), result)

    def get_number(self, obj):
        result = ''
        while obj:
            result = str(obj.val) + result
            obj = obj.next
        return int(result)
