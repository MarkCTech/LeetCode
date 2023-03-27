from typing import Optional

# Explanation: 342 + 465 = 807


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstnum = secondnum = ""

        while l1:
            firstnum += str(l1.val)
            l1 = l1.next
        while l2:
            secondnum += str(l2.val)
            l2 = l2.next

        result = str(int(firstnum[::-1]) + int(secondnum[::-1]))[::-1]
        head = nodes = ListNode(0)
        generator = (ListNode(int(x)) for x in result)

        for i in generator:
            nodes.next = i
            nodes = nodes.next
        return head.next


def main():

    head1 = None
    for x in [2, 4, 3]:
        head1 = ListNode(x, next=head1)  # Create and add another node

    head2 = None
    for x in [5, 6, 4]:
        head2 = ListNode(x, next=head2)

    solver = Solution()
    result = solver.addTwoNumbers(head1, head2)

    while result:
        print(result.val)
        result = result.next


if __name__ == '__main__':
    main()
