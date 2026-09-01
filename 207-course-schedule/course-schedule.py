class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Code here
        adj_list =[[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        #O(N)

        for u,v in prerequisites:
            adj_list[u].append(v)
            indegrees[v] += 1
        queue = deque()
        result = []
        #O(N)
        for i in range(0,numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        #O(V + E)
        while len(queue) !=0:
            current_node = queue.popleft() # 1
            result.append(current_node)
            for adjNode in adj_list[current_node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
        if len(result) == numCourses:
            return True
        return False   

        #i  solve this question using BFS BCZ we want a poper ordering 