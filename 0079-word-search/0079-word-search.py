class Solution(object):
    def exist(self, board, word):
        n,m = len(board), len(board[0])
        visited = set()

        def dfs(r,c,idx):

            if len(word) == idx:
                return True
            
            if (r,c) in visited or not(0<=r<n and 0<=c<m) or word[idx]!=board[r][c]:
                return False

            visited.add((r,c))

            for dx,dy in [[-1,0],[0,1],[1,0],[0,-1]]:
                nr,nc = dx+r, dy+c
                if dfs(nr,nc,idx+1):
                    return True
            visited.remove((r,c))

        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False