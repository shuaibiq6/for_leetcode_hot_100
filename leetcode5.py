# 206反转链表
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
def reverseList(head):
    if not head:#依旧链表的头节点就能代表整条链表，如果头结点为空则链表为空
        return None
    prev = None#定义prev和curr的初始位置
    curr = head
    while curr :#
        Next_Node = curr.next
        curr.next = prev
        prev = curr
        curr = Next_Node
    return prev
#链表的头节点就能代表整条链表,而prev在反转结束之后指向的位置是反转后链表的头结点
        