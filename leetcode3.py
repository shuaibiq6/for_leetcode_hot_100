#160交叉链表（相交链表）
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。 
# 通过两个指针运动相遇来判断链表相交位置
#pA走完a链表从headB开始走b链表，不能调到pB，只有从headB开始走才能保证完整遍历整个b链
#如果跳到pB可能pB位置不在b链头部，无法完整遍历
class Solution:
    def InterSectionNode(self,headA,headB):
        if not headA or not headB:      #判断链表是否为空（判断、头结点是否为空，如果头结点为空则链表一定为空）
            return None
        pA,pB=headA,headB               #定义pA，pB两个指针位于两个头结点位置
        while pA != pB:
            pA = pA.next if pA else headB #定义移动路线，pA先走headA链表，走完之后开始走headB
            pB = pB.next if pB else headA #通过pB=pB.next if pB实现在B链表上的移动，通过else headA实现从B链表到A链表的跳转！！！！
        return pA                       #pA和pB位置相同时返回pA的位置