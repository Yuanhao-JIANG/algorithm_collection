class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def last_node(self):
        curr_node = self.head_node
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        return curr_node

    def has_data(self, i):
        curr_node = self.head_node
        while curr_node is not None:
            if curr_node.data == i:
                return True
            curr_node = curr_node.next_node
        return False

    def list_all(self):
        result = []
        curr_node = self.head_node
        while curr_node is not None:
            result.append(curr_node.data)
        return result
