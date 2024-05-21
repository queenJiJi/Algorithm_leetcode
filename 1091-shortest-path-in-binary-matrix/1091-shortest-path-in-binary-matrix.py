from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        row_len,col_len = len(grid), len(grid[0])
        visited= [[False]*col_len for _ in range(row_len)]
        dr = [-1,1,0,0,-1,-1,1,1]
        dc = [0,0,-1,1,-1,1,-1,1]
        def bfs(r,c,path):
            q = deque()
            q.append((r,c,path))
            visited[r][c] = True

            if grid[0][0]==1 or grid[row_len-1][col_len-1] == 1:
                return -1

            while q:
                cur_r,cur_c,cur_path = q.popleft()

                if (cur_r,cur_c) == (row_len-1, col_len-1):
                    return cur_path
                
                for i in range(8):
                    next_r,next_c =cur_r+dr[i], cur_c+dc[i]
                    if 0<=next_r<row_len and 0<=next_c<col_len and grid[next_r][next_c] == 0:
                        if not visited[next_r][next_c]:
                            q.append((next_r,next_c,cur_path+1))
                            visited[next_r][next_c] = True
            return -1
        return bfs(0,0,1)
                