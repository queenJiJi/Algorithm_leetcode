from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        q = deque()
        q.append([0,0,1])
        visited=[[False]*n for _ in range(n)]

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        while q:
            r,c,dist = q.popleft()
            visited[r][c] = True

            if r==n-1 and c==n-1:
                return dist

            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]:
                nr,nc = dr+r,dc+c
                if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc] == 0:
                    q.append([nr,nc,dist+1])
                    visited[nr][nc] = True

        return -1

    #    q=deque()
    #    q.append((0,0,1))
    #    n = len(grid)
    #    visited=[[False]*n for _ in range(n)]

    #    while q:
    #         cur_r,cur_c,path = q.popleft()
    #         visited[cur_r][cur_c] = True

    #         if cur_r==0 and cur_c==0 and grid[cur_r][cur_c] == 1:
    #             return -1
            
    #         if (cur_r,cur_c) == (n-1, n-1):
    #             return path            
            
    #         for dr,dc in [[-1,0],[1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
    #             next_r, next_c = cur_r+dr, cur_c+dc
    #             if 0<=next_r<n and 0<=next_c<n and grid[next_r][next_c] == 0:
    #                 if not visited[next_r][next_c]:
    #                     q.append((next_r,next_c,path+1))
    #                     visited[next_r][next_c] = True
    #    return -1
    
       

                