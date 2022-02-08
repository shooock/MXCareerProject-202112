# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k ==0 or not head.next:
            return head
        i = 1
        cur = head
        while cur.next:
            cur = cur.next
            i+=1

        cut_p = i-k%i
        if cut_p ==i:
            return head

        else:
            cur.next = head
            while cut_p >0:
                cur = cur.next
                cut_p-=1
        head = cur.next
        cur.next = None
        return head
