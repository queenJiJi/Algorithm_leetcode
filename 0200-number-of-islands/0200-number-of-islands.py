from collections import deque
class Solution(object):
    def numIslands(self, grid):
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited[i][j] == True

            while q:
                cur_r,cur_c = q.popleft()
                
                for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nr,nc = cur_r+dr, cur_c+dc
                    if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc] == '1':
                        q.append((nr,nc))
                        visited[nr][nc] = True
        n,m=len(grid),len(grid[0])
        answer = 0
        visited= [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)
                    answer +=1
        return answer
       
                    

        
