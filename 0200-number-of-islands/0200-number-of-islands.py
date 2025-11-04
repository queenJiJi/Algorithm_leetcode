class Solution(object):
    from collections import deque

    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        cnt = 0
        q = deque()
        visited = set()

        def bfs(i,j):
            visited.add((i,j))
            q.append((i,j))

            while q:
                x,y = q.popleft()

                for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                    nr,nc = x+dx,y+dy

                    if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited and grid[nr][nc] == '1':
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return True

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    if (i,j) not in visited and bfs(i,j):
                        cnt+=1
        print(visited)
        return cnt
        