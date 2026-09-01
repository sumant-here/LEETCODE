class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Code here
        adj_list =[[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        #O(N)

        for u,v in prerequisites:
            adj_list[v].append(u) # here we  just reverse it bcz we have to completer the conneted course and then come to the course which is connect to that course 
            indegrees[u] += 1  # and u ka indegree banao 
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
            return result #true im returing earlier
        return [] #false returing earier 
        