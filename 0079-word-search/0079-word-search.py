class Solution(object):
    def exist(self, board, word):
        n,m = len(board), len(board[0])
        visited=[[False for _ in range(m)] for _ in range(n)]
        
        def dfs(r,c,idx):
            if idx == len(word):
                return True
            
            if not(0<=r<n and 0<=c<m and word[idx]==board[r][c] and not visited[r][c]):
                return False

            visited[r][c] = True

            for dx,dy in [[-1,0],[0,-1],[0,1],[1,0]]:
                nr,nc = dx+r, dy+c
                if dfs(nr,nc,idx+1):
                    return True
            visited[r][c] = False
            return False

        
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False