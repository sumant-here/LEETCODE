import sys
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        adj_list = [[] for _ in range(n)]
        for u,v,w in roads:
            adj_list[u].append([v,w])
            adj_list[v].append([u,w]) # undirected graph so it connect with it lie this 

        distance =[sys.maxsize for _ in range(n)]
        ways = [ 0 for _ in range(n)]
        distance [0] = 0 
        ways[0] = 1 # zero distance ku jiba paui 1 way and distance zero lagibo 
        p_q = [[0,0]]
        while len(p_q) !=0:
            dist, node = heapq.heappop(p_q)
            for adjNode, weight in adj_list[node]:
                new_dist = dist + weight 
                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    heapq.heappush(p_q,[new_dist,adjNode])
                    ways[adjNode] = ways[node] # update with previus
                elif new_dist == distance[adjNode]:
                    ways[adjNode] += ways[node]
        return ways[n-1] % mod 


