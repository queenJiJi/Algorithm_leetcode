class Solution(object):
    def canVisitAllRooms(self, rooms):
       # dfs 
        visit = [False] * len(rooms)

        def dfs(cur_v):
            visit[cur_v] = True

            for next_v in rooms[cur_v]:
                if not visit[next_v]:
                    dfs(next_v)
        dfs(0)

        return all(visit)                    