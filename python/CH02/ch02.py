
class ListNode:

    def __init_(self, val, next):
        self.val = val
        self.next = next

    def next(self):
        if self is None:
            self = node

def sum_lists(l1, l2, direction = 1):

    def sum_lists_forward(l1, l2):
        res = None
        carry = 0
        while l1 and l2:
            a = l1.val + l2.val
            res.append(ListNode(a%10, None))