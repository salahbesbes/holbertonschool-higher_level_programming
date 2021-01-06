#!/usr/bin/python3
""" empty module """


class Node:
    """ Node Class """

    def __init__(self, data=None, next_node=None):
        """ init args
            Args:
                data(int): integer
                next_node (Node): Next Node class
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ getter data """
        return self.__data

    @property
    def next_node(self):
        """ getter next_node """
        return self.__next_node

    @data.setter
    def data(self, data):
        """ setter data """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, next_node):
        """ setter next_node """
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node


class SinglyLinkedList:
    """ linked list """

    def __init__(self):
        self.head = None
        pass

    def sorted_insert(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        elif value <= self.head.data:
            newNode.next_node = self.head
            self.head = newNode
        else:
            current = self.head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node

            newNode.next_node = current.next_node
            current.next_node = newNode

    def __str__(self):
        h = self.head
        s = ""
        while h.next_node is not None:
            s += "{}\n".format(h.data)
            h = h.next_node
        s += "{}".format(h.data)
        return s
