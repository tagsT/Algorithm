# -*- coding: utf-8 -*-

"""
@author: tag
Created on 2018-03-21

"""

import os


class SingleLink:
    head = None
    def __init__(self):
        pass
    class Node:
        next = None
        data = None
        def __init__(self, data):
            self.data = data

    # 增加节点
    def addNode(self, data):
        if type(data) != int:
            raise Exception("[Error] Input Integer.")
        newNode = SingleLink.Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            temp_head = self.head
            while(temp_head.next != None):
                temp_head = temp_head.next
            temp_head.next = newNode

    # 删除节点
    def deleteNode(self, index):
        if type(index) != int:
            raise Exception("[Error] Input Integer.")
        elif index < 0:
            raise Exception("[Error] Index need beyond 0.")
        elif index >= self.getLength():
            raise Exception("[Error] Index beyond link length.")
        if index == 0:
            self.head = self.head.next
        else:
            i = 1
            pre_head = self.head
            cur_head = self.head.next
            while(cur_head != None):
                if (i == index):
                    pre_head.next = cur_head.next
                    break
                pre_head = cur_head
                cur_head = cur_head.next
                i += 1

    # 链表->列表
    def link2List(self):
        _list = []
        temp_head = self.head
        while(temp_head != None):
            _list.append(temp_head.data)
            temp_head = temp_head.next
        return _list

    # 链表长度
    def getLength(self):
        len = 0
        temp_head = self.head
        while(temp_head != None):
            len += 1
            temp_head = temp_head.next
        return len

    # 链表反转
    def reversedLink(self):
        temp_nodes= self.head
        pre_node = None
        while(temp_nodes != None):
            temp_node = SingleLink.Node(temp_nodes.data)
            temp_node.next = pre_node
            pre_node = temp_node
            temp_nodes = temp_nodes.next
        self.head = temp_node

    # 链表排序
    def sortLink(self, sort=0):
        if (sort == 0 or sort == 1) == False:
            raise Exception("[Error] Param::sort error")
        cur_node = self.head
        while(cur_node != None):
            next_node = cur_node.next
            while(next_node != None):
                if sort == 0:
                    if next_node.data < cur_node.data:
                        temp = cur_node.data
                        cur_node.data = next_node.data
                        next_node.data = temp
                elif sort == 1:
                    if next_node.data > cur_node.data:
                        temp = cur_node.data
                        cur_node.data = next_node.data
                        next_node.data = temp
                next_node = next_node.next
            cur_node = cur_node.next

    # 链表去重
    def setLink(self):
        temp_node1 = self.head
        while temp_node1.next != None:
            temp_node2 = temp_node1.next
            while temp_node2 != None:
                if temp_node1.data == temp_node2.data:
                    temp_node1.next = temp_node2.next
                temp_node2 = temp_node2.next
            temp_node1 = temp_node1.next


def main():
    # 初始化
    singlelink = SingleLink()
    # 添加节点 [3,2,1,6,5,5,4,4]
    singlelink.addNode(3)
    singlelink.addNode(2)
    singlelink.addNode(1)
    singlelink.addNode(6)
    singlelink.addNode(5)
    singlelink.addNode(5)
    singlelink.addNode(4)
    singlelink.addNode(4)
    # 删除 index=2的数据
    singlelink.deleteNode(2)
    print(singlelink.link2List())  # [3, 2, 6, 5, 5, 4, 4]
    # 链表反转
    singlelink.reversedLink()
    print(singlelink.link2List())  # [4, 4, 5, 5, 6, 2, 3]
    # 链表排序 默认升序，0升序，1降序
    singlelink.sortLink(sort=1)
    print(singlelink.link2List())  # [6, 5, 5, 4, 4, 3, 2]
    # 链表去重
    singlelink.setLink()
    print(singlelink.link2List()) # [6, 5, 4, 3, 2]

if __name__ == "__main__":
  main()
