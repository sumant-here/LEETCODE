class Solution:
    def dfs(self,r,c,visited,rows,cols,board):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if board [r][c] == "X":
            return
        if visited [r][c] == 1:
            return

        
        visited[r][c] = 1
        self.dfs(r-1,c,visited,rows,cols,board)
        self.dfs(r,c-1,visited,rows,cols,board)
        self.dfs(r,c+1,visited,rows,cols,board)
        self.dfs(r+1,c,visited,rows,cols,board)




    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited =[[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r ==rows -1 or c == cols-1:
                    if board [r][c] == "O":

                        if visited [r][c] == 0:
                            self.dfs(r,c,visited,rows,cols,board)
        for r in range(rows):
            for c in range(cols):
                if board [r][c] == "O" and visited[r][c] ==0:
                    board[r][c] ="X"
