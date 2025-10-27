class Solution(object):
    def exist(self, board, word):
        visited = set()
        n,m = len(board) , len(board[0])
        def backtrack(r,c, idx):

            if idx ==  len(word):
                return True

            if not(0<=r<n and 0<=c<m) or (r,c) in visited or word[idx]!=board[r][c]:
                return False

            visited.add((r,c))

            for dr,dc in [[-1,0],[0,1],[0,-1],[1,0]]:
                nr,nc = dr+r, dc+c

                if backtrack(nr,nc,idx+1):
                    return True
            visited.remove((r,c))
            
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True
        return False

        
        