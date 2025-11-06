class Solution(object):
    from collections import deque
    def canFinish(self, numCourses, prerequisites):
        q = deque()
        visited = []
        indegree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            cur_v = q.popleft()
            visited.append(cur_v)

            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                if indegree[next_v] == 0:
                    q.append(next_v)
                    
        return True if len(visited) == numCourses else False
                    