import collections
class Solution(object):
    def numIslands(self, grid):
        m,n = len(grid), len(grid[0])
        visited= [[False]*n for _ in range(m)]
        count =0 
        def dfs(r,c):
            visited[r][c] = True
            for dr,dc in [[-1,0],[0,1],[1,0],[0,-1]]:
                next_r,next_c = dr+r,dc+c
                if 0<=next_r<m and 0<=next_c<n and not visited[next_r][next_c] and grid[next_r][next_c] == '1':
                    dfs(next_r,next_c)


        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r,c)
                    count+=1
        return count
       
                    

        
