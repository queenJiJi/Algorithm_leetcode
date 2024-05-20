class Solution(object):
    def numIslands(self, grid):
        row_len,col_len = len(grid), len(grid[0])
        visited=[[False]*col_len for _ in range(row_len)]
        count = 0
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r,c):
            visited[r][c] = True

            for i in range(4):
                next_r = r+ dr[i]
                next_c = c+ dc[i]

                if 0<=next_r<row_len and 0<=next_c<col_len and grid[next_r][next_c] == "1":
                    if not visited[next_r][next_c]:
                        dfs(next_r,next_c)
                        visited[next_r][next_c] = True
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    count+=1
        return count