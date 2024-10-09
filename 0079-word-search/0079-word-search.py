class Solution(object):
    def exist(self, board, word):
        n,m = len(board), len(board[0])
        
        def dfs(r,c,idx):
            if len(word) == idx:
                return True

            # 경계 벗어나거나 현재 문자가 일치하지 않는 경우
            if r<0 or r>=n or c<0 or c>=m or word[idx] !=board[r][c]:
                return False

            tmp = board[r][c] # 방문한 셀을 임시로 마킹
            board[r][c] = '#' # 방문 표시

            # 상하좌우탐색
            find = (dfs(r+1,c, idx+1) or dfs(r,c+1,idx+1) or dfs(r-1,c,idx+1) or dfs(r,c-1,idx+1))
            
            board[r][c] = tmp # 백트래킹: 탐색 후 원래 값으로 복원
            return find
            

        for r in range(n):
            for c in range(m):
                if dfs(r,c,0):
                    return True
        return False
        