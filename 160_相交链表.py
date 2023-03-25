"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
题目数据 保证 整个链式结构中不存在环。


分别为链表A和链表B设置指针A和指针B，然后开始遍历链表，如果遍历完当前链表，则将指针指向另外一个链表的头部继续遍历，直至两个指针相遇。
最终两个指针分别走过的路径为：
指针A :a+c+b
指针B :b+c+a
明显 a+c+b = b+c+a,因而如果两个链表相交，则指针A和指针B必定在相交结点相遇。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        nodeA = headA
        nodeB = headB
        while(nodeA !=nodeB):
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
