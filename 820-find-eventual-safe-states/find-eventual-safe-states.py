from collections import deque 
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # TERMINAL NODE RO OUT DEGREE 0 THIBO AND In degree chalibo
        # TOPO sort sabubele in degree re logau ame 
        #edges Ku reverse koriba 
        V = len(graph)
        adj_list = [[] for _ in range(V)]
        for node in range(V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node) # ulta oppend koli
        queue=deque()
        indegrees =[0 for _ in range(V)]
        for node in range(len(adj_list)):
            for adjNode in adj_list[node]:
                indegrees [adjNode] += 1
        #add alll the nodes with indegree 0 on queue
        for node in range(0,V):
            if indegrees[node] == 0 :
                queue.append(node)
        result = []
        while len(queue) !=0:
            node = queue.popleft()
            result.append(node)
            for adjNode in adj_list[node]:
                indegrees [adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
        result.sort()
        return result 

