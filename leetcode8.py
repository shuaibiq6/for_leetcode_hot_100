#19题 删除倒数第n个链表
#依旧快慢指针
#整体思路：fast先走n步（假设要删除倒数第n个数字），然后fast和slow一起走，直到fast走完
# fast走完之后把slow的next直接指向slow.next.next，把slow和slow.next.next中间那个slow.next当痘给挤了
# 而slow.next刚好是倒数第n个
class ListNode:
    def __init__(self,val = 0,next = None):#引入列表每个结点的值和指针两个元素
        self.val = val
        self.next = next
    def removeNthFormEnd(head,n):
        dummy = ListNode(-1,head)           #定义dummy位置，（-1，head）代表dummy的值和dumm.next的指向
        slow = dummy                        #定义slow和fast的初始位置
        fast = dummy
        for i in range(n):                  #若n=2则i=0,1，fast = fast.next执行两次，fast向前走n步
            fast = fast.next
        while fast.next:                    #只要fast.next还存在就继续执行后续内容
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next          #删除的数字是倒数第n个，跟正数第几无关因此dummy正引入不影响
        return dummy.next