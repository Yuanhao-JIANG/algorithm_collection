import heapq


class Dijkstra:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.q = []
        self.d = []
        self.pi = []

    def set_graph(self, graph):
        self.graph = graph

    def init_single_source(self):
        for v in range(self.graph.vertex_size):
            self.d.append(None)
            self.pi.append(None)

    def relax(self, u, v):
        if self.d[v] is None:
            self.d[v] = self.d[u] + self.graph.get_weight(u, v)
            self.pi[v] = u
            heapq.heappush(self.q, (self.d[v], v))
        if self.d[v] > self.d[u] + self.graph.get_weight(u, v):
            self.d[v] = self.d[u] + self.graph.get_weight(u, v)
            self.pi[v] = u
            for i in range(len(self.q)):
                if self.q[i][1] == v:
                    self.q[i] = (self.d[v], v)
                    heapq.heapify(self.q)
                    break

    def dijkstra(self):
        self.init_single_source()
        heapq.heappush(self.q, (0, self.source))
        self.d[self.source] = 0
        while len(self.q) != 0:
            (d, u) = heapq.heappop(self.q)
            for x in self.graph.out(u):
                self.relax(u, x)
