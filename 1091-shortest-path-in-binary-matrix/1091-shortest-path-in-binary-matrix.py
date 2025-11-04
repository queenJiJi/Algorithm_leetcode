class Solution(object):
    from collections import deque
    def shortestPathBinaryMatrix(self, grid):
            n = len(grid)

            if grid[0][0]!= 0 or grid[n-1][n-1]!=0:
                    return -1

            q = deque()
            q.append((0,0,1))
            visited = [[False]*n for _ in range(n)]
            # check = [[-2]*n for _ in range(n)]
            # check[0][0] = 1
            visited[0][0] = True

            while q:
                x,y,path = q.popleft()
                if (x,y)==(n-1,n-1):
                    # print(visited)
                    # print(check)
                    return path

                for dr,dc in [[-1,0],[0,-1],[0,1],[1,0],[-1,1],[1,-1],[1,1],[-1,-1]]:
                    nr,nc=x+dr, y+dc

                    if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]==0:
                        q.append((nr,nc,path+1))
                        visited[nr][nc] = True
                        # check[nr][nc] = path
                        # print(path)
            # print(check)
            return -1

        
        