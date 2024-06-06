from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
          # 그래프, 방문을 마킹해줄 visited, indegree 저장해주는 변수들 세팅
        graph = [[] for _ in range(numCourses)]
        visited = []
        indegree = [0] * numCourses

        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i] +=1

        # 위상 정렬 수행
        q= deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)

        while q:
            cur_v = q.popleft()
            visited.append(cur_v)
            
            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                if indegree[next_v] == 0:
                    q.append(next_v)

        if len(visited) != numCourses:
            return []
        return visited