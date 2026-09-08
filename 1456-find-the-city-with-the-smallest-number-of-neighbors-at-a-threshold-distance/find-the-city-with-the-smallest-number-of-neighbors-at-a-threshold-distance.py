class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_matrix = [[sys.maxsize for _ in range(n)]for _ in range(n)]
        for u ,v , w in edges:
            adj_matrix [u][v] = w
            adj_matrix[v][u] = w
        for i in range (n) :
            adj_matrix[i][i] = 0 
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj_matrix[i][via] != sys.maxsize and adj_matrix[via][j] != sys.maxsize:
                        adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][via]+adj_matrix[via][j])
        min_neigh = n 
        city = - 1
        for i in range(n):
            count = 0 
            for j in range(n):
                if adj_matrix[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_neigh:
                min_neigh = count
                city = i 
        return city 