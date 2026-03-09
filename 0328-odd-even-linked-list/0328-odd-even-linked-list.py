# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        if not head.next:
            return head

        even = head.next
        odd = head

        even_start = head.next
        prev_odd = None


        while even and odd:
            if odd.next:
                odd.next = odd.next.next
            
            if even.next:
                even.next = even.next.next
            
            prev_odd = odd
            odd = odd.next
            even = even.next
        
        if odd:
            odd.next = even_start
        else:
            prev_odd.next = even_start

        return head
        
