# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next

        cur = head
        num, reminder = divmod(n, k)
        parts = [None] * k
        i = 0
        while cur and i < k:
            parts[i] = cur

            if i < reminder:
                part_size = num + 1
            else:
                part_size = num

            for j in range(part_size - 1):
                cur = cur.next
            temp = cur.next
            cur.next = None
            cur = temp
            i += 1
        return parts