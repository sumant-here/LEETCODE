class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        # Path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u, v):

        # Find parents
        pu = self.find(u)
        pv = self.find(v)

        # Already in same set
        if pu == pv:
            return True

        # Union by rank
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return False # as the parent s are not same there fore 



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        extra_edges = 0 

         # TC -----> O( E 4alpha)
        for u  , v  in connections:
            if ds.union(u,v):
                extra_edges += 1
        component = 0 

        #TC -----> O(V)
        for i in range(n):
            if ds.find(i) == i :
                component += 1
        if extra_edges >= component - 1:
            return component - 1
        return -1


        # o e + o v 