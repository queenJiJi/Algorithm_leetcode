from collections import deque

class Solution(object):
    def exist(self, board, word):
        n,m = len(board),len(board[0])
        visited= [[False]*m for _ in range(n)]

        def dfs(r, c, word_idx):
            # 탈출조건
            if word_idx == len(word):
                return True
            # 먼저 거르기
            if not(0<=r<n and 0<=c<m) or visited[r][c] or word[word_idx]!= board[r][c]:
                return False
            
            visited[r][c] = True
            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr,nc = r+dr,c+dc
                if dfs(nr,nc,word_idx+1): 
                    return True
            visited[r][c] = False

        for r in range(n):
            for c in range(m):
                if dfs(r,c,0):
                    return True
        return False      

        # n = len(board)
        # m = len(board[0])
        # path = set()
        # def dfs(r,c,cur_word_idx):
        #         # 탈출 조건:
        #         if len(word)==cur_word_idx:
        #             return True
        #         # 안되는 조건 
        #         if (r<0 or c<0 or r>=n or c>=m or # out of range이거나
        #             word[cur_word_idx] != board[r][c] or # 찾는 단어랑 보드에 있는 단어가 일치하지 않거나
        #             (r,c) in path): # 이미 방문한 곳을 또 방문하려고 한다면
        #             return False
        #         # 문제가 없다면
        #         path.add((r,c)) # 해당 letter를 path에 추가
        #         # 상,하,좌,우 다 살핌
        #         result = (dfs(r+1,c,cur_word_idx+1) or 
        #                 dfs(r-1,c,cur_word_idx+1) or 
        #                 dfs(r,c-1,cur_word_idx+1) or 
        #                 dfs(r,c+1,cur_word_idx+1))

        #         path.remove((r,c))
        #         return result
        

        
        # # 보드 내부를 돌면서 하나씩 확인
        # for r in range(n):
        #     for c in range(m):
        #         if dfs(r,c, 0): # 어떤 결과값이 나온다면
        #             return True
        # # 루프를 다 돌았는데도 일치하는게없다면
        # return False

        # row_len, col_len = len(board), len(board[0])
    
        # def bfs(start_r, start_c):
        #     q = deque()
        #     q.append((start_r, start_c, 0))  # (row, col, index_in_word)
        #     visited = set()
        #     visited.add((start_r, start_c))
            
        #     while q:
        #         cur_r, cur_c, index = q.popleft()
                
        #         if index == len(word) - 1:
        #             return True
                
        #         for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        #             nr, nc = cur_r + dr, cur_c + dc
                    
        #             if 0 <= nr < row_len and 0 <= nc < col_len and (nr, nc) not in visited:
        #                 if board[nr][nc] == word[index + 1]:
        #                     q.append((nr, nc, index + 1))
        #                     visited.add((nr, nc))
            
        #     return False
            
        # for r in range(row_len):
        #     for c in range(col_len):
        #         if board[r][c] == word[0]:
        #             if bfs(r, c):
        #                 return True
        
        # return False