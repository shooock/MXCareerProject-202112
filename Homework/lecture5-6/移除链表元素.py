# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        h1 = h2 = ListNode(-1) # 建立伪头，初始化双指针
        h2.next = head # 建立伪头和head联系
        while h2.next: # 遍历指针的循环条件
            if h2.next.val == val:
                h2.next = h2.next.next # 移除目标元素
            else:h2 = h2.next # 遍历指针右移
        return h1.next # 返回新的头结点