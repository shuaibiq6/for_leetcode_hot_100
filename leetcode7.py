# 21合并有序链表
class ListNode:
    def __init__(self,val = 0,next = None):#给引入的每个参数添加值和指针两个元素
        self.val = val
        self.next = next
    def mergeTwoLists(self,list1,list2):
        dummy = ListNode()              #创建一个链表，dummy是表头
        current = dummy                 #定义current的初始位置，后续current从表头位置开始移动
        while list1 and list2:          #当list1和list2同时存在时才能判断两者谁更小，所以必须是and
            if list1.val < list2.val:   #list1和list2都是链表头结点，链表头结点能代表整条链表
                current.next = list1
                list1 = list1.next      #目的是实现指针在链表上的移动
            else:
                current.next = list2    #将current的指针指向list2结点
                list2 = list2.next
            current = current.next      #实现current的移动，保证current永远在链表的最后一位
        current.next = list1 or list2   #while list1 and list2的对立情况，当list1或list2其中之一指向none时，剩余部分接上另一条链表，两条链表存在其中之一即可
        return dummy.next               #dummy初始位置