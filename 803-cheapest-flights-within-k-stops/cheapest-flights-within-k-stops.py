import sys
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u,v ,cost in flights:
            adj_list[u].append([v,cost])
        min_cost =[sys.maxsize for _ in range(n)]
        min_cost[src] = 0 
        queue = deque()
        queue.append([0,src,0]) #steps, node, cost
        while len(queue) !=0:
            step,node,cost = queue.popleft()
            for adjNode,price in adj_list[node]:
                new_cost = cost + price
                if new_cost < min_cost[adjNode]:
                    new_step = step + 1
                    if new_step == k +1:
                        if adjNode != dst:
                            continue
                    min_cost[adjNode] = new_cost
                    queue.append([new_step,adjNode,new_cost])
        if min_cost[dst] == sys.maxsize:
            return -1
        return min_cost[dst]

        #here i didnot use the priroty w=queue so that E logV not come TC = len(flights)
        
        