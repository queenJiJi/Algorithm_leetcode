from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        # bfs
        start_v = 0
       
        visited=[False]*len(rooms)
        def bfs(start_v):
            q = deque()
            q.append(start_v)

            while q:
                cur_v = q.popleft()
                visited[cur_v] = True
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        visited[next_v] = True
                        q.append(next_v)
        bfs(0)
        return all(visited)
       # dfs 
        # visit = [False] * len(rooms)

        # def dfs(cur_v):
        #     visit[cur_v] = True

        #     for next_v in rooms[cur_v]:
        #         if not visit[next_v]:
        #             dfs(next_v)
        # dfs(0)

        # return all(visit)                    