class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1 : ListNode, list2 :ListNode) -> ListNode:
        li = []
        while list1:
            li.append(list1.val)
            list1 = list1.next

        while list2:
            li.append(list2.val)
            list2 = list2.next
        #li에 정렬안된 리스트 
        tmp = None
        head = None 

        #li  = [1,1,2,4,5,6]
        for val in sorted(li):
            if not tmp: 
                tmp = ListNode(val)
                head = tmp
            else:
                tmp.next = ListNode(val)
                tmp = tmp.next
        return head
