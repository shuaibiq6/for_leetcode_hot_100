# 141. 环形链表
# 题目描述
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 思路，本质快慢指针，目的是证明两个指针运动路线是一个环形
#fast走的快速度为2，slow走得慢速度为1，如果fast跑完一圈情况下还能跟slow相遇，那么就说明该链表存在环
#fast.next的前提条件是fast存在，fast.next.next的前提条件是fast.next存在
def hasCycle(head) :
    slow = fast =head          #定义初始位置
    while fast and fast.next:  #只有当fast和fast.next都存在时，fast才能走两步
        slow = slow.next
        fast = fast.next.next
        if fast == slow :   #当fast和slow相遇时返回true证明存在环
            return True     #判断是否同一位置是再fast和slow开始运动之后执行的，因此if判断必须再while之下
    return False 