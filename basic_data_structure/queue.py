from basic_data_structure.node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.head = self.tail = n
        else:
            self.tail.next_node = n
            self.tail = n

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            n = self.head
            self.head = n.next_node
            if self.head is None:
                self.tail = None
            else:
                n.next_node = None
            return n.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

