import collections
class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n= len(grid[0])
        visited = [[False]*n for _ in range(m)]
        count = 0
        def bfs(r,c):
            visited[r][c] = True
            q = collections.deque()
            q.append([r,c])

            while q:
                cur_r, cur_c = q.popleft()

                for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    next_r = cur_r + dr
                    next_c = cur_c+dc
                    if 0<=next_r<m and 0<=next_c<n and grid[next_r][next_c] =='1' and not visited[next_r][next_c]:
                        q.append((next_r,next_c))
                        visited[next_r][next_c] = True      
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    bfs(r,c)
                    count+=1
        return count
                    

        
