import sys
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r = len(heights)
        c = len(heights[0])
        ea = [[sys.maxsize for _ in range(c)]for _ in range(r)]
        ea [0][0] = 0 
        pq = [[0,0,0]]
        while len(pq) !=0 :
            ef , i , j = heapq.heappop(pq)
            if i == r -1 and j == c-1:
                return ef
            for x , y in [[-1,0],[0,-1],[1,0],[0,1]]:
                ni , nj = i + x , j + y
                if ni < 0 or ni >= r or nj < 0 or nj >= c :
                    continue
                neweff = max(ef,abs(heights[ni][nj]-heights[i][j]))
                if neweff < ea[ni][nj]:
                    ea [ni][nj] = neweff
                    heapq.heappush(pq,[neweff,ni,nj])
# no need to write  -1  or return kind of thisng beacause no path is blocked here  TC - 0(E logV) 0(nxm4 log(nxm))