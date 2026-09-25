from collections import deque
class Solution:

    # def bfs(self,i,j,visited,grid):
    #     rows  = len(grid)
    #     cols = len(grid[0])
    #     queue = deque()
    #     queue.append((i,j)) 
    #     visited [i][j] = 1
    #     while len(queue) != 0:
    #         x , y = queue.popleft()
    #         for xx,yy in [(-1,0),(0,-1),(0,1),(1,0)]:
    #             new_i , new_j = x + xx, y + yy
    #             if new_i < 0 or new_j < 0 or new_i >=rows or new_j >= cols:
    #                 continue
    #             if grid[new_i][new_j] =="0":
    #                 continue
    #             if visited[new_i][new_j] == 1:
    #                 continue
    #             visited[new_i][new_j] = 1
    #             queue.append((new_i,new_j))
                    

    def numIslands(self, grid: List[List[str]]) -> int:
        # rows = len(grid)
        # cols = len(grid[0])
        # count = 0 
        # visited = [[0 for _ in range(cols)]for _ in range(rows)]
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and visited[r][c]  == 0:
        #             count += 1
        #             self.bfs(r,c,visited,grid)
        # return count        
        m = len(grid)
        n = len(grid[0])
        dirc = [(-1,0),(0,-1),(1,0),(0,1)]
        vis = set()
        count =  0 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0" or (r,c) in vis:
                    continue
                count += 1
                vis.add((r,c))
                q = deque()
                q.append((r,c))
                while q:
                    r1, c1 = q.popleft()
                    for dr , dc in dirc:
                        nr = r1 + dr 
                        nc = c1 + dc 
                        if 0<= nr < m and 0<= nc < n and grid[nr][nc] == "1" and (nr,nc) not in vis:
                            vis.add((nr,nc))
                            q.append((nr,nc))
        return count

