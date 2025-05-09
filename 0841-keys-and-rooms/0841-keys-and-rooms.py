from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        q = deque()
        q.append(0)
        visit = [False]* len(rooms)
        visit[0] = True

        while q:
            cur_room = q.popleft()

            for next_room in rooms[cur_room]:
                if not visit[next_room]:
                    visit[next_room] = True
                    q.append(next_room)
        return True if all(visit) else False

        