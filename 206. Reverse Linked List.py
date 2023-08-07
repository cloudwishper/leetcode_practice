# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param head: head node of a linked list.
        :return: reversed linked list.
        """
        if not head:
            return head
    
        dummy_node = ListNode()
        dummy_node.next = head

        # move each tmp node to the location right after dummy node one by one
        while head.next:
            tmp_node = head.next
            head.next = tmp_node.next
            tmp_node.next = dummy_node.next
            dummy_node.next = tmp_node

        return dummy_node.next 
