import numpy as np
from basic_data_structure.node import Node
from basic_data_structure.linked_list import LinkedList


class AdjacencyMatrix:
    def __init__(self, n):
        self.vertex_size = n
        self.mat = np.zeros((n, n))

    def is_edg(self, i, j):
        if self.mat[i][j]:
            return True
        else:
            return False

    def set_edg(self, i, j):
        self.mat[i][j] = 1

    def out(self, i):
        out_list = []
        for j in range(self.vertex_size):
            if self.mat[i][j] == 1:
                out_list.append(j)
        return out_list

    def in_(self, j):
        in_list = []
        for i in range(self.vertex_size):
            if self.mat[i][j] == 1:
                in_list.append(i)
        return in_list

    def get_weight(self, u, v):
        return 1


class AdjacencyList:
    def __init__(self, n):
        self.vertex_size = n
        self.vertex_list = []
        for i in range(n):
            linked_list = LinkedList()
            self.vertex_list.append(linked_list)

    def is_edg(self, i, j):
        return self.vertex_list[i].has_data(j)

    def set_edg(self, i, j):
        new_node = Node(j)
        self.vertex_list[i].last_node().next_node = new_node

    def out(self, i):
        return self.vertex_list[i].list_all()

    def in_(self, j):
        in_list = []
        for i in self.vertex_size:
            if self.vertex_list[i].has_data(j):
                in_list.append(i)
        return in_list

    def get_weight(self, u, v):
        return 1
