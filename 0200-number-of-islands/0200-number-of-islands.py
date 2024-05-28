import collections
class Solution(object):
    def numIslands(self, grid):
        q = collections.deque()
        m,n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        count = 0

        def dfs(r,c):
            visited[r][c] = True
            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                next_r,next_c = r+dr, c+dc
                if 0<=next_r<m and 0<=next_c<n and grid[next_r][next_c]=='1':
                    if not visited[next_r][next_c]:
                        dfs(next_r,next_c)

        # def bfs(r,c):
        #     q.append((r,c))
        #     while q:
        #         cur_r,cur_c = q.popleft()
        #         visited[cur_r][cur_c] = True
                
        #         for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        #             next_r,next_c = cur_r+dr, cur_c+dc
        #             if 0<=next_r<m and 0<=next_c<n and grid[next_r][next_c]=='1':
        #                 if not visited[next_r][next_c]:
        #                     q.append((next_r,next_c))
        #                     visited[next_r][next_c] = True

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    # bfs(r,c)
                    dfs(r,c)
                    count+=1
        return count


        