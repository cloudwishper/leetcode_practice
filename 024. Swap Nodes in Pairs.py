# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param head: head node of a linked list.
        :return: swap every two adjacent nodes of input linked list and return head.
        """
        if not head or not head.next:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        pointer1 = head
        pointer2 = head.next
        tmp_node = dummy_node

        # use two pointers to swap each pair nodes and then move to next two nodes
        while True:
            pointer1.next = pointer2.next
            pointer2.next = pointer1
            tmp_node.next = pointer2
            tmp_node = pointer1
            pointer1 = pointer1.next
            if not pointer1:
                break
            pointer2 = pointer1.next
            if not pointer2:
                break

        return dummy_node.next 
