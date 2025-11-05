class Solution(object):
    from collections import deque
    def shortestPathBinaryMatrix(self, grid):
        visited = set()
        q = deque()
        q.append((0,0,1))
        n = len(grid)
        visited.add((0,0))

        if grid[0][0] != 0 or grid[n-1][n-1] !=0:
            return -1
        
        while q:
            cur_r,cur_c, path = q.popleft()

            if (cur_r,cur_c) == (n-1,n-1):
                return path

            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1],[-1,1],[1,-1],[-1,-1],[1,1]]:
                nr,nc = cur_r+dx, cur_c+dy

                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc]==0:
                    q.append((nr,nc,path+1))
                    visited.add((nr,nc))
        return -1
        