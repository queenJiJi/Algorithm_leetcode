class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited= [False]*len(rooms)

        def dfs(start_v):
            visited[start_v] = True

            for next_v in rooms[start_v]:
                if visited[next_v] == False:
                    dfs(next_v)
            return visited 
        
        dfs(0)

        return True if all(visited) else False 