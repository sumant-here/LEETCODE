import sys
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return - 1
        rows = len(grid)
        cols = len(grid[0])
        di =[[sys.maxsize for _ in range(cols) ]for _ in range(rows)]
        di [0][0] = 1
        queue = deque()
        queue.append([1,0,0])
        while len(queue) !=0 :
            d , i , j = queue.popleft()
            for x,y in [[1,0],[0,-1],[-1,0],[0,1],[-1,-1],[-1,1],[1,1],[1,-1]]:
                n_i , n_j = i + x , j + y
                if n_i < 0 or n_i >= rows or n_j < 0 or n_j >= cols:
                    continue
                if grid[n_i][n_j] ==1:
                    continue
                d_t = d + 1
                if d_t < di [n_i][n_j] :
                    di[n_i][n_j] = d_t
                    queue.append([d_t,n_i,n_j])
        if di[rows-1][cols-1] == sys.maxsize:
            return - 1
        return di[rows-1][cols-1]



        #0RC