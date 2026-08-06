#交叉链表（相交链表）
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。 
# 通过两个指针运动相遇来判断链表相交位置
# 示例：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为8（注意，如果两个链表相交则不能为0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。
# 换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
class Solution:
    def InterSectionNode(self,headA,headB):
        if not headA or not headB:      #判断链表是否为空（判断、头结点是否为空，如果头结点为空则链表一定为空）
            return None
        pA,pB=headA,headB               #定义pA，pB两个指针位于两个头结点位置
        while pA != pB:
            pA=pA.next if pA else headB #定义移动路线，pA先走headA链表，走完之后开始走headB
            pB=pB.next if pB else headA #通过pB=pB.next if pB实现在B链表上的移动，通过else headA实现从B链表到A链表的跳转
        return pA