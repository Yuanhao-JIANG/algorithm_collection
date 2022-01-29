from basic_data_structure.node import Node


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            pop_node = self.head
            self.head = self.head.next_node
            pop_node.next_node = None
            return pop_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
