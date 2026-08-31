# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        curr, prev = second, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while prev:
            temp1, temp2 = head.next, prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2
