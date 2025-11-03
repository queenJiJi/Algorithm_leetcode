class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = [False]*len(rooms) 

        def dfs(room):
            visited[room] = True

            for next_room in rooms[room]:
                if not visited[next_room]:
                    visited[next_room] = True
                    dfs(next_room)
        
        dfs(0)

        return True if all(visited) else False